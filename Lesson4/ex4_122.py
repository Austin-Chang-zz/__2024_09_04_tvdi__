import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk


class Window(ThemedTk):
    def __init(self,*args, **kwargs):
        super().__init__(*args,**kwargs)
        self.title("TkThemes GUI Layout")

        # Create a frame for buttons
        top_frame = ttk.Frame(self,borderwidth=1,relief='sunken')
        top_frame.pack(padx=10,expand=True,fill='x')

        # Configure 3 equal-sized columns in the top frame
        for i in range(3):
            top_frame.columnconfigure(i, weight=1)


        # Create buttons in a grid layout
        for i in range(3):
            btn = ttk.Button(top_frame, text=f"Button {i+1}")
            btn.grid(row=0, column=i, sticky=tk.EW, padx=5)  # Use grid with sticky to extend



        # set up the main frame
        main_frame = ttk.Frame(self)
        main_frame.pack(fill=tk.BOTH,expand=True,padx=10,pady=10)

        # create 3 columns in main frame
        for i in range(3):
            main_frame.columnconfigure(i,weight=1)
            main_frame.rowconfigure(0,weight=1)

        style = ttk.Style()
        # Configure different styles for different button sizes
        style.configure("Biggest.TButton", background="red")
        style.configure("Bigger.TButton", background="orange")
        style.configure("Middle.TButton", background="yellow")
        style.configure("Small.TButton", background="green")

        # create a frame in each column
        for col in range(3):
            column_frame = ttk.Frame(main_frame,relief='groove',borderwidth=2)
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
                    btn = ttk.Button(column_frame, text=size, style="Biggest.TButton")
                    btn.grid(row=row,column=0,sticky="nsew",padx=5,pady=5,ipady=30)
                    column_frame.rowconfigure(row,weight=3)
                elif size == "bigger":
                    btn = ttk.Button(column_frame, text=size, style="Bigger.TButton")
                    btn.grid(row=row,column=0,sticky="nsew",padx=5,pady=5,ipady=20)
                    column_frame.rowconfigure(row,weight=2)
                elif size == "middle":
                    btn = ttk.Button(column_frame, text=size, style="Middle.TButton")
                    btn.grid(row=row,column=0,sticky="nsew",padx=5,pady=5,ipady=5)
                    column_frame.rowconfigure(row,weight=1)
                else:
                    btn = ttk.Button(column_frame, text=size, style="Small.TButton")
                    btn.grid(row=row,column=0,sticky="nsew",padx=5,pady=2,ipady=5)
                    column_frame.rowconfigure(row,weight=1)
    

def main():
     window = Window(theme="arc")
     window.mainloop()

if __name__ == "__main__":
    main()





   
