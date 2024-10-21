
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])
]

# задаем функцию которая принтмает в аргументе наш список данных
def calculate_structure_sum(data_structure):
    # переменные которые у нас будут участвовать в подсчете результата
    sum_numbers = 0
    sum_strings = 0

    # задаем функцию в функции для обработки данных, которая обрабатывает переменные в списке
    def recurse(data):
        # говорим что мы работаем с переменными из верхней функции (которые не являются глобальными)
        nonlocal sum_numbers, sum_strings
        # запускаем операторы проверки. Если данные имеют след тип, то мы их обрабатываем по разному

        # обработака доя списков/множеств/кортежей
        if isinstance(data, list) or isinstance(data, tuple) or isinstance(data, set):
            for item in data:
                recurse(item)
        # обработка для словарей
        elif isinstance(data, dict):
            for value in data.values():
                recurse(value)
            for key in data.keys():
                recurse(key)
        # обработка для чисел и строк
        elif isinstance(data, int) or isinstance(data, str):
            if isinstance(data, int):
                sum_numbers += data
            elif isinstance(data, str):
                sum_strings += len(data)

    recurse(data_structure)
    # возвращаем результат
    return sum_numbers + sum_strings

result = calculate_structure_sum(data_structure)
print(result)
