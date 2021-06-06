import socket,time
HOST = '127.0.0.1'   # Server's hostname or IP address
PORT = 1234          # Port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as Client:
    Client.connect((HOST, PORT))
    data = Client.recv(1024).decode()
    print('Server : '+data)
    msg = input('  -> ')
    while msg.lower().strip() != 'bye':
        Client.sendall(msg.encode())
        data = Client.recv(1024).decode()
        print(' Server : '+data)
        msg = input(' -> ')
    Client.close()    
