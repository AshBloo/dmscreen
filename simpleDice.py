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
btn_config={"Flip a coin": coinflip, "Roll a d6": d6, "Roll a d20": d20}

for i, label in enumerate(btn_config):
    window.columnconfigure(i, weight=1, minsize=20)
    frame=tk.Frame(
        master=window,
        relief=tk.RAISED,
        borderwidth=1
    )
    frame.grid(row=0, column=i, padx=5)
    button=tk.Button(master=frame, text=label, command=btn_config.get(label))
    button.pack()

window.columnconfigure(len(btn_config)+1, weight=2, minsize=20)
frame=tk.Frame(
    master=window,
    relief=tk.FLAT,
    borderwidth=1
)
frame.grid(row=0,column=len(btn_config)+1,padx=5)
lbl_result=tk.Label(master=frame, text="0")
lbl_result.pack()

window.mainloop()