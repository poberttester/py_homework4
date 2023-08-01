import numpy as np

# транспонированиt матрицы
def transposing(matrix):
    """Функция для транспонирования квадратной матрицы, принемает на вход коллекцию"""
    return np.transpose(matrix)


def reverse_kwargs(**kwargs):
    """Функция принимающая на вход только ключевые параметры(kwargs) и возвращающая словарь,
       где ключ — значение переданного аргумента, а значение — имя аргумента."""

    try:
        new_dict = {
            value: key for key, value in kwargs.items()
        }
        return new_dict
    except TypeError:
        new_dict = {
            str(value): key for key, value in kwargs.items()
        }
        return new_dict







