﻿# T2 : Tip Converter

import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Tip Calculator")
root.geometry("800x600+100+100")
f=("Century")

def calculate_tip():
	try:
		bill_amount = float(entry_bill_amount.get())
		tip_percentage = float(entry_tip_percentage.get())
		num_people = int(entry_num_people.get())

		if not (0 <= bill_amount <= 100000):
			raise ValueError("Bill amount must be between 0 and 10,000")

		if not (0 <= tip_percentage <= 100):
			raise ValueError("Tip percentage must be between 0 and 100")

		if not (1 <= num_people <= 20):
			raise ValueError("Number of people must be between 1 and 10")

		tip_amount = (bill_amount * tip_percentage) / 100
		total_amount = bill_amount + tip_amount
		amount_per_person = total_amount / num_people

		result_label.config(text=f"Tip Amount: Rs. {tip_amount:.2f}\n"
					 f"Total Amount: Rs. {total_amount:.2f}\n"
					 f"Amount per Person: Rs. {amount_per_person:.2f}")

	except ValueError as e:
		messagebox.showerror("Input Error", str(e))


def clear_fields():
	entry_bill_amount.delete(0, tk.END)
	entry_tip_percentage.delete(0, tk.END)
	entry_num_people.delete(0, tk.END)
	result_label.config(text="")

label_title = tk.Label(root, text="Tip Calculator",font=(f, 20, "bold"))
label_title.pack(pady=20)	

label_bill_amount = tk.Label(root, text="Bill Amount:",font=(f, 16, "bold"))
label_bill_amount.pack()

entry_bill_amount = tk.Entry(root)
entry_bill_amount.pack(pady=10)

label_tip_percentage = tk.Label(root, text="Tip Percentage:",font=(f, 16, "bold"))
label_tip_percentage.pack()

entry_tip_percentage = tk.Entry(root)
entry_tip_percentage.pack(pady=10)

label_num_people = tk.Label(root, text="Number of People:",font=(f, 16, "bold"))
label_num_people.pack()

entry_num_people = tk.Entry(root)
entry_num_people.pack(pady=10)

calculate_button = tk.Button(root, text="Calculate", command=calculate_tip, font=(f, 14, "bold"))
calculate_button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

clear_button = tk.Button(root, text="Clear", command=clear_fields, font=(f, 14, "bold"))
clear_button.pack()
		
root.mainloop()
