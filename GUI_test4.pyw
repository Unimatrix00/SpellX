from tkinter import *

class App(Frame):
    
    def run_script(self):
        sys.stdout = self
        import SpellX_by_Attila_Kardos      # Call my script

    def build_widgets(self):
        self.text1 = Text(self)
        self.text1.pack(side=TOP)
        self.button = Button(self)
        self.button["text"] = "Trigger script"
        self.button["command"] = self.run_script
        self.button.pack(side=TOP)

    def write(self, txt):
        self.text1.insert(INSERT, txt)
        self.update_idletasks()             # Force the GUI to update
        
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.build_widgets()
              

root = Tk()
root.title("Spell-X")           # To setup the name of the window
root.wm_iconbitmap('XX.ico')    # To replace the Tkinter icon
app = App(master = root)
app.mainloop()

