# Погружение в Python (семинары)
## Урок 12. ООП. Финал

### Задание 1
Создайте класс студента.
- Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
- Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы.
- Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
- Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых. 


### Решение
**Задание 1**

Решение представлено в файле *my_utils5/my_student.py*. 
Реализован класс MyStudent в соответствие с заданием.

Проверка работы класса предоставлена в файле *main.py*


### Результат работы:
    /home/user/Work/Python/dz3/Py3HW12/venv/bin/python /home/user/Work/Python/dz3/Py3HW12/main.py 
    --== Тестирование класса MyFactorial ==--
    Вычисление факториала:
    815915283247897734345611269596115894272000000000
    Просмотр "кэша" вычисленных значений факториала:
    {1: 1, 2: 2, 3: 6, 4: 24, 5: 120, 6: 720, 7: 5040, 8: 40320, 9: 362880, 10: 3628800, 11: 39916800, 12: 479001600, 13: 6227020800, 14: 87178291200, 15: 1307674368000, 16: 20922789888000, 17: 355687428096000, 18: 6402373705728000, 19: 121645100408832000, 20: 2432902008176640000, 21: 51090942171709440000, 22: 1124000727777607680000, 23: 25852016738884976640000, 24: 620448401733239439360000, 25: 15511210043330985984000000, 26: 403291461126605635584000000, 27: 10888869450418352160768000000, 28: 304888344611713860501504000000, 29: 8841761993739701954543616000000, 30: 265252859812191058636308480000000, 31: 8222838654177922817725562880000000, 32: 263130836933693530167218012160000000, 33: 8683317618811886495518194401280000000, 34: 295232799039604140847618609643520000000, 35: 10333147966386144929666651337523200000000, 36: 371993326789901217467999448150835200000000, 37: 13763753091226345046315979581580902400000000, 38: 523022617466601111760007224100074291200000000, 39: 20397882081197443358640281739902897356800000000, 40: 815915283247897734345611269596115894272000000000}
    
    --== Тестирование класса MyFactorial ==--
    2
    24
    720
    40320
    
    --== Тестирование класса MyRectangle ==--
    Прямоугольник 5 x 4
    Ширина прямоугольника: 5
    Высота прямоугольника: 4
    Прямоугольник 7 x 7
    Ошибка установки параметров!
    Проверка вывода словаря __dict__ c установленным кортежем __slots__:
    Кортеж __slots__ установлен, __dict__ - недоступен
    
    --== ДОМАШНЕЕ ЗАДАНИЕ!!!! ==--
    --== Тестирование класса MyStudent ==--
    Ошибка в параметрах. Имя или фамилия начинаются с маленькой буквы
    Ошибка в параметрах. В имени или фамилии содержатся цифры
    Алекандр Демьяненко
    {'_first_name': 'Алекандр', '_last_name': 'Демьяненко', 'file_lessons': 'lessons.csv'}
    my_student=Алекандр Демьяненко {'Физика': {'grades': [5, 2, 4, 5, 2, 5, 3, 3, 5], 'tests': [12, 85, 31, 72, 69, 91]}, 'Химия': {'grades': [2, 2, 5, 3, 2], 'tests': [98, 58, 21, 25, 56, 28, 96, 92, 69, 79, 68, 60]}, 'Программирование': {'grades': [5, 2, 2, 4], 'tests': [100, 29, 9, 1]}, 'Математика': {'grades': [4, 4, 5, 2, 2, 2, 3, 3, 4, 5, 2], 'tests': [0, 98, 66, 82, 34, 71, 31, 68, 53]}, 'Физкультура': {'grades': [3, 2, 2, 5, 5, 5], 'tests': [72, 53, 84, 94, 69, 16, 75, 91]}}
    
    Средние баллы по оценкам и тестам по предметам:
    Предмет: Физика, Средний балл по оценкам: 3.78, Средний балл по тестам: 60.00
    Предмет: Химия, Средний балл по оценкам: 2.80, Средний балл по тестам: 62.50
    Предмет: Программирование, Средний балл по оценкам: 3.25, Средний балл по тестам: 34.75
    Предмет: Математика, Средний балл по оценкам: 3.27, Средний балл по тестам: 55.89
    Предмет: Физкультура, Средний балл по оценкам: 3.67, Средний балл по тестам: 69.25
    
    Средний балл по оценкам и тестам по всем предметам вместе: По оценкам: 3.35, По тестам: 56.48
    
    Process finished with exit code 0
