# TODO 5_2 Сделать калькулятор: у пользователя спрашивается число, потом действие и второе число
print('Введите 1-е число=:')
number_1 = int(input())
print('Введите действие + - * / :')
deistvie = str(input())
print('Введите 2-е число=:')
number_2 = int(input())

if deistvie == "+":
    print(number_1 + number_2)
else:
    if deistvie == "-":
        print(number_1 - number_2)
    else:
        if deistvie == "*":
            print(number_1 * number_2)
        else:
            if deistvie == "/":
                print(number_1 / number_2)
