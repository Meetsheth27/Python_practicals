import tkinter as tk
from tkinter import messagebox

# Dummy credentials
USERNAME = "admin"
PASSWORD = "1234"

def login():
    user = entry_username.get()
    pwd = entry_password.get()

    if user == USERNAME and pwd == PASSWORD:
        messagebox.showinfo("Login Success", "Welcome!")
    else:
        messagebox.showerror("Login Failed", "Invalid Username or Password")

# Create window
root = tk.Tk()
root.title("Login Page")
root.geometry("300x200")

# Username label and entry
label_username = tk.Label(root, text="Username")
label_username.pack(pady=5)

entry_username = tk.Entry(root)
entry_username.pack(pady=5)

# Password label and entry
label_password = tk.Label(root, text="Password")
label_password.pack(pady=5)

entry_password = tk.Entry(root, show="*")
entry_password.pack(pady=5)

# Login button
login_button = tk.Button(root, text="Login", command=login)
login_button.pack(pady=10)

# Run the app
root.mainloop()