SSS### HW_05b: Изменчивые функции и генераторы

###########
# Деревья #
###########

def tree(label, branches=[]):
    """Создаёт новое дерево с заданным корневым значением и списком ветвей."""
    for branch in branches:
        assert is_tree(branch), 'ветви должны быть деревьями'
    return [label] + list(branches)

def label(tree):
    """Возвращает корневое значение дерева."""
    return tree[0]

def branches(tree):
    """Возвращает список ветвей дерева."""
    return tree[1:]

def is_tree(tree):
    """Возвращает True, если аргумент — дерево, иначе False."""
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    """Возвращает True, если список веток пуст, иначе False."""
    return not branches(tree)

def print_tree(t, indent=0):
    """Выводит представление дерева, в котором каждое значение узла
    сдвигается на два пробела за каждый уровень глубины.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    """
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)

def copy_tree(t):
    """Возвращает копию t. Используется только для тестов.

    >>> t = tree(5)
    >>> copy = copy_tree(t)
    >>> t = tree(6)
    >>> print_tree(copy)
    5
    """
    return tree(label(t), [copy_tree(b) for b in branches(t)])

# Вопрос 1.
def make_counter():
    """Возвращает функцию counter.

    >>> c = make_counter()
    >>> c('a')
    1
    >>> c('a')
    2
    >>> c('b')
    1
    >>> c('a')
    3
    >>> c2 = make_counter()
    >>> c2('b')
    1
    >>> c2('b')
    2
    >>> c('b') + c2('b')
    5
    """
    unical_str = []
    un_unical_str = []
    def counter(strk):
        assert type(strk) == str, 'Ты ввел не строку'
        nonlocal unical_str, un_unical_str

        if strk not in unical_str:
            unical_str += [strk]
            un_unical_str += [strk]
            return 1
        else:
            un_unical_str += [strk]
            counter = 0
            for i in un_unical_str:
                if i == strk:
                    counter += 1
            return counter           
    return counter

# Вопрос 2.
def make_fib():
    """Возвращает функцию, возвращающую следующее число Фибоначчи при каждом вызове.

    >>> fib = make_fib()
    >>> fib()
    0
    >>> fib()
    1
    >>> fib()
    1
    >>> fib()
    2
    >>> fib()
    3
    >>> fib2 = make_fib()
    >>> fib() + sum([fib2() for _ in range(5)])
    12
    """
    num_nechet = 1
    num_chet = 0
    num = 0
    def num_fib():
        nonlocal num, num_nechet, num_chet
        if num == 0:
            num += 1
            return num_chet
        elif num == 1:
            num += 1            
            return num_nechet
        else:
            if num % 2 == 0:
                num_chet = num_nechet + num_chet
                num += 1
                return num_chet
            else:
                num_nechet = num_nechet + num_chet
                num += 1
                return num_nechet           
    return num_fib

# Вопрос 3.
def make_withdraw(balance, password):
    """Возвращает защищённую паролем функцию withdraw.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> error = w(90, 'hax0r')
    >>> error
    'Недостаточно средств'
    >>> error = w(25, 'hwat')
    >>> error
    'Неверный пароль'
    >>> new_bal = w(25, 'hax0r')
    >>> new_bal
    50
    >>> w(75, 'a')
    'Неверный пароль'
    >>> w(10, 'hax0r')
    40
    >>> w(20, 'n00b')
    'Неверный пароль'
    >>> w(10, 'hax0r')
    "Твой аккаунт заблокирован. Попытки входа: ['hwat', 'a', 'n00b']"
    >>> w(10, 'l33t')
    "Твой аккаунт заблокирован. Попытки входа: ['hwat', 'a', 'n00b']"
    >>> type(w(10, 'l33t')) == str
    True
    """
    failed_passw = []
    def withdraw(amount, passwd):
        nonlocal balance, password, failed_passw
        if len(failed_passw) >= 3:
            return 'Твой аккаунт заблокирован. Попытки входа: {}'.format(failed_passw)  
        
        if passwd != password:
            failed_passw += [passwd]
            return 'Неверный пароль'
        else:
            if amount > balance:
                return 'Недостаточно средств'
            balance = balance - amount
            return balance
    return withdraw

# Вопрос 4.
def make_joint(withdraw, old_password, new_password):
    """Возвращает защищенную паролем функцию, которая присоединяется к существующей функции withdraw с новым паролем.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> make_joint(w, 'my', 'secret')
    'Неверный пароль'
    >>> j = make_joint(w, 'hax0r', 'secret')
    >>> w(25, 'secret')
    'Неверный пароль'
    >>> j(25, 'secret')
    50
    >>> j(25, 'hax0r')
    25
    >>> j(100, 'secret')
    'Недостаточно средств'

    >>> j2 = make_joint(j, 'secret', 'code')
    >>> j2(5, 'code')
    20
    >>> j2(5, 'secret')
    15
    >>> j2(5, 'hax0r')
    10

    >>> j2(25, 'password')
    'Неверный пароль'
    >>> j2(5, 'secret')
    "Твой аккаунт заблокирован. Попытки входа: ['my', 'secret', 'password']"
    >>> j(5, 'secret')
    "Твой аккаунт заблокирован. Попытки входа: ['my', 'secret', 'password']"
    >>> w(5, 'hax0r')
    "Твой аккаунт заблокирован. Попытки входа: ['my', 'secret', 'password']"
    >>> make_joint(w, 'hax0r', 'hello')
    "Твой аккаунт заблокирован. Попытки входа: ['my', 'secret', 'password']"
    """
    strk = withdraw(0, old_password)
    def f_withdraw(amount, passwd):
        nonlocal old_password, new_password, withdraw
        if passwd == new_password or passwd == old_password: 
            return withdraw(amount, old_password)
        else:
            return withdraw(amount, passwd)     
    return strk if type(strk) == str else f_withdraw


# Вопрос 5.
def height(t):
    if is_leaf(t):
        return 0
    else:
        depths = [1+height(b) for b in branches(t)]
    x = 0    
    for i in depths:
        if i>x:
            x = i
    return x

def find_path(t,x,h):
    if label(t) == x and h==0:
        return [x]
    else:
        path = [str(label(t))] + [find_path(b,x, h-1) for b in branches(t) if label(b) != None]
        path = [p for p in path if p!='None']
        for i in range(len(path)):
            if type(path[i]) == list:
                path = path[:i] + [p for p in path[i]] + path[(i+1):len(path)]          
        if not x in path:
            path = 'None'

        return path
def int_path(path):
    return [int(p) for p in path]

def generate_paths(t, x):
    """Возвращает генератор всех возможных путей от корня t до значения x в виде списков.

    >>> t1 = tree(1, [tree(2, [tree(3), tree(4, [tree(6)]), tree(5)]), tree(5)])
    >>> print_tree(t1)
    1
      2
        3
        4
          6
        5
      5
    >>> next(generate_paths(t1, 6))
    [1, 2, 4, 6]
    >>> path_to_5 = generate_paths(t1, 5)
    >>> sorted(list(path_to_5))
    [[1, 2, 5], [1, 5]]

    >>> t2 = tree(0, [tree(2, [t1])])
    >>> print_tree(t2)
    0
      2
        1
          2
            3
            4
              6
            5
          5
    >>> path_to_2 = generate_paths(t2, 2)
    >>> sorted(list(path_to_2))
    [[0, 2], [0, 2, 1, 2]]
    """

    h = height(t)
    new = []
    while h >= 0:
        new =find_path(t,x,h)
        if type(new) == list:
            #for p in range(len(new)):
                #if type(p) == list
            new = int_path(new)
            yield new
        h -= 1
   