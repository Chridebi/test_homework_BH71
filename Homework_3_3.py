# TODO 3.3 Пользователь вводит Имя, Возраст и Город, сформировать приветственное сообщение путем форматирования
#  3-мя способами
print("vvedite Name")
Name = input()
Age = 45
Town = "Monreal"
print("Hello %s your age is %d. You are from %s." % (Name, Age, Town))
print("Hello {} your age is {}. You are from {}.".format(Name, Age, Town))
print(f"Hello {Name} your age is {Age}. You are from {Town}.")
