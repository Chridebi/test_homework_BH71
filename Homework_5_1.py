# TODO 5_1 Вывести первые N чисел кратные M и больше K
try:
    print('Vvedite n:')
    n = int(input())
    print('Vvedite kratnost M:')
    M = int(input())
    print('Vvedite K:')
    K = int(input())
    print('Vvedite N:')
    N = int(input())
except:
    raise ValueError(f"Voznikla osibka vvoda:")
else:
    if M > n:
        print(f"Nevernyj vvod")
        print(f"Vvedite M<{n}, M=")
        M = int(input())
    if K > n:
        print(f"Nevernyj vvod")
        print(f"Vvedite K<{n}, K=")
        K = int(input())
    spisok_of_numbers = [i for i in range(n) if (i % M == 0 and i > K)]
    if N > len(spisok_of_numbers):
        print(f"Vvedite N<={len(spisok_of_numbers)}, N=")
        N = int(input())

print('Вывод первых N чисел кратных M и больше K:')
for i in range(N):
    print(spisok_of_numbers[i], end=" ")
