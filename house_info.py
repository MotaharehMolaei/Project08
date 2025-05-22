from tkinter import *
import tkinter.ttk as ttk

window = Tk()
window.title("House Info")
window.geometry("750x320")


# ID
Label(window, text="ID").place(x=20, y=20)
id = IntVar(value=1)
Entry(window, textvariable=id, state="readonly").place(x=100, y=20)

# Address
Label(window, text="Address").place(x=20, y=60)
address = StringVar()
Entry(window, textvariable=address, width=30).place(x=100, y=60)

# Region
Label(window, text="Region").place(x=20, y=100)
region = StringVar()
Entry(window, textvariable=region).place(x=100, y=100)

# Checkboxes
has_elevator = IntVar()
Checkbutton(window, text="Elevator", variable=has_elevator).place(x=100, y=140)
has_parking = IntVar()
Checkbutton(window, text="Parking", variable=has_parking).place(x=180, y=140)
has_storage = IntVar()
Checkbutton(window, text="Storage", variable=has_storage).place(x=260, y=140)

# Rooms
Label(window, text="Rooms").place(x=20, y=180)
rooms = IntVar(value=1)
Entry(window, textvariable=rooms).place(x=100, y=180)

# Table
table = ttk.Treeview(window, columns=[1,2,3,4,5,6,7], show="headings")
table.heading(1, text="Id")
table.heading(2, text="Address")
table.heading(3, text="Region")
table.heading(4, text="Elevator")
table.heading(5, text="Parking")
table.heading(6, text="Storage")
table.heading(7, text="Rooms")

table.column(1, width=60)
table.column(2, width=100)
table.column(3, width=100)
table.column(4, width=100)
table.column(5, width=100)
table.column(6, width=100)
table.column(7, width=100)

table.bind("<<TreeviewSelect>>")
table.place(x=330, y=20)

Button(window, text="Save", width=10).place(x=20, y=250)
Button(window, text="Clear", width=10).place(x=140, y=250)
window.mainloop()