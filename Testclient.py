#Test Client for the MSNB-Server

import socket
import pickle
import threading

HOST = "127.0.0.1"
PORT = 61111

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))



def send():
    Tuple= ("Green","2x4y")
    
    while True:
        data = input("senden: ")
        
        if (data == "tuple"):
            print("Send Tuple")
            s.sendall(pickle.dumps(Tuple))
            continue
        
        if (data == "end"):
            #send server that user has left
            print("closing connections...")
            s.sendall(pickle.dumps(data))
            s.close()
            send_thread.join()
            
            #Force program to end (Produces Errors)
            try:
                exit (0)
            except ConnectionAbortedError:
                pass
            
        s.sendall(pickle.dumps(data))

        
def receive():
    received = s.recv(1024)#Empfangen
    #print(repr(data))
    received_readable = pickle.loads(received)
    received_readable = pickle.loads(received_readable)
    print("\nreceived: ", received_readable)


while 1:
    #Start threading
    send_thread = threading.Thread(target=send)
    send_thread.daemon = True
    send_thread.start()
    
    #receive_thread = threading.Thread(target=receive)
    #receive_thread.start()
    receive()
    


        




