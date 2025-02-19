import tkinter as tk
from tkinter import messagebox

def calculate_loan():
    loan_type = loan_type_var.get()
    loan_amount = loan_entry.get()
    loan_years = year_entry.get()
    
    if loan_type not in ["1", "2", "3"]:
        messagebox.showerror("Error", "ประเภทเงินกู้ไม่ถูกต้อง กรุณาเลือกใหม่")
        return
    
    try:
        loan = float(loan_amount)
        year = int(loan_years)
    except ValueError:
        messagebox.showerror("Error", "กรุณากรอกข้อมูลให้ถูกต้อง")
        return
    
    if loan_type == "1":
        interest = loan * (year * 0.069)
    elif loan_type == "2":
        interest = loan * (year * 0.06745)
    elif loan_type == "3":
        interest = loan * (year * 0.06595)
    
    total = loan + interest
    
    result_label.config(text=f"จำนวนเงินต้น: {loan:,.2f} บาท\n"
                             f"ดอกเบี้ยที่ต้องจ่าย: {interest:,.2f} บาท\n"
                             f"รวมทั้งหมดที่ต้องจ่าย: {total:,.2f} บาท")

# สร้าง GUI
root = tk.Tk()
root.title("Loan Calculator")
root.geometry("600x500")  # เพิ่มขนาดหน้าต่างให้ใหญ่ขึ้น
root.configure(bg="#FFC0CB")

tk.Label(root, text="Loan Calculator", font=("Arial", 22, "bold"), fg="white", bg="#FF69B4").pack(fill=tk.X, pady=10)

tk.Label(root, text="ประเภทเงินกู้: ", font=("Arial", 16), bg="#FFC0CB").pack()
tk.Label(root, text="1. เงินกู้ที่มีระยะเวลา", font=("Arial", 14), bg="#FFC0CB").pack()
tk.Label(root, text="2. เงินเบิกเกินบัญชี", font=("Arial", 14), bg="#FFC0CB").pack()
tk.Label(root, text="3. ลูกค้ารายย่อยชั้นดี", font=("Arial", 14), bg="#FFC0CB").pack()

loan_type_var = tk.StringVar()
loan_type_entry = tk.Entry(root, textvariable=loan_type_var, width=30, font=("Arial", 16))
loan_type_entry.pack(pady=5)

tk.Label(root, text="จำนวนเงินกู้:", font=("Arial", 16), bg="#FFC0CB").pack()
loan_entry = tk.Entry(root, width=30, font=("Arial", 16))
loan_entry.pack(pady=5)

tk.Label(root, text="จำนวนปี:", font=("Arial", 16), bg="#FFC0CB").pack()
year_entry = tk.Entry(root, width=30, font=("Arial", 16))
year_entry.pack(pady=5)

calculate_button = tk.Button(root, text="คำนวณ", command=calculate_loan, bg="#FF69B4", fg="white", font=("Arial", 16, "bold"), width=15)
calculate_button.pack(pady=10)

result_label = tk.Label(root, text="", bg="#FFC0CB", font=("Arial", 16, "bold"))
result_label.pack(pady=10)

root.mainloop()
