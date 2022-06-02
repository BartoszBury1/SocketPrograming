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
    print("Witaj w swoim Banku \n 1) Zarejestruj się \n 2) Zaloguj się \n 0) wyłącz aplikację")

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
        
        f = open(f"konta\{msgLogin1}.pkl", "rb")
        output = pickle.load(f)
        f.close()
        print(output)
        
        

    if msgIndex == "2":
        msgLogin = input("Podaj Login >> ")
        send(msgLogin)

        msgHaslo = input("Podaj Hasło >> ")
        send(msgHaslo)

        
    
        linia =  linecache.getline(f"{msgLogin}.txt",2)
        if f"{msgHaslo}" in linia.split():
            Zalogowano = True
     
            print(f"witaj na swoim koncie: {msgLogin}\n")
        else:
            print("Złe hasło")
        while Zalogowano:  

                print(" 1) Wpłać środki\n 2) Sprawdź dostępne saldo\n 0) Wyloguj")
            
                msgSaldo = input(">> ")
            
                send(msgSaldo)
                if msgSaldo == "1":
                    
                    msgWprSaldo = input("Wprowadź kwote do wpłaty >>")
                    send(msgWprSaldo)

                elif msgSaldo == "2":
                    print("")
                    
                

                elif msgSaldo == "0":
                    print("Wyloguj")
                    Zalogowano = False

    
        

                
            
        

        
        





















