# Server
#2do check Tuple
#Let send sth work
import socket
import threading
import pickle

client_conn = []

def broadcast(data, conn):
    #send received to all clients
    print (client_conn)
    for clients in client_conn:
        #Except sender
        #if conn == clients:
            #Not send Message to sender
         #   continue
        
        clients.sendall(data)


def echo(conn, addr):
    
    print('Connected by', addr)
    
    #add new connection to list
    client_conn.append(conn)

    while True:
        data = conn.recv(1024)
        print('Received from client', repr(data))
        received = pickle.loads(data)
        print('Received:', received)
        print(type(received))
        
        if type(received) == str:
            print("String")
            broadcast(data, conn)
            
            #M#aybe later needed##
            #add new player
            #if received == "red" or received == "green" or received == "jellow" or received == "green":
                #broadcast(data, conn)
                #client_conn.append(conn)
            
        elif type(received) == tuple:
            #Spielfeld bzw. Positionen übertragen
            print("Tuple")
            broadcast(data, conn)

    conn.close()



HOST = '127.0.0.1' 
PORT = 61111

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()
while True:
    conn, addr = s.accept()
    echo_thread = threading.Thread(target=echo, args=(conn, addr))
    echo_thread.start()