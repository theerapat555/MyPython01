#1. no parameter on return
# parameter คือ ตัวแปรประเภทหนึ่ง ที่ใช้ได้เฉพาะในฟังก์ชันนั้นๆ เขียนอยู่ในวงเล็บหลังชื่อฟังก์ชัน
# return คือ ค่าที่ส่บ่งบอกถึงการจบการทำงานของฟังก์ชันนั้นๆ และสั่งค่าที่อยู่หลัง return กลับไปที่จุดเรียกฟังก์ชัน(ถ้ามี)
'''
def func_name():
    คำสั่ง
    คำสั่ง
    คำสั่ง
    ....
'''

print('wow')

def showHI():
    print('HI')

print('woo')

def showHEY():
    print('HEY')

print('wii')

showHI()
showHEY()