### HW_04: Абстрактные типы данных

# Вопрос 1.
def interval(a, b):
    """Создает интервал от a до b."""
    return [a, b]

def lower_bound(x):
    """Возвращает нижнюю границу интервала x."""
    return x[0]

def upper_bound(x):
    """Возвращает верхнюю границу интервала x."""
    return x[1]

def str_interval(x):
    """Возвращает строковое представление интервала x.

    >>> str_interval(interval(-1, 2))
    'от -1 до 2'
    """
    return f'от {lower_bound(x)} до {upper_bound(x)}'

def add_interval(x, y):
    """Возвращает интервал всевозможных сумм значений из x и y.

    >>> str_interval(add_interval(interval(-1, 2), interval(4, 8)))
    'от 3 до 10'
    """
    lower = lower_bound(x) + lower_bound(y)
    upper = upper_bound(x) + upper_bound(y)
    return interval(lower, upper)

def mul_interval(x, y):
    """Возвращает интервал всевозможных произведений значений из x и y.

    >>> str_interval(mul_interval(interval(-1, 2), interval(4, 8)))
    'от -8 до 16'
    """
    p1 = lower_bound(x) * lower_bound(y)
    p2 = lower_bound(x) * upper_bound(y)
    p3 = upper_bound(x) * lower_bound(y)
    p4 = upper_bound(x) * upper_bound(y)
    return interval(min(p1, p2, p3, p4), max(p1, p2, p3, p4))

# Вопрос 2.
def div_interval(x, y):
    """Возвращает интервал, содержащий частные любых значений из x на 
    любые значения из y.

    Деление реализовано как умножение x на величину, обратную к y.

    >>> str_interval(div_interval(interval(-1, 2), interval(4, 8)))
    'от -0.25 до 0.5'
    """
    assert lower_bound(y) * upper_bound(y) > 0, 'Ошибка, интервал пересекает ноль'
    reciprocal_y = interval(1/upper_bound(y), 1/lower_bound(y))
    return mul_interval(x, reciprocal_y)

# Вопрос 3.
def sub_interval(x, y):
    """Возвращает интервал, содержащий разности любых значений из x с 
    любыми значениями из y.

    >>> str_interval(sub_interval(interval(-1, 2), interval(4, 8)))
    'от -9 до -2'
    """
    sub_y = interval(-upper_bound(y), -lower_bound(y))
    return add_interval(x, sub_y)

# Вопрос 4.
def par1(r1, r2):
    return div_interval(mul_interval(r1, r2), add_interval(r1, r2))

def par2(r1, r2):
    one = interval(1, 1)
    rep_r1 = div_interval(one, r1)
    rep_r2 = div_interval(one, r2)
    return div_interval(one, add_interval(rep_r1, rep_r2))

# Вот эти два интервала дают разные результаты при вычислении сопротивления параллельных резисторов:
a = interval(2,5); b = interval(2,30)

# Вопрос 5.
def multiple_references_explanation():
    return """Проблема множественных ссылок возникает при явном использовании одинаковых интервалов в каком-либо выражении. 
    Например, если у нас есть заданный интервал r1 и мы перемножим его с заданным интервалов r2 и разделим на их сумму, у 
    нас возникнет следующая ситуация: интервалы r1 и r2 явно используются дважды при вычислении, а это, в свою очередь,
    увеличивает границы конечного интервала, который не будет являеться строгим. Данную проблему можно избежать, если преобразовать
    уравнение таким образом, чтобы в нем не использовались одинаковые интервалы при вычислении. Такой подход уменьшает границы интервала
    и устраняет некоторые минусы, присущие интервальной арифметике. 
    Таким образом, так как в par2, в отличии от par1, явно не используются одинаковые интервалы, она лучше"""

# Вопрос 6.
def quadratic(x, a, b, c):
    """Возвращает интервал, описывающий область значения квадратичной функции с
    коэффициентами a, b и c для интервала области определения x.

    >>> str_interval(quadratic(interval(0, 2), -2, 3, -1))
    'от -3 до 0.125'
    >>> str_interval(quadratic(interval(1, 3), 2, -3, 1))
    'от 0 до 10'
    """
    extremum = -(b/(2*a))
    f = lambda x: a*(x**2) + b*x + c
    if extremum >= lower_bound(x) and extremum <= upper_bound(x):
        lower = min(f(extremum),f(lower_bound(x)), f(upper_bound(x)))
        upper = max(f(extremum),f(lower_bound(x)), f(upper_bound(x)))
    else:
        lower = min(f(lower_bound(x)), f(upper_bound(x)))
        upper = max(f(lower_bound(x)), f(upper_bound(x)))    

    return interval(lower, upper)

