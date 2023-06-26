# Погружение в Python (семинары)
# Урок 12. ООП. Финал

import my_utils5 as mu5

if __name__ == '__main__':
    print('--== Тестирование класса MyFactorial ==--')
    my_factorial = mu5.MyFactorial(40)
    print('Вычисление факториала:')
    print(my_factorial.get_factorial())
    print('Просмотр "кэша" вычисленных значений факториала:')
    print(my_factorial)

    with mu5.MyFactorial(7, 'contex_manager.json') as fact:
        fact.get_factorial()

    print('\n--== Тестирование класса MyFactorial ==--')
    for i in mu5.MyRangeFactorial(2, 10, 2):
        print(i)

    print('\n--== Тестирование класса MyRectangle ==--')
    rec = mu5.MyRectangle(5, 4)
    print(rec)
    print(f'Ширина прямоугольника: {rec.width}')
    print(f'Высота прямоугольника: {rec.height}')

    rec.height = 7
    rec.width = 7
    print(rec)

    try:
        rec.height = 10
        rec.width = -10
        print(rec)
    except ValueError:
        print('Ошибка установки параметров!')

    print('Проверка вывода словаря __dict__ c установленным кортежем __slots__:')
    try:
        print(f'Хранитель атрибутов: {rec.__dict__=}')
    except AttributeError:
        print('Кортеж __slots__ установлен, __dict__ - недоступен')


    print('\n--== ДОМАШНЕЕ ЗАДАНИЕ!!!! ==--')
    print('--== Тестирование класса MyStudent ==--')

    try:
        my_bad_student1 = mu5.MyStudent('вася', 'Петров', 'lessons.csv')
        print(my_bad_student1.full_name)
    except ValueError:
        print('Ошибка в параметрах. Имя или фамилия начинаются с маленькой буквы')

    try:
        my_bad_student2 = mu5.MyStudent('Петя', 'Васе4кин', 'lessons.csv')
        print(my_bad_student2.full_name)
    except ValueError:
        print('Ошибка в параметрах. В имени или фамилии содержатся цифры')

    my_student = mu5.MyStudent('Алекандр','Демьяненко','lessons.csv')
    print(my_student.full_name)
    print(my_student.__dict__)
    print(f'{my_student=}')
