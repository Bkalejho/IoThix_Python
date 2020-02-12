import socket
import base64
import ssl
import time


msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"
mailserver = ("SMTP.Office365.com", 587)
username = "iothix@outlook.com"
recipient = "bkalejho@gmail.com"
password = "ab11235813ba"
crlfMesg = '\r\n'

# Create a socket object: AF_INET=ipv4, SOC_STREAM=TCP
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

clientSocket.connect(mailserver)
recv = clientSocket.recv(2048)
recv = recv.decode()
print("Message after connection request:" + recv)

heloCommand = 'HELO Alejho\r\n'
clientSocket.send(heloCommand.encode('utf-8'))
recv = clientSocket.recv(2048)
recv = recv.decode()
print("Message after EHLO command:" + recv)

starttlsCommand = "STARTTLS\r\n"
clientSocket.send(starttlsCommand.encode())
recv = clientSocket.recv(1024)
recv = recv.decode()
print("Message after STARTTLS command:" + recv)

context = ssl.create_default_context()
clientSocket = context.wrap_socket(clientSocket, server_hostname="SMTP.Office365.com")

heloCommand = 'EHLO Alejho\r\n'
clientSocket.send(heloCommand.encode())
recv = clientSocket.recv(1024)
recv = recv.decode()
print("Message after EHLO_TLS command:" + recv)

authCommand = 'AUTH LOGIN\r\n'
clientSocket.send(authCommand.encode())
recv = clientSocket.recv(1024)
recv = recv.decode()
print("Message after AUTH LOGIN command:" + recv)

user64 = base64.b64encode(username.encode('utf-8'))
pass64 = base64.b64encode(password.encode('utf-8'))

#print(user64)

clientSocket.send(user64)
clientSocket.send(crlfMesg.encode())
recv = clientSocket.recv(1024)
recv = recv.decode()
print("Message after USER:" + recv)

#print(pass64)

clientSocket.send(pass64)
clientSocket.send(crlfMesg.encode())
recv = clientSocket.recv(1024)
recv = recv.decode()
print("Message after PASS:" + recv)

# Tell server the message's sender
fromMesg = 'MAIL FROM: <' + username + '>\r\n'
#print(fromMesg)
clientSocket.send(fromMesg.encode())
recv = clientSocket.recv(1024)
recv = recv.decode()
print("Message after fromMesg:" + recv)

# Tell server the message's recipient
rcptMesg = 'RCPT TO: <' + recipient + '>\r\n'
#print(rcptMesg)
clientSocket.send(rcptMesg.encode())
recv = clientSocket.recv(1024)
recv = recv.decode()
print("Message after rcptMesg:" + recv)

# Give server the message
dataMesg = 'DATA\r\n'
#print(dataMesg)
clientSocket.send(dataMesg.encode())
recv = clientSocket.recv(1024)
recv = recv.decode()
print("Message after dataMesg:" + recv)

mailbody = """\
Subject: Que se dice lo mas jony

mensaje sin libreria \r\n"""
#print(mailbody)
clientSocket.send(mailbody.encode())
fullStop = '\r\n.\r\n'
#print(fullStop)
clientSocket.send(fullStop.encode())
recv = clientSocket.recv(1024)
recv = recv.decode()
print("Message after mailbody:" + recv)

# Signal the server to quit
quitMesg = 'QUIT\r\n'
#print(quitMesg)
clientSocket.send(quitMesg.encode())
recv = clientSocket.recv(1024)
recv = recv.decode()
print("Message after QUIT:" + recv)

clientSocket.close()