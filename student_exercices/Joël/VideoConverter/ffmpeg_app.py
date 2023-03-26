import tkinter as tk
 
 
LARGE_FONT= ("Verdana", 12)
ser = None
file = None
 
class MarkerApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        
        container.pack(side = "top", fill = "both", expand = True)
        
        container.grid_rowconfigure(0,weight = 1)
        container.grid_columnconfigure(0,weight = 1)
        
        self.frames = {}
        
        for F in (StartPage):
        
            frame = F(container,self)
            
            self.frames[F] = frame
            
            frame.grid(row = 0, column = 0, sticky = "nsew")
        
        self.show_frame(StartPage)
        
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
 
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text = "Test Joel", font = LARGE_FONT)
        label.grid(row = 0, column = 0)

        self.btnScan = tk.Button(self, text="Scan Ports",
                         command=self.scan_ports, height = 10, width = 20)
        
        self.txtPort = tk.Text(self,height = 10, width = 80 )
        self.ePort = tk.Entry(self, width = 80)
        self.ePort.insert(0, "Enter Arduino Port Number")
        
        self.btnScan.grid(row = 1, column = 0)
        self.txtPort.grid(row = 1, column = 1)
        self.btnConn.grid(row = 2, column = 0)
        self.ePort.grid(row = 2, column = 1)
        
    def scan_ports(self):
      
        ports = list(serial.tools.list_ports.comports())
        for p in ports:
          print (p)
          self.txtPort.insert(tk.END,p)
          
          self.txtPort.insert(tk.END,"\n")