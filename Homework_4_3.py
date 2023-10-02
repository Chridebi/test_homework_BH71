# TODO 4.3 *Заполнить словарь где ключами будут выступать числа от 0 до n, а
# значениями вложенный словарь с ключами "name" и "email", а значения
# для этих ключей будут браться с клавиатуры

n = int(input('Vvedite n:'))

data_dict = {i:   {"name": input('Vvedite name: '), "email": input('Vvedite email: ')} for i in range(0, n)}
print(data_dict)
