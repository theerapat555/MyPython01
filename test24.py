#สร้างโปรแกรมคำนวณอายุของจากปีเกิด (พ.ศ.) ของพนักงานโรงงานแห่งหนึ่ง 
#โดยป้อนชื่อและปีเกิดทางแป้นพิมพ์ ทั้งนี้โปรแกรมจะหยุดทำงานก็ต่อเมมื่อป้อนชื่อพนักงาน เป็น SAU ก็จะหยุดทำงาน
from datetime import datetime

print('----------------------------')
print('โปรแกรมคำนวณอายุพนักงาน')
print('----------------------------')

while True:
    emp_name = input('ป้อนฃื่อพนักงาน: ')
    if emp_name.upper() == 'SAU':
        break
    emp_year = int(input('ป้อนปีเกิด (พ.ศ.): '))
    emp_age = (datetime.now().year + 543) - emp_year
    print(f'คุณ {emp_name} เกิดปี {emp_year} อายุ {emp_age} ปี')
      