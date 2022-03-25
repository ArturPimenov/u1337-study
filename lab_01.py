### Лабораторная работа № 1: Выражения и управляющие инструкции

# Вопрос 1. 
def _q_01():
    """
    Часть 1
    >>> 3                                                       # doctest: +SKIP
    3
    >>> 2 + 3                                                   # doctest: +SKIP
    5
    >>> -16 - -16                                               # doctest: +SKIP
    0
    >>> 3 * 4 + 1                                               # doctest: +SKIP
    13
    >>> 3 * (4 + 1)                                             # doctest: +SKIP
    15
    >>> 2 ** 3                                                  # doctest: +SKIP
    8
    
    Часть 2
    >>> x = 4                                                   # doctest: +SKIP
    >>> 3 + x                                                   # doctest: +SKIP
    7
    >>> x + y                                                   # doctest: +SKIP
    Traceback (most recent call last):
        ...
    NameError: name 'y' is not defined
    >>> x, y = 1, 2                                             # doctest: +SKIP
    >>> 3 + x                                                   # doctest: +SKIP
    4
    >>> x + y                                                   # doctest: +SKIP
    3

    Часть 3
    >>> from operator import mul, add                           # doctest: +SKIP
    >>> mul(3, 4)                                               # doctest: +SKIP
    12
    >>> mul(3, add(4, 1))                                       # doctest: +SKIP
    15
    >>> pow(2, 3)                                               # doctest: +SKIP
    8
    >>> pow(pow(2, 3), abs(-2))                                 # doctest: +SKIP
    64
    """
    return 0

# Вопрос 2.
def _q_02():
    """
    Часть 1
    >>> def xk(c, d):                                           # doctest: +SKIP
    ...     if c == 4:
    ...         return 6
    ...     elif d >= 4:
    ...         return 6 + 7 + c
    ...     else:
    ...         return 25
    >>> xk(10, 10)                                              # doctest: +SKIP 
    23
    >>> xk(10, 6)                                               # doctest: +SKIP
    23
    >>> xk(4, 6)                                                # doctest: +SKIP
    6
    >>> xk(0, 0)                                                # doctest: +SKIP
    25

    Часть 2
    >>> def how_big(x):                                         # doctest: +SKIP
    ...     if x > 10:
    ...         print('очень много')
    ...     elif x > 5:
    ...         return 'много'
    ...     elif x > 0:
    ...         print('мало')
    ...     else:
    ...         print("нисколько")
    >>> how_big(7)                                              # doctest: +SKIP
    'много'
    >>> how_big(12)                                             # doctest: +SKIP
    очень много
    >>> how_big(1)                                              # doctest: +SKIP
    мало
    >>> how_big(-1)                                             # doctest: +SKIP
    нисколько

    Часть 3
    >>> n = 3                                                   # doctest: +SKIP
    >>> while n >= 0:                                           # doctest: +SKIP
    ...     n -= 1
    ...     print(n)
    2
    1
    0
    -1

    Часть 4
    >>> positive = 27                                           # doctest: +SKIP
    >>> while positive:                                         # doctest: +SKIP
    ...    print("positive?")
    ...    positive -= 3
    positive?
    positive?
    positive?
    positive?
    positive?
    positive?
    positive?
    positive?
    positive?

    Часть 5
    >>> positive = -9                                           # doctest: +SKIP
    >>> negative = -12                                          # doctest: +SKIP
    >>> while negative:                                         # doctest: +SKIP
    ...    if positive:
    ...        print(negative)
    ...    positive += 3
    ...    negative += 3
    -12
    -9
    -6
    """
    return 0

