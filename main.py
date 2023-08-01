# Напишите функцию для транспонирования матрицы Пример: [[1, 2, 3], [4, 5, 6]] -> [[1,4], [2,5], [3, 6]]
#
# Напишите функцию принимающую на вход только ключевые параметры(kwargs) и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента. Если ключ не хешируем, используйте его строковое представление.
# reverse_kwargs(rev=True, acc="YES", stroka=4) -> {True: "rev", "YES": 'acc', 4: "stroka"}
from functions import transposing, reverse_kwargs


transpose_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(transposing(transpose_matrix))

print(reverse_kwargs(nice_day=True, choise_number=55, some_text="Hello", some_list=[1, 3]))
