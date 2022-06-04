import socket
import select

HEADER_LENGTH = 10

IP = "192.168.219.30"
PORT = int(input("Set the port to 1000 to 9999: "))


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind((IP, PORT))

server_socket.listen()
sockets_list = [server_socket]

clients = {}
print(f'Listening for connections on the ip of {IP} and a port of {PORT}...')


def receive_message(client_socket):

    try:
        message_header = client_socket.recv(HEADER_LENGTH)
        
        if not len(message_header):
            return False

        message_length = int(message_header.decode('utf-8').strip())
        return {'header': message_header, 'data': client_socket.recv(message_length)}

    except:
        return False

while True:
    read_sockets, _, exception_sockets = select.select(sockets_list, [], sockets_list)
   
    for notified_socket in read_sockets:
        if notified_socket == server_socket:
            client_socket, client_address = server_socket.accept()
            user = receive_message(client_socket)
            
            if user is False:
                continue

            sockets_list.append(client_socket)
            clients[client_socket] = user

            print('New connection from {}:{}, username: {}'.format(*client_address, user['data'].decode('utf-8')))

        else:
            message = receive_message(notified_socket)

            if message is False:
                print('Closed connection from: {}'.format(clients[notified_socket]['data'].decode('utf-8')))
                sockets_list.remove(notified_socket)

                del clients[notified_socket]
                continue
           
            user = clients[notified_socket]

            print(f'New message from {user["data"].decode("utf-8")}: {message["data"].decode("utf-8")}')

            for client_socket in clients:
                if client_socket != notified_socket:
                    client_socket.send(user['header'] + user['data'] + message['header'] + message['data'])

    for notified_socket in exception_sockets:
        sockets_list.remove(notified_socket)
        del clients[notified_socket]