# Вопрос 3.
def _q_03():
    """
    Часть 1
    >>> True and 13                                             # doctest: +SKIP
    13
    >>> False or 0                                              # doctest: +SKIP
    0
    >>> not 10                                                  # doctest: +SKIP
    False
    >>> not None                                                # doctest: +SKIP
    True

    Часть 2
    >>> True and 1 / 0 and False                                # doctest: +SKIP
    Traceback (most recent call last):
    ...
    ZeroDivisionError: division by zero
    >>> True or 1 / 0 or False                                  # doctest: +SKIP
    True
    >>> True and 0                                              # doctest: +SKIP
    0
    >>> False or 1                                              # doctest: +SKIP
    1
    >>> 1 and 3 and 6 and 10 and 15                             # doctest: +SKIP
    15
    >>> 0 or False or 2 or 1 / 0                                # doctest: +SKIP
    2

    Часть 3
    >>> not 0                                                   # doctest: +SKIP
    True
    >>> (1 + 1) and 1                                           # doctest: +SKIP
    1
    >>> 1/0 or True                                             # doctest: +SKIP
    Traceback (most recent call last):
    ...
    ZeroDivisionError: division by zero
    >>> (True or False) and False                               # doctest: +SKIP
    False
    """
    return 0

# Вопрос 4.
def both_positive(x, y):
    """
    Возвращает True, если x и y — положительные.

    >>> both_positive(-1, 1)
    False
    >>> both_positive(1, 1)
    True
    """
    return x > 0 and y > 0                      # эту строчку можно и нужно изменить

# Вопрос 5.
def sum_digits(n):
    """
    Суммирует все цифры n.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> x = sum_digits(123) # проверяет применение return, а не print
    >>> x
    6
    """
    if n > 0:
        sum_of_number = 0    
        while n:
            sum_of_number += n % 10
            n //= 10
        return sum_of_number            

# Вопрос 6.
def _q_06():
    """
    Часть 1
    >>> def ab(c, d):                                           # doctest: +SKIP
    ...     if c > 5:
    ...         print(c)
    ...     elif c > 7:
    ...         print(d)
    ...     print('foo')
    >>> ab(10, 20)                                              # doctest: +SKIP
    10
    foo

    Часть 2
    >>> def bake(cake, make):                                   # doctest: +SKIP
    ...     if cake == 0:
    ...         cake = cake + 1
    ...         print(cake)
    ...     if cake == 1:
    ...         print(make)
    ...     else:
    ...         return cake
    ...     return make
    >>> bake(0, 29)                                             # doctest: +SKIP
    1
    29
    29
    >>> bake(1, "беспонтовый пирожок")                          # doctest: +SKIP
    беспонтовый пирожок
    'беспонтовый пирожок'
    """
    return 0

# Вопрос 7.
def factors(n):
    """
    Выводит все числа, которые делят `n` без остатка.

    >>> factors(20)
    20
    10
    5
    4
    2
    1
    """
    i = n
    while i:
        if not n%i:
            print(i)
        i -= 1             

# Вопрос 8.
def falling(n, k):
    """
    Вычисляет нисходящий факториал n глубины k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 0)
    1
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    """
    assert(n >= 0 and k >= 0 and k <= n)
    muul = 1
    while k:
        muul *= n
        n -= 1
        k -= 1
    return muul                    

# Вопрос 9.
def double_eights(n):
    """
    Возвращает True, если в n содержится комбинация цифр 88.
    
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    while n:
        lit_first = n % 10
        n //= 10
        lit_second = n % 10
        if lit_first == 8 and lit_first == lit_second:
            return True
    return False        


# Ниже этого места трогать ничего не нужно.

if __name__ == '__main__':
    import doctest, sys
    finder = doctest.DocTestFinder()
    runner = doctest.DocTestRunner(doctest.OutputChecker(), optionflags=doctest.FAIL_FAST)
    doctest.OutputChecker.output_difference = lambda a, b, c, d: ""
    m = sys.modules.get('__main__')
    for test in finder.find(m, m.__name__):
        if test.name.split('.')[1][:2] != '_q': continue
        for example in test.examples: example.options[doctest.SKIP] = False
        if  runner.run(test).failed != 0: break