
def cal_loan():
    while True :
        print ("กอรกปะเภทเงินกู้ (ตัวเลข) \n 1. เงินกู้ที่มีระยะเวลา \n 2. เงินเบิกเกินบัญชี \n 3. ลูกค้ารายย่อยชั้นดี")
        type = input("เลือกประเภทเงินกู้ ")
        
        if type not in ["1" , "2" , "3"] :
            print ("ประเภทเงินกู้ไม่ตรงกับที่ต้องการ    กรุณากรอกใหม่")
            continue

        try :
            loan = float(input("กรอกจำนวนเงินกู้ ")) 
            year = int (input("กรอกจำนวนปี "))
        except ValueError :
            print ("กรุณากรอหใหม่ให้ถูกต้อง")
            continue
        if type == "1" :
            interest = loan * (year * 0.069)
        elif type == "2" :
            interest = loan * (year * 0.06745)
        elif type == "3" :
            interest = loan * (year * 0.06595)

        total = loan + interest

        print(f"\nจำนวนเงินต้น: {loan} บาท")
        print(f"ดอกเบี้ยที่ต้องจ่าย: {interest:,.2f} บาท")
        print(f"รวมทั้งหมดที่ต้องจ่าย: {total:,.2f} บาท\n")
        break

cal_loan()