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
from random import randint


class MyFioRange:
    """
    Класс - дескриптор для контроля ввода имени и фамилии
    """

    def __init__(self):
        pass

    def __set_name__(self, owner, name):
        """
        Создаем защищенный параметр
        :param owner:
        :param name:
        :return:
        """
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        """
        Читаем защищенный атрибут
        :param instance:
        :param owner:
        :return:
        """
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        """
        Изменяем с проверкой защищенный атрибут
        :param instance:
        :param value:
        :return:
        """
        self.validate(value)
        setattr(instance, self.param_name, value)

    def __delete__(self, instance):
        """
        Запрет на удаление атрибута
        :param instance:
        :return:
        """
        raise AttributeError(f'Свойство "{self.param_name}" нельзя удалять')

    @staticmethod
    def validate(value):
        """
        Проверка при вводе атрибута. Для всех экземпляров класса метод одинаковый, поэтому он @staticmethod
        :param value:
        :return:
        """
        if not isinstance(value, str):
            raise TypeError(f'Значение {value} должно быть строкой')
        if not value.istitle():
            raise ValueError('Строка должна начинаться с большой буквы')
        if any(ch.isdigit() for ch in value):
            raise ValueError('В строке не должно быть цифр')


class MyGrade:
    """
    Класс для хранения значения оценки или результатов теста по предмету
    реализована проверка вводимого диапазона
    """
    _value: int

    def __init__(self, value: int, min_value: int = None, max_value: int = None):
        self._min_value = min_value
        self._max_value = max_value
        if self._validate(value):
            self._value = value

    def __call__(self, *args, **kwargs):
        return self._value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if self._validate(value):
            self._value = value

    def _validate(self, value):
        if self._min_value and value < self._min_value:
            raise ValueError('Значение меньше минимального')
        if self._max_value and value > self._max_value:
            raise ValueError('Значение больше максимального')
        return True

    def __str__(self):
        return str(self._value)

    def __repr__(self):
        return str(self._value)


class MyStudent:
    """
    Класс - студент, для закрепления навыков работы с ООП
    """
    first_name = MyFioRange()
    last_name = MyFioRange()
    courses = {}
    MAX_LEN_GRADES_IN_COURSE = 20  # Максимальное количество оценок по предмету

    def __init__(self, first_name, last_name, file_lessons='lessons.csv'):
        self.first_name = first_name
        self.last_name = last_name
        self.file_lessons = file_lessons
        if file_lessons:  # Читаем список предметов из CSV файла
            with open(file_lessons, 'r', encoding='UTF-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    self.courses[row['course']] = {'grades': [], 'tests': []}

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __repr__(self):
        return f'{self.full_name} {self.courses}'

    def gen_fake_data(self):
        """
        Генерируем фейковые данные по всем предметам (оценки + результаты тестов)
        :return:
        """
        for k, v in self.courses.items():
            self.courses[k]['grades'] = \
                [MyGrade(randint(2, 5), 2, 5) for _ in range(randint(1, self.MAX_LEN_GRADES_IN_COURSE))]
            self.courses[k]['tests'] = \
                [MyGrade(randint(0, 100), 0, 100) for _ in range(randint(1, self.MAX_LEN_GRADES_IN_COURSE))]

    def get_avg_course(self, name_course, variant='grades'):
        """
        Возвращаем средний балл по оценкам или по тестам по определенному курсу
        :param name_course:
        :param variant:
        :return:
        """
        return sum(map(lambda x: x(), self.courses[name_course][variant])) / len(self.courses[name_course][variant])

    def get_courses(self):
        """
        Возвращаем список курсов (предметов), которые у нас есть
        :return:
        """
        return list(self.courses.keys())

    def get_avg_all(self, variant='grades'):
        """
        Возвращаем средний балл по оценкам или тестам по всем предметом, вместе взятым
        :param variant:
        :return:
        """
        return sum([self.get_avg_course(course, variant) for course in self.get_courses()]) \
            / len(self.courses)
