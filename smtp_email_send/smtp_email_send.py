# Import socket module
import socket
import base64
import time


msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"
mailserver = ("smtp.gmail.com", 25)

# Create a socket object: AF_INET=ipv4, SOC_STREAM=TCP
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

clientSocket.connect(mailserver)
recv = clientSocket.recv(1024)
recv = recv.decode()
print("Message after connection request:" + recv)
if recv[:3] != '220':
    print('220 reply not received from server.')

heloCommand = 'EHLO Alejho\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024)
recv1 = recv1.decode()
print("Message after EHLO command:" + recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# starttlsCommand = "STARTTLS\r\n"
# clientSocket.send(starttlsCommand.encode())
# recv2 = clientSocket.recv(1024)
# recv2 = recv2.decode()
# print("Message after STARTTLS command:" + recv2)
#
# heloCommand = 'EHLO Alejho\r\n'
# clientSocket.send(heloCommand.encode())
# recv1 = clientSocket.recv(1024)
# recv1 = recv1.decode()
# print("Message after EHLO command:" + recv1)
# # if recv1[:3] != '250':
# #     print('250 reply not received from server.')

# authCommand = 'AUTH LOGIN\r\n'
# clientSocket.send(authCommand.encode())
# recv1 = clientSocket.recv(1024)
# recv1 = recv1.decode()
# print("Message after AUTH LOGIN command:" + recv1)

#Info for username and password
username = "bkalejho@gmail.com"
password = "c(6203)c"
base64_str = ("\x00"+username+"\x00"+password).encode()
base64_str = base64.b64encode(base64_str)
authMsg = "AUTH PLAIN ".encode()+base64_str+"\r\n".encode()
clientSocket.send(authMsg)
recv_auth = clientSocket.recv(1024)
print(recv_auth.decode())

# close the connection
clientSocket.close()