import socket
import time

host_name = "localhost"
port = 4545

web_socket = socket.socket()
web_socket.connect((host_name,port))

print("connection establised {}{}".format(host_name, port))

message = input("----::")
print("server loading...")

while message != "çıkış":
    web_socket.send(message.encode())
    gelen_veri = web_socket.recv(1024).decode()

    print("SERVER: " + gelen_veri)

    message = input("----::")
    print("server loading...")

web_socket.close()