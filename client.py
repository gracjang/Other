"""Gracjan Grochowski ISSP"""
import sys
import socket

""" Variables to open socket server"""
host = ''
port = 3200

mySocket = socket.socket()


try:
    mySocket.connect((host, port))
    print("Connected to server !")
    message = input("> ")
except:
    print("Couldnt connect with the socket-server:")
    sys.exit(1)
"""Loop over message quit"""
while message != 'quit':
    try:
        mySocket.send(message.encode())
        data = mySocket.recv(1024).decode()
        print('Message: ' + str(data[6:]))
        message = input(">> ")
    except:
        print("ERROR")
print('\r','\n','>>CONNECTION CLOSE<<','\r','\n')
mySocket.close()


"""Example : """
""" > python3 serwer.py &
    > python3 client.py
    > lower INF
    > Message inf
    > upper inf
    > message INF
    > quit
    > Connection CLOSE
 """