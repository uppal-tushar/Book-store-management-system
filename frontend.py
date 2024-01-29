from tkinter import *

import backend

def get_selected_row(event):

    global selected_tuple
    index = list1.curselection()[0]  # get the index of the selected row
    selected_tuple = list1.get(index)  # get the row in list
    t1.delete(0, END)
    t1.insert(END, selected_tuple[1])
    t2.delete(0, END)
    t2.insert(END, selected_tuple[2])
    t3.delete(0, END)
    t3.insert(END, selected_tuple[3])
    t4.delete(0, END)
    t4.insert(END, selected_tuple[4])


def view_command():

    list1.delete(0, END)  # clear the list box
    for row in backend.view():
        list1.insert(END, row)


def search_command():

    list1.delete(0, END)
    for row in backend.search(
        title_text.get(), Author_text.get(), Year_text.get(), isbn_text.get()
    ):
        list1.insert(END, row)  # insert the row in the listBox


def add_command():

    backend.insert(
        title_text.get(), Author_text.get(), Year_text.get(), isbn_text.get()
    )  # add the the data to the database
    list1.delete(0, END)
    list1.insert(
        END, (title_text.get(), Author_text.get(), Year_text.get(), isbn_text.get())
    )


def delete_command():

    backend.delete(selected_tuple[0])
    list1.delete(0, END)
    for row in backend.view():
        list1.insert(END, row)


def update_command():

    backend.update(
        selected_tuple[0],
        title_text.get(),
        Author_text.get(),
        Year_text.get(),
        isbn_text.get(),
    )  # update the selected row in the database
    list1.delete(0, END)
    for row in backend.view():
        list1.insert(END, row)  # insert the updated row in the the listB0x


window = Tk()  # create the window(outer structure of the app
window.wm_title("BookStore")  # give the title to the app

l1 = Label(window, text="Title")  # create the title label
l1.grid(row=0, column=0)  # position the title label

title_text = StringVar()  # create an object that contain the Title of Book
t1 = Entry(window, textvariable=title_text)  # create the entry box for title label
t1.grid(row=0, column=1)  # position the Entry Box

l2 = Label(window, text="Author")  # create the Author label
l2.grid(row=0, column=2)  # position the Author label

Author_text = StringVar()  # create an object that contain the Author Name
t2 = Entry(window, textvariable=Author_text)  # create the entry box for Author  label
t2.grid(row=0, column=3)  # position the Entry Box

l3 = Label(window, text="Year")  # create the Year label
l3.grid(row=1, column=0)  # position the Year label

Year_text = StringVar()  # create an object that contain the Year value
t3 = Entry(window, textvariable=Year_text)  # create the entry box for Year label
t3.grid(row=1, column=1)  # position the Entry Box

l4 = Label(window, text="ISBN")  # create the isbn label
l4.grid(row=1, column=2)  # position the ISBN label

isbn_text = StringVar()  # create an object that contain the isbn value
t4 = Entry(window, textvariable=isbn_text)  # create the entry box for isbn label
t4.grid(row=1, column=3)  # position the Entry Box

list1 = Listbox(
    window, height=6, width=35
)  # create the listbox that show all the output of each command
list1.grid(row=2, column=0, rowspan=6, columnspan=2)  # position the List Box

sb1 = Scrollbar(window)  # create the scroll bar
sb1.grid(row=2, column=2, rowspan=6)  # position the scroll bar

list1.configure(yscrollcommand=sb1.set)  # create the scroll bar according to the y axis
sb1.configure(command=list1.yview)  # connect the scroll bar to the list box

list1.bind(
    "<<ListboxSelect>>", get_selected_row
)  # this will help to collect the data of the selected row

b1 = Button(
    window, text="View All", width=12, command=view_command
)  # create the View All Button
b1.grid(row=2, column=3)  # position the button

b2 = Button(
    window, text="Search Entry", width=12, command=search_command
)  # create the Search Entry Button
b2.grid(row=3, column=3)  # position the button

b3 = Button(
    window, text="Add Entry", width=12, command=add_command
)  # create the Add Entry Button
b3.grid(row=4, column=3)  # position the button

b4 = Button(
    window, text="Update", width=12, command=update_command
)  # create the update Button
b4.grid(row=5, column=3)  # position the button

b5 = Button(
    window, text="Delete", width=12, command=delete_command
)  # create the Delete Button
b5.grid(row=6, column=3)  # position the button

b6 = Button(
    window, text="close", width=12, command=window.destroy
)  # create the Close Button
b6.grid(row=7, column=3)  # position the button

window.mainloop()
