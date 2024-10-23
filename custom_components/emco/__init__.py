import logging
import socket
import xml.etree.ElementTree as ET
import asyncio
import serial
import functools
from homeassistant.core import HomeAssistant
from homeassistant.helpers.discovery import async_load_platform
from homeassistant.helpers.dispatcher import async_dispatcher_send
from homeassistant.helpers.typing import ConfigType
from .const import DOMAIN, SERIAL_PORT, BAUDRATE, PARITY, VTOW, WTOV, SERVER_IP, SERVER_PORT, BINARY_DATA

_LOGGER = logging.getLogger(__name__)

PLATFORMS = ["sensor", "binary_sensor", "button"]  # Define the platforms to be loaded

async def async_setup(hass: HomeAssistant, config: ConfigType):
    """Set up the emco integration asynchronously."""
    # Get configuration data from configuration.yaml
    hass.data[DOMAIN] = {}

    hass.loop.create_task(async_read_serial(hass))

    # Serial data service
    async def async_handle_serial_command(call):
        """Handle the serial data command service asynchronously."""
        lock_name = call.data.get("lock_name")
        _LOGGER.info(f"Serial command received for {lock_name}, sending data to serial port.")
        await async_send_serial_data(lock_name)
    
    # Elevator call service
    async def async_handle_ev_call(call):
        """Handle the elevator call and update the sensor states."""
        _LOGGER.info(f"Handle ev call, sending data to tcp.") 
        await async_ev_call(hass)

    hass.services.async_register(DOMAIN, "send_serial_data", async_handle_serial_command)
    hass.services.async_register(DOMAIN, "ev_call", async_handle_ev_call)

    # Load platforms
    hass.async_create_task(async_load_platform(hass, 'sensor', DOMAIN, {}, config))
    hass.async_create_task(async_load_platform(hass, 'binary_sensor', DOMAIN, {}, config))
    hass.async_create_task(async_load_platform(hass, 'button', DOMAIN, {}, config))

    return True

async def async_read_serial(hass: HomeAssistant):
    """Read from the serial port asynchronously using pyserial."""
    try:
        ser = serial.Serial(
            SERIAL_PORT,
            BAUDRATE,
            parity=PARITY,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=1
        )
        _LOGGER.info(f"Opened serial port: {SERIAL_PORT}")

        loop = asyncio.get_running_loop()

        while True:
            # Read one line asynchronously using run_in_executor
            line = await loop.run_in_executor(None, functools.partial(ser.readline))
            if not line or bytes([0x00, 0xE1, 0x05, 0x70, 0xDB, 0x30, 0x01, 0x30]) in line:
                continue  # No or dummy data, continue
            log = ' '.join(f'{byte:02X}' for byte in line)
            _LOGGER.info(f"Data received: {log}")
            
            data = await handle_serial_data(hass, line, ser)

            # Update the binary sensor state based on the received data
            await update_binary_sensor_state(hass, data, ser)

    except Exception as e:
        _LOGGER.error(f"Failed to read from serial port: {e}")
    finally:
        ser.close()

async def handle_serial_data(hass: HomeAssistant, line, ser):
    """Handle serial data and send commands to the serial port asynchronously."""
    data = None
    loop = asyncio.get_running_loop()

    if WTOV['idleTOfront_ring'] in line:
        data = "FRONT_ON"
        _LOGGER.info(f"Front on - handle_serial_data")
        await loop.run_in_executor(None, functools.partial(ser.write, VTOW['front_ringTOav']))
    elif WTOV['front_ringTOidle'] in line:
        data = "FRONT_OFF"
        _LOGGER.info(f"Front off - handle_serial_data")
    elif WTOV['comm_ringTOidle'] in line or WTOV['comm_avTOidle'] in line:
        data = "COMMUNAL_OFF"
        _LOGGER.info(f"Communal off - handle_serial_data")
    elif WTOV['idleTOcomm_ring'] in line:
        data = "COMMUNAL_ON"
        _LOGGER.info(f"Communal on - handle_serial_data")
        await loop.run_in_executor(None, functools.partial(ser.write, VTOW['comm_ringTOav']))

    if data:
        await loop.run_in_executor(None, ser.flush)  # Wait for data to be sent
        _LOGGER.info(f"Sent command to serial port: {data}")
    
    return data

async def update_binary_sensor_state(hass: HomeAssistant, data: str, ser):
    """Update the binary sensor state in Home Assistant."""
    loop = asyncio.get_running_loop()
    _LOGGER.info(f"Data received: {data}")
    communal_sensor_entity = self._hass.data[DOMAIN].get("communal_sensor")
    front_sensor_entity = self._hass.data[DOMAIN].get("front_sensor")
    if data == "COMMUNAL_ON":
        communal_sensor_entity.set_state(True)        
        await asyncio.sleep(30)
        await loop.run_in_executor(None, functools.partial(ser.write, VTOW['comm_avTOidle']))
        communal_sensor_entity.set_state(False)        
    elif data == "COMMUNAL_OFF":
        communal_sensor_entity.set_state(False)        
    elif data == "FRONT_ON":
        front_sensor_entity.set_state(True)
        await asyncio.sleep(30)
        await loop.run_in_executor(None, functools.partial(ser.write, VTOW['front_ringTOidle']))
        front_sensor_entity.set_state(False)
    elif data == "FRONT_OFF":
        front_sensor_entity.set_state(False)

