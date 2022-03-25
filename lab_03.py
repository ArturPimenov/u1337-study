### Лабораторная работа № 3: Рекурсия

# Вопрос 1
def sum(n):
    """Вычисляет сумму всех положительных целых от 1 до n включительно.
    Считай, что n >= 1.

    >>> sum(1)
    1
    >>> sum(5)  # 1 + 2 + 3 + 4 + 5
    15
    """
    
    return 1 if n ==1 else n + sum(n-1)    

# Подвопрос 2.1
def sum_every_other_number(n):
    """Возвращает частичную сумму натуральных чисел до n включительно, в которую числа входят через одно.

    >>> sum_every_other_number(8)
    20
    >>> sum_every_other_number(9)
    25
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1    
    else:
        return n + sum_every_other_number(n - 2)
    
# Подвопрос 2.2
def fibonacci(n):
    """Возвращает n-ое число Фибоначчи.

    >>> fibonacci(11)
    89
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Подвопрос 2.3
def even_digits(n):
    """Возвращает долю чётных цифр в числе n.

    >>> even_digits(23479837) # 3 / 8
    0.375
    """
    counter = 0
    if n == 0:
        return 0
    elif len(str(n)) == 1:
        if n%2 == 0:
            return 1
        else:
            return 0        
    else:   
        if n % 2 == 0:
            return even_digits(n//10) + (1 - even_digits(n//10))/len(str(n))       
        else:
            return even_digits(n//10) - even_digits(n//10) * (1/(len(str(n)))) 

# Вопрос 3
def hailstone(n):
    """Выводит последовательность чисел-градин. Возвращает кол-во элементов.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    print(n)
    if n==1:
        return 1
    else:
        if n%2 == 0:
            return 1 + hailstone(n//2)
        else:
            return 1 + hailstone(3*n + 1)        



# Вопрос 4
def gcd(a, b):
    """Возвращает НОД для a и b. Нужно использовать рекурсию.

    >>> gcd(34, 19)
    1
    >>> gcd(39, 91)
    13
    >>> gcd(20, 30)
    10
    >>> gcd(40, 40)
    40
    """
    if a < b:
        a, b = b, a

    if a%b == 0:
        return b    

    else:
        return gcd(b, a%b)

# Вопрос 5
def paths(m, n):
    """Вычисляет количество путей из одного угла в другой на поле M на N.

    >>> paths(2, 2)
    2
    >>> paths(5, 7)
    210
    >>> paths(117, 1)
    1
    >>> paths(1, 157)
    1
    """
    if m == 1 or n == 1:
        return 1          
    else:
        return paths(m-1,n) + paths(m, n-1)

# Вопрос 6
from operator import abs
def print_move(origin, destination):
    """Печатает информацию о перемещении диска."""
    print("Перемещение диска со стержня", origin, "на стержень", destination)

def move_stack(n, start, end):
    """Выводит последовательность перемещений n дисков с начального стержня
    на конечный в соответствии с правилами Ханойских башен .

    Аргументы:
        n (int): количество дисков
        start (int): начальный стержень, то есть 1, 2 или 3 
        end (int): конечный стержень, то есть 1, 2 или 3

    В задаче в точности три стержня, начальный и конечный должны различаться. Предполагается,
    что на начальном стержне находится не менее n дисков увеличивающегося размера, а конечный
    либо пуст, либо верхний диск больше любого другого из n дисков на первом стержне.

    >>> move_stack(1, 1, 3)
    Перемещение диска со стержня 1 на стержень 3
    >>> move_stack(2, 1, 3)
    Перемещение диска со стержня 1 на стержень 2
    Перемещение диска со стержня 1 на стержень 3
    Перемещение диска со стержня 2 на стержень 3
    >>> move_stack(3, 1, 3)
    Перемещение диска со стержня 1 на стержень 3
    Перемещение диска со стержня 1 на стержень 2
    Перемещение диска со стержня 3 на стержень 2
    Перемещение диска со стержня 1 на стержень 3
    Перемещение диска со стержня 2 на стержень 1
    Перемещение диска со стержня 2 на стержень 3
    Перемещение диска со стержня 1 на стержень 3
    """
    assert 1 <= start <= 3 and 1 <= end <= 3 and start != end, "Плохие аргументы"
    if (start == 1 or start == 3) and (end == 1 or end == 3):
        independened_two = 2
    elif (start == 1 and end == 2) or (start == 2 and end == 1):
        independened_two = 3
    else:
        independened_two = 1             


    if n==1:
        print_move(start, end)
    elif n==2:
        print_move(start, independened_two)
        print_move(start, end)
        print_move(independened_two, end)
    elif n==3:
        print_move(start, end)
        print_move(start, independened_two)
        print_move(end, independened_two)
        print_move(start, end)
        print_move(independened_two, start)
        print_move(independened_two, end)
        print_move(start, end)    
    else:
        move_stack(n-1, start, independened_two)
        print_move(start, end)
        move_stack(n-1, independened_two, end)       




