from guizero import App, MenuBar, TextBox
from random import randint
from datetime import datetime
from time import sleep
now = datetime.now()
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

def Encrypt_file():
    print("Encrypt file option: Sorry, but this option is currently a WIP. For now the only way to encrypt a message is to type the message in manually. (or copy-paste the message)")

def Decrypt_file():
    print("Decrypt file option: Sorry, but this option is currently a WIP. For now the only way to decrypt an encrypted message is to type the message in manually. (or copy-paste the message)")

def Encrypt_user():
    print("Encrypt user option")

def Decrypt_user():
    print("Decrypt user option")

def Generate():
    print("Generate option")
    sheetin = TextBox(app, 'OTP Count')
    lengthin = TextBox(app, 'Length')
    #sheets = int(input('How many one-time pads would you like to generate? '))
    #length = int(input('What will be your maximum message length? '))
    sheets = int(sheetin.get())
    length = int(lengthin.get())
    for sheet in range(sheets):
        with open("otp " + str(now.year) + " "+ str(now.month) + " " + str((now.day + sheet) % 30) + ".txt","w") as  f:
            for i in range(length):
                f.write(str(randint(0,26))+"\n")
                
def Exit():
    print("Goodbye")
    exit()

app = App()
menubar = MenuBar(app,
                  ["Encrypt", "Decrypt", "Other"],
                  [
                      [ ["Encrypt from file", Encrypt_file], ["Encrypt user input", Encrypt_user] ],
                      [ ["Decrypt from file", Decrypt_file], ["Decrypt user input", Decrypt_user] ],
                      [ ["Generate one time pads", Generate ], ["Exit", Exit] ]
                  ])
app.display()
