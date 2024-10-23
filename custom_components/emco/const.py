"""Constants for the emco integration."""

DOMAIN = "emco"
SERIAL_PORT = "/dev/ttyUSB0"
BAUDRATE = 3840
PARITY = 'E'  # Even parity
VTOW = {'front_ringTOunlock': bytes([0x7f, 0xb4, 0x00, 0x00, 0xee]),
        'front_ringTOav': bytes([0x7f, 0xb7, 0x00, 0x00, 0xee]),
        'front_ringTOidle': bytes([0x7f, 0xb8, 0x00, 0x00, 0xee]),
        'idleTOav': bytes([0x7f, 0xb9, 0x00, 0x00, 0xee]),
        'avTOidle': bytes([0x7f, 0xba, 0x00, 0x00, 0xee]),
        'comm_ringTOav': bytes([0x7f, 0x5f, 0x00, 0x00, 0xee]),
        'comm_avTOidle': bytes([0x7f, 0x60, 0x00, 0x00, 0xee]),
        'comm_avTOunlock': bytes([0x7f, 0x61, 0x00, 0x00, 0xee])
        }

WTOV = {'idleTOfront_ring': bytes([0x7f, 0xb5, 0x00, 0x00, 0xee]),
        'front_ringTOidle': bytes([0x7f, 0xb6, 0x00, 0x00, 0xee]),
        'idleTOcomm_ring': bytes([0x7f, 0x5a, 0x00, 0x00, 0xee]),
        'comm_ringTOidle': bytes([0x7f, 0x5c, 0x00, 0x00, 0xee]),
        'comm_avTOidle': bytes([0x7f, 0x5e, 0x00, 0x00, 0xee])
        }
