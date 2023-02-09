# This code creates a Tkinter GUI with labels for each text box, and the account information is saved in a text file named accounts.txt in a JSON format. 
# When you run the code, a window should appear with labels and text boxes, and you can enter the account information and retrieve 
# it just as in the previous example.

# Note that in this version, the account information is appended to the text file whenever the Submit button is clicked in the "Create Account" section. 
# The account information is retrieved by matching the account name that is entered in the "Retrieve Account" section, 
# and the corresponding username and password are printed out.



import tkinter as tk
import json

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()
        
    def create_widgets(self):
        tk.Label(self, text="Account Name:").pack()
        self.create_account_name = tk.Entry(self)
        self.create_account_name.pack()
        
        tk.Label(self, text="Username:").pack()
        self.create_username = tk.Entry(self)
        self.create_username.pack()
        
        tk.Label(self, text="Password:").pack()
        self.create_password = tk.Entry(self, show="*")
        self.create_password.pack()
        
        self.create_submit = tk.Button(self, text="Submit", command=self.create_account)
        self.create_submit.pack()
        
        tk.Label(self, text="Retrieve Account:").pack()
        self.retrieve_account_name = tk.Entry(self)
        self.retrieve_account_name.pack()
        
        self.retrieve_submit = tk.Button(self, text="Submit", command=self.retrieve_account)
        self.retrieve_submit.pack()
    
    def create_account(self):
        account_name = self.create_account_name.get()
        username = self.create_username.get()
        password = self.create_password.get()
        
        account = {"account_name": account_name, "username": username, "password": password}
        
        with open("accounts.txt", "a") as f:
            f.write(json.dumps(account) + "\n")
        
        self.create_account_name.delete(0, tk.END)
        self.create_username.delete(0, tk.END)
        self.create_password.delete(0, tk.END)
        
    def retrieve_account(self):
        account_name = self.retrieve_account_name.get()
        
        with open("accounts.txt", "r") as f:
            for line in f:
                account = json.loads(line)
                if account["account_name"] == account_name:
                    print(f"Username: {account['username']}\nPassword: {account['password']}")
                    return
                    
        print("Account not found.")

root = tk.Tk()
app = Application(master=root)
app.mainloop()
