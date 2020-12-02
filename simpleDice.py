import random
import tkinter as tk

def coinflip():
    lbl_result["text"]=str(random.randint(1,2))

def d6():
    lbl_result["text"]=str(random.randint(1,6))

def d20():
    lbl_result["text"]=str(random.randint(1,20))

window=tk.Tk()
window.rowconfigure(0, weight=1, minsize=50)
btn_labels={0: "Flip a coin", 1: "Roll a d6", 2: "Roll a d20"}
btn_commands={0: coinflip, 1: d6, 2: d20}

for i in btn_labels:
    window.columnconfigure(i, weight=1, minsize=20)
    frame=tk.Frame(
        master=window,
        relief=tk.RAISED,
        borderwidth=1
    )
    frame.grid(row=0, column=i, padx=5)
    button=tk.Button(master=frame, text=f"{btn_labels[i]}", command=btn_commands[i])
    button.pack()

window.columnconfigure(len(btn_labels)+1, weight=2, minsize=20)
frame=tk.Frame(
    master=window,
    relief=tk.FLAT,
    borderwidth=1
)
frame.grid(row=0,column=len(btn_labels)+1,padx=5)
lbl_result=tk.Label(master=frame, text="0")
lbl_result.pack()

window.mainloop()