SERVER_IP = "192.168.0.42"
SERVER_PORT = 8989
pre_DATA = bytes([0x78, 0xe7, 0xd1, 0xeb, 0xc2, 0xb4, 0x0, 0x1d, 0x66, 0x9, 0x83, 0x55, 0x8, 0x0, 0x45, 0x0, 0x3, 0x48, 0xb0, 0xaf, 0x40, 0x0, 0x80, 0x6, 0x1f, 0x29, 0xac, 0x14, 0x6, 0xe6, 0xac, 0x14, 0xc8, 0xc8, 0xc0, 0x18, 0x4c, 0x90, 0x44, 0xd7, 0x9d, 0x89, 0xfe, 0x3d, 0xd0, 0x7a, 0x50, 0x18, 0x83, 0x2c, 0x11, 0x79, 0x0, 0x0, 0x30, 0x0, 0x30, 0x0, 0x30, 0x0, 0x30, 0x0, 0x30, 0x0, 0x37, 0x0, 0x38, 0x0, 0x34, 0x0, 0x3c, 0x0, 0x6d, 0x0, 0x65, 0x0, 0x73, 0x0, 0x73, 0x0, 0x61, 0x0, 0x67, 0x0, 0x65, 0x0, 0x3e, 0x0, 0xa, 0x0, 0x9, 0x0, 0x3c, 0x0, 0x68, 0x0, 0x65, 0x0, 0x61, 0x0, 0x64, 0x0, 0x65, 0x0, 0x72, 0x0, 0x3e, 0x0, 0xa, 0x0, 0x9, 0x0, 0x9, 0x0, 0x3c, 0x0, 0x74, 0x0, 0x79, 0x0, 0x70, 0x0, 0x65, 0x0, 0x3e, 0x0, 0x69, 0x0, 0x6e, 0x0, 0x76, 0x0, 0x6f, 0x0, 0x6b, 0x0, 0x65, 0x0, 0x3c, 0x0, 0x2f, 0x0, 0x74, 0x0, 0x79, 0x0, 0x70, 0x0, 0x65, 0x0, 0x3e, 0x0, 0xa, 0x0, 0x9, 0x0, 0x9, 0x0, 0x3c, 0x0, 0x66, 0x0, 0x65, 0x0, 0x65, 0x0, 0x64, 0x0, 0x62, 0x0, 0x61, 0x0, 0x63, 0x0, 0x6b, 0x0, 0x3e, 0x0, 0x74, 0x0, 0x72, 0x0, 0x75, 0x0, 0x65, 0x0, 0x3c, 0x0, 0x2f, 0x0, 0x66, 0x0, 0x65, 0x0, 0x65, 0x0, 0x64, 0x0, 0x62, 0x0, 0x61, 0x0, 0x63, 0x0, 0x6b, 0x0, 0x3e, 0x0, 0xa, 0x0, 0x9, 0x0, 0x9, 0x0, 0x3c, 0x0, 0x64, 0x0, 0x65, 0x0, 0x73, 0x0, 0x74, 0x0, 0x3e, 0x0, 0x53, 0x0, 0x79, 0x0, 0x73, 0x0, 0x74, 0x0, 0x65, 0x0, 0x6d, 0x0, 0x4d, 0x0, 0x61, 0x0, 0x6e, 0x0, 0x61, 0x0, 0x67, 0x0, 0x65, 0x0, 0x72, 0x0, 0x3c, 0x0, 0x2f, 0x0, 0x64, 0x0, 0x65, 0x0, 0x73, 0x0, 0x74, 0x0, 0x3e, 0x0, 0xa, 0x0, 0x9, 0x0, 0x3c, 0x0, 0x2f, 0x0, 0x68, 0x0, 0x65, 0x0, 0x61, 0x0, 0x64, 0x0, 0x65, 0x0, 0x72, 0x0, 0x3e, 0x0, 0xa, 0x0, 0x9, 0x0, 0x3c, 0x0, 0x62, 0x0, 0x6f, 0x0, 0x64, 0x0, 0x79, 0x0, 0x3e, 0x0, 0xa, 0x0, 0x9, 0x0, 0x9, 0x0, 0x3c, 0x0, 0x64, 0x0, 0x65, 0x0, 0x76, 0x0, 0x69, 0x0, 0x63, 0x0, 0x65, 0x0, 0x3e, 0x0, 0xa, 0x0, 0x9, 0x0, 0x9, 0x0, 0x9, 0x0, 0x3c, 0x0, 0x75, 0x0, 0x69, 0x0, 0x64, 0x0, 0x3e, 0x0, 0x30, 0x0, 0x31, 0x0, 0x30, 0x0, 0x32, 0x0, 0x30, 0x0, 0x31, 0x0, 0x3c, 0x0, 0x2f, 0x0, 0x75, 0x0, 0x69, 0x0, 0x64, 0x0, 0x3e, 0x0, 0xa, 0x0, 0x9, 0x0, 0x9, 0x0, 0x9, 0x0, 0x3c, 0x0, 0x75, 0x0, 0x69, 0x0, 0x64, 0x0, 0x6e, 0x0, 0x61, 0x0, 0x6d, 0x0, 0x65, 0x0, 0x3e, 0x0, 0xe8, 0xb2, 0xc0, 0xc9, 0xf0, 0xc5, 0xd9, 0xb3, 0x3c, 0x0, 0x2f, 0x0, 0x75, 0x0, 0x69, 0x0, 0x64, 0x0, 0x6e, 0x0, 0x61, 0x0, 0x6d, 0x0, 0x65, 0x0, 0x3e, 0x0, 0xa, 0x0, 0x9, 0x0, 0x9, 0x0, 0x9, 0x0, 0x3c, 0x0, 0x64, 0x0, 0x6f, 0x0, 0x6e, 0x0, 0x67, 0x0, 0x3e, 0x0, 0x31, 0x0, 0x31, 0x0, 0x34, 0x0, 0x3c, 0x0, 0x2f, 0x0, 0x64, 0x0, 0x6f, 0x0, 0x6e, 0x0, 0x67, 0x0, 0x3e, 0x0, 0xa, 0x0, 0x9, 0x0, 0x9, 0x0, 0x9, 0x0, 0x3c, 0x0, 0x68, 0x0, 0x6f, 0x0, 0x3e, 0x0, 0x33, 0x0, 0x30, 0x0, 0x30, 0x0, 0x32, 0x0, 0x3c, 0x0, 0x2f, 0x0, 0x68, 0x0, 0x6f, 0x0, 0x3e, 0x0, 0xa, 0x0, 0x9, 0x0, 0x9, 0x0, 0x9, 0x0, 0x3c, 0x0, 0x73, 0x0, 0x65, 0x0, 0x72, 0x0, 0x76, 0x0, 0x69, 0x0, 0x63, 0x0, 0x65, 0x0, 0x3e, 0x0, 0xa, 0x0, 0x9, 0x0, 0x9, 0x0, 0x9, 0x0, 0x9, 0x0, 0x3c, 0x0, 0x6e, 0x0, 0x61, 0x0, 0x6d, 0x0, 0x65, 0x0, 0x3e, 0x0, 0x65, 0x0, 0x6c, 0x0, 0x65, 0x0, 0x76, 0x0, 0x61, 0x0, 0x74, 0x0, 0x6f, 0x0, 0x72, 0x0, 0x3c, 0x0, 0x2f, 0x0, 0x6e, 0x0, 0x61, 0x0, 0x6d, 0x0, 0x65, 0x0, 0x3e, 0x0, 0xa, 0x0, 0x9, 0x0, 0x9, 0x0, 0x9, 0x0, 0x9, 0x0, 0x3c, 0x0, 0x61, 0x0, 0x72, 0x0, 0x67, 0x0, 0x75, 0x0, 0x6d, 0x0, 0x65, 0x0, 0x6e, 0x0, 0x74, 0x0, 0x3e, 0x0, 0x64, 0x0, 0x6f, 0x0, 0x77, 0x0, 0x6e, 0x0, 0x3c, 0x0, 0x2f, 0x0, 0x61, 0x0, 0x72, 0x0, 0x67, 0x0, 0x75, 0x0, 0x6d, 0x0, 0x65, 0x0, 0x6e, 0x0, 0x74, 0x0, 0x3e, 0x0, 0xa, 0x0, 0x9, 0x0, 0x9, 0x0, 0x9, 0x0, 0x9, 0x0, 0x3c, 0x0, 0x65, 0x0, 0x78, 0x0, 0x70, 0x0, 0x6c, 0x0, 0x69, 0x0, 0x63, 0x0, 0x69, 0x0, 0x74, 0x0, 0x3e, 0x0, 0x5e, 0x0, 0x3c, 0x0, 0x2f, 0x0, 0x65, 0x0, 0x78, 0x0, 0x70, 0x0, 0x6c, 0x0, 0x69, 0x0, 0x63, 0x0, 0x69, 0x0, 0x74, 0x0, 0x3e, 0x0, 0xa, 0x0, 0x9, 0x0, 0x9, 0x0, 0x9, 0x0, 0x9, 0x0, 0x3c, 0x0, 0x63, 0x0, 0x6f, 0x0, 0x6d, 0x0, 0x6d, 0x0, 0x65, 0x0, 0x6e, 0x0, 0x74, 0x0, 0x3e, 0x0, 0x65, 0x0, 0x6c, 0x0, 0x65, 0x0, 0x76, 0x0, 0x61, 0x0, 0x74, 0x0, 0x6f, 0x0, 0x72, 0x0, 0x20, 0x0, 0x63, 0x0, 0x61, 0x0, 0x6c, 0x0, 0x6c, 0x0, 0x3c, 0x0, 0x2f, 0x0, 0x63, 0x0, 0x6f, 0x0, 0x6d, 0x0, 0x6d, 0x0, 0x65, 0x0, 0x6e, 0x0, 0x74, 0x0, 0x3e, 0x0, 0xa, 0x0, 0x9, 0x0, 0x9, 0x0, 0x9, 0x0, 0x3c, 0x0, 0x2f, 0x0, 0x73, 0x0, 0x65, 0x0, 0x72, 0x0, 0x76, 0x0, 0x69, 0x0, 0x63, 0x0, 0x65, 0x0, 0x3e, 0x0, 0xa, 0x0, 0x9, 0x0, 0x9, 0x0, 0x3c, 0x0, 0x2f, 0x0, 0x64, 0x0, 0x65, 0x0, 0x76, 0x0, 0x69, 0x0, 0x63, 0x0, 0x65, 0x0, 0x3e, 0x0, 0xa, 0x0, 0x9, 0x0, 0x3c, 0x0, 0x2f, 0x0, 0x62, 0x0, 0x6f, 0x0, 0x64, 0x0, 0x79, 0x0, 0x3e, 0x0, 0xa, 0x0, 0x3c, 0x0, 0x2f, 0x0, 0x6d, 0x0, 0x65, 0x0, 0x73, 0x0, 0x73, 0x0, 0x61, 0x0, 0x67, 0x0, 0x65, 0x0, 0x3e, 0x0])
BINARY_DATA = pre_DATA[0x36:]