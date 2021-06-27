# Server NV&OS Mensch sei nicht beleidigt!
#Import libraries
import socket
import threading
import pickle
import time

#set global variables
global client_conn
client_conn = []
global turn_player
turn_player = 0

def broadcast(data, conn):
    global client_conn
    #send received to all clients
    print(client_conn)
    for clients in client_conn:
        #except sender
        if conn == clients:
            continue
        clients.sendall(data)

def echo(conn, addr):
    global client_conn, turn_player
    packet = []
    print('Connected by', addr)

    #not add connection to list if there are four players
    if (len(client_conn) >= 4):
        pass
    
    #Add player to conn list
    else:
        client_conn.append(conn)
    print("einträge Conn liste: ", len(client_conn))
    
    while True:
        data = conn.recv(4096)
        #if received is empty
        if not data:
            break
        
        packet.append(data)
        print(type(data))
        received = pickle.loads(b"".join(packet))
        packet = []
        print('Received:', received)
        print(type(received))
        
        if type(received) == str:
            broadcast(data, conn)
            #if new player has joined and sended NEW codeword
            if received == "NEW":
                
                #let first player start game
                if conn == client_conn[0]:
                    text = "TURN"
                    conn.sendall(pickle.dumps(text))
        
        else:
            #send gamefield to other players
            broadcast(data, conn)
    conn.close()

#set host IP and Port
HOST = '127.0.0.1'
PORT = 61111

#Initialize Server-Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()

#start threading
while True:
    conn, addr = s.accept()
    echo_thread = threading.Thread(target=echo, args=(conn, addr))
    echo_thread.start()