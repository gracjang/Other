import socket
host = ''
port = 5000

mySocket = socket.socket()
mySocket.connect((host, port))
message = input("> ")

while message != 'quit':
    mySocket.send(message.encode())
    data = mySocket.recv(1024).decode()
    print('Message: ' + str(data[6:]))
    message = input(">> ")


mySocket.close()