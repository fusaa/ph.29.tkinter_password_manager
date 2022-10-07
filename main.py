import tkinter
import pyperclip

from tkinter import messagebox
from random import choice, randint, shuffle





# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    # password_list = []

    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))
    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)
    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)

    password_letters = [choice(letters) for _ in range(nr_letters)]
    password_symbols = [choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)
    # for char in password_list:
    #   password += char

    # print(f"Your password is: {password}")
    password_entry.delete(0,tkinter.END)
    password_entry.insert(0,password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
# website_entry = None
# username_entry = None
# password_entry = None

def save():
    #messagebox.showinfo(title="Title", message="message")
    if len(username_entry.get()) < 1 or len(password_entry.get()) < 2:
        messagebox.showinfo(title = "Oops", message='Username or pwd bad')
        return


    is_ok = messagebox.askokcancel(title=website_entry, message=f"Email {username_entry.get()}, with: \n {password_entry.get()}")
    if is_ok:
        spacer = ' | '
        print("web" + str(website_entry.get()))
        string = website_entry.get() + spacer + username_entry.get() + spacer + password_entry.get() + '\n'
        with open('data.txt', 'a') as file:
            file.write(string)
        website_entry.delete(0,tkinter.END)
        # username_entry.delete(0,tkinter.END)
        password_entry.delete(0, tkinter.END)





# ---------------------------- UI SETUP ------------------------------- #

screen = tkinter.Tk()
screen.config(padx = 30, pady = 30)#, width = 300, height = 400)
screen.title("Password Manager")

canvas = tkinter.Canvas(height = 200, width =200, highlightthickness = 0)
logo_image = tkinter.PhotoImage(file='logo.png')
canvas.create_image(100,100,image = logo_image)
canvas.grid(row=0, column=1)

# LABELS

website_label = tkinter.Label(text = 'Website:')
username_label = tkinter.Label(text = 'Email/Username:')
password_label = tkinter.Label(text = 'Password:')

# Entries:

website_entry = tkinter.Entry(width=62)
website_entry.focus()
username_entry = tkinter.Entry(width = 62)
username_entry.insert(0,"mail@mail.com")
password_entry = tkinter.Entry(width = 31)

# Buttons:

generate_pwd_b = tkinter.Button(text = "Generate Password", width = 24, command=password_generator)
add_b = tkinter.Button(text = "Add", width = 53, command = save)
# Positions:

website_label.grid(row = 1, column = 0)
username_label.grid(row = 2, column = 0)
password_label.grid(row = 3, column = 0)

website_entry.grid(row = 1, column = 1, columnspan=2,sticky = 'W')
username_entry.grid(row = 2, column = 1,columnspan=2,sticky = 'W')
password_entry.grid(row = 3, column = 1, columnspan=1,sticky = 'W')

generate_pwd_b.grid(row =3, column = 2,sticky = 'W', columnspan=1)
add_b.grid(row =4, column =1, columnspan=2, sticky = 'W')






screen.mainloop()
