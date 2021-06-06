import socket
HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 1234        
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as Server:
    Server.bind((HOST, PORT))
    Server.listen()
    print (" Started listening at IP :%s  Port :  %s "%(HOST, PORT))
    print (' Waiting for a connection ....')
    connection, address = Server.accept()
    with connection:
        print(' Connection has been established with', address)
        connection.sendall(b'Start sending!')
        while True:
            data = connection.recv(1024).decode()
            if not data:
                print (' No more data from client, Session has been terminated ')
                break

            print(" Client: " + str(data))
            data = input('  -> ')
            connection.sendall(data.encode())
