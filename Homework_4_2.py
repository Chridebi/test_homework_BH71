# TODO 4.2 Без использования collections, написать программу, которая будет
# создавать словарь для подсчитывания количества вхождений каждой
# буквы в текст введенный с клавиатуры
# text = "The start to the Harry Potter film series is filled with valiant heroes and irresistible characters."
print('Vvedite text:')
text = str(input())
spisok = sorted(list(text))
conv_dict = tuple(spisok)
conv_dict_new = {conv_dict[i]: spisok.count(conv_dict[i]) for i in range(len(conv_dict))}
print(conv_dict_new)
