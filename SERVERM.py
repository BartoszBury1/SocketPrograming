

import linecache

import random
from _thread import *
import socket as s





HOST = s.gethostbyname(s.gethostname())
PORT = 5050 
BUFFER = 1024

server_socket = s.socket()


server_socket = s.socket(s.AF_INET, s.SOCK_STREAM)
server_socket.bind((HOST , PORT))


server_socket.listen(3)

while True:

    client_socket, address = server_socket.accept()

    print(f"Uzyskano połączenie od {address}| ")
    

    msg = "Witaj w banku BARBANK\n"  "1) Stwórz nowe konto\n" "2) Zaloguj się\n""0) Wyjście z aplikacji".encode("utf-8")
    client_socket.send(msg)
    


    
    index = client_socket.recv(BUFFER).decode("utf-8")
    #print(f"{index}")



    

    def welcome():

        ind = index.encode("utf-8")
        client_socket.send(ind)
        
        
        if index == "1":

                fname = client_socket.recv(BUFFER).decode("utf-8")
                print(f"{fname}")
                        
                with open (f"{fname}.txt", "w") as f:
                    f.write(f"{fname}")

                PESEL = client_socket.recv(BUFFER).decode("utf-8")
                print(f"{PESEL}")

                with open (f"{fname}.txt", "a") as f:
                    f.write(f"\n{PESEL}\n")
                        
                passwd = client_socket.recv(BUFFER).decode("utf-8")
                print(f"{passwd}")

                with open (f"{fname}.txt", "a") as f:
                    f.write(f"{passwd}\n")

                surname = client_socket.recv(BUFFER).decode("utf-8")
                print(f"{surname}")


                with open (f"{fname}.txt", "a") as f:
                    f.write(f"{surname}\n")    



                Nrkonta =  random.randint(10000,100000)
                with open(f"{fname}.txt" , "a") as f:
                    f.write("%d \n" % Nrkonta)

                msg4 = "Dziękujemy za stworzenie konta! \n".encode("utf-8")
                client_socket.send(msg4)

                msgL = "Kliknij 1) aby się teraz zalogować".encode("utf-8")
                client_socket.send(msgL)

                Zalog = client_socket.recv(BUFFER).decode("utf-8")
                #print(Zalog)
                if Zalog == "1":
                    print("Siema stary chuju")
    
                    
                             

            
    def Login():                         

        if index == "2":


                fname = client_socket.recv(BUFFER).decode("utf-8")
                #print(f"{fname}")

                    
                passwdc = client_socket.recv(BUFFER).decode("utf-8")
                #print(f"{passwdc}")


                
                linia =  linecache.getline(f"{fname}.txt",3)
                if f"{passwdc}" in linia.split():
                    msgA = "Witaj na swoim koncie "f"{fname}\n".encode("utf-8")
                    client_socket.send(msgA)

                    msgS = "1) Wpłać środki\n2) Sprawdź dostępne saldo".encode("utf-8")
                    client_socket.send(msgS)


                    WysSaldo = client_socket.recv(BUFFER).decode("utf-8")
                    #print(f"{WysSaldo}")
                    
                    if WysSaldo == "1":

                        msgWS = "Podaj kwote do wpłaty: ".encode("utf-8")
                        client_socket.send(msgWS)

                        Kwota = int(client_socket.recv(BUFFER).decode("utf-8"))
                        print(int(Kwota))


                        with open(f"{fname}.txt" , "a") as f:
                            f.write("%d \n" % Kwota)

                    if WysSaldo == "2":

                        LineSaldo = linecache.getline(f"{fname}.txt",6).encode("utf-8")
                        client_socket.send(LineSaldo)

                        print(LineSaldo)
                        

                        

                        

                else:
                    msgD = "Hasło się nie zgadza spróbuj ponownie "f"{fname}".encode("utf-8")
                    client_socket.send(msgD)
                    
                    
                    
    
    welcome()
    Login()
    
    
    
    
    

    

            

            
            

    
     
        


    if index == "0":
        discon = client_socket.recv(BUFFER).decode("utf-8")
        discon = "Wyszedłeś z aplikacji".encode("utf-8")
        client_socket.send(discon)
        s.close()
        
        

    
        





    
    
       


        
        
  


#passwd = client_socket.recv(BUFFER).decode("utf-8")
     #   print({passwd})


        

       

        


    








#    if index == "2":
#        msg2 = "Podaj login".encode("utf-8")
#        client_socket.send(msg2)
#
#        user_name = client_socket.recv(BUFFER).decode("utf-8")
#        print(f"{user_name}")
#    elif f == fname:
#        print("co chcesz dalej zrobić")
#
        
         
       
    
    
    
 
    



#
#    else :
#        msg3 = "Zły wybór".encode("utf-8")
#        client_socket.send(msg3)


  
    

    
    



