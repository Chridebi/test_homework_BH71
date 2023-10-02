# TODO 5_3 Вывести четные числа от 2 до N по 5 в строку
print('Vvedite n:')
n = int(input())
spisok = [i for i in range(1, n+1) if i % 2 == 0]
for i in range(1, len(spisok)+1):
    if i % 5 != 0 or i == 0:
        print(spisok[i-1], end=" ")
    else:
        print(spisok[i-1], end="\n ")
