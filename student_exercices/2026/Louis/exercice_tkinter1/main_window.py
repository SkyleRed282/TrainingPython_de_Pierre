import tkinter
from alert_button import alertButton


class mainWindow(tkinter.Tk):

    def __init__(self):
        super().__init__()

        self.title('Some title')
        self.geometry('300x100')


        alertButton(master=self, text='Alert 1', alert_text="Alert 1")
        alertButton(master=self, text='Alert 2', alert_text="Alert 2")
        self.mainloop()