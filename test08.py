# สร้างโปรแกรมคำนวณเงินเดือนสุทธิที่ต้องจ่ายหลังจากหักภาษีแล้ว 7% ของเงินเดือน  และหักค่าประกันสังคม 3% ของเงินเดือน
# โดยรับค่ารหัสพนักงาน ชื่อพนักงาน เงินเดือน ทางแป้นพิมพ์ และแสดงผลข้อมูลที่รับมา
# พร้อมกับรายละเอียดว่าต้องเสียภาษีกี่บาท หักค่าประกันสังคมกี่บาท และต้องจ่ายเงินเดือนสุทธิกี่บาท
  
print('++++++++++++++++++++')
print(' โปรแกรมคำนวณเงินเดือน')
print('++++++++++++++++++++')
emp_code = input('ป้อนรหัสพนักงาน: ')
emp_name = input('ป้อนชื่อพนักงาน: ')
emp_salary = input('ป้อนเงินเดือน: ')
print('++++++++++++++++++++')
tax = float( emp_salary ) * 7 / 100            # หรือ emp_salary * 0.07
insurence = float( emp_salary ) * 3 / 100      # หรือ emp_salary * 0.03
emp_salary_net = float( emp_salary ) - tax - insurence
print(f'รหัส: {emp_code} ชื่อ: {emp_name} เงินเดือน: {emp_salary}')
print(f'หักภาษี {tax} บาท')
print(f'หักค่าประกันสังคม {insurence} บาท')
print(f'ต้องจ่ายเงินเดือนสุทธิ {emp_salary_net} บาท')
print('++++++++++++++++++++')
# ใช้ ,
print('รหัส:' ,emp_code, 'ชื่อ:' ,emp_name, 'เงินเดือน:' ,emp_salary,)
print('หักภาษี ',tax, 'บาท')
print('หักค่าประกันสังคม' ,insurence, 'บาท')
print('ต้องจ่ายเงินเดือนสุทธิ' ,emp_salary_net, 'บาท')
print('+++++++++++++++++++')
# ใช้ +
print('รหัส:'+emp_code+ 'ชื่อ:' +emp_name+'เงินเดือน:'+emp_salary)
print('หักภาษี ' +str(tax) + 'บาท')
print('หักค่าประกันสังคม' +str(insurence) + 'บาท')
print('ต้องจ่ายเงินเดือนสุทธิ' +str(emp_salary_net) + 'บาท')
print('++++++++++++++++++++')
# ใช้เมธอด format
print('รหัส: {}' .format(emp_code) + 'ชื่อ: {}' .format(emp_name) + 'เงินเดือน: {}' .format(emp_salary) )
print('หักภาษี {}' .format(tax) + 'บาท')
print('หักค่าประกันสังคม {}' .format(insurence) + 'บาท')
print('ต้องจ่ายเงินเดือนสุทธิ {}' .format(emp_salary_net) + 'บาท')
print('++++++++++++++++++++')