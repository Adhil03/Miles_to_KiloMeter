from tkinter import *


def mile_to_km():
    new_text = float(mile.get())
    km.config(text=int(int(new_text) * float(1.609)))


window = Tk()

window.title("Miles to Kilometer calculator")
window.config(padx=30, pady=30)

is_equal = Label(text="is equal to")
# is_equal.pack()
is_equal.grid(column=0, row=1)

mile = Entry(width=10)
# mile.pack()
mile.get()
mile.grid(column=1, row=0)

km = Label(text="0")
# km.pack()
km.grid(column=1, row=1)

cal_button = Button(text="Calculate", command=mile_to_km)
# cal_button.pack()
cal_button.grid(column=1, row=2)

mile_lab = Label(text="Miles")
# mile_lab.pack()
mile_lab.grid(column=2, row=0)

km_lab = Label(text="KM")
# km_lab.pack()
km_lab.grid(column=2, row=1)


window.mainloop()
