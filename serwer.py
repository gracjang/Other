"""Gracjan Grochowski ISSP"""
import socket
import time
host = ''
port = 3200
"""Open socket server"""
mySocket = socket.socket()
mySocket.bind((host, port))
"""Listen socket and accept connection"""
mySocket.listen(1)
conn, addr = mySocket.accept()
time.sleep(2)
print("Connection from: " + str(addr))

print("Server using :\n1. quit \n2. lower [word]\n3. upper [word]")
"""Main lopp when conn is True and converting data from client"""
while True:
    try:
        data = conn.recv(1024).decode()
        if not data:
            break
        if str(data[:5]) == "lower":
            conn.send(data.encode().lower())
        elif str(data[:5]) == "upper":
            conn.send(data.encode().upper())
        elif str(data[:5]) != "upper" and str(data[:5]) != "lower" or str(data) == " ":
            data = "      ERROR ! \nServer using : \n1. quit \n2. lower \n3. upper"
            conn.send(data.encode())

    except:
        print("ERROR")
conn.close()