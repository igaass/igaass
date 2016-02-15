
#!/usr/bin/env python3
import socket, ssl, pprint

port=10222
host='10.77.6.220' #'localhost'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Require a certificate from the server. We used a self-signed certificate
# so here ca_certs must be the server certificate itself.
ssl_sock = ssl.wrap_socket(s, ca_certs=None)
#"server.crt", cert_reqs=ssl.CERT_REQUIRED)

ssl_sock.connect((host, port))

print(repr(ssl_sock.getpeername()))
print(ssl_sock.cipher())
print(pprint.pformat(ssl_sock.getpeercert()))

ssl_sock.write('''

{
  "USER": "ALEXEY",
  "HOSTNAME": "#PM",
  "LOAN": {
    "ACTION": "INSERT",
    "CUSTOMERNUMBER": "000514",
    "CURRENTACCOUNT": "4578600051408",
    "DECISIONTYPE": 7,
    "EB_LOANPURPOSE": 12,
    "REPAYMENTTYPE": 5,
    "BANKCOMMENTS": "Demo",
    "MONTHPAYMENT": "12",
    "MINMONTHPAYMENT": "0",
    "LOANCHANGES": [
      {
        "ACTION": "INSERT",
        "LOANLIMIT": 100,
        "INTERESPAYMENTSHIFT": 1,
        "INTERESTPERIODSHIFT": 3
      }
    ],
    "LOANSUBTYPE": "401",
    "LOANMANAGER": "ALEXEY"
  }
}
'''.encode()
)

data = ssl_sock.read(8192)

# print("Got from server",data)
print(data.decode())
ssl_sock.close()

if False: # from the Python 2.7.3 docs
    # Set a simple HTTP request -- use httplib in actual code.
    ssl_sock.write("""GET / HTTP/1.0\r
    Host: www.verisign.com\n\n""".encode())

    # Read a chunk of data.  Will not necessarily
    # read all the data returned by the server.
    data = ssl_sock.read()

    # note that closing the SSLSocket will also close the underlying socket
    ssl_sock.close()