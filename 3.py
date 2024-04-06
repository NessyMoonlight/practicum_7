import math
while True:
    a = int(input())
    if math.sqrt(a)%1 == 0:
        print('число является полным квадратом')
        break
    else:
        print('число не является полным квадратом, '
              'введите полный квадрат')
