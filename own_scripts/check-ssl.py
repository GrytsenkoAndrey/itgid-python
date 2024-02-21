import ssl
import socket
from pprint import pprint

def get_ssl_certificate(url, port=443):
    context = ssl.create_default_context()

    with socket.create_connection((url, port)) as sock:
        with context.wrap_socket(sock, server_hostname=url) as ssock:
            certificate = ssock.getpeercert()
    return certificate

url = 'https://api.push.apple.com'
certificate = get_ssl_certificate(url)

pprint(certificate)