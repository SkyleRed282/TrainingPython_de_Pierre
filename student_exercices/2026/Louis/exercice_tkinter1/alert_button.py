import tkinter
from tkinter.messagebox import showinfo


class alertButton(tkinter.Button):

    def __init__(self, master, text, alert_text):
        super().__init__(
            master=master,
            text=text,
            command=self.show_alert
        )

        self.alert_text = alert_text
        self.pack(padx=10, pady=5)

    def show_alert(self):
        showinfo(message=self.alert_text)
