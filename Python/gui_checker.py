import tkinter as tk
from passwords import *

class Application(tk.Frame):
    '''
    Visualise phone numbers and minutes associated with them.
    '''
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        data = getData()
        for phone in data:
            self.text = tk.Label(self, text=phone)
            # Using grid instead of pack - has row and col, alight(sticky)
            self.text.grid(sticky='W')

        self.exit = tk.Button(self, text="Изход", fg="red", command=root.destroy)
        self.exit.grid()
        # self.exit.pack(side="bottom")

root = tk.Tk()
root.title = 'Latest topics'
app = Application(master=root)
app.mainloop()