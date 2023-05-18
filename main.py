#1

class OddIterator:
    def __init__(self, n):
        if n < 1:
            raise ValueError("Неправильне значення N")
        self.n = n
        self.nepar = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.nepar > self.n:
            raise StopIteration("Кінець ітерації")
        odd_number = self.nepar
        self.nepar += 2
        return odd_number
try:
    n = int(input("Введіть значення N: "))
    iterator = OddIterator(n)
    for number in iterator:
        print(number)
except ValueError as e:
    print("Помилка:", e)
except StopIteration as e:
    print("Кінець ітерації:", e)

#2

class SquareGenerator:
    def __init__(self,b):
        if not isinstance(b, (int,float)):
            raise TypeError("Це повинно бути числом")
        self.b = b
    def generator_square(self):
        for i in range(1,int(self.b) + 1):
            yield i**2

try:
    for num in SquareGenerator(b = int(input("Введіть знач b:"))).generator_square():
         print(num)
except TypeError as e:
    print(e)
#3

class ListIterator:
    def __init__(self, lst):
        self.lst = lst
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= len(self.lst):
            raise StopIteration
        element = self.lst[self.current]
        self.current += 1
        return element

N = int(input("Введіть значення N: "))
numbers = list(range(1, N + 1))

iterator = ListIterator(numbers)
for element in iterator:
    print(element)

#4

def multiply_by(n):
    def zamik(x):
        return x * n
    return zamik

multiply_by_n = multiply_by(n = int(input("Введіть число:")))
result = multiply_by_n(int(input("Введіть кількість замиканнь:")))
print(result)
