import socket
import struct
import fcntl

import subprocess

HOST = '0.0.0.0'
ROBOT_PORT = 5800
MJPEG_PORT = 5801
KIOSK_PORT = 5802


def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    result = "." + socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15].encode())
    )[20:24])
    return result


def get_ip_address_windows(ifname):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("192.168.50.1", 8080))
        ip = s.getsockname()[0]
        s.close()
    except:
        ip = 'unknown'
    return ip


def get_netstat_output():
    try:
        p = subprocess.Popen(['netstat', '-a'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, err = p.communicate()
    except Exception as e:
        output = 'netstat not available\n%s' % str(e)
    return output


def check_port(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex(('127.0.0.1', port))
        return True if result == 0 else False
    except Exception as e:
        return False
