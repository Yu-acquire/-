
print('请输入两个数字')
print("输入'q'时停止")

while True:
    first_number = input("first_number:")
    if  first_number == 'q':
        break
    second_number = input("second_number:")
    try:
        anwer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(anwer)