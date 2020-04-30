# Import socket module
import socket
import ssl

#create default context to ssl
context = ssl.create_default_context()

# Create a socket object
s = socket.socket()

# Define the port on which you want to connect
port = 9004

# connect to the server on local computer
s.connect(('192.168.1.2', port))
#tie the socket to ssl
s_ssl = context.wrap_socket(s, server_addr = '192.168.1.2')
s.send(b'Este es el cliente')

# receive data from the server
print(s.recv(1024))
# close the connection
s.close()

