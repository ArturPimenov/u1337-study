### HW_02: Рекурсия

# Вопрос 1.

def g(n):
    """Возвращает значение G(n), вычисленное рекурсивно.

    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    """
    if n <=3:
        return n 
    else:
        return g(n-1) + 2*g(n-2) + 3*g(n-3)

def g_iter(n):
    """Возвращает значение G(n), вычисленное итеративно.

    >>> g_iter(1)
    1
    >>> g_iter(2)
    2
    >>> g_iter(3)
    3
    >>> g_iter(4)
    10
    >>> g_iter(5)
    22
    """
    art_n = 4
    #Cлагаемые в G(n). Изначально берется случай n==4
    g, g1, g2, g3 = 0, 3, 2, 1

    #Слагаемые в искуственном G(n). Изначально берется случай n==4
    s, s1, s2, s3 = 0, 3, 2, 1

    if n <= 3:
        return n

    else:
        while art_n <= n:
            s = s1 + 2*s2 + 3*s3    
            if art_n == n:
                g1, g2, g3 = s1, s2, s3
            else:
                s1, s2, s3 = s, s1, s2
            art_n += 1  

        g = g1 + 2*g2 + 3*g3    
        return g

# Вопрос 2.

def has_seven(k):
    """Проверка наличия цифры 7 в k
    >>> has_seven(3)
    False
    >>> has_seven(7)
    True
    >>> has_seven(2734)
    True
    >>> has_seven(2634)
    False
    >>> has_seven(734)
    True
    >>> has_seven(7777)
    True
    """
    return has_seven(k//10) if k%10 != 7 and k//10 else k%10 == 7

# Вопрос 3.

"1 2 3 4 5 6 [7] 6 5 4 3 2 1 [0] 1 2 [3] 2 1 0 [-1] 0 1 2 3 4 [5] [4] 5 6"

def oper_ins(n):
    if n==1:
        return 1    
    elif (has_seven(n) or not n%7) and oper_ins(n-1) == 1:
        return -1   
    elif (has_seven(n) or not n%7) and oper_ins(n-1) == -1:
        return 1
    else:
        return oper_ins(n-1)

def pingpong(n):
    """Возвращает n-ый элемент последовательности «пинг-понг».

    >>> pingpong(7)
    7
    >>> pingpong(8)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    0
    >>> pingpong(30)
    6
    >>> pingpong(68)
    2
    >>> pingpong(69)
    1
    >>> pingpong(70)
    0
    >>> pingpong(71)
    1
    >>> pingpong(72)
    0
    >>> pingpong(100)
    2
    """
    return 1 if n==1 else pingpong(n-1) + oper_ins(n-1)

# Вопрос 4.

def make_has_number(number):
    def has_number(k):
        return has_number(k//10) if k%10 != number and k//10 else k%10 == number
    return has_number   

def n_o_n(k, number):
    if make_has_number(number)(k%10):
        return n_o_n(k//10, number) + 1
    elif k:
        return n_o_n(k//10, number)
    else:   
        return 0    

def ten_pairs(n):
    """Возвращает число пар цифр в положительном целом n, в сумме образующих 10.

    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    """
    if n and make_has_number(10 - n%10)(n) and n%10 == 5:
        return n_o_n(n, 10 - n%10) - 1 + ten_pairs(n//10)

    elif n and make_has_number(10 - n%10)(n):   
        return n_o_n(n, 10 - n%10) + ten_pairs(n//10)

    elif n:
        return ten_pairs(n//10) 

    else:
        return 0

# Вопрос 5.

def true_stepen(n,m):
    if pow(2, m) >= n:
        return true_stepen(n, m-1)
    else:
        return m    

def count_partition(n, m):
    if n==0:
        return 1    
    elif n<0:
        return 0
    elif pow(2,m) < 1:
        return 0
    else:
        with_m = count_partition(n-pow(2,m), m)
        without_m = count_partition(n, m-1)
        return with_m + without_m   

def count_change(amount):
    """Возвращает количество способов размена amount киберденьгами.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    """
    return count_partition(amount, true_stepen(amount,amount))

# Вопрос 6.

from operator import sub, mul

def make_anonymous_factorial():
    """Возвращает выражение, вычисляющее факториал.

    >>> make_anonymous_factorial()(5)
    120
    """
    return lambda n: 1 if n==1 else n*make_anonymous_factorial()(n-1)