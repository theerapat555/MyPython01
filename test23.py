# คำสั่ง break, continue
# break ใน loop ทำงานเมื่อใดจบ loop ทันที
# continue ใน loop ทำงานเมื่อใดจบ loop แค่รอบนั้นทันทีแล้วไปต่อรอบต่อไป

for aa in range(5):
    if aa == 2 :
        break
    print(aa ,'hello...')

print('--------------------')

for aa in range(5):
    if aa == 2 :
        continue
    print(aa ,'hello...')