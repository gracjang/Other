import socket
host = ''
port = 5000

mySocket = socket.socket()
mySocket.bind((host, port))

mySocket.listen(1)
conn, addr = mySocket.accept()
print("Connection from: " + str(addr))
print("Server using :\n1. quit \n2. lower [word]\n3. upper [word]")

while True:
    data = conn.recv(1024).decode()
    if not data:
        break
    if str(data[:5]) == "lower":
        conn.send(data.encode().lower())
    elif str(data[:5]) == "upper":
        conn.send(data.encode().upper())
    elif str(data[:5]) != "upper" and str(data[:5]) != "lower":
        data = "      ERROR ! \nServer using : \n1. quit \n2. lower \n3. upper"
        conn.send(data.encode())

conn.close()