
import linecache
import pickle
import socket
import threading
import random

HEADER = 1024
PORT = 5051 

SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT )
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "  !DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM )
server.bind(ADDR)



def handle_client(conn, addr  ):
    print(f"[NEW CONNECTION] {addr} connected. ")
    
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length: 
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False


            
            if msg == "1":
                Dict = {}
                
                msg_length = conn.recv(HEADER).decode(FORMAT)
                if msg_length: 
                    msg_length = int(msg_length)
                    msg = conn.recv(msg_length).decode(FORMAT)
                    #if msg == DISCONNECT_MESSAGE:
                        #connected = False
                #print(msg) Nazwa użytkownika

                Dict["Nazwa użytkownika"] = {msg}

                f = open(f"konta\{msg}.pkl", "wb")
                pickle.dump(Dict, f)
                f.close()

               # with open (f"{msg}.txt", "w") as f:
                #   f.write(f"{msg}\n")
                 #   f.close()


                msg_length = conn.recv(HEADER).decode(FORMAT)
                if msg_length: 
                    msg_length = int(msg_length)
                    msgHaslo = conn.recv(msg_length).decode(FORMAT)
                   # if msg == DISCONNECT_MESSAGE:
                       # connected = False
                #print(msgHaslo) Hasło

                Dict["Haslo"] = {msgHaslo}

                f = open(f"konta\{msg}.pkl", "wb")
                pickle.dump(Dict, f)
                f.close()

                

                msg_length = conn.recv(HEADER).decode(FORMAT)
                if msg_length: 
                    msg_length = int(msg_length)
                    msgNazwisko = conn.recv(msg_length).decode(FORMAT)
                   
                #print(msgNazwisko) Nazwisko

                Dict["SurName"] = {msgNazwisko}

                f = open(f"konta\{msg}.pkl", "wb")
                pickle.dump(Dict, f)
                f.close()

               

                msg_length = conn.recv(HEADER).decode(FORMAT)
                if msg_length: 
                    msg_length = int(msg_length)
                    msgPESEL = conn.recv(msg_length).decode(FORMAT)
                  
                #print(msgNazwisko) Nazwisko

                Dict["PESEL"] = {msgPESEL}
                f = open(f"konta\{msg}.pkl", "wb")
                pickle.dump(Dict, f)
                f.close()

               
        
                Dict["NrKonta"] = {random.randint(10000,100000)}
                f = open(f"konta\{msg}.pkl", "wb")
                pickle.dump(Dict, f)
                f.close()

           
            elif msg == "2":

                msg_length = conn.recv(HEADER).decode(FORMAT)
                if msg_length: 
                    msg_length = int(msg_length)
                    msgLogin = conn.recv(msg_length).decode(FORMAT)
                    
           

            

                  
                #print(msgLogin) Login


                msg_length = conn.recv(HEADER).decode(FORMAT)
                if msg_length: 
                    msg_length = int(msg_length)
                    msgHaslo = conn.recv(msg_length).decode(FORMAT)


                  
                #print(msgHaslo) Hasło





                #linia =  linecache.getline(f"{msgLogin}.txt",2)
               # if f"{msgHaslo}" in linia.split():
                 #   msg_length = conn.recv(HEADER).decode(FORMAT)
                  #  if msg_length: 
                 #       msg_length = int(msg_length)
                  #      msgSaldo = conn.recv(msg_length).decode(FORMAT)
                    
                    #print(msgSaldo) # Saldo

                   # if msgSaldo == "1":
                      #  msg_length = conn.recv(HEADER).decode(FORMAT)
                       # if msg_length: 
                       #     msg_length = int(msg_length)
                       #     msgWprSaldo = conn.recv(msg_length).decode(FORMAT)
                    

                       # f = open(f"{msgLogin}.txt" , "a")
                       # f.write(msgWprSaldo)
                       # f.close()

                        

    

    conn.close()

    
    
                                
        

def start():
    server.listen()
    print(f"[Nasłuchiwanie] Server nasłuchuje na {SERVER} ")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn,addr))
        thread.start()
        print(f"[Aktywne połączenia: ] {threading.active_count() - 1}")


print("[Włączanie] Serwer się włącza")
start()


