
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
                

                Dict["UserName"] = {msg}

                f = open(f"konta\{msg}.pkl", "wb")
                pickle.dump(Dict, f)
                f.close()

            


                msg_length = conn.recv(HEADER).decode(FORMAT)
                if msg_length: 
                    msg_length = int(msg_length)
                    msgHaslo = conn.recv(msg_length).decode(FORMAT)
               

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
#Login
                msg_length = conn.recv(HEADER).decode(FORMAT)
                if msg_length: 
                    msg_length = int(msg_length)
                    msgLogin = conn.recv(msg_length).decode(FORMAT)

                    
                f = open(f"konta\{msgLogin}.pkl", "rb")
                output = pickle.load(f)
                f.close()
                print(output["UserName"])

                  
                

#Hasło
                msg_length = conn.recv(HEADER).decode(FORMAT)
                if msg_length: 
                    msg_length = int(msg_length)
                    msgHaslo = conn.recv(msg_length).decode(FORMAT)
                
                f = open(f"konta\{msgLogin}.pkl", "rb")
                output = pickle.load(f)
                f.close()
                print(type(output["Haslo"]))
                outputStr = " ".join(output["Haslo"])
                print(type(outputStr))

                if outputStr == msgHaslo:
                    msg_length = conn.recv(HEADER).decode(FORMAT)
                    if msg_length: 
                        msg_length = int(msg_length)
                        msgSaldo = conn.recv(msg_length).decode(FORMAT)
                        #print(msgSaldo)

               



                if msgSaldo == "1":
                    msg_length = conn.recv(HEADER).decode(FORMAT)
                    if msg_length: 
                        msg_length = int(msg_length)
                        msgWprSaldo = conn.recv(msg_length).decode(FORMAT)

                    #print(msgWprSaldo)

                    Dict["Saldo"] = {msgWprSaldo}
                    f = open(f"konta\{msgLogin}.pkl", "wb")
                    pickle.dump(Dict, f)
                    f.close()
                 

                if msgSaldo == "3":
                    msg_length = conn.recv(HEADER).decode(FORMAT)
                    if msg_length: 
                        msg_length = int(msg_length)
                        msgWypSaldo = conn.recv(msg_length).decode(FORMAT)

                        print(msgWypSaldo)

                
                    #    Dict["Saldowyp"] = {msgWprSaldo-msgWypSaldo}
                     #   f = open(f"konta\{msgLogin}.pkl", "wb")
                      #  pickle.dump(Dict, f)
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


