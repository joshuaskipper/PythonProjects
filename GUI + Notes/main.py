from tkinter import *

# #pick side
# label.pack(side="left")

# #Change text/label
# label["text"] = "new text"
# label.config(text="new text")

# Button
km = 0
def button_clicked():
    miles = float(input.get())
    km = round(miles * 1.6)
    kilo.config(text=km)

# Create Window
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=200)
window.config(padx=2, pady=6)
# Create label
label = Label(text="Miles", font=("Arial", 12, ""))
label.grid(column=1, row=0)
label.config(pady=1, padx=1)

convert = Label(text="")
convert.grid(column=3, row=3)

kilo = Label(text="0", font=("Arial", 12, ""))
kilo.grid(column=2,row=4)

word = Label(text="Kilometers", font=("Arial", 12, ""))
word.grid(column=4, row=4)

equal = Label(text=f"is equal to", font=("Arial", 11, ""))
equal.grid(column=1, row=4)
equal.config()




# Entry
input = Entry()
input.grid(column=2, row=0)





button = Button(text="Calculate", command=button_clicked)
button.grid(column=2, row=10)


window.mainloop()
