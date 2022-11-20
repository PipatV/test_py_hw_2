#ข้อ2 ISBN 
#รับตัวเลข
num = input()

#นำตัวเลขมาใช้ตามสมการ
sum_num = (10*int(num[0]))+(9*int(num[1]))+(8*int(num[2]))+(7*int(num[3]))+(6*int(num[4]))+(5*int(num[5]))+(4*int(num[6]))+(3*int(num[7]))+(2*int(num[8]))   

# หาตัวสุดท้าย ได้ตัวเลขมา ลบ 11 ลงตัว
num_10 = 11-(sum_num%11) 

# print(sum_num)
# print(num_10)

#แสดงค่าโดยต่อ Str
print(num+str(num_10))
