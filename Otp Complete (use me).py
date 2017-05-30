#This is the main project. All the other files are old and may not work as
#intended. Even so, this program still is a WIP, and still has a few large holes
#in need of fixing. Feel free to try to help.
from tkinter import *
#import guizero
from random import randint
from datetime import datetime
from time import sleep
now = datetime.now()
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
done = False
sheets = 0
length = 0
##"otp " + str(now.year) + " "+ str(now.month) + " " + str((now.day + sheet) % 30)
##"otp"+str(now.year)+str(now.month)+str((now.day) + ".txt","w"
##"otp"+str(now.year)+"/"+str(now.month)+"/"+str(now.day)+"-"+str(now.hour)+"."+str(now.minute)+"."+str(now.second)+"-No."+str(sheet)
def donebuttonGen():
    sheets = int(sheetin.get())
    length = int(lengthin.get())
    for sheet in range(sheets):
        with open("otp " + str(now.year) + " "+ str(now.month) + " " + str((now.day + sheet) % 30)+".txt","w") as f:
            for i in range(length):
                f.write(str(randint(0,26))+"\n")
    sheetin.delete(0, END)
    lengthin.delete(0, END)
    sheetin.insert(0, "number of OTPs")
    lengthin.insert(0, "length of each OTP")
    #sheetin.configure(state="disabled")
    #lengthin.configure(state="disabled")
    sheetin.pack_forget()
    lengthin.pack_forget()
    pushbutton.pack_forget()
    wordContents.set("One Time Pad Machine")

def donebuttonEncU():
    plaintext = ""
    sheet = load_sheet(filenameEncU.get())
    plaintext = get_plaintext(plaintext, sheet)
    
def donebuttonEncU2(plaintext3, sheet3):
    plaintext3 = filenameEncU.get()
    plaintext3 = plaintext3.lower()
    print(plaintext3)
    print(sheet3)
    ciphertextz = Encrypt(plaintext3, sheet3)
    print(ciphertextz)
    filenameEncU.delete(0, END)
    filenameEncU.insert(0, "Enter the name of the new file to save encrypted message on")
    pushbutton2.configure(command=lambda: donebuttonEncU3(plaintext3, sheet3, ciphertextz))

def donebuttonEncU3(plaintext4, sheet4, ciphertexts):
    filename = filenameEncU.get()
    save_file(filename, ciphertexts)
    print("Sucess, encrypted file saved")
    wordContents.set("Success, encrypted file saved")
    pushbutton2.configure(command=lambda: donebuttonEncU())
    pushbutton2.pack_forget()
    filenameEncU.pack_forget()
    sleep(1)
    wordContents.set("One Time Pad Machine")

def donebuttonDecU():
    sheet = load_sheet(filenameDecU.get())
    #filename = input('Type in the name of the file to be decrypted ')
    filenameDecU.delete(0, END)
    filenameDecU.insert(0, "Enter the name of the file to be decrypted")
    print(sheet)
    pushbutton3.configure(command=lambda: donebuttonDecU2(sheet))
    
def donebuttonDecU2(sheet2):
    filename = filenameDecU.get()
    ciphertext = load_file(filename)
    plaintext = Decrypt(ciphertext, sheet2)
    print('The message reads:')
    wordContents.set("The message reads:")
    sleep(1)
    print('')
    print(plaintext)
    print("Success")
    wordContents.set(plaintext)
    sleep((len(plaintext)/10)+1)
    filenameDecU.delete(0, END)
    filenameDecU.insert(0, "Type in the filename of the OTP you want to use ")
    pushbutton3.configure(command=lambda: donebuttonDecU())
    filenameDecU.pack_forget()
    pushbutton3.pack_forget()
    wordContents.set("One Time Pad Machine")

def test():
    wordContents.set("Success!")
    print("YOUUUUUU GOT IT!")
    sleep(1)
    wordContents.set("One Time Pad Machine")

def button():
    done = True
    print("True")
                
def get_plaintext(plaintext2, sheet2):
    print(plaintext2)
    print(sheet2)
    filenameEncU.delete(0, END)
    filenameEncU.insert(0, "Enter message to be encrypted")
    pushbutton2.configure(command=lambda: donebuttonEncU2(plaintext2, sheet2))
    
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

def Decrypt(ciphertext, sheet):
    plaintext = ''
    for position, character in enumerate(ciphertext):
        if character not in ALPHABET:
            plaintext += character
        else:
            decrypted = (ALPHABET.index(character) - int(sheet[position])) % 26
            plaintext += ALPHABET[decrypted]
    return plaintext

