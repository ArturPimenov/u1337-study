### Лабораторная работа № 2: Лямбда-выражения и функции высшего порядка"""

# Вопрос 1. 
def _q_01():
    """
    Часть 1
    >>> lambda x: x                                             # doctest: +SKIP +ELLIPSIS
    <function ...
    >>> a = lambda x: x                                         # doctest: +SKIP
    >>> a(5)                                                    # doctest: +SKIP
    5
    >>> b = lambda: 3                                           # doctest: +SKIP
    >>> b()                                                     # doctest: +SKIP
    3
    >>> c = lambda x: lambda: print('123')                      # doctest: +SKIP
    >>> c(88)                                                   # doctest: +SKIP +ELLIPSIS  
    <function ...
    >>> c(88)()                                                 # doctest: +SKIP
    123
    >>> d = lambda f: f(4)                                      # doctest: +SKIP
    >>> def square(x):                                          # doctest: +SKIP
    ...     return x * x
    >>> d(square)                                               # doctest: +SKIP
    16

    Часть 2
    >>> z = 3                                                   # doctest: +SKIP
    >>> e = lambda x: lambda y: lambda: x + y + z               # doctest: +SKIP
    >>> e(0)(1)()                                               # doctest: +SKIP
    4
    >>> f = lambda z: x + z                                     # doctest: +SKIP
    >>> f(3)                                                    # doctest: +SKIP
    Traceback (most recent call last):
      File "C:\Python39\lib\doctest.py", line 1336, in __run
        exec(compile(example.source, filename, "single",
      File "<doctest __main__._q_01[15]>", line 1, in <module>
        f(3)                                                    # doctest: +SKIP
      File "<doctest __main__._q_01[14]>", line 1, in <lambda>
        f = lambda z: x + z                                     # doctest: +SKIP
    NameError: name 'x' is not defined
   

    Часть 3
    >>> higher_order_lambda = lambda f: lambda x: f(x)          # doctest: +SKIP
    >>> g = lambda x: x * x                                     # doctest: +SKIP
    >>> higher_order_lambda(2)(g)                               # doctest: +SKIP
    Traceback (most recent call last):
    ...
    TypeError: 'int' object is not callable
    >>> higher_order_lambda(g)(2)                               # doctest: +SKIP
    4
    >>> call_thrice = lambda f: lambda x: f(f(f(x)))            # doctest: +SKIP
    >>> call_thrice(lambda y: y + 1)(0)                         # doctest: +SKIP
    3
    >>> print_lambda = lambda z: print(z)                       # doctest: +SKIP
    >>> print_lambda                                            # doctest: +SKIP +ELLIPSIS 
    <function ...
    >>> one_thousand = print_lambda(1000)                       # doctest: +SKIP
    1000
    >>> one_thousand                                            # doctest: +SKIP
    """
    return 0

# Вопрос 2. 
def _q_02():
    """
    Часть 1
    >>> def even(f):                                            # doctest: +SKIP
    ...     def odd(x):
    ...         if x < 0:
    ...             return f(-x)
    ...         return f(x)
    ...     return odd
    >>> janet = lambda x: x                                     # doctest: +SKIP
    >>> brad = even(janet)                                      # doctest: +SKIP
    >>> brad                                                    # doctest: +SKIP  +ELLIPSIS 
    <function ...
    >>> brad(61)                                                # doctest: +SKIP
    61
    >>> brad(-4)                                                # doctest: +SKIP
    4

    Часть 2
    >>> def cake():                                             # doctest: +SKIP
    ...    print('гадость')
    ...    def pie():
    ...        print('сладость')
    ...        return 'торт'
    ...    return pie
    >>> chocolate = cake()                                      # doctest: +SKIP
    гадость
    >>> chocolate                                               # doctest: +SKIP +ELLIPSIS 
    <function ...
    >>> chocolate()                                             # doctest: +SKIP
    сладость
    'торт'
    >>> more_chocolate, more_cake = chocolate(), cake           # doctest: +SKIP
    сладость
    >>> more_chocolate                                          # doctest: +SKIP
    'торт'
    >>> def snake(x, y):                                        # doctest: +SKIP
    ...    if cake == more_cake:
    ...        return lambda: x + y
    ...    else:
    ...        return x + y
    >>> snake(10, 20)                                           # doctest: +SKIP +ELLIPSIS 
    <function ...
    >>> snake(10, 20)()                                         # doctest: +SKIP
    30
    >>> cake = 'торт'                                           # doctest: +SKIP
    >>> snake(10, 20)                                           # doctest: +SKIP
    30
    """
    return 0

