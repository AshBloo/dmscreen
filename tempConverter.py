import tkinter as tk

def celsius_to_fahrenheit():
    celsius=ent_temperature.get()
    fahrenheit=float(celsius)*(9/5)+32
    lbl_result["text"]=f"{round(fahrenheit, 2)} \N{DEGREE FAHRENHEIT}"


window=tk.Tk()
window.title("Temperature Converter")

frm_entry=tk.Frame(master=window)
ent_temperature=tk.Entry(master=frm_entry, width=10)
lbl_temp=tk.Label(master=frm_entry, text="\N{DEGREE CELSIUS}")

ent_temperature.grid(row=0, column=0, sticky="e")
lbl_temp.grid(row=0, column=1, sticky="w")

btn_convert=tk.Button(
    master=window,
    text="\N{RIGHTWARDS BLACK ARROW}",
    command=celsius_to_fahrenheit
)
lbl_result=tk.Label(master=window, text="\N{DEGREE FAHRENHEIT}")

frm_entry.grid(row=0, column=0, padx=10)
btn_convert.grid(row=0, column=1, pady=10)
lbl_result.grid(row=0, column=2, padx=10)

window.mainloop()