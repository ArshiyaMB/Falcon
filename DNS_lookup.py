#DNS LookUp 
# gathering ip address of a domain name

import socket 

def get_ip(domain):
    try:
        return socket.gethostbyname(domain, timeout=30)
    except socket.gaierror:
        return None

def get_domain(ip):
    try:
        hostname = socket.gethostbyaddr(ip, timeout=30)
        return hostname[0]
    except Exception:
        return None