async def async_send_serial_data(lock_name: str):
    """Send data to the serial port asynchronously based on the button name using pyserial."""
    try:
        ser = serial.Serial(
            SERIAL_PORT,
            BAUDRATE,
            parity=PARITY,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=1
        )
        
        await send_and_update_state(ser, lock_name)
        
        await asyncio.sleep(0)  # 비동기 대기 (다른 작업을 루프에 허용)

    except Exception as e:
        _LOGGER.error(f"Failed to send data to serial port: {e}")
    finally:
        ser.close()

async def send_and_update_state(ser, lock_name: str):
    """Send specific data to the serial port and update sensor state asynchronously."""
    loop = asyncio.get_running_loop()  
    communal_sensor_entity = self._hass.data[DOMAIN].get("communal_sensor")
    front_sensor_entity = self._hass.data[DOMAIN].get("front_sensor")  

    if lock_name == "communal_open":        
        # 시리얼 포트로 데이터 쓰기 (비동기적으로 실행)
        await loop.run_in_executor(None, functools.partial(ser.write, VTOW['comm_avTOunlock']))
        await asyncio.sleep(5)  # 5초 대기
        await loop.run_in_executor(None, functools.partial(ser.write, VTOW['comm_avTOidle']))
        communal_sensor_entity.set_state(False)

    elif lock_name == "front_open":
        # 시리얼 포트로 데이터 쓰기 (비동기적으로 실행)
        await loop.run_in_executor(None, functools.partial(ser.write, VTOW['front_ringTOunlock']))
        await asyncio.sleep(5)  # 5초 대기
        await loop.run_in_executor(None, functools.partial(ser.write, VTOW['front_ringTOidle']))
        front_sensor_entity.set_state(False)

    elif lock_name == "front_start":
        await loop.run_in_executor(None, functools.partial(ser.write, VTOW['idleTOav']))

    elif lock_name == "front_stop":
        await loop.run_in_executor(None, functools.partial(ser.write, VTOW['avTOidle']))

    await loop.run_in_executor(None, ser.flush)  # 전송된 데이터를 즉시 시리얼 포트로 밀어내기

async def async_ev_call(hass: HomeAssistant):
    """Handle the elevator call and update the sensor states asynchronously using asyncio TCP connection."""
    try:
        reader, writer = await asyncio.open_connection(SERVER_IP, SERVER_PORT)
        _LOGGER.info(f"Connected to {SERVER_IP}:{SERVER_PORT}")

        # Send binary data
        writer.write(BINARY_DATA)
        await writer.drain()  # 데이터가 전송될 때까지 기다림

        BUFFER_SIZE = 2048  # Buffer size for receiving data

        # Receive and process the data
        while True:
            packet = await reader.read(BUFFER_SIZE)
            if not packet:
                _LOGGER.info("No more data. Closing the connection.")
                break

            packet = packet.replace(b'\x00', b'')[8:]
            packet = packet.replace(b'\xe8\xb2\xc0\xc9\xf0\xc5\xd9\xb3', b'\xeb\x8b\xa8\xec\xa7\x80\xec\x97\xb0\xeb\x8f\x99') \
                           .replace(b'\xd8\xc5\xac\xb9\xa0\xbct\xc70\xd1 Q\xc7\xf5\xb2', b'\xec\x97\x98\xeb\xa6\xac\xeb\xb2\xa0\xec\x9d\xb4\xed\x84\xb0 \xec\x9d\x91\xeb\x8b\xb5')

            try:
                root = ET.fromstring(packet)
                service = root.find('body').find('device').find('service')
                state = 'ev_1' if '27^' in service.find('explicit').text else 'ev_2'
                direction = service.find('direction').text
                floor = service.find('explicit').text.split('^')[1]

                status = {'state': direction, 'floor': floor}
                _LOGGER.info(f"Received elevator status: {status}")

                # 비동기 dispatcher로 이벤트 전송
                async_dispatcher_send(hass, 'ev_update_sensor', f'{state}_state', direction)    
                async_dispatcher_send(hass, 'ev_update_sensor', f'{state}_floor', f'{floor}층')    

                if direction == 'arrive':
                    await asyncio.sleep(5)
                    async_dispatcher_send(hass, 'ev_update_sensor', 'ev_1_state', 'unknown')    
                    async_dispatcher_send(hass, 'ev_update_sensor', 'ev_1_floor', 'unknown')    
                    async_dispatcher_send(hass, 'ev_update_sensor', 'ev_2_state', 'unknown')    
                    async_dispatcher_send(hass, 'ev_update_sensor', 'ev_2_floor', 'unknown')      
            except ET.ParseError:
                _LOGGER.error("Failed to parse the received XML data.")

        writer.close()
        await writer.wait_closed()

    except Exception as e:
        _LOGGER.error(f"Failed to connect to the elevator server: {e}")
