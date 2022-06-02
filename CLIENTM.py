import socket as s
import linecache

BUFFER = 1024
host = s.gethostbyname(s.gethostname())
port = 5050

client_socket = s.socket(s.AF_INET, s.SOCK_STREAM)
client_socket.connect((host,port))

while True:

    print(client_socket.recv(BUFFER).decode("utf-8"))

    
    
    index = input(">>> ").encode("utf-8")
    client_socket.send(index)
        
    ind = (client_socket.recv(BUFFER).decode("utf-8"))


 
    if  ind == "1" :
        fname = input("Podaj Login>> ").encode("utf-8")
        client_socket.send(fname)

        PESEL = input("Podaj pesel>> ").encode("utf-8")
        client_socket.send(PESEL)

        passwd = input("Podaj hasło>> ").encode("utf-8")
        client_socket.send(passwd)

        surrname = input("Podaj nazwisko>> ").encode("utf-8")
        client_socket.send(surrname)  

        print(client_socket.recv(BUFFER).decode("utf-8"))

        print(client_socket.recv(BUFFER).decode("utf-8")) 

        
        

    
    if ind == "2":
        
        fname = input("Podaj Login>> ").encode("utf-8")
        client_socket.send(fname)
            
        passwdc = input("Podaj Swoje hasło>> ").encode("utf-8")
        client_socket.send(passwdc)

        msgS  = (client_socket.recv(BUFFER).decode("utf-8"))
        print(msgS)

        msgA  = (client_socket.recv(BUFFER).decode("utf-8"))
        print(msgA)

        WysSaldo = input(">>>> ").encode("utf-8")
        client_socket.send(WysSaldo)

        
        if WysSaldo == "1":
            msgWS = (client_socket.recv(BUFFER).decode("utf-8"))
            print(msgWS)

            WprKwote = input(">>>> ").encode("utf-8")
            client_socket.send(WprKwote)

        
        if WysSaldo == "2":

            Saldo = (client_socket.recv(BUFFER).decode("utf-8"))
            print(f"Dostępne saldo: {Saldo}")

        





        

        

     

    if ind == "0":
        discon = "Wyjście z aplikacji".encode("utf-8")
        client_socket.send(discon)
        print(client_socket.recv(BUFFER).decode("utf-8"))

        

    
  



 




    



    
 




#user_name = input("Login>>").encode("utf-8")
#client_socket.send(user_name)


#print(client_socket.recv(BUFFER).decode("utf-8"))

