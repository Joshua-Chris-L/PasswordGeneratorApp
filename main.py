from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letter = [random.choice(letters) for char in range(nr_letters)]
    password_symbol = [random.choice(symbols) for cha in range(nr_symbols)]
    password_number = [random.choice(numbers) for ch in range(nr_numbers)]

    password_list = password_letter + password_symbol + password_number
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
    # password = ""
    # for char in password_list:
    #  password += char
    # print(f"Your password is: {password}")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(message="Please do not leave any field empty")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}"
                                                              f"\nPassword: {password}.\n Is this ok to save?")
        if is_ok:
            try:
                with open("data.json", "r") as datafile:
                    # Reading the old data
                    data = json.load(datafile)
            except FileNotFoundError:
                with open("data.json", "w") as datafile:
                    # Create a new file
                    json.dump(new_data, datafile, indent=4)
            else:
                # updating the old data with the new data
                data.update(new_data)
                with open("data.json", "w") as datafile:
                    # Saving Updated Data
                    json.dump(data, datafile, indent=4)
            finally:
                # datafile.write(f"{website}| {email} | {password} \n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ---------------------------------- #
FONT_NAME = "Courier"

# Window Setup
window = Tk()
window.title("Password Manager")
window.config(padx=10, pady=10)


#  ----------------------Find Password --------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title="website", message=f"email: {email}\n password: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")


# Canvas Setup
canvas = Canvas(width=300, height=300)  # bg=YELLOW, highlightthickness=0)
my_pass_img = PhotoImage(file="logo.png")
canvas.create_image(200, 200, image=my_pass_img)
canvas.grid(column=1, row=0)

# Label Window
website_label = Label(text="Website: ", font=(FONT_NAME, 20))
website_label.grid(column=0, row=1)
Email_label = Label(text="Email/Username: ", font=(FONT_NAME, 20))
Email_label.grid(column=0, row=2)
password_label = Label(text="Password: ", font=(FONT_NAME, 20))
password_label.grid(column=0, row=3)

# Website entries
website_entry = Entry(width=50)
website_entry.grid(row=1, column=1, columnspan=1)
website_entry.focus()
email_entry = Entry(width=67)
email_entry.grid(row=2, column=1, columnspan=2)
password_entry = Entry(width=50)
password_entry.grid(row=3, column=1)
email_entry.insert(0, "joshchro@email.com")

# Buttons
search_button = Button(text="Search Button", width=11, command=find_password)
search_button.grid(row=1, column=2)
generate_password_button = Button(text="Generate Password", width=14, command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1)



window.mainloop()
