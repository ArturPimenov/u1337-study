### Лабораторная работа № 8: Подготовка к контрольной"""

###############################
# Определение связных списков #
###############################

class Link:
    """Связный список.

    >>> s = Link(1)
    >>> s.first
    1
    >>> s.rest is Link.empty
    True
    >>> s = Link(2, Link(3, Link(4)))
    >>> s.second
    3
    >>> s.first = 5
    >>> s.second = 6
    >>> s.rest.rest = Link.empty
    >>> s                                    # Отображает результат repr(s)
    Link(5, Link(6))
    >>> s.rest = Link(7, Link(Link(8, Link(9))))
    >>> s
    Link(5, Link(7, Link(Link(8, Link(9)))))
    >>> print(s)                             # Выводит результат str(s)
    <5 7 <8 9>>
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    @property
    def second(self):
        return self.rest.first

    @second.setter
    def second(self, value):
        self.rest.first = value

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'

# Вопрос 1.
def deep_len(lnk):
    """Возвращает «глубокий» размер связного списка с возможными вложениями.

    >>> deep_len(Link(1, Link(2, Link(3))))
    3
    >>> deep_len(Link(Link(1, Link(2)), Link(3, Link(4))))
    4
    >>> levels = Link(Link(Link(1, Link(2)), \
            Link(3)), Link(Link(4), Link(5)))
    >>> print(levels)
    <<<1 2> 3> <4> 5>
    >>> deep_len(levels)
    5
    """
    counter = 0
    while lnk:
        if isinstance(lnk.first, Link):
            counter += deep_len(lnk.first)
        else:    
            counter +=1 
        lnk = lnk.rest
    return counter    

# Рекурсия/Древовидная рекурсия
# Вопрос 3.

def insert_into_all(item, nested_list):
    """В предположении, что nested_list — это список списков, возвращает новый
    список, включающий всё, что было в nested_list, но к каждому вложенному
    списку в начало добавляется элемент item.

    >>> nl = [[], [1, 2], [3]]
    >>> insert_into_all(0, nl)
    [[0], [0, 1, 2], [0, 3]]
    """
    for n_l in nested_list:
        n_l.insert(0, item)

    return nested_list    

def subseqs(s):
    """В предположении, что S является списком, возвращает вложенный список
    всевозможных подпоследовательностей элементов исходного списка.
    Подпоследовательности могут быть добавлены в любом порядке.

    >>> seqs = subseqs([1, 2, 3])
    >>> sorted(seqs)
    [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
    >>> subseqs([])
    [[]]
    """
    #nest_list = [[]]
    #copy = [[]]
    #while s:
     #   nest_list.extend(insert_into_all(s.pop(), copy))
      #  copy = eval(repr(nest_list))
    #return nest_list 
    if len(s) == 0:
        return [[]]
    else:  
        return insert_into_all(s[0], subseqs(s[1:])) + subseqs(s[1:])  
    

# Вопрос 4.
def inc_subseqs(s):
    """В предположении, что S является списком, возвращает вложенный список
    всевозможных подпоследовательностей элементов исходного списка, за
    исключением подпоследовательностей с убывающим порядком хотя бы двух
    соседних элементов. Подпоследовательности могут быть добавлены в любом порядке.

    >>> seqs = inc_subseqs([1, 3, 2])
    >>> sorted(seqs)
    [[], [1], [1, 2], [1, 3], [2], [3]]
    >>> inc_subseqs([])
    [[]]
    >>> seqs2 = inc_subseqs([1, 1, 2])
    >>> sorted(seqs2)
    [[], [1], [1], [1, 1], [1, 1, 2], [1, 2], [1, 2], [2]]

    """
    i, j, prev = 0, 0, 0
    subs = sorted(subseqs(s))
    subbs = sorted(subseqs(s))
    while i < len(subs):
        if subs[i] == []:
            i += 1
            continue     
        while j < len(subs[i]):
            if subs[i][j] < prev:
                subbs.pop(subbs.index(subs[i]))
                break
            prev = subs[i][j]
            j += 1
        i += 1
        prev, j = 0, 0        
    return subbs

# ООП
# Вопрос 5.

class Keyboard:
    """Класс Keyboard принимает некоторое количество кнопок Button, и имеет
    словарь для сопоставления положения кнопок (ключи) и кнопок Button (значения).

    >>> b1 = Button(0, "H")
    >>> b2 = Button(1, "I")
    >>> k = Keyboard(b1, b2)
    >>> k.buttons[0].key
    'H'
    >>> k.press(1)
    'I'
    >>> k.press(2) #Тут нет кнопки
    ''
    >>> k.typing([0, 1])
    'HI'
    >>> k.typing([1, 0])
    'IH'
    >>> b1.times_pressed
    2
    >>> b2.times_pressed
    3

    """

    def __init__(self, *args):
        self.buttons = {}
        for b in args:
            self.buttons[b.pos] = b

    def press(self, info):
        """Принимает положение нажатой кнопки и возвращает результат"""
        if info in self.buttons.keys():
            self.buttons[info].times_pressed += 1
            return '{}'.format(self.buttons[info].key)
        return ''    

    def typing(self, typing_input):
        """Принимает список положений нажатых кнопок и возвращает
        результирующую последовательность результатов нажатий"""
        full_press = ''
        for t_i in typing_input:
            full_press += self.press(t_i)
        return full_press    

class Button:
    def __init__(self, pos, key):
        self.pos = pos
        self.key = key
        self.times_pressed = 0

# Nonlocal
# Вопрос 6.
def make_advanced_counter_maker():
    """Создаёт функцию, которая создает счётчики, понимающие сообщения
    "count", "global-count", "reset", и "global-reset".

    Смотри на примеры:

    >>> make_counter = make_advanced_counter_maker()
    >>> tom_counter = make_counter()
    >>> tom_counter('count')
    1
    >>> tom_counter('count')
    2
    >>> tom_counter('global-count')
    1
    >>> jon_counter = make_counter()
    >>> jon_counter('global-count')
    2
    >>> jon_counter('count')
    1
    >>> jon_counter('reset')
    >>> jon_counter('count')
    1
    >>> tom_counter('count')
    3
    >>> jon_counter('global-count')
    3
    >>> jon_counter('global-reset')
    >>> tom_counter('global-count')
    1
    """
    messages = ['count', 'global-count', 'reset', 'global-reset']
    global_count = 0
    def make_counter():
        count = 0
        def counter(message):
            nonlocal count, global_count
            if message == messages[0]:
                count += 1
                print(count)
            elif message == messages[1]:
                global_count += 1
                print(global_count)
            elif message == messages[2]:
                count = 0
            elif message == messages[3]:
                global_count = 0
        return counter
    return make_counter                        

# Вопрос 8.
# Списки
def all_prefiks(link):
    a_p = []
    i = 0
    for l in link:
        if not a_p:
            a_p.append(l)
        else:
            a_p += [a_p[i] + l]
            i += 1 
    return a_p           


def trade(first, second):
    """Производит обмен наименьшими префиксами (подпоследовательностями) списков
    first и second, которые одинаковы по сумме элементов.

    >>> a = [1, 1, 3, 2, 1, 1, 4]
    >>> b = [4, 3, 2, 7]
    >>> trade(a, b) # Меняет 1+1+3+2=7 на 4+3=7
    'По рукам!'
    >>> a
    [4, 3, 1, 1, 4]
    >>> b
    [1, 1, 3, 2, 2, 7]
    >>> c = [3, 3, 2, 4, 1]
    >>> trade(b, c)
    'Нет!'
    >>> b
    [1, 1, 3, 2, 2, 7]
    >>> c
    [3, 3, 2, 4, 1]
    >>> trade(a, c)
    'По рукам!'
    >>> a
    [3, 3, 2, 1, 4]
    >>> b
    [1, 1, 3, 2, 2, 7]
    >>> c
    [4, 3, 1, 4, 1]
    """
    m, n = 1, 1
    prefiks = [all_prefiks(first), all_prefiks(second)]
    min_len_p, max_len_p = min(prefiks[0], prefiks[1]), max(prefiks[0], prefiks[1])
    for i in prefiks[0]:
        for j in prefiks[1]:
            if i==j:
                first[:m], second[:n] = second[:n], first[:m]
                return 'По рукам!'
            n += 1  
        m += 1
        n = 1      
    return 'Нет!'

# Вопрос 9.
# Генераторы
def permutations(seq):
    """Генерирует все перестановки заданной последовательности. Каждая
    перестановка — это список элементов исходной последовательности в другом
    порядке. Перестановки могут выдаваться в любом порядке.

    >>> perms = permutations([100])
    >>> type(perms)
    <class 'generator'>
    >>> next(perms)
    [100]
    >>> try:
    ...     next(perms)
    ... except StopIteration:
    ...     print('Больше вариантов нет!')
    Больше вариантов нет!
    >>> sorted(permutations([1, 2, 3])) # Возвращает отсортированный список результатов
    [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    >>> sorted(permutations((10, 20, 30)))
    [[10, 20, 30], [10, 30, 20], [20, 10, 30], [20, 30, 10], [30, 10, 20], [30, 20, 10]]
    >>> sorted(permutations("ab"))
    [['a', 'b'], ['b', 'a']]

    """
    if len(seq) == 1:
        yield [seq[0]]
    else:
        for perm in permutations(seq[1:]):
            for i in range(len(perm) + 1):
                perm.insert(i, seq[0])
                p = list(perm)
                yield p
                perm.pop(i)

# Вопрос 10.
# Рекурсивные объекты
def make_to_string(front, mid, back, empty_repr):
    """ Возвращает функцию, которая преобразует связные списки в строки.

    >>> umputun_to_string = make_to_string("[", "|-]-->", "", "[]")
    >>> bobuk_to_string = make_to_string("(", " . ", ")", "()")
    >>> lst = Link(1, Link(2, Link(3, Link(4))))
    >>> umputun_to_string(lst)
    '[1|-]-->[2|-]-->[3|-]-->[4|-]-->[]'
    >>> umputun_to_string(Link.empty)
    '[]'
    >>> bobuk_to_string(lst)
    '(1 . (2 . (3 . (4 . ()))))'
    >>> bobuk_to_string(Link.empty)
    '()'
    """
    def list_to_string(link):
        if link is Link.empty:
            return empty_repr     
        else:
            return front + str(link.first) + mid + list_to_string(link.rest) + back
    return list_to_string            
# Вопрос 10.
def tree_map(fn, t):
    """Применяет функцию fn ко всем элементам дерева t и возвращает новое дерево
    с результатами.

    >>> numbers = Tree(1,
    ...                [Tree(2,
    ...                      [Tree(3),
    ...                       Tree(4)]),
    ...                 Tree(5,
    ...                      [Tree(6,
    ...                            [Tree(7)]),
    ...                       Tree(8)])])
    >>> print(tree_map(lambda x: 2**x, numbers))
    2
      4
        8
        16
      32
        64
          128
        256
    >>> print(numbers)
    1
      2
        3
        4
      5
        6
          7
        8
    """
    if not t.branches:
        return Tree(fn(t.label))
    else:
        return Tree(fn(t.label), [tree_map(fn, b) for b in t.branches])


# Вопрос 12.
def long_paths(tree, n):
    """Возвращает список всех путей в дереве, которые не короче n.

    >>> t = Tree(3, [Tree(4), Tree(4), Tree(5)])
    >>> left = Tree(1, [Tree(2), t])
    >>> mid = Tree(6, [Tree(7, [Tree(8)]), Tree(9)])
    >>> right = Tree(11, [Tree(12, [Tree(13, [Tree(14)])])])
    >>> whole = Tree(0, [left, Tree(13), mid, right])
    >>> for path in long_paths(whole, 2):
    ...     print(path)
    ...
    <0 1 2>
    <0 1 3 4>
    <0 1 3 4>
    <0 1 3 5>
    <0 6 7 8>
    <0 6 9>
    <0 11 12 13 14>
    >>> for path in long_paths(whole, 3):
    ...     print(path)
    ...
    <0 1 3 4>
    <0 1 3 4>
    <0 1 3 5>
    <0 6 7 8>
    <0 11 12 13 14>
    >>> long_paths(whole, 4)
    [Link(0, Link(11, Link(12, Link(13, Link(14)))))]
    """
    def f(tree):
        sp = []
        sp_b1 = []
        sp_b2 = []
        if not tree.branches:
            return [Link(tree.label)]
        else:
            for b in tree.branches:
                if not b.branches:
                    sp_b1.append(f(b)[0])
                else:
                    sp_b2 += f(b)
                    for i in sp_b2:
                        sp_b1 += [i]
                    sp_b2 = []        
            
            for b in sp_b1:
                sp += [Link(tree.label, b)]

            return sp    

    ret_sp = []
    all_paths = f(tree)
    for p in all_paths:
        if deep_len(p) > n:
            ret_sp += [p]
    return ret_sp        
        
##############
# Класс Tree #
##############
# [Link(tree.label, next(i)[0]) for i in sp]    
            #for p in list([f(b) for b in tree.branches]):
                #for t_p in p:
                    #sp += [Link(tree.label, t_p)]
                    #print(p, "           ", sp)
                #yield sp

        #if not tree.branches:
            #yield [Link(tree.label)]
        #for b in tree.branches:
            #print(repr(b))
            #p = [Link(tree.label, Link(f(b)))]
            #yield p
class Tree:
    """
    >>> t = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
    >>> t.label
    3
    >>> t.branches[0].label
    2
    >>> t.branches[1].is_leaf()
    True
    """
    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(self.label, branch_str)

    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = '  ' * indent + str(t.label) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str
        return print_tree(self).rstrip()