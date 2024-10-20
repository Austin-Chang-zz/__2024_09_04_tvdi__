from ttkthemes import ThemedTk
from tkinter import ttk

class Window(ThemedTk):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.title('使用ttk的套件')
        style = ttk.Style(self)        
        topFrame = ttk.Frame(self,borderwidth=1,relief='groove')  # top frame ---------------
        topFrame.pack(padx=10,pady=(10,0),ipadx=10,ipady=10,expand=True,fill='x')

        btn1 = ttk.Button(topFrame,text="按鈕1")
        btn1.pack(side='left',expand=True,fill='x',padx=10)

        btn2 = ttk.Button(topFrame,text="按鈕2")
        btn2.pack(side='left',expand=True,fill='x')
        
        btn3 = ttk.Button(topFrame,text="按鈕3")
        btn3.pack(side='left',expand=True,fill='x',padx=10)
        
        bottomFrame = ttk.Frame(self,width=500,height=300,borderwidth=1,relief='sunken') # bottom frame ---------
        bottomFrame.pack(padx=10,pady=10)

        # create 3 columns in bottom frame
        for i in range(3):
            bottomFrame.columnconfigure(i,weight=1)
            bottomFrame.rowconfigure(0,weight=1)

        # create a frame in each column
        for col in range(3):
            column_frame = ttk.Frame(bottomFrame,relief='groove',borderwidth=2)
            column_frame.grid(row=0,column=col,sticky='nsew',padx=5)
            column_frame.columnconfigure(0,weight=1)
            if col == 0: # left column
                sizes = ["biggest",'small','small']
            elif col == 1: # middle column
                sizes = ["bigger","small","bigger"]
            else: # right column
                sizes = ["middle","middle","middle"]

            # add buttons in each column
            for row, size in enumerate(sizes):
                btn = ttk.Button(column_frame,text=size)
                if size == "biggest":
                    btn.grid(row=row,column=0,sticky="nsew",padx=5,pady=5,ipady=30)
                    column_frame.rowconfigure(row,weight=3)
                elif size == "bigger":
                    btn.grid(row=row,column=0,sticky="nsew",padx=5,pady=5,ipady=20)
                    column_frame.rowconfigure(row,weight=2)
                elif size == "middle":
                    btn.grid(row=row,column=0,sticky="nsew",padx=5,pady=5,ipady=5)
                    column_frame.rowconfigure(row,weight=1)
                else:
                    btn.grid(row=row,column=0,sticky="nsew",padx=5,pady=2,ipady=5)
                    column_frame.rowconfigure(row,weight=1)



def main():
    window = Window(theme="arc")
    window.mainloop()

if __name__ == '__main__':
    main()