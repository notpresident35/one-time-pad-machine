#Initial semi-finished one time pad machine.
#still stretching out the gui muscles
from guizero import App, MenuBar, TextBox, PushButton
from random import randint
from datetime import datetime
from time import sleep
now = datetime.now()
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
done = False

def button():
    done = True
    print("True")
def get_plaintext():
    plaintext = input('Please type your message ')
    return plaintext.lower()

def load_sheet(filename):
    with open(filename, "r") as f:
        contents = f.read().splitlines()
    return contents

def load_file(filename):
    with open(filename, "r") as f:
        contents = f.read()
    return contents

def save_file(filename, data):
    with open(filename, 'w') as f:
        f.write(data)

def Decrypt():
    plaintext = ''
    for position, character in enumerate(ciphertext):
        if character not in ALPHABET:
            plaintext += character
        else:
            decrypted = (ALPHABET.index(character) - int(sheet[position])) % 26
            plaintext += ALPHABET[decrypted]
    return plaintext

def Encrypt():
    print("Encrypt user option")
    ciphertext = ''
    for position, character in enumerate(plaintext):
        if character not in ALPHABET:
            ciphertext += character
        else:
            encrypted = (ALPHABET.index(character) + int(sheet[position])) % 26
            ciphertext += ALPHABET[encrypted]
    return ciphertext

def Encrypt_file():
    print("Encrypt file option: Sorry, but this option is currently a WIP. For now the only way to encrypt a message is to type the message in manually. (or copy-paste the message)")

def Decrypt_file():
    print("Decrypt file option: Sorry, but this option is currently a WIP. For now the only way to decrypt an encrypted message is to type the message in manually. (or copy-paste the message)")

def Encrypt_user():
    filename = input('Type in the filename of the OTP you want to use ')
    sheet = load_sheet(filename)
    plaintext = get_plaintext()
    ciphertext = encrypt(plaintext, sheet)
    filename = input('What will be the name of the encrypted file? ')
    save_file(filename, ciphertext)
    
def Decrypt_user():
    print("Decrypt user option")
    filename = input('Type in the filename of the OTP you want to use ')
    sheet = load_sheet(filename)
    filename = input('Type in the name of the file to be decrypted ')
    ciphertext = load_file(filename)
    plaintext = decrypt(ciphertext, sheet)
    print('The message reads:')
    print('')
    print(plaintext)
def Generate():
    print("Generate option")
    #sheets = int(input('How many one-time pads would you like to generate? '))
    #length = int(input('What will be your maximum message length? '))
    sheetin = TextBox(app, '1')
    lengthin = TextBox(app, '1')
    pushbutton = PushButton(app, button, text="done")
    while True:
        pushbutton = PushButton(app, button)
        #if sheetin.get() != "1" & lengthin.get() != '1':
        print(done)
        if done == True:
            print("sucessful entry")
            #sheetin = TextBox(app, '1')
            #lengthin = TextBox(app, '1')
            sheets = int(sheetin.get())
            print("3")
            length = int(lengthin.get())
            print("exiting")
            break
    print("done")
    for sheet in range(sheets):
        with open("otp " + str(now.year) + " "+ str(now.month) + " " + str((now.day + sheet) % 30) + ".txt","w") as f:
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
