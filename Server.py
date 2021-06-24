# Server NV&OS Mensch sei nicht beleidigt!
import socket
import threading
import pickle

client_conn = []
turn_player = 0

def broadcast(data, conn):
    #send received to all clients
    print (client_conn)
    for clients in client_conn:
        #except sender
        if conn == clients:
            continue
        clients.sendall(data)

def echo(conn, addr):    
    print('Connected by', addr)
    #add new connection to list
    if (len(client_conn) >= 4):
        #not add connection to list if there are four players
        pass
    else:
        client_conn.append(conn)
        
    print("einträge Conn liste: ", len(client_conn))
    
    while True:
        data = conn.recv(1024)
        print('Received from client', repr(data))
        received = pickle.loads(data)
        print('Received:', received)
        print(type(received))
        
        if type(received) == str:
            print("String")
            broadcast(data, conn)
            #if received == 
                #broadcast(data, conn)
            
        else:
            global turn_player
            #Spielfeld bzw. Positionen übertragen
            broadcast(data, conn)

            
            #decide which player ist the next
            if (turn_player >= len(client_conn)):
                turn_player = 0
                print("reset")
                
            print("spieler: ", turn_player)
            
            #send message that it is next players turn
            text = "Your Turn"
            client_conn[turn_player].sendall(pickle.dumps(text))
            
            turn_player += 1

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