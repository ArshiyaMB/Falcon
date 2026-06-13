import ssl 
import socket
from datetime import datetime


def get_ssl_info(domain):
    try:
        context = ssl.create_default_context()

        with socket.create_connection((domain, 443)) as sock:
            with context.wrap_socket(
                sock
                , server_hostname = domain
            ) as ssl_sock:
                cert = ssl_sock.getpeercert(timeout=10)
                return extract_data(cert)
    except Exception as err:
        print(f"fail to get SSL Certification : {err}")
        return None

def extract_data(cert):
    issuer = cert.get('issuer', 'N/A')
    try:
        data = {
            'Country': issuer[0][0][1] or 'N/A',
            'Orgnazation': issuer[1][0][1] or 'N/A',
            'Common Name': issuer[2][0][1] or 'N/A',
            'Version': cert['version'] or 'N/A',
            'Serial Number': cert['serialNumber'] or 'N/A',
            'Start from': cert['notBefore'] or 'N/A',
            'End on': cert['notAfter'] or 'N/A',
            'Days Left': '',
            'Expired': '',
            'Subject A-ltname': ''.join([f"\n\t{item[0]} : {item[1]}" for item in cert['subjectAltName']])
        }
    except:
        data ='N/A'
        return data
    days_remaining = datetime.strptime(
        cert['notAfter'],
         "%b %d %H:%M:%S %Y %Z"
        ) - datetime.now()
    data['Days Left'] = days_remaining.days

    if days_remaining.days <= 0:
        data['Expired'] = "Yes ⚠"
    elif days_remaining.days <31:
        data['Expired'] = "Expire soon ⚠"
    else:
        data['Expired'] = "No ✅"

    return data