# Вопрос 3. 
def lambda_curry2(func):
    """
    Возвращает каррированную версию функции func от двух аргументов.
    >>> from operator import add
    >>> x = lambda_curry2(add)
    >>> y = x(3)
    >>> y(5)
    8
    """
    return lambda x: lambda y: func(x,y)

# Вопрос 5.
def compose1(f, g):
    """
    Возвращает функцию h такую, что h(x) = f(g(x)).

    >>> add_one = lambda x: x + 1        # прибавляет единицу к x
    >>> square = lambda x: x**2
    >>> a1 = compose1(square, add_one)   # (x + 1)^2
    >>> a1(4)
    25
    >>> mul_three = lambda x: x * 3      # умножает 3 на x
    >>> a2 = compose1(mul_three, a1)     # ((x + 1)^2) * 3
    >>> a2(4)
    75
    >>> a2(5)
    108
    """
    return lambda x: f(g(x))

def composite_identity(f, g):
    """
    Возвращает функцию одного аргумента, которая возвращает True,
    если f(g(x)) равно g(f(x)). Можешь считать, что результат g(x)
    может быть аргументом f и наоборот.

    >>> add_one = lambda x: x + 1        # прибавляет единицу к x
    >>> square = lambda x: x**2
    >>> b1 = composite_identity(square, add_one)  
    >>> b1(0)                            # (0 + 1)^2 == 0^2 + 1
    True
    >>> b1(4)                            # (4 + 1)^2 != 4^2 + 1
    False
    """
    return lambda x: True if compose1(f,g)(x) == compose1(g,f)(x) else False

# Вопрос 6.
def count_factors(n):
    """Возвращает количество положительных целых делителей n."""
    i, count = 1, 0
    while i <= n:
        if n % i == 0:
            count += 1
        i += 1
    return count

def count_primes(n):
    """Возвращает число простых чисел, встречающихся до и включая n."""
    i, count = 1, 0
    while i <= n:
        if is_prime(i):
            count += 1
        i += 1
    return count

def is_prime(n):
    return count_factors(n) == 2 # только множители 1 и n

def count_cond(condition):
    """
    Возвращает функцию одного аргумента N, которая подсчитывает все числа от 1 до N,
    для которых выполняется предикат condition — функция двух аргументов.

    >>> count_factors = count_cond(lambda n, i: n % i == 0)
    >>> count_factors(2)   # 1, 2
    2
    >>> count_factors(4)   # 1, 2, 4
    3
    >>> count_factors(12)  # 1, 2, 3, 4, 6, 12
    6

    >>> is_prime = lambda n, i: count_factors(i) == 2
    >>> count_primes = count_cond(is_prime)
    >>> count_primes(2)    # 2
    1
    >>> count_primes(3)    # 2, 3
    2
    >>> count_primes(4)    # 2, 3
    2
    >>> count_primes(5)    # 2, 3, 5
    3
    >>> count_primes(20)   # 2, 3, 5, 7, 11, 13, 17, 19
    8
    """
    def h(n):
        i, count = 1, 0
        while i <= n:
            if condition(n, i):
                count += 1
            i += 1
        return count
    return h

# Вопрос 7.
def cycle(f1, f2, f3):
    """Возвращает функцию, которая является функцией высшего порядка.

    >>> def add1(x):
    ...     return x + 1
    >>> def times2(x):
    ...     return x * 2
    >>> def add3(x):
    ...     return x + 3
    >>> my_cycle = cycle(add1, times2, add3)
    >>> identity = my_cycle(0)
    >>> identity(5)
    5
    >>> add_one_then_double = my_cycle(2)
    >>> add_one_then_double(1)
    4
    >>> do_all_functions = my_cycle(3)
    >>> do_all_functions(2)
    9
    >>> do_more_than_a_cycle = my_cycle(4)
    >>> do_more_than_a_cycle(2)
    10
    >>> do_two_cycles = my_cycle(6)
    >>> do_two_cycles(1)
    19
    """
    def g(n):
        def p(x):
            i, t1, t2, t3 = 1, f1, f2, f3
            while i <= n:
                x = t1(x)
                t1, t2, t3 = t2, t3, t1
                i += 1
            return x
        return p            
    return g
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