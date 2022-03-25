""" Домашнее задание № 1 """

# Вопрос 1.

from operator import add, sub
def a_plus_abs_b(a, b):
    """Возвращает a+abs(b), но не использует abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    """
    if b < 0:
        op = sub
    else:
        op = add
    return op(a, b)

# Вопрос 2.

def two_of_three(a, b, c):
    """Возвращает x*x + y*y, где x и y — два наибольших значения среди a, b, c.

    >>> two_of_three(1, 2, 3)
    13
    >>> two_of_three(5, 3, 1)
    34
    >>> two_of_three(10, 2, 8)
    164
    >>> two_of_three(5, 5, 5)
    50
    """
    return max(a,b)**2 + max(min(a,b), c)**2

# Вопрос 3.

def if_function(condition, true_result, false_result):
    """Возвращает true_result, если условие condition истинно и false_result в противном случае.

    >>> if_function(True, 2, 3)
    2
    >>> if_function(False, 2, 3)
    3
    >>> if_function(3==2, 3+2, 3-2)
    1
    >>> if_function(3>2, 3+2, 3-2)
    5
    """
    if condition:
        return true_result
    else:
        return false_result

def with_if_statement():
    """
    >>> result = with_if_statement()
    2
    >>> print(result)
    None
    """
    if c():
        return t()
    else:
        return f()

def with_if_function():
    """
    >>> result = with_if_function()
    1
    2
    >>> print(result)
    None
    """
    return if_function(c(), t(), f())

def c():
    return 0

def t():
    print('1')

def f():
    print('2')

# Вопрос 4.

def hailstone(n):
    """Выводит сиракузскую последовательность (числа-градины), начинающуюся с n, и возвращает её длину.

    >>> a = hailstone(10)  # Семь элементов: 10, 5, 16, 8, 4, 2, 1
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
    i = 1
    while n:
        print(n)
        if not n%2 and n == 1:
            n //= 2     
        else:
            n = n*3 + 1
        i += 1  
    return i  

# Вопрос 5.
"""Строка кода, которая выводит сама себя на экран"""
challenge_question_program = """
c_q_p = "print('c_q_p' + ' = ' + repr(c_q_p) + '; ' + c_q_p)"; print('c_q_p' + ' = ' + repr(c_q_p) + '; ' + c_q_p)
"""