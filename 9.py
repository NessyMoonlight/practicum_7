n, k, r = map(int, input('введите через пробел длину нити,'
                   'на сколько % она увеличивается и '
                   'длину, которая должна в итоге получиться: \n').split())

day = 1
while n < r:
    n = n + n * (k / 100)
    day += 1
print(day)