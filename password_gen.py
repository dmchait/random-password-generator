import string
import tkinter
from random import choice
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox


charsets = string.ascii_letters + string.digits + string.punctuation


def password_create():
    entry.delete(0, END)
    pass_length = length.get()
    password = ""
    if strength.get() == 1:
        for i in range(0, pass_length):
            password += choice(string.ascii_letters)
        return ''.join(password)
    elif strength.get() == 0:
        for i in range(0, pass_length):
            password += choice(string.ascii_letters + string.digits)
        return ''.join(password)
    elif strength.get() == 2:
        for i in range(0, pass_length):
            password += choice(charsets)
        return ''.join(password)
    else:
        tkinter.messagebox.showinfo("Please choose a length")


def generate():
    new_pw = password_create()
    entry.insert(10, new_pw)


def save():
    passwd = entry.get()
    pwd.append(passwd)
    acc_name = entryAccount.get()
    acct.append(acc_name)
    with open("Saved_Passwords.txt", "w") as f:
        for (passwd, acc_name) in zip(pwd, acct):
            # write password to output file
            f.writelines("{0},{1}\n".format(passwd, acc_name))


# Main function
root = Tk()
strength = IntVar()
length = IntVar()
root.title("Random Password Generator")
root.geometry("415x75")

# Establish list to store generated passwords
# list to store account name for password
pwd = []
acct = []

# Label and Entry forms for generated password
password_random = Label(root, text="Password:")
password_random.grid(row=0)
entry = Entry(root)
entry.grid(row=0, column=1)

# Label and entry forms for account name
account = Label(root, text="Account Name:")
account.grid(row=1)
entryAccount = Entry(root)
entryAccount.grid(row=1, column=1)

# Label for Length of password
pass_label = Label(root, text="Length:")
pass_label.grid(row=2)

# Button to generate the password and save passwords to list
genBtn = Button(root, text="Generate", command=generate)
genBtn.grid(row=0, column=2)
saveBtn = Button(root, text="Save", command=save)
saveBtn.grid(row=0, column=3)

# Radio buttons for choice of desired password strength
# Default Choice for password strength is good
# Establish combobox for length of password
r_weak = Radiobutton(root, text="Weak", variable=strength, value=1)
r_weak.grid(row=1, column=2, sticky='E')
r_good = Radiobutton(root, text="Good", variable=strength, value=0)
r_good.grid(row=1, column=3, sticky='E')
r_strong = Radiobutton(root, text="Strong", variable=strength, value=2)
r_strong.grid(row=1, column=4, sticky='E')
combo = Combobox(root, textvariable=length)

# Combo Box for length of your password
# Values range starts at 8 as standard minimum pw length
# Values range ends at 16 as standard maximum pw length
combo['values'] = (8, 9, 10, 11, 12, 13, 14, 15, 16)
combo.current(0)
combo.bind('<<ComboboxSelected>>')
combo.grid(column=1, row=2)

root.mainloop()
