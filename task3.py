import tkinter as tk
from tkinter import messagebox
import random
import string


class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("400x400")

     
        self.title_label = tk.Label(root, text="Password Generator", font=("Arial", 18))
        self.title_label.pack(pady=20)

       
        self.length_label = tk.Label(root, text="Enter password length:", font=("Arial", 12))
        self.length_label.pack(pady=10)

        self.length_entry = tk.Entry(root, font=("Arial", 12))
        self.length_entry.pack(pady=10)

        
        self.include_uppercase = tk.BooleanVar(value=True)
        self.include_digits = tk.BooleanVar(value=True)
        self.include_special = tk.BooleanVar(value=True)

        self.uppercase_check = tk.Checkbutton(root, text="Include Uppercase Letters", var=self.include_uppercase, font=("Arial", 12))
        self.uppercase_check.pack()

        self.digits_check = tk.Checkbutton(root, text="Include Digits", var=self.include_digits, font=("Arial", 12))
        self.digits_check.pack()

        self.special_check = tk.Checkbutton(root, text="Include Special Characters", var=self.include_special, font=("Arial", 12))
        self.special_check.pack()

       
        self.generate_button = tk.Button(root, text="Generate Password", font=("Arial", 12), command=self.generate_password)
        self.generate_button.pack(pady=20)

       
        self.result_label = tk.Label(root, text="Generated Password: ", font=("Arial", 12))
        self.result_label.pack(pady=10)

   
    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length < 1:
                messagebox.showerror("Error", "Password length must be at least 1.")
                return
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number for the password length.")
            return

      
        characters = string.ascii_lowercase  
        if self.include_uppercase.get():
            characters += string.ascii_uppercase
        if self.include_digits.get():
            characters += string.digits
        if self.include_special.get():
            characters += string.punctuation

        
        password = ''.join(random.choice(characters) for _ in range(length))

      
        self.result_label.config(text=f"Generated Password: {password}")


if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
