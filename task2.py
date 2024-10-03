
import tkinter as tk
from tkinter import messagebox

# Create the main calculator application class
class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("300x300")

        # Create labels and entry boxes for user input
        self.num1_label = tk.Label(root, text="Enter First Number:", font=("Arial", 12))
        self.num1_label.pack(pady=10)
        
        self.num1_entry = tk.Entry(root, font=("Arial", 12))
        self.num1_entry.pack(pady=10)

        self.num2_label = tk.Label(root, text="Enter Second Number:", font=("Arial", 12))
        self.num2_label.pack(pady=10)
        
        self.num2_entry = tk.Entry(root, font=("Arial", 12))
        self.num2_entry.pack(pady=10)

        # Create a dropdown for selecting the operation
        self.operation_label = tk.Label(root, text="Choose Operation:", font=("Arial", 12))
        self.operation_label.pack(pady=10)

        self.operation_var = tk.StringVar()
        self.operation_var.set("Add")  # Default option

        self.operation_menu = tk.OptionMenu(root, self.operation_var, "Add", "Subtract", "Multiply", "Divide")
        self.operation_menu.pack(pady=10)

        # Create a button for performing the calculation
        self.calculate_button = tk.Button(root, text="Calculate", font=("Arial", 12), command=self.calculate)
        self.calculate_button.pack(pady=10)

        # Create a label for displaying the result
        self.result_label = tk.Label(root, text="Result: ", font=("Arial", 12))
        self.result_label.pack(pady=10)

    # Function to perform the calculation based on the operation chosen
    def calculate(self):
        try:
            num1 = float(self.num1_entry.get())
            num2 = float(self.num2_entry.get())
            operation = self.operation_var.get()

            if operation == "Add":
                result = num1 + num2
            elif operation == "Subtract":
                result = num1 - num2
            elif operation == "Multiply":
                result = num1 * num2
            elif operation == "Divide":
                if num2 != 0:
                    result = num1 / num2
                else:
                    messagebox.showerror("Error", "Division by zero is not allowed.")
                    return
            else:
                result = "Invalid Operation"

            self.result_label.config(text=f"Result: {result}")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers.")

# Main function to run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
