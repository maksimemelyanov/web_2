import socket
import os.path

HOST = "localhost"
PORT = 8000

sock = socket.socket()
sock.bind((HOST, PORT))
sock.listen(5)

while True:
    connection, address = sock.accept()
    data = connection.recv(2048)
    address = data.split('\n')[0].split(' ')[1]
    path=''
    path = './' + address
    
    if not os.path.isfile(path):
        path ='./index.html'
            
    file = open(path, 'rb')
    connection.send("""HTTP/1.1 200 OK\nContent-Type: text/html\n\n\n""" + file.read())
    file.close()
    connection.close()    
sock.close()