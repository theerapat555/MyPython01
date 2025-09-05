# สร้างโปรแกรมรับข้อมูลจำนวนเต็ม 5 จำนวนจากผู้ใช้
# และคำนวณหาผลรวม และค่าเฉลี่ยของข้อมูลที่รับเข้ามา
# เป็นเท่าใด แล้วแสดงผลทางหน้าจอ
# สูตร  
# ผลรวม = เลขตัวที่1 + เลขตัวที่2 + เลขตัวที่3 + เลขตัวที่4 + เลขตัวที่5
# ค่าเฉลี่ย = ผลรวมของเลข 5 จำนวน / 5
 
# ============================
# Program  Average  5  Number
# ============================
# Enter number 1 : <input>
# Enter number 2 : <input>
# Enter number 3 : <input>
# Enter number 4 : <input>
# Enter number 5 : <input>
# ============================
# Sum of 5 number is : <output>
# Average of 5 number is : <output>
# ============================
# Sum of 5 number is : <output>
# Average of 5 number is : <output>
# ============================
# Sum of 5 number is : <output>
# Average of 5 number is : <output>
# ============================
# Sum of 5 number is : <output>
# Average of 5 number is : <output>
# ============================
print('โปรแกรทหาผลรวมแลำค่าเฉลี่ยจาก 5 เลข')
print('+++++++++++++++++++++++++++++++++++++')
Number1 = input('โปรดป้อนเลข')
Number2 = input('โปรดป้อนเลข')
Number3 = input('โปรดป้อนเลข')
Number4 = input('โปรดป้อนเลข')
Number5 = input('โปรดป้อนเลข')
Numbermix = float(Number1) + float(Number2) + float(Number3) + float(Number4) + float(Number5)

average = Numbermix / 5

print('ผลลัพธ์ของ 5 เลข =', Numbermix)
print('ค่าเฉลี่ยของ 5 เลข =', average)