# TODO 3.1 Пользователь вводит предложение, заменить все пробелы на "-" 2-мя способами
# text = "The start to the Harry Potter film series is filled with valiant heroes and irresistible characters."
print('Vvedite предложение:')
text = str(input())
print(text.replace(" ", "-"))
print("-".join(text.split(" ")))
