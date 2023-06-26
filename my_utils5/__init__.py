"""
Init-файл для пакета с моими классами для 11-ого домашнего задания
"""
from my_utils5.my_math import MyFactorial
from my_utils5.my_math import MyRangeFactorial
from my_utils5.my_geometry import MyRectangle
from my_utils5.my_student import MyStudent
from my_utils5.my_student import MyGrade

# Эти классы будем "экспортировать" для внешней работы
__all__ = ['MyFactorial', 'MyRangeFactorial', 'MyRectangle', 'MyStudent', 'MyGrade']
