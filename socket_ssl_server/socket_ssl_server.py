# first of all import the socket library
import socket
import ssl

# create a default context for ssl socket
context = ssl.create_default_context()
# next create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket successfully created")

# reserve a port on your computer in our
# case it is 12345 but it can be anything
port = 9004

# Next bind to the port
# we have not typed any ip in the ip field
# inst                                                                                                                                      ead we have inputted an empty string
# this makes the server listen to requests
# coming from other computers on the network
s.bind(('192.168.1.2', port))
print("socket binded to %s" % (port))

# put the socket into listening mode
s.listen(5)
print("socket is listening")

# a forever loop until we interrupt it or
# an error occurs

while True:
    # Establish connection with client.
    c, addr = s.accept()

    # tie the socket to ssl
    s_ssl = context.wrap_socket(s, server_side = True)

    print('Got connection from', addr[0])

    mssg = s_ssl.recv(1024)
    print(mssg.decode("ascii"))

    # send a thank you message to the client.
    #c.send(b'Thank you for connecting and talk to me ')

    # Close the connection with the client
    c.close()

print("Se acabó el programa")