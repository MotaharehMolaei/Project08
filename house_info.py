from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg
from file_manager import *
from validator import *
from house import House

# TODO line 8 has error
house_list = read_from_file("houses.dat")

def load_data(house_list):
    house_list = read_from_file("houses.dat")
    for row in table.get_children():
        table.delete(row)

    for house in house_list:
        visual_house = (
            house[0],
            house[1],
            house[2],
            "✓" if house[3] else "",
            "✓" if house[4] else "",
            "✓" if house[5] else "",
            house[6]
        )
        table.insert("", END, values=visual_house)

def reset_form():
    id.set(len(house_list) + 1)
    address.set("")
    region.set("")
    has_elevator.set(0)
    has_parking.set(0)
    has_storage.set(0)
    rooms.set(1)
    load_data(house_list)

def save_btn_click():
    house = House(
        id.get(),
        address.get(),
        region.get(),
        bool(has_elevator.get()),
        bool(has_parking.get()),
        bool(has_storage.get()),
        rooms.get()
    )

    errors = house_validator()

    if errors:
        msg.showerror("Validation Error", "\n".join(errors))
    else:
        house_list.append(house)
        write_to_file("houses.dat", house_list)
        msg.showinfo("Success", "House saved successfully.")
        reset_form()

def table_select(x):
    selected = table.item(table.focus())["values"]
    if selected:
        id.set(selected[0])
        address.set(selected[1])
        region.set(selected[2])
        has_elevator.set(1 if selected[3] else 0)
        has_parking.set(1 if selected[4] else 0)
        has_storage.set(1 if selected[5] else 0)
        rooms.set(selected[6])

def edit_btn_click():
    pass

def remove_btn_click():
    pass

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
Entry(window, textvariable=address).place(x=100, y=60)

# Region
Label(window, text="Region").place(x=20, y=100)
region = StringVar()
Entry(window, textvariable=region).place(x=100, y=100)

# Rooms
Label(window, text="Rooms").place(x=20, y=140)
rooms = IntVar(value=1)
Entry(window, textvariable=rooms).place(x=100, y=140)


# Checkboxes
Label(window, text="Options").place(x=20, y=180)
has_elevator = IntVar()
Checkbutton(window, text="Elevator", variable=has_elevator).place(x=100, y=180)
has_parking = IntVar()
Checkbutton(window, text="Parking", variable=has_parking).place(x=100, y=200)
has_storage = IntVar()
Checkbutton(window, text="Storage", variable=has_storage).place(x=100, y=220)



# Table
table = ttk.Treeview(window, columns=[1,2,3,4,5,6,7], show="headings")
table.heading(1, text="Id", anchor="center")
table.heading(2, text="Address", anchor="center")
table.heading(3, text="Region", anchor="center")
table.heading(4, text="Elevator", anchor="center")
table.heading(5, text="Parking", anchor="center")
table.heading(6, text="Storage", anchor="center")
table.heading(7, text="Rooms", anchor="center")

table.column(1, width=60, anchor="center")
table.column(2, width=150, anchor="center")
table.column(3, width=100, anchor="center")
table.column(4, width=100, anchor="center")
table.column(5, width=100, anchor="center")
table.column(6, width=100, anchor="center")
table.column(7, width=100, anchor="center")

table.bind("<<TreeviewSelect>>", table_select)
table.place(x=310, y=20, height=310)

Button(window, text="Save", width=6, command=save_btn_click,bg="lightblue", fg="black").place(x=40, y=260)
Button(window, text="Edit", width=6, command=edit_btn_click,bg="lightblue", fg="black").place(x=120, y=260)
Button(window, text="Remove", width=6, command=remove_btn_click,bg="lightblue", fg="black").place(x=200, y=260)
Button(window, text="Clear", width=6, command=reset_form,bg="lightblue", fg="black").place(x=40, y=300, width=214)

reset_form()
window.mainloop()
