from ast import Dict
import linecache
import pickle
import socket



HEADER = 1024
PORT = 5051 
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "Wyłączono"

SERVER = socket.gethostbyname(socket.gethostname() )
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM )

client.connect(ADDR)


def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length) )
    client.send(send_length)
    client.send(message)

Zalogowano = False    
connected = True
while connected:
    print("Witaj w Banku BartBNK \n 1) Zarejestruj się \n 2) Zaloguj się \n 0) wyłącz aplikację")

    msgIndex = input(">>> ")
    send(msgIndex)

    if  msgIndex == "1":

        msgLogin1 = input("Podaj Nazwe użytkownika >> ")
        send(msgLogin1)

        msgHaslo = input("Podaj Hasło >> ")
        send(msgHaslo)


        msgNazwisko = input("Podaj nazwisko >> ")
        send(msgNazwisko)

        msgPESEL = input("Podaj PESEL >> ")
        send(msgPESEL)


        print("Możesz się teraz zalogować!: ")
        
        
        
        

    if msgIndex == "2":
        msgLogin = input("Podaj Login >> ")
        send(msgLogin)

        msgHaslo = input("Podaj Hasło >> ")
        send(msgHaslo)

        
        f = open(f"konta\{msgLogin}.pkl", "rb")
        output = pickle.load(f)
        f.close()
        #print(type(output["Haslo"]))
        outputStr = " ".join(output["Haslo"])
        #print(type(outputStr))

                
        if outputStr == msgHaslo:
            Zalogowano = True
            print(f"Witaj na swoim koncie: {msgLogin}")
        elif output != msgHaslo:
            Zalogowano = False
            print("============================")
            print("Złe hasło zaloguj ponownie")
            print("============================")

    while Zalogowano:

            print(" 1) Wpłać pierwsze środki\n 2) Sprawdź dostępne saldo\n 3) Wypłać środki \n 0) Wyloguj")
            
            msgSaldo = input(">> ")
            
            send(msgSaldo)
            if msgSaldo == "1":
                    
                msgWprSaldo = input("Wprowadź kwote do wpłaty >>")
                send(msgWprSaldo)



            elif msgSaldo == "2":
                f = open(f"konta\{msgLogin}.pkl", "rb")
                output = pickle.load(f)
                f.close()
                print("Twoje dostępne środki: ")
                print("============")
                print(output["Saldo"].pop())
                print("============")
                
            #elif msgSaldo == "3":
             #   print("Twoje dostępne środki z których możesz wypłacić to: ")
            #    f = open(f"konta\{msgLogin}.pkl", "rb")
             #   output = pickle.load(f)
             #   f.close()
             #   print("============")
              #  print(output["Saldo"].pop())
              #  print("============")

              #  msgWypSaldo = input("Wprowadź kwote do wypłaty >>")
               # send(msgWypSaldo)

               # f = open(f"konta\{msgLogin}.pkl", "rb")
               # output = pickle.load(f)
               # f.close()
               # print("============")
               # print(output["Saldo"].pop()-msgWypSaldo)
               # print("============")

              

            elif msgSaldo == "0":
                print("Wyloguj")
                Zalogowano = False

    
        

                
            
        

        
        





















