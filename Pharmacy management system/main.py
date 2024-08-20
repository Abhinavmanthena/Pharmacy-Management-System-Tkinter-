import tkinter as tk
from tkinter import messagebox
class PharmacyManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Pharmacy Management System")
        self.root.geometry("300x400")
        self.medications=[]
        self.createwidgets()
    def createwidgets(self):
        tk.Label(self.root,text="Medication Name").grid(row=0,column=0,padx=10,pady=5)
        self.med_name_entry=tk.Entry(self.root)
        self.med_name_entry.grid(row=0,column=1,padx=10,pady=5)

        tk.Label(self.root,text="Quantity:").grid(row=1,column=0,padx=10,pady=5)
        self.quantity_entry=tk.Entry(self.root)
        self.quantity_entry.grid(row=1,column=1,padx=10,pady=5)

        add_button=tk.Button(self.root,text="Add Medication",command=self.add_medication)
        add_button.grid(row=2,column=0,columnspan=2,padx=10,pady=5)

        self.med_listbox=tk.Listbox(self.root,width=40,height=10)
        self.med_listbox.grid(row=3,column=0,columnspan=2,padx=10,pady=5)

        delete_button=tk.Button(self.root,text="Delete Selected",command=self.delete_medication)
        delete_button.grid(row=4,column=0,columnspan=2,padx=10,pady=5)

    def add_medication(self):
        med_name=self.med_name_entry.get()
        quantity=self.quantity_entry.get()
        if med_name and quantity:
            try:
                quantity=int(quantity)
                if quantity <0:
                    raise ValueError
            except ValueError:
                messagebox.showerror("error","Quantity must be non-negative integer.")
                return
            self.medications.append((med_name, quantity))
            self.update_med_listbox()
            self.med_name_entry.delete(0,tk.END)
            self.quantity_entry.delete(0,tk.END)
        else:
            messagebox.showerror("error","Please enter both both Medication name and Qunatity")

    def delete_medication(self):
        selected_index=self.med_listbox.curselection()
        if selected_index:
            index=selected_index[0]
            del self.medications[index]
            self.update_med_listbox()
        else:
            messagebox.showerror("Error","Please select a medication to delete")


    def update_med_listbox(self):
        self.med_listbox.delete(0,tk.END)
        for med_name,quantity in self.medications:
            self.med_listbox.insert(tk.END,f"{med_name} - Qunatity: {quantity}")


root=tk.Tk()
app=PharmacyManagementSystem(root)
root.mainloop()










