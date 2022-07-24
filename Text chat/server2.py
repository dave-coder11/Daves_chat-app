import socket
import threading
 
PORT = 5050
 

SERVER = socket.gethostbyname(socket.gethostname())
 
ADDRESS = (SERVER, PORT)
 

FORMAT = "utf-8"
 

clients, names = [], []

server = socket.socket(socket.AF_INET,
                       socket.SOCK_STREAM)

server.bind(ADDRESS)

 
 
def startChat():
 
    print("server is working on " + SERVER)
 
    server.listen()
 
    while True:
 
        conn, addr = server.accept()
        conn.send("NAME".encode(FORMAT))
 
        name = conn.recv(1024).decode(FORMAT)
 

        names.append(name)
        clients.append(conn)
 
        print(f"Name is :{name}")
 

        broadcastMessage(f"{name} has joined the chat!".encode(FORMAT))
 
        conn.send('Connection successful!'.encode(FORMAT))
 

        thread = threading.Thread(target=handle, args=(conn, addr))
        thread.start()
 

        print(f"active connections {threading.activeCount()}")
 

 
def handle(conn, addr):
 
    print(f"new connection {addr}")
    connected = True
 
    while connected:
        message = conn.recv(1024)
 
        broadcastMessage(message)
 

    conn.close()
 

 
 
def broadcastMessage(message):
    if message[0] == '@':
        i = 1
        while message[i] != ' ':
            end_message = end_message + message[i]
            i += 1
        if end_message == 'server ':
            length = len(message)
            while length != 0:
                end_message_server = end_message_server + message[i]
                i =+ 1
                length =-1
            print(f'A message for the server ({end_message_server}).')

            
    for client in clients:
        client.send(message)
 
 
startChat()