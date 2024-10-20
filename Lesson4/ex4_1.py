import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk

def create_gui():
    root = ThemedTk(theme="arc")
    root.title("TkThemes GUI Layout")
    root.geometry("600x400")

    # Create a frame for buttons
    top_frame = ttk.Frame(root)
    top_frame.pack(fill=tk.X, padx=150, pady=10)

    # Configure 3 equal-sized columns in the top frame
    for i in range(3):
        top_frame.columnconfigure(i, weight=1)



    # # Create buttons in a loop
    # for i in range(3):
    #     ttk.Button(top_frame, text=f"按鈕 {i+1}").pack(side=tk.LEFT, padx=5)

    # Create buttons in a grid layout
    for i in range(3):
        btn = ttk.Button(top_frame, text=f"Button {i+1}")
        btn.grid(row=0, column=i, sticky=tk.EW, padx=5)  # Use grid with sticky to extend



    # set up the main frame
    main_frame = ttk.Frame(root)
    main_frame.pack(fill=tk.BOTH,expand=True,padx=10,pady=10)

    # create 3 columns in main frame
    for i in range(3):
        main_frame.columnconfigure(i,weight=1)
        main_frame.rowconfigure(0,weight=1)

    # create a frame in each column
    for col in range(3):
        column_frame = ttk.Frame(main_frame,relief='groove',borderwidth=2)
        column_frame.grid(row=0,column=col,sticky='nsew',padx=5)
        column_frame.columnconfigure(0,weight=1)
        if col == 0: # left column
            sizes = ["bigger",'middle','middle']
        elif col == 1: # middle column
            sizes = ["small","biggest","small"]
        else: # right column
            sizes = ["small","small","small"]

        # add buttons in each column
        for row, size in enumerate(sizes):
            btn = ttk.Button(column_frame,text=size)
            if size == "biggest":
                btn.grid(row=row,column=0,sticky="nsew",padx=5,pady=15,ipady=30)
                column_frame.rowconfigure(row,weight=3)
            elif size == "bigger":
                btn.grid(row=row,column=0,sticky="nsew",padx=5,pady=10,ipady=20)
                column_frame.rowconfigure(row,weight=2)
            elif size == "middle":
                btn.grid(row=row,column=0,sticky="nsew",padx=5,pady=5,ipady=10)
                column_frame.rowconfigure(row,weight=1)
            else:
                btn.grid(row=row,column=0,sticky="nsew",padx=5,pady=2,ipady=5)
                column_frame.rowconfigure(row,weight=1)
    return root

if __name__ == "__main__":
    app = create_gui()
    app.mainloop()





   
