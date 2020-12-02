import tkinter as tk

#Useful bits
#Label = Widget to display text
#Button = Widget that can contain text and perform an action when clicked
#Entry - Text entry widget, single line only
#Text - As above but multi-line (don't see why theres a distinction, yet)
#Frame - Rectangular region used to group widgets / provide padding

#Step 1 (Super Basics)
window1 = tk.Tk() #Creates the window
greeting = tk.Label(text = "Hello, Tkinter") #Creates a greeting "widget"
greeting.pack() #Places the above widget into the window
window1.mainloop() #This seemed to initialise the whole thing, for some reason nothing worked until this (contrary to the guide I'm using atm)

#Step 2 (Customising the Basics)
window2 = tk.Tk()
title = tk.Label(
    text = "Dungeon Masters Screen Test",
    foreground = "white", #Sets text colour [red,orange,yellow,green,blue,purple,etc.]
    #Can also use fg and bg!
    background = "black", #Set background colour [as above, most html colour names work. Can also use hex]
    width = 30, #This is in "text units", so 10 wide is less than 10 tall!
    height = 10
)
title.pack()
window2.mainloop()

#Step 3 (Button Time!)
window3 = tk.Tk()
button = tk.Button( #Buttons are just labels but with T E X T U R E
    text = "Click here to TPK!",
    width = 25,
    height = 5,
    bg = "#78572a",
    fg = "white"
)
button.pack()
window3.mainloop()

#Step 4 (User Entry)
#This bit didn't work well since I'm not running it in a shell?
#But basically: .get() retrieves entry, .delete() deletes entry, .insert() inserts entry. Easy

#Step 5 (Frames)
window4 = tk.Tk()
frameA = tk.Frame()
frameB = tk.Frame()
labelA = tk.Label(master=frameA, text = "I'm in frame A")
labelA.pack()
labelB = tk.Label(master=frameB, text = "I'm in frame B")
labelB.pack()
frameB.pack() #Packing order matters!
frameA.pack()
window4.mainloop()

#Step 6 (FANCY Frames)
border_effects = {
    "flat": tk.FLAT,
    "sunken": tk.SUNKEN,
    "raised": tk.RAISED,
    "groove": tk.GROOVE,
    "ridge": tk.RIDGE,
}
window5 = tk.Tk() #Its around this point where I start calling this tiktok

for relief_name, relief in border_effects.items(): 
     frame = tk.Frame(master = window5, relief = relief, borderwidth = 5)
     frame.pack(side = tk.LEFT)
     label = tk.Label(master = frame, text = relief_name)
     label.pack()

window5.mainloop()

#Quick word about naming conventions!
#Label uses lbl prefix -> lbl_example
#Button uses btn, Entry uses ent, Text uses txt, Frame uses frm

#Step 7 (Geometry basics (.pack options))
window6 = tk.Tk()
frame1 = tk.Frame(master = window6, width = 100, height = 100, bg = "red")
frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True) # fill=tk.(X or Y) would limit this to up/down or left/right
frame2 = tk.Frame(master=window6, width=50, height=50, bg = "yellow")
frame2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True) # side=tk.LEFT sets it to fill from the left, naturally
frame3 = tk.Frame(master=window6, width=25, height=25, bg = "blue")
frame3.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
window6.mainloop()

#Step 8 (Know your .place)
window8 = tk.Tk() #Skipping 7 because honestly its confusing me now
frame = tk.Frame(master = window8, width = 150, height = 150)
frame.pack()
lbl_1 = tk.Label(master = frame, text = "I'm at (0,0)", bg = "red")
lbl_1.place(x = 0, y = 0)
lbl_2 = tk.Label(master = frame, text = "I'm at (75,75)", bg = "blue")
lbl_2.place(x = 75, y = 75)
window8.mainloop()

#Step 9 (.grid, or how I learned to stop using .pack and love the bomb)
window9 = tk.Tk()
for i in range(3):
    window9.columnconfigure(i, weight = 1, minsize = 75)
    window9.rowconfigure(i, weight = 1, minsize = 50)
    for j in range(3):
        frame = tk.Frame(
            master = window9,
            relief = tk.RAISED,
            borderwidth = 1
        )
        frame.grid(row = i, column = j, padx = 5, pady = 5) #Padding uses pixels, not text units
        label = tk.Label(master = frame, text = f"Row {i}\nColumn {j}")
        label.pack(padx = 5, pady = 5)
window9.mainloop()

#Step 10 
window10 = tk.Tk()

window10.rowconfigure(0, minsize=50)
window10.columnconfigure([0, 1, 2, 3], minsize=50)

label1 = tk.Label(text="1", bg="black", fg="white")
label2 = tk.Label(text="2", bg="black", fg="white")
label3 = tk.Label(text="3", bg="black", fg="white")
label4 = tk.Label(text="4", bg="black", fg="white")

label1.grid(row=0, column=0)
label2.grid(row=0, column=1, sticky="ew")
label3.grid(row=0, column=2, sticky="ns")
label4.grid(row=0, column=3, sticky="nsew") #North, South, East, West

window10.mainloop()

#Step 11 (Events and commands!)

def increase():
    value = int(lbl_value["text"])
    lbl_value["text"] = f"{value + 1}"

def decrease():
    value = int(lbl_value["text"])
    lbl_value["text"] = f"{value - 1}"

window11 = tk.Tk()

window11.rowconfigure(0, minsize=50, weight=1)
window11.columnconfigure([0, 1, 2], minsize=50, weight=1)

btn_increase = tk.Button(master=window11, text="+", command=increase)
btn_increase.grid(row=0, column=2, sticky="nsew")

btn_decrease = tk.Button(master=window11, text="-", command=decrease)
btn_decrease.grid(row=0, column=0, sticky="nsew")

lbl_value = tk.Label(master=window11, text="0")
lbl_value.grid(row=0, column=1)

window11.mainloop()

#End of basics