# Вопрос 7.
def polynomial(x, c):
    """Возвращает интервал, описывающий область значения полиномиальной функции с
    коэффициентами c для интервала области определения x.

    >>> str_interval(polynomial(interval(0, 2), [-1, 3, -2]))
    'от -3 до 0.125'
    >>> str_interval(polynomial(interval(1, 3), [1, -3, 2]))
    'от 0 до 10'
    >>> str_interval(polynomial(interval(0.5, 2.25), [10, 24, -6, -8, 3]))
    'от 18.0 до 23.0'
    """
    c = list(reversed(c))
    def f(z):
        g = 0
        for i in range(len(c)):
            g += c[i]*pow(z, len(c) - i - 1) 
        return g

    c_df = [c[i] * (len(c) - i - 1) for i in range(len(c)) if (len(c) - i - 1) != 0]
    all_extremums = find_zero_in_polynom(c_df)
    need_extremums = [i for i in all_extremums if i>= lower_bound(x) and i<= upper_bound(x)]
    lower = 0
    upper = 0


    for i in range(len(need_extremums)):
        if i == 0:
            lower = f(need_extremums[i])
            upper = f(need_extremums[i])
        else:
            if f(need_extremums[i]) < lower:
                lower = f(need_extremums[i])
            if f(need_extremums[i]) > upper:
                upper = f(need_extremums[i])

    return interval(min(lower, f(lower_bound(x)), f(upper_bound(x))), max(upper, f(lower_bound(x)), f(upper_bound(x))))

# Метод Ньютона (вдруг пригодится)

def improve(update, close, guess=1, max_updates=100):
    """Итеративно улучшает guess с помощью update, пока close(guess) является ложью или
    количество итераций меньше max_updates."""
    k = 0
    while not close(guess) and k < max_updates:
        guess = update(guess)
        k = k + 1
    return guess

def approx_eq(x, y, tolerance=1e-15):
    return abs(x - y) < tolerance

def find_zero(f, df, guess=1):
    """Возвращает нули функции f, имеющую производную df."""
    def near_zero(x):
        return approx_eq(f(x), 0)
    return improve(newton_update(f, df), near_zero, guess)

def find_zero_left(f, df, point):
    """Возвращает нули функции f, имеющую производную df."""
    def near_zero(x):
        return approx_eq(f(x), 0)
    return improve(newton_update(f, df), near_zero, point - 0.1)

def find_zero_right(f, df, point):
    """Возвращает нули функции f, имеющую производную df."""
    def near_zero(x):
        return approx_eq(f(x), 0)
    return improve(newton_update(f, df), near_zero, point + 0.1)    

def newton_update(f, df):
    """Возвращает функцию update для функции f, имеющей производную df, используя
    метод Ньютона."""
    def update(x):
        return x - f(x) / df(x)
    return update

def find_zero_in_polynom(c):
    """Находит все нули заданного полинома"""
    def f(z):
        g = 0
        for i in range(len(c)):
            g += c[i]*pow(z, len(c) - i - 1) 
        return g

    def df(z):
        g = 0
        for i in range(len(c)):
            g += c[i] * (len(c) - i - 1) * pow(z, len(c) - i - 2)
        return g

    if len(c) == 2:
        return [find_zero_left(f, df, 1)]
    elif len(c) == 3:
        c_df = [c[i] * (len(c) - i - 1) for i in range(len(c)) if (len(c) - i - 1) != 0] 
        return [find_zero_left(f, df, find_zero_in_polynom(c_df)[0]), find_zero_right(f, df, find_zero_in_polynom(c_df)[0])]    
    else:
        c_df = [c[i] * (len(c) - i - 1) for i in range(len(c)) if (len(c) - i - 1) != 0]
        extremums = find_zero_in_polynom(c_df)
        nulls = []
        for i in range(len(extremums)):
            nulls += [find_zero_left(f, df, extremums[i])]
            nulls += [find_zero_right(f, df, extremums[i])] 
        return nulls