def Encrypt(plaintext, sheet):
    ciphertext = ''
    for position, character in enumerate(plaintext):
        if character not in ALPHABET:
            ciphertext += character
        else:
            #print((ALPHABET.index(character) + int(sheet[position])) % 26)
            encrypted = (ALPHABET.index(character) + int(sheet[position])) % 26
            ciphertext += ALPHABET[encrypted]
    return ciphertext

def Encrypt_file():
    wordContents.set('Option "Encrypt from file" failed. WIP option')
    print("Encrypt file option: Sorry, but this option is currently a WIP. For now the only way to encrypt a message is to type the message in manually. (or copy-paste the message)")
    sleep(1)
    wordContents.set("One Time Pad Machine")
    
def Decrypt_user():
    wordContents.set('Option "Decrypt user input" failed. WIP option')
    print("Decrypt user option: Sorry, but this option is currently a WIP. For now the only way to decrypt an encrypted message is to use a text file.")
    sleep(1)
    wordContents.set("One Time Pad Machine")

def Encrypt_user():
    wordContents.set("Encrypt a message")
    print("Encrypt user option")
    #filename = input('Type in the filename of the OTP you want to use')
    filenameEncU.pack()
    pushbutton2.pack()
    #plaintext = get_plaintext()
    #ciphertext = Encrypt(plaintext, sheet)
    #filename = input('What will be the name of the encrypted file? ')
    #save_file(filename, ciphertext)
    
def Decrypt_file():
    wordContents.set("Decrypt an encrypted message")
    print("Decrypt file option")
    filenameDecU.pack()
    pushbutton3.pack()
##    filename = input('Type in the filename of the OTP you want to use ')
##    sheet = load_sheet(filename)
##    filename = input('Type in the name of the file to be decrypted ')
##    ciphertext = load_file(filename)
##    plaintext = decrypt(ciphertext, sheet)
##    print('The message reads:')
##    print('')
##    print(plaintext)
    
def Generate():
    wordContents.set("Generate new one time pads")
    print("Generate option")
    #sheets = int(input('How many one-time pads would you like to generate? '))
    #length = int(input('What will be your maximum message length? '))
    sheetin.pack()
    lengthin.pack()
    pushbutton.pack()
    #while True:
    #pushbutton = guizero.PushButton(app, button, text="done")
    #if sheetin.get() != "1" & lengthin.get() != '1':
    #print(done)
    #print("exiting")
    #break
    #print("done")
    
##def Exit():
##    print("Goodbye")
##    exit()

##app = guizero.App()
window = Tk()
words = Label(window, text="")
wordContents = StringVar()
words["textvariable"] = wordContents
wordContents.set("One Time Pad Machine")
words.pack()
sheetin = Entry(window)
lengthin = Entry(window)
filenameEncU = Entry(window)
filenameDecU = Entry(window)
sheetin.insert(0, "number of OTPs")
lengthin.insert(0, "length of each OTP")
filenameEncU.insert(0, "Type in the filename of the OTP you want to use")
filenameDecU.insert(0, "Type in the filename of the OTP you want to use ")
pushbutton = Button(window, command=donebuttonGen, text="Done")
pushbutton2 = Button(window, command=donebuttonEncU, text="Done")
pushbutton3 = Button(window, command=donebuttonDecU, text="Done")
window.title("One Time Pad")
window.geometry("300x300")
#ent = Entry(window)
#btn = Button(window, command=button, text="Button")
menubar = Menu(window)
#encryptbar = Menu(menubar)
menubar.add_command(label="Generate", command=Generate)
menubar.add_command(label="Exit", command=window.destroy)
encmenu = Menu(menubar, tearoff=0)
encmenu.add_command(label="Encrypt from file", command=Encrypt_file)
encmenu.add_command(label="Encrypt user input", command=Encrypt_user)
menubar.add_cascade(label="Encrypt", menu=encmenu)
decmenu = Menu(menubar, tearoff=0)
decmenu.add_command(label="Decrypt from file", command=Decrypt_file)
decmenu.add_command(label="Decrypt user input", command=Decrypt_user)
decmenu.add_separator()
decmenu.add_command(label="Derp", command=test)
menubar.add_cascade(label="Decrypt", menu=decmenu)
##                  ["Encrypt", "Decrypt", "Other"],
##                  [
##                      [ ["Encrypt from file", Encrypt_file], ["Encrypt user input", Encrypt_user] ],
##                      [ ["Decrypt from file", Decrypt_file], ["Decrypt user input", Decrypt_user] ],
##                      [ ["Generate one time pads", Generate ], ["Exit", Exit] ]
##                  ])

#ent.pack()
#btn.pack()
window.config(menu=menubar)
#app.display()
window.mainloop()
