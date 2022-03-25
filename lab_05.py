### Лабораторная работа № 5: Списки и деревья"""
from random import choice
from itertools import zip_longest
# Вопрос 1.
def acorn_finder(t):
    """Возвращает True, если t содержит узел со значением 'жёлудь', иначе False.

    >>> scrat = tree('жёлудь')
    >>> acorn_finder(scrat)
    True
    >>> sproul = tree('roots', [tree('ветвь1', [tree('лист'), tree('жёлудь')]), tree('ветвь2')])
    >>> acorn_finder(sproul)
    True
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> acorn_finder(numbers)
    False
    """
    if label(t) == "жёлудь":
        return True
    else:
        for branch in branches(t):
            if acorn_finder(branch):
                return True
    return False   

# Вопрос 2.

def f(t, val):
    return tree(label(t), [f(b,val) for b in branches(t) if label(b) != val or not is_leaf(b)]) 
        #if (label(b) != val and  not is_leaf(b))])

def prune_leaves(t, vals):
    """Возвращает изменённую копию t, в которой все листья со значениями, равными
    элементам списка vals, удаляются.  Возвращает None, если от дерева ничего не осталось.

    >>> t = tree(2)
    >>> print(prune_leaves(t, (1, 2)))
    None
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    >>> print_tree(prune_leaves(numbers, (3, 4, 6, 7)))
    1
      2
      3
        5
      6
    """
    if is_leaf(t): 
        for val in vals:
            if label(t) == val:
                return None
    copy = t 
    for val in vals:
        copy = f(copy, val)

    return copy
        
# Вопрос 3.
def memory(n):
    """
    >>> f = memory(10)
    >>> f(lambda x: x * 2)
    20
    >>> f(lambda x: x - 7)
    13
    >>> f(lambda x: x > 5)
    True
    """
    def g(pravilo):
        nonlocal n
        n = pravilo(n)
        print(n)

    return g    

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

# Шекспир и словари

# Вопрос 4.
def build_successors_table(tokens):
    """Возвращает словарь: ключи — слова; значения — списки последующих слов.

    >>> text = ['We', 'came', 'to', 'investigate', ',', 'catch', 'bad', 'guys', 'and', 'to', 'eat', 'pie', '.']
    >>> table = build_successors_table(text)
    >>> sorted(table)
    [',', '.', 'We', 'and', 'bad', 'came', 'catch', 'eat', 'guys', 'investigate', 'pie', 'to']
    >>> table['to']
    ['investigate', 'eat']
    >>> table['pie']
    ['.']
    >>> table['.']
    ['We']
    """
    table = {}
    prev = '.'
    for word in tokens:
        if prev not in table:
            table[prev] = [word]
        else:
            table[prev] = table[prev] + [word] 
        prev = word
    return table

# Вопрос 5.
def construct_sent(word, table):
    """Печатает случайную фразу начиная со слова word, составляя её по table.

    >>> table = {'Wow': ['!'], 'Sentences': ['are'], 'are': ['cool'], 'cool': ['.']}
    >>> construct_sent('Wow', table)
    'Wow!'
    >>> construct_sent('Sentences', table)
    'Sentences are cool.'

    """
    import random
    result = ''
    while word not in ['.', '!', '?']:
        result += word + ' '
        word = choice(table[word])   
    return result.strip() + word

def shakespeare_tokens(path='shakespeare.txt', url='http://composingprograms.com/shakespeare.txt'):
    """Возвращает слова пьес Шекспира списком."""
    import os
    from urllib.request import urlopen
    if os.path.exists(path):
        return open('shakespeare.txt', encoding='ascii').read().split()
    else:
        shakespeare = urlopen(url)
        return shakespeare.read().decode(encoding='ascii').split()

# Раскомментируй две следующие строки
# tokens = shakespeare_tokens()
# table = build_successors_table(tokens)

def random_sent():
    import random
    return construct_sent(random.choice(table['.']), table)

# Вопрос 6.
def sprout_leaves(t, vals):
    """Наращивает новые листы, содержащие данные из vals на каждый лист
    исходного дерева t и возвращает результирующее дерево.

    >>> t1 = tree(1, [tree(2), tree(3)])
    >>> print_tree(t1)
    1
      2
      3
    >>> new1 = sprout_leaves(t1, [4, 5])
    >>> print_tree(new1)
    1
      2
        4
        5
      3
        4
        5

    >>> t2 = tree(1, [tree(2, [tree(3)])])
    >>> print_tree(t2)
    1
      2
        3
    >>> new2 = sprout_leaves(t2, [6, 1, 2])
    >>> print_tree(new2)
    1
      2
        3
          6
          1
          2
    """

    if branches(t):
        return tree(label(t), [sprout_leaves(b,vals) for b in branches(t)])
    else:

        return tree(label(t), [tree(i) for i in vals]) 

# Вопрос 7.
def add_trees(t1, t2):
    """
    >>> numbers = tree(1,
    ...                [tree(2,
    ...                      [tree(3),
    ...                       tree(4)]),
    ...                 tree(5,
    ...                      [tree(6,
    ...                            [tree(7)]),
    ...                       tree(8)])])
    >>> print_tree(add_trees(numbers, numbers))
    2
      4
        6
        8
      10
        12
          14
        16
    >>> print_tree(add_trees(tree(2), tree(3, [tree(4), tree(5)])))
    5
      4
      5
    >>> print_tree(add_trees(tree(2, [tree(3)]), tree(2, [tree(3), tree(4)])))
    4
      6
      4
    >>> print_tree(add_trees(tree(2, [tree(3, [tree(4), tree(5)])]), \
    tree(2, [tree(3, [tree(4)]), tree(5)])))
    4
      6
        8
        5
      5
    """

    united_of_tree = zip_longest(t1, t2, fillvalue=[])
    united_of_tree = list(united_of_tree)
    if not label(united_of_tree)[0]:
        label_tree = 0 + label(united_of_tree)[1]
    elif not label(united_of_tree)[1]:
        label_tree = label(united_of_tree)[0] + 0
    else:        
        label_tree = label(united_of_tree)[0] + label(united_of_tree)[1]
    return tree(label_tree, [add_trees(b[0], b[1]) for b in branches(united_of_tree)])

#number1 = tree(2, [tree(3)])
#number2 = tree(2, [tree(3), tree(4)])
#print_tree(add_trees(number1, number2))
#print(list(zip(numbers, numbers)))
#print(numbers)
#print_tree(add_trees(numbers,numbers))