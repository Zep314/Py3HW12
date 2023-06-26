"""
Класс - студента, для закрепления работы с ООП
"""

# Создайте класс студента.
# - Используя дескрипторы проверяйте ФИО на первую заглавную букву и
# наличие только букв.
# - Названия предметов должны загружаться из файла CSV при создании
# экземпляра. Другие предметы в экземпляре недопустимы.
# - Для каждого предмета можно хранить оценки (от 2 до 5) и результаты
# тестов (от 0 до 100).
# - Также экземпляр должен сообщать средний балл по тестам для каждого
# предмета и по оценкам всех предметов вместе взятых.
import csv


class FioRange:
    def __init__(self):
        pass

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def __delete__(self, instance):
        raise AttributeError(f'Свойство "{self.param_name}" нельзя удалять')

    def validate(self, value):
        if not isinstance(value, str):
            raise TypeError(f'Значение {value} должно быть строкой')
        if not value.istitle():
            raise ValueError('Строка должна начинаться с большой буквы')
        if any(ch.isdigit() for ch in value):
            raise ValueError('В строке не должно быть цифр')


class MyStudent:
    """
    Класс - студент, для закрепления навыков работы с ООП
    """
    first_name = FioRange()
    last_name = FioRange()
    courses = []

    def __init__(self, first_name, last_name, file_lessons='lessons.csv'):
        self.first_name = first_name
        self.last_name = last_name
        self.file_lessons = file_lessons
        if file_lessons:
            with open(file_lessons, 'r', encoding='UTF-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    self.courses.append({row['course']:[{'grades':[]}, {'tests':[]}]})

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __repr__(self):
        return f'{self.courses}'

