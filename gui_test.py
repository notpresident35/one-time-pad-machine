##from guizero import App, Text, TextBox, PushButton, Picture
##textOutput = "Hello"
##def say_hi():
##    welcome_message.set( hi_input.get() )
##app = App(title="Hello world")
##welcome_message = Text(app, text=textOutput)
##hi_input = TextBox(app)
##update_text = PushButton(app, command=say_hi, text="Display new text")
##google_pic = Picture(app, image="gui_test.gif")
##app.display()
import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=root.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

root = tk.Tk()
app = Application(master=root)
app.mainloop()
