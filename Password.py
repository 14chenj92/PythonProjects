import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext
import random

# Arrays of characters to include in the password
lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numeric = "0123456789"
specialchar = "!\"#$%&'()*+,-./\\:;<=>?@[\\]^_`{|}~"


def generate_password(length, use_lowercase, use_uppercase, use_numeric, use_specialchar):
  if not (use_lowercase or use_uppercase or use_numeric or use_specialchar):
    return "Select at least one character type."

  password_final = []
  if use_lowercase:
    password_final += lowercase
  if use_uppercase:
    password_final += uppercase
  if use_numeric:
    password_final += numeric
  if use_specialchar:
    password_final += specialchar

  complete_password = []
  if use_lowercase:
    complete_password.append(random.choice(lowercase))
  if use_uppercase:
    complete_password.append(random.choice(uppercase))
  if use_numeric:
    complete_password.append(random.choice(numeric))
  if use_specialchar:
    complete_password.append(random.choice(specialchar))

  for _ in range(length - len(complete_password)):
    complete_password.append(random.choice(password_final))

  random.shuffle(complete_password)
  return ''.join(complete_password)


def on_generate():
  try:
    length = int(entry_length.get())
    if length < 8 or length > 128:
      messagebox.showerror("Invalid Input",
                           "Choose a number between 8 and 128 characters.")
      return
  except ValueError:
    messagebox.showerror("Invalid Input", "Please enter a valid number.")
    return

  use_lowercase = var_lowercase.get()
  use_uppercase = var_uppercase.get()
  use_numeric = var_numeric.get()
  use_specialchar = var_specialchar.get()

  password = generate_password(length, use_lowercase, use_uppercase,
                               use_numeric, use_specialchar)
  result_label.config(text=f'Your Password is: {password}')


# Setting up the Tkinter window
root = tk.Tk()
root.title("Password Generator")

title = tk.Label(root, text="Password Generator", font=("Arial", 30))
title.pack(pady=10)
# Password length entry
tk.Label(root, text="Choose a password length (8-128 characters):").pack()
entry_length = tk.Entry(root, bg="white")
entry_length.pack()

# Checkboxes for character types
var_lowercase = tk.BooleanVar()
var_uppercase = tk.BooleanVar()
var_numeric = tk.BooleanVar()
var_specialchar = tk.BooleanVar()

chat_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, state='disabled', width=50, height=20)
chat_display.pack(pady=10)

tk.Checkbutton(root, text="Include lowercase letters",
               variable=var_lowercase).pack()
tk.Checkbutton(root, text="Include uppercase letters",
               variable=var_uppercase).pack()
tk.Checkbutton(root, text="Include numbers", variable=var_numeric).pack()
tk.Checkbutton(root,
               text="Include special characters",
               variable=var_specialchar).pack()

# Generate button
tk.Button(root, text="Generate Password", command=on_generate).pack()

# Result label
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()

