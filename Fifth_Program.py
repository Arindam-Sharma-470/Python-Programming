import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import requests

class CurrencyConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("USD Currency Converter")

        self.api_url = "https://api.exchangerate-api.com/v4/latest/USD"
        self.currencies = self.get_currencies()

        self.create_widgets()

    def get_currencies(self):
        response = requests.get(self.api_url)
        data = response.json()
        return data["rates"]

    def create_widgets(self):
        self.amount_label = tk.Label(self.root, text="Amount in USD:")
        self.amount_label.grid(column=0, row=0, padx=10, pady=10)

        self.amount_entry = tk.Entry(self.root)
        self.amount_entry.grid(column=1, row=0, padx=10, pady=10)

        self.target_currency_label = tk.Label(self.root, text="Convert to:")
        self.target_currency_label.grid(column=0, row=1, padx=10, pady=10)

        self.target_currency_combobox = ttk.Combobox(self.root, values=list(self.currencies.keys()))
        self.target_currency_combobox.grid(column=1, row=1, padx=10, pady=10)

        self.convert_button = tk.Button(self.root, text="Convert", command=self.convert_currency)
        self.convert_button.grid(column=0, row=2, columnspan=2, padx=10, pady=10)

        self.result_label = tk.Label(self.root, text="Result:")
        self.result_label.grid(column=0, row=3, columnspan=2, padx=10, pady=10)

    def convert_currency(self):
        try:
            amount = float(self.amount_entry.get())
            target_currency = self.target_currency_combobox.get()
            if target_currency in self.currencies:
                converted_amount = amount * self.currencies[target_currency]
                self.result_label.config(text=f"Result: {converted_amount:.2f} {target_currency}")
            else:
                messagebox.showerror("Error", "Invalid target currency.")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CurrencyConverterApp(root)
    root.mainloop()
