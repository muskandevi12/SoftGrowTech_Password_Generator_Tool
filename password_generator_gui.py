import random
import string
import tkinter as tk
from tkinter import simpledialog, messagebox


def generate_password(length):
    letters = string.ascii_letters
    numbers = string.digits
    special_chars = string.punctuation

    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(numbers),
        random.choice(special_chars)
    ]

    all_chars = letters + numbers + special_chars

    for i in range(length - 4):
        password.append(random.choice(all_chars))

    random.shuffle(password)

    return ''.join(password)


def start_password_generator():
    length = simpledialog.askinteger(
        "Password Length",
        "Enter password length:"
    )

    if length is None:
        return

    if length < 4:
        messagebox.showerror(
            "Error",
            "Password length must be at least 4."
        )
        return

    satisfied = False

    while not satisfied:
        password = generate_password(length)

        satisfied = messagebox.askyesno(
            "Generated Password",
            f"Your password is:\n\n{password}\n\nAre you satisfied with this password?"
        )

    messagebox.showinfo(
        "Final Password",
        f"Your final password is:\n\n{password}"
    )


root = tk.Tk()
root.title("Password Generator Tool")
root.geometry("400x250")

title_label = tk.Label(
    root,
    text="Password Generator Tool",
    font=("Arial", 18, "bold")
)
title_label.pack(pady=30)

generate_button = tk.Button(
    root,
    text="Generate Password",
    font=("Arial", 14),
    command=start_password_generator
)
generate_button.pack(pady=20)

root.mainloop()































# import random
# import string

# def generate_password(length):
#     if length < 4:
#         return "Password length must be at least 4."

#     letters = string.ascii_letters
#     numbers = string.digits
#     special_chars = string.punctuation

#     password = [
#         random.choice(string.ascii_lowercase),
#         random.choice(string.ascii_uppercase),
#         random.choice(numbers),
#         random.choice(special_chars)
#     ]

#     all_chars = letters + numbers + special_chars

#     for i in range(length - 4):
#         password.append(random.choice(all_chars))

#     random.shuffle(password)

#     return ''.join(password)


# try:
#     length = int(input("Enter password length: "))
#     password = generate_password(length)
#     print("Generated Password:", password)

# except ValueError:
#     print("Please enter a valid number.")
