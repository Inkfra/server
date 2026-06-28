import socket
import ipaddress

def dns_lookup(hostname):
    if not hostname:
        return None

    try:
        ipaddress.ip_address(hostname)
        return hostname
    except ValueError:
        pass

    try:
        return socket.gethostbyname(hostname)
    except socket.gaierror:
        return hostname