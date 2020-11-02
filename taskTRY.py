# task1

# num1 = input("введите первое число: ")
# num2 = input("введите второе число: ")
# res = None
# try:
#     num1 = int(num1)
#     num2 = int(num2)
#     res = num1 / num2
#     print(res)
# except ZeroDivisionError:
#     raise Exception('на ноль делить нельзя')

# task2 

# num1 = input("введите первое число: ")
# num2 = input("введите второе число: ")
# res = None
# try:
#     num1 = int(num1)
#     num2 = int(num2)
#     res = num1 + num2
#     print(res)
# except ValueError:
#     raise Exception('нужно ввести число')

# task3

# sodi = {'a': 1, 'b': 2, 'c': 3, 'd': 4}    
# try:
#     sodi['e']
# except KeyError:
#     raise Exception("В словаре нет такого ключа!")

# task4

# slovo = input('введи лист: ')
# try:
#     if slovo.startswith('[') and slovo.endswith(']'):
#         print(slovo)
#     elif slovo != slovo.startswith('['):
#         raise Exception('Данная программа принимает только List')
# finally:
#     print()

# task5

# listy = [1, 2, 3, 4, 5, 6, 8, 13]
# try:
#     kol = listy[-1]
#     listy[9]
# except IndexError:
#     raise Exception(f'{kol} - последний индекс')
