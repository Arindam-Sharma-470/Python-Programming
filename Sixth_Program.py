import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from tkinter import scrolledtext

# Database setup
conn = sqlite3.connect('billing_software.db')
cursor = conn.cursor()

# Create tables if they don't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS Product (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price REAL NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Customer (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS SalesTransaction (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    total_price REAL NOT NULL,
    FOREIGN KEY(customer_id) REFERENCES Customer(id),
    FOREIGN KEY(product_id) REFERENCES Product(id)
)
''')

conn.commit()

class BillingSoftwareApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Billing Software")

        self.create_widgets()

    def create_widgets(self):
        # Tabs
        tab_control = ttk.Notebook(self.root)
        
        self.product_tab = ttk.Frame(tab_control)
        self.customer_tab = ttk.Frame(tab_control)
        self.billing_tab = ttk.Frame(tab_control)
        
        tab_control.add(self.product_tab, text='Products')
        tab_control.add(self.customer_tab, text='Customers')
        tab_control.add(self.billing_tab, text='Billing')
        tab_control.pack(expand=1, fill='both')

        self.create_product_tab()
        self.create_customer_tab()
        self.create_billing_tab()

    def create_product_tab(self):
        # Product Entry
        self.product_name_label = tk.Label(self.product_tab, text="Product Name:")
        self.product_name_label.grid(column=0, row=0, padx=10, pady=10)
        
        self.product_name_entry = tk.Entry(self.product_tab)
        self.product_name_entry.grid(column=1, row=0, padx=10, pady=10)
        
        self.product_price_label = tk.Label(self.product_tab, text="Product Price:")
        self.product_price_label.grid(column=0, row=1, padx=10, pady=10)
        
        self.product_price_entry = tk.Entry(self.product_tab)
        self.product_price_entry.grid(column=1, row=1, padx=10, pady=10)
        
        self.add_product_button = tk.Button(self.product_tab, text="Add Product", command=self.add_product)
        self.add_product_button.grid(column=0, row=2, columnspan=2, padx=10, pady=10)

    def create_customer_tab(self):
        # Customer Entry
        self.customer_name_label = tk.Label(self.customer_tab, text="Customer Name:")
        self.customer_name_label.grid(column=0, row=0, padx=10, pady=10)
        
        self.customer_name_entry = tk.Entry(self.customer_tab)
        self.customer_name_entry.grid(column=1, row=0, padx=10, pady=10)
        
        self.customer_phone_label = tk.Label(self.customer_tab, text="Customer Phone:")
        self.customer_phone_label.grid(column=0, row=1, padx=10, pady=10)
        
        self.customer_phone_entry = tk.Entry(self.customer_tab)
        self.customer_phone_entry.grid(column=1, row=1, padx=10, pady=10)
        
        self.add_customer_button = tk.Button(self.customer_tab, text="Add Customer", command=self.add_customer)
        self.add_customer_button.grid(column=0, row=2, columnspan=2, padx=10, pady=10)

    def create_billing_tab(self):
        # Billing Section
        self.customer_label = tk.Label(self.billing_tab, text="Customer:")
        self.customer_label.grid(column=0, row=0, padx=10, pady=10)
        
        self.customer_combobox = ttk.Combobox(self.billing_tab)
        self.customer_combobox.grid(column=1, row=0, padx=10, pady=10)
        self.load_customers()

        self.product_label = tk.Label(self.billing_tab, text="Product:")
        self.product_label.grid(column=0, row=1, padx=10, pady=10)
        
        self.product_combobox = ttk.Combobox(self.billing_tab)
        self.product_combobox.grid(column=1, row=1, padx=10, pady=10)
        self.load_products()

        self.quantity_label = tk.Label(self.billing_tab, text="Quantity:")
        self.quantity_label.grid(column=0, row=2, padx=10, pady=10)
        
        self.quantity_entry = tk.Entry(self.billing_tab)
        self.quantity_entry.grid(column=1, row=2, padx=10, pady=10)
        
        self.add_transaction_button = tk.Button(self.billing_tab, text="Add Transaction", command=self.add_transaction)
        self.add_transaction_button.grid(column=0, row=3, columnspan=2, padx=10, pady=10)

        self.invoice_button = tk.Button(self.billing_tab, text="Generate Invoice", command=self.generate_invoice)
        self.invoice_button.grid(column=0, row=4, columnspan=2, padx=10, pady=10)

        self.transactions_listbox = tk.Listbox(self.billing_tab)
        self.transactions_listbox.grid(column=0, row=5, columnspan=2, padx=10, pady=10)

        self.invoice_text = scrolledtext.ScrolledText(self.billing_tab, width=40, height=10, wrap=tk.WORD)
        self.invoice_text.grid(column=0, row=6, columnspan=2, padx=10, pady=10)

    def load_customers(self):
        cursor.execute("SELECT id, name FROM Customer")
        customers = cursor.fetchall()
        self.customer_combobox['values'] = [f"{customer[0]}: {customer[1]}" for customer in customers]

    def load_products(self):
        cursor.execute("SELECT id, name FROM Product")
        products = cursor.fetchall()
        self.product_combobox['values'] = [f"{product[0]}: {product[1]}" for product in products]

    def add_product(self):
        name = self.product_name_entry.get()
        price = float(self.product_price_entry.get())
        cursor.execute("INSERT INTO Product (name, price) VALUES (?, ?)", (name, price))
        conn.commit()
        self.product_name_entry.delete(0, tk.END)
        self.product_price_entry.delete(0, tk.END)
        messagebox.showinfo("Success", "Product added successfully!")
        self.load_products()

    def add_customer(self):
        name = self.customer_name_entry.get()
        phone = self.customer_phone_entry.get()
        cursor.execute("INSERT INTO Customer (name, phone) VALUES (?, ?)", (name, phone))
        conn.commit()
        self.customer_name_entry.delete(0, tk.END)
        self.customer_phone_entry.delete(0, tk.END)
        messagebox.showinfo("Success", "Customer added successfully!")
        self.load_customers()

    def add_transaction(self):
        customer_id = int(self.customer_combobox.get().split(":")[0])
        product_id = int(self.product_combobox.get().split(":")[0])
        quantity = int(self.quantity_entry.get())
        cursor.execute("SELECT price FROM Product WHERE id=?", (product_id,))
        price = cursor.fetchone()[0]
        total_price = price * quantity
        cursor.execute("INSERT INTO SalesTransaction (customer_id, product_id, quantity, total_price) VALUES (?, ?, ?, ?)", (customer_id, product_id, quantity, total_price))
        conn.commit()
        self.transactions_listbox.insert(tk.END, f"Customer {customer_id} bought {quantity} of product {product_id} for ${total_price:.2f}")
        messagebox.showinfo("Success", "Transaction added successfully!")

    def generate_invoice(self):
        invoice_text = "Invoice\n\n"
        for i in self.transactions_listbox.curselection():
            transaction = self.transactions_listbox.get(i)
            invoice_text += transaction + "\n"
        self.invoice_text.delete(1.0, tk.END)
        self.invoice_text.insert(tk.END, invoice_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = BillingSoftwareApp(root)
    root.mainloop()
