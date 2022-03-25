""" Домашнее задание № 2 """

# Необходимые определения
from operator import add, mul, sub

square = lambda x: x * x
identity = lambda x: x
triple = lambda x: 3 * x
increment = lambda x: x + 1

# Вопрос 1.

def product(n, term):
    """
    Возвращает произведение первых n членов (terms) последовательности.
    
    Аргументы:
        n (int): количество перемножаемых элементов последовательности.
        term (func): функция одного аргумента.

    >>> product(3, identity)  # 1 * 2 * 3
    6
    >>> product(5, identity)  # 1 * 2 * 3 * 4 * 5
    120
    >>> product(3, square)    # 1^2 * 2^2 * 3^2
    36
    >>> product(5, square)    # 1^2 * 2^2 * 3^2 * 4^2 * 5^2
    14400
    >>> product(3, increment) # (1+1) * (2+1) * (3+1)
    24
    >>> product(3, triple)    # 1*3 * 2*3 * 3*3
    162
    """
    assert(n >= 0)
    k = 1
    total = 1;
    while k <= n:
        total *= term(k)
        k += 1          
    return total

def factorial(n):
    """
    Возвращает факториал n при n >= 0, используя функцию product.

    >>> factorial(4)  # 4 * 3 * 2 * 1
    24
    >>> factorial(6)  # 6 * 5 * 4 * 3 * 2 * 1
    720
    """
    return product(n, identity)

# Вопрос 2.

def accumulate(combiner, base, n, term):
    """
    Возвращает результат объединения (combining) первых n членов последовательности.

    >>> accumulate(add, 0, 5, identity)  # 0 + 1 + 2 + 3 + 4 + 5
    15
    >>> accumulate(add, 11, 5, identity) # 11 + 1 + 2 + 3 + 4 + 5
    26
    >>> accumulate(add, 11, 0, identity) # 11
    11
    >>> accumulate(add, 11, 3, square)   # 11 + 1^2 + 2^2 + 3^2
    25
    >>> accumulate(mul, 2, 3, square)    # 2 * 1^2 * 2^2 * 3^2
    72
    >>> accumulate(lambda x, y: x + y + 1, 2, 3, square)
    19
    """
    total, i = base, 1 
    while i <= n:
        total = combiner(total, term(i))
        i += 1
    return total    

def summation_using_accumulate(n, term):
    """
    Возвращает сумму term(1) + ... + term(n). Реализация с использованием accumulate.

    >>> summation_using_accumulate(5, square)
    55
    >>> summation_using_accumulate(5, triple)
    45
    """
    return accumulate(add, 0, n, term)

def product_using_accumulate(n, term):
    """
    Возвращает произведение term(1) * ... * term(n). Реализация с использованием accumulate.

    >>> product_using_accumulate(3, lambda x: (x+1)*(x+5)*x)
    48384
    >>> product_using_accumulate(4, square)
    576
    >>> product_using_accumulate(6, triple)
    524880
    """
    return accumulate(mul, 1, n, term)

# Вопрос 3.

def double(f):
    """
    Возвращает функцию, применяющую f дважды.

    Аргументы:
        f (func): функция одного аргумента.

    >>> double(square)(2)
    16
    """
    def g(n):
        return f(f(n))
    return g

# Вопрос 4.

def make_repeater(f, n):
    """Возвращает функцию, применяющую f n раз.

    Аргументы:
        f (func): функция одного аргумента.
        n (int): количество применений функции f.
        
    >>> add_three = make_repeater(increment, 3)
    >>> add_three(5)
    8
    >>> make_repeater(triple, 5)(1) # 3 * 3 * 3 * 3 * 3 * 1
    243
    >>> make_repeater(square, 2)(5) # square(square(5))
    625
    >>> make_repeater(square, 4)(5) # square(square(square(square(5))))
    152587890625
    >>> make_repeater(square, 0)(5) # Да, применение функции ноль раз тоже имеет смысл! 
    5
    """
    def fff(x):
        k = 0
        while k < n:
            x = f(x)
            k += 1
        return x
    return fff

def compose1(f, g):
    """Возвращает функцию h такую, что h(x) = f(g(x))."""
    def h(x):
        return f(g(x))
    return h

# Вопрос 5.

def zero(f):
    return lambda x: x

def successor(n):
    return lambda f: lambda x: f(n(f)(x))

def one(f):
    """Число Чёрча 1."""
    return lambda x: f(x)

def two(f):
    """Число Чёрча 2."""
    return lambda x: f(f(x))

three = successor(two)
four = successor(three)

def church_to_int(n):
    """Преобразует число Чёрча n в целое число Python.

    >>> church_to_int(zero)
    0
    >>> church_to_int(one)
    1
    >>> church_to_int(two)
    2
    >>> church_to_int(three)
    3
    """
    return n(increment)(0)

def add_church(m, n):
    """Возвращает число Чёрча m + n для чисел Чёрча m и n.

    >>> church_to_int(add_church(two, three))
    5
    """
    number, k, summ = zero, 0, church_to_int(m) + church_to_int(n)
    while k < summ:
        number = successor(number)
        k += 1 
    return number

def mul_church(m, n):
    """Возвращает число Чёрча m * n для чисел Чёрча m и n.

    >>> four = successor(three)
    >>> church_to_int(mul_church(two, three))
    6
    >>> church_to_int(mul_church(three, four))
    12
    """
    number, k, summ = zero, 0, church_to_int(m) * church_to_int(n)
    while k < summ:
        number = successor(number)
        k += 1 
    return number

def pow_church(m, n):
    """Возвращает число Чёрча m ** n для чисел Чёрча m и n.

    >>> church_to_int(pow_church(two, three))
    8
    >>> church_to_int(pow_church(three, two))
    9
    """
    number, k, summ = zero, 0, church_to_int(m) ** church_to_int(n)
    while k < summ:
        number = successor(number)
        k += 1 
    return number