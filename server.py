import socket
import time

host_name = "localhost"
port = 4545

web_socket = socket.socket()
web_socket.bind((host_name, port))
web_socket.listen(1)

connecct, address = web_socket.accept()

print(str(address) + "connection establised")

while True:
    while True:
        try:
           gelen_veri = str(connecct.recv(1024).decode())
           print("client şunu yolladı: " + gelen_veri)
           break
        except ConnectionResetError:
           time.sleep(2)
           connecct, address = web_socket.accept()
           print(str(address) + "connection establised")
    if gelen_veri  == "çıkış":
        break
    else:
        message = input("----::")
        print("client bekleniyor")
        connecct.send(message.encode())

connecct.close()