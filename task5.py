import tkinter as tk
from tkinter import messagebox, simpledialog

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address


class ContactManager:
    def __init__(self, root):
        self.contacts = []  
        
        
        self.root = root
        self.root.title("Contact Manager")
        
      
        self.add_contact_button = tk.Button(self.root, text="Add Contact", command=self.add_contact)
        self.add_contact_button.pack(pady=5)
        
        
        self.view_contacts_button = tk.Button(self.root, text="View Contacts", command=self.view_contacts)
        self.view_contacts_button.pack(pady=5)
        
        
        self.search_contact_button = tk.Button(self.root, text="Search Contact", command=self.search_contact)
        self.search_contact_button.pack(pady=5)
        
       
        self.update_contact_button = tk.Button(self.root, text="Update Contact", command=self.update_contact)
        self.update_contact_button.pack(pady=5)
        
        
        self.delete_contact_button = tk.Button(self.root, text="Delete Contact", command=self.delete_contact)
        self.delete_contact_button.pack(pady=5)
    
    
    def add_contact(self):
        name = simpledialog.askstring("Input", "Enter contact name:")
        phone = simpledialog.askstring("Input", "Enter contact phone number:")
        email = simpledialog.askstring("Input", "Enter contact email:")
        address = simpledialog.askstring("Input", "Enter contact address:")
        
        if name and phone:
            new_contact = Contact(name, phone, email, address)
            self.contacts.append(new_contact)
            messagebox.showinfo("Success", f"Contact {name} added!")
        else:
            messagebox.showerror("Error", "Name and phone number are required!")

    
    def view_contacts(self):
        if not self.contacts:
            messagebox.showinfo("Info", "No contacts available.")
            return
        
        contact_list_window = tk.Toplevel(self.root)
        contact_list_window.title("Contact List")
        
        for contact in self.contacts:
            tk.Label(contact_list_window, text=f"Name: {contact.name}, Phone: {contact.phone}").pack()
    
    
    def search_contact(self):
        search_term = simpledialog.askstring("Input", "Enter name or phone number to search:")
        
        if not search_term:
            messagebox.showerror("Error", "Please enter a valid search term!")
            return
        
        found = False
        search_result_window = tk.Toplevel(self.root)
        search_result_window.title("Search Results")
        
        for contact in self.contacts:
            if search_term in contact.name or search_term in contact.phone:
                tk.Label(search_result_window, text=f"Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}, Address: {contact.address}").pack()
                found = True
        
        if not found:
            messagebox.showinfo("Info", "No matching contact found.")
    
    
    def update_contact(self):
        search_term = simpledialog.askstring("Input", "Enter the name of the contact to update:")
        
        if not search_term:
            messagebox.showerror("Error", "Please enter a valid name!")
            return
        
        for contact in self.contacts:
            if search_term == contact.name:
                contact.phone = simpledialog.askstring("Input", f"Enter new phone number for {contact.name}:")
                contact.email = simpledialog.askstring("Input", f"Enter new email for {contact.name}:")
                contact.address = simpledialog.askstring("Input", f"Enter new address for {contact.name}:")
                messagebox.showinfo("Success", f"Contact {contact.name} updated!")
                return
        
        messagebox.showinfo("Info", "Contact not found.")

    
    def delete_contact(self):
        search_term = simpledialog.askstring("Input", "Enter the name of the contact to delete:")
        
        if not search_term:
            messagebox.showerror("Error", "Please enter a valid name!")
            return
        
        for contact in self.contacts:
            if search_term == contact.name:
                self.contacts.remove(contact)
                messagebox.showinfo("Success", f"Contact {contact.name} deleted!")
                return
        
        messagebox.showinfo("Info", "Contact not found.")
    

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManager(root)
    root.mainloop()

