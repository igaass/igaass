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

# print (repr(ssl_sock.getpeername()))
# print (ssl_sock.cipher())
# print (pprint.pformat(ssl_sock.getpeercert()))

ssl_sock.write(('''
{
  "USER": "ALEXEY",
  "HOSTNAME": "#PM",
  "CUSTOMER": {
    "ACTION": "INSERT",
    "CUSTOMERCLASS": 1,
    "PERSONALID": "7146567494",
    "PERSONALIDCOUNTRYCODE": "AA",
    "FIRSTNAME": "Michaelsk",
    "LASTNAME": "Malitov",
    "DATEOFBIRTH": "17.10.1991",
    "SEX": 2,
    "R_LOCATION": "Jeschrt",
    "R_POSTALCODE": "12345",
    "R_PLACE": "Seene 4-15",
    "R_COUNTRYCODE": "AA",
    "R_COUNTRY": "Poland",
    "LOCATIONCODE": "0",
    "EMAIL": "info@seene.pl",
    "PHONE2": "5212345",
    "CUSTOMERDOCUMENT": [
      {
        "ACTION": "INSERT",
        "DOCUMENTTYPE": "102",
        "DOCUMENTNUMBER": "AL003298",
        "DOCUMENTISSUEDBY": "PPL",
        "DOCUMENTISSUEDON": "14.09.2010",
        "EXPIRYDATE": "31.01.2016"
      },
      {
        "ACTION": "INSERT",
        "DOCUMENTTYPE": "102",
        "DOCUMENTNUMBER": "ABZ07289",
        "DOCUMENTISSUEDBY": "PPLK",
        "DOCUMENTISSUEDON": "16.08.2015",
        "EXPIRYDATE": "31.12.2019"
      }
    ]
  }
}
''').encode()
)

data = ssl_sock.read(8192)


# print("Got from server",data)
print(data.decode())

if False: # from the Python 2.7.3 docs
    # Set a simple HTTP request -- use httplib in actual code.
    ssl_sock.write("""GET / HTTP/1.0\r
    Host: www.verisign.com\n\n""".encode())

    # Read a chunk of data.  Will not necessarily
    # read all the data returned by the server.
    data = ssl_sock.read()

    # note that closing the SSLSocket will also close the underlying socket
    ssl_sock.close()