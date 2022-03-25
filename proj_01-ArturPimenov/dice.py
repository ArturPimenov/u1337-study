"""Функции, имитирующие броски игральных костей.

Функция dice (игральная кость) не принимает аргументов и возвращает число
от 1 до n (включительно), где n — число граней у кости.

Типы игральных костей:

 -  Честная кость (fair dice) выдает возможные значения с равной вероятностью.
    Примеры: four_sided, six_sided

 -  Для тестирования функций, использующих броски костей dice, используется
    детерминированная тестовая кость, которая циклически возвращает элементы
    последовательности, заданной аргументами функции make_test_dice.
"""

from random import randint

def make_fair_dice(sides):
    """Возвращает честную кость, которая равновероятно возвращает целое число
    от 1 до заданного количества граней SIDES."""
    assert type(sides) == int and sides >= 1, 'Неверное значение sides'
    def dice():
        return randint(1,sides)
    return dice

four_sided = make_fair_dice(4)
six_sided = make_fair_dice(6)

def make_test_dice(*outcomes):
    """Возвращает тестовую детерминированную циклическую кость
    (цикл по OUTCOMES).

    >>> dice = make_test_dice(1, 2, 3)
    >>> dice()
    1
    >>> dice()
    2
    >>> dice()
    3
    >>> dice()
    1
    >>> dice()
    2

    В сигнатуре функции используется ещё нерассмотренный в курсе синтаксис.
    Лучший способ его понять — почитать документацию и поискать примеры.
    """
    assert len(outcomes) > 0, 'Нужно указать последовательность результатов outcomes'
    for o in outcomes:
        assert type(o) == int and o >= 1, 'Результат не положительное целое'
    index = len(outcomes) - 1
    def dice():
        nonlocal index
        index = (index + 1) % len(outcomes)
        return outcomes[index]
    return dice