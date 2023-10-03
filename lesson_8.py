class A:


"""Магические методы"""
def __init__(self, email, age):
    """

    :param self:
    :param email: почта пользователя
    :param age: возраст пользователя
    :return:
    """
    self.email = email
    self.age = age

class Product:
    def __init__(self, name=str, price: float):
        """

        :param name:
        :param price:
        """
        self.name = name
        self.price = price

Product1 = Product(name="Latte", price = 5.0)

def set_discount (self):
    if product1.price * 0.90 > 4 :
       product.price *= 0.9
    else:
       self.price *= 0.95

def __str__(self):
    return f"{self.name}: {self.price}$"

def __bool__(self):
    return self.is_published

def __len__(self):
    return round(self.price**2)

class Category:
    def __int__(self, name: str, product: list[Products]):
        self.name = name
        self.products = products

category1 = Category(name="Coffee", products=[products1, products1])
for i in category1:
    print(i)
"""Для реализации итераторов 2 метода"""
def __iter__(self):
    return self

def __next__(self):
    self.i += 1
    if self.i < len (self.products) -1:
        return self.products[self.i]
    else:
        self.i = -1
        raise StopIteration

from random import radint

a = randint(a:0, b:10)
if f!=0:
    return
else:
    raise StopIteration

def __len__(self):
    return len(self.products)

def __getitem__(self, item):
    return self.products[item]
"""Магические методы для сравнения"""
def __gt__(self, other):
    pass
def __ge__(self, other):
    pass
def __lt__(self, other):
    pass
def __le__(self, other):
    return not  self
def __eq__(self, other):
    pass

def __ne__(self, other):
    pass

Product1 = Product(name="Latte", price = 5.0)
Product2 = Product(name="Capucino", price = 4.5)
print (Product1 > Product2)
def __gt__(self, other):
    if isinstance(other, Product):
        return self.price == other.price
    elif isinstance(other, Product):

"""левое сложение"""
def __add__(self, other):
    pass

"""правое сложение"""
def __radd__(self, other):
    return self.__add__(other)

"""+ равно"""
def __iadd__(self, other):
    pass

"""not or"""
def __xor__(self, other):
    pass