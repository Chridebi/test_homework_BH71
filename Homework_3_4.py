# TODO 3.4 Пользователь вводит 3 числа, сказать сколько из них положительных
# и сколько отрицательных
print('Vvedite number 1:')
a = float(input())
print('Vvedite number 2:')
b = float(input())
print('Vvedite number 3:')
c = float(input())

print("count_plus=", (a > 0) + (b > 0) + (c > 0))
print("count_minus=", (a < 0) + (b < 0) + (c < 0))
