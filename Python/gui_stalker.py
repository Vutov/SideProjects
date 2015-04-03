import tkinter as tk
from stalker import *

class Application(tk.Frame):
    '''
        Visualizing the latest data got from stalker
    '''
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        # data = ['За обучителната система  - въпроси/предложения/бъгове 02/04/2015 03:30:10', '[Team Building] Следизпитно парти - 05.04 - Желаещи? 01/04/2015 12:20:47', '[Team Building] Танго - безплатен урок - 7ми април 30/03/2015 12:34:51', '[Homework] Digital Marketing & SEO - “Подготовка към проекта” 03/04/2015 15:32:05', 'Места, на които трябва да седим по време на изпита 03/04/2015 15:06:12', '[Homework] Programming Basics - Math for developers - Problem {3} 03/04/2015 14:57:55', '[Technical Issue] Prodvigator.bg 03/04/2015 13:08:16', '[Technical Issue] Системата за определяне на място на изпита 03/04/2015 12:50:52', '[Useful Info] SEO - за начинаещи (книга) - На Български! 03/04/2015 12:13:39', 'Мога ли да ползвам WordPress website за целите на курсов проект? 03/04/2015 11:43:18', 'Нощувка в София 03/04/2015 06:14:16', 'Какво следва след приемния изпит? 03/04/2015 04:44:51', '[Technical Issue] Visual Studio - Преместване 03/04/2015 01:47:58']
        data = get_topics()
        for topic in data:
            self.text = tk.Label(self, text=topic)
            # Using grid instead of pack - has row and col, alight(sticky)
            self.text.grid(sticky='W')
            # self.text.pack(side='top')

        self.exit = tk.Button(self, text="QUIT", fg="red", command=root.destroy)
        self.exit.grid()
        # self.exit.pack(side="bottom")

root = tk.Tk()
root.title = 'Latest topics'
app = Application(master=root)
app.mainloop()