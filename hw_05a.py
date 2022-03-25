### HW_05a: Абстрактные типы данных

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
def replace_leaf(t, old, new):
    """Возвращает новое дерево, в котором все листы со значением old заменены на new.

    >>> yggdrasil = tree('odin',
    ...                  [tree('balder',
    ...                        [tree('thor'),
    ...                         tree('loki')]),
    ...                   tree('frigg',
    ...                        [tree('thor')]),
    ...                   tree('thor',
    ...                        [tree('sif'),
    ...                         tree('thor')]),
    ...                   tree('thor')])
    >>> laerad = copy_tree(yggdrasil) # копирование yggdrasil для тестирования
    >>> print_tree(replace_leaf(yggdrasil, 'thor', 'freya'))
    odin
      balder
        freya
        loki
      frigg
        freya
      thor
        sif
        freya
      freya
    >>> laerad == yggdrasil # Проверка, что исходное дерево не изменилось
    True
    """
    if label(t) == old and not branches(t):
        return tree(new, [replace_leaf(b, old, new) for b in branches(t)])
    else:
        return tree(label(t), [replace_leaf(b, old, new) for b in branches(t)])

##########
# Мобили #
##########

def mobile(left, right):
    """Создаёт мобиль из правой и левой сторон."""
    assert is_side(left), "Аргумент left должен быть стороной (side)"
    assert is_side(right), "Аргумент right должен быть стороной (side)"
    return ['mobile', left, right]

def is_mobile(m):
    """Проверяет, что m является мобилем."""
    return type(m) == list and len(m) == 3 and m[0] == 'mobile'

def left(m):
    """Возвращает левую сторону мобиля."""
    assert is_mobile(m), "Аргумент m должен быть мобилем (mobile)"
    return m[1]

def right(m):
    """Возвращает правую сторону мобиля."""
    assert is_mobile(m), "Аргумент m должен быть мобилем (mobile)"
    return m[2]

def side(length, mobile_or_weight):
    """Создаёт ветвь (сторону) из длины стержня length и одного из:
       мобиля mobile или груза weight."""
    assert is_mobile(mobile_or_weight) or is_weight(mobile_or_weight)
    return ['side', length, mobile_or_weight]

def is_side(s):
    """Проверяет, что s — сторона side."""
    return type(s) == list and len(s) == 3 and s[0] == 'side'

def length(s):
    """Возвращает длину стержня стороны."""
    assert is_side(s), "Аргумент s должен быть стороной (side)"
    return s[1]

def end(s):
    """Возвращает мобиль или груз."""
    assert is_side(s), "Аргумент s должен быть стороной (side)"
    return s[2]

# Вопрос 2.
def weight(size):
    """Создаёт груз размера size."""
    assert size > 0
    return ['weight', size]

def size(w):
    """Возвращает размер груза."""
    assert is_weight(w), 'Аргумент w должен быть грузом (weight)'
    return w[1]

def is_weight(w):
    """Проверяет, что w — груз."""
    return type(w) == list and len(w) == 2 and w[0] == 'weight'

def examples():
    t = mobile(side(1, weight(2)),
               side(2, weight(1)))
    u = mobile(side(5, weight(1)),
               side(1, mobile(side(2, weight(3)),
                              side(3, weight(2)))))
    v = mobile(side(4, t), side(2, u))
    return (t, u, v)

def total_weight(m):
    """Возвращает полный вес m — груза или мобиля.

    >>> t, u, v = examples()
    >>> total_weight(t)
    3
    >>> total_weight(u)
    6
    >>> total_weight(v)
    9
    """
    if is_weight(m):
        return size(m)
    else:
        assert is_mobile(m), "Аргумент m должен быть мобилем или грузом"
        return total_weight(end(left(m))) + total_weight(end(right(m)))

# Вопрос 3.
def balanced(m):
    """Проверяет, что мобиль m сбалансирован.

    >>> t, u, v = examples()
    >>> balanced(t)
    True
    >>> balanced(v)
    True
    >>> w = mobile(side(3, t), side(2, u))
    >>> balanced(w)
    False
    >>> balanced(mobile(side(1, v), side(1, w)))
    False
    >>> balanced(mobile(side(1, w), side(1, v)))
    False
    """
    if is_weight(m):
        return True

    moment = lambda side: length(side(m)) * total_weight(end(side(m)))

    if moment(left) != moment(right):
        return False  
    else:
        c = balanced(end(left(m)))
        d = balanced(end(right(m)))
        return False if not c or not d else True                         
            

       

# Вопрос 4.
def totals_tree(m):
    """Возвращает дерево, описывающее распределение веса в мобиле.

    >>> t, u, v = examples()
    >>> print_tree(totals_tree(t))
    3
      2
      1
    >>> print_tree(totals_tree(u))
    6
      1
      5
        3
        2
    >>> print_tree(totals_tree(v))
    9
      3
        2
        1
      6
        1
        5
          3
          2
    """
    if is_weight(m):
        return tree(size(m))

    return [total_weight(m)] + [totals_tree(end(left(m))), totals_tree(end(right(m)))]
  