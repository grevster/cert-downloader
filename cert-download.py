import socket, ssl
import OpenSSL

hostname='www.bbc.co.uk'
port=443

context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ssl_sock = context.wrap_socket(s, server_hostname=hostname)
ssl_sock.connect((hostname, port))
ssl_sock.close()
cert = ssl.get_server_certificate((hostname, port))
x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)
der = OpenSSL.crypto.dump_certificate(OpenSSL.crypto.FILETYPE_ASN1, x509)

with open('./tmp/'+hostname+'.der', 'wb') as f: f.write(der)