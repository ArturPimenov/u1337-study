### Лабораторная работа № 4: Абстракция данных и списки"""

# Вопрос 1. 
def _q_01():
    """
    Часть 1
    >>> x = [1, 3, [5, 7], 9]                                   # doctest: +SKIP
    >>> x[2][1]                                               # doctest: +SKIP
    7
    >>> x = [[7]]                                               # doctest: +SKIP
    >>> x[0][0]                                               # doctest: +SKIP
    7
    >>> x = [3, 2, 1, [9, 8, 7]]                                # doctest: +SKIP
    >>> x[3][2]                                               # doctest: +SKIP
    7
    >>> x = [[3, [5, 7], 9]]                                    # doctest: +SKIP
    >>> x[0][1][1]                                               # doctest: +SKIP
    7

    Часть 2
    >>> lst = [3, 2, 7, [84, 83, 82]]                           # doctest: +SKIP
    >>> lst[4]                                                  # doctest: +SKIP
    Traceback (most recent call last):
    ...
    IndexError: list index out of range
    >>> lst[3][0]                                               # doctest: +SKIP
    84
    """
    return 0

# Вопрос 2. 
def _q_02():
    """
    Часть 1
    >>> [x*x for x in range(5)]                                 # doctest: +SKIP
    [0, 1, 4, 9, 16]
    >>> [n for n in range(10) if n % 2 == 0]                    # doctest: +SKIP
    [0, 2, 4, 6, 8]
    >>> ones = [1 for i in ["привет", "как", "сам"]]            # doctest: +SKIP
    >>> ones + [str(i) for i in [6, 3, 8, 4]]                   # doctest: +SKIP
    [1, 1, 1, '6', '3', '8', '4']
    >>> [i+5 for i in [n for n in range(1,4)]]                  # doctest: +SKIP
    [6, 7, 8]

    Часть 2
    >>> [i**2 for i in range(10) if i < 3]                      # doctest: +SKIP
    [0, 1, 4]
    >>> lst = ['привет' for i in [1, 2, 3]]                     # doctest: +SKIP
    >>> print(lst)                                              # doctest: +SKIP
    ['привет', 'привет', 'привет']
    >>> lst + [i for i in ['1', '2', '3']]                      # doctest: +SKIP
    ['привет', 'привет', 'привет', '1', '2', '3']
    """
    return 0

# Вопрос 3.
def if_this_not_that(i_list, this):
    """
    Определи функцию, которая принимает список целых `i_list` и целое число
    `this`. Каждый элемент в `i_list`, если элемент больше `this`, выводится в консоль; 
    в противном случае выводится слово `that`.

    >>> original_list = [1, 2, 3, 4, 5]
    >>> if_this_not_that(original_list, 3)
    that
    that
    that
    4
    5
    """
    for elem in i_list:
        if elem > this:
            print(elem)
        else:
            print("that")    

# Вопрос 4.
def make_city(name, lat, lon):
    """
    >>> city = make_city('Ярославль', 0, 1)
    >>> get_name(city)
    'Ярославль'
    >>> get_lat(city)
    0
    >>> get_lon(city)
    1
    """
    return [name, lat, lon]

def get_name(city):
    """
    >>> city = make_city('Ярославль', 0, 1)
    >>> get_name(city)
    'Ярославль'
    """
    return city[0]

def get_lat(city):
    """
    >>> city = make_city('Ярославль', 0, 1)
    >>> get_lat(city)
    0
    """
    return city[1]

def get_lon(city):
    """
    >>> city = make_city('Ярославль', 0, 1)
    >>> get_lon(city)
    1
    """
    return city[2]

from math import sqrt
def distance(city1, city2):
    """
    >>> city1 = make_city('city1', 0, 1)
    >>> city2 = make_city('city2', 0, 2)
    >>> distance(city1, city2)
    1.0
    >>> city3 = make_city('city3', 6.5, 12)
    >>> city4 = make_city('city4', 2.5, 15)
    >>> distance(city3, city4)
    5.0
    """
    return sqrt((get_lon(city1) - get_lon(city2))**2 + (get_lat(city1) - get_lat(city2))**2)

# Вопрос 5.
def closer_city(lat, lon, city1, city2):
    """
    Возвращает название города city1 или города city2 в зависимости от того, 
    какой из них ближе к координате (lat, lon).

    >>> moscow = make_city('Москва', 55.75, 37.616667)
    >>> saint_petersburg = make_city('Питер', 59.9375, 30.308611)
    >>> closer_city(57.616667, 39.85, moscow, saint_petersburg)
    'Москва'
    >>> london = make_city('Лондон', 51.507222, -0.1275)
    >>> mumbai = make_city('Мумбаи', 18.975, 72.825833)
    >>> closer_city(57.616667, 39.85, london, mumbai)
    'Лондон'
    """
    virtual_place = make_city('V-P', lat, lon)

    return get_name(city1) if distance(city1, virtual_place) <= distance(city2, virtual_place) else get_name(city2)

# Вопрос 6.
make_city = lambda name, lat, lon: { 'name': name, 'lat': lat, 'lon': lon }
get_name = lambda city: city['name']
get_lat = lambda city: city['lat']
get_lon = lambda city: city['lon']

# Вопрос 7.
def create_row(size):
    """
    Возвращает отдельную пустую строку поля заданного размера. Каждый пустой 
    элемент обозначается строкой '-'.

    >>> create_row(5)
    ['-', '-', '-', '-', '-']
    """
    return ['-']*size

def create_board(rows, columns):
    """Возвращает игровое поле заданного размера.

    >>> create_board(3, 5)
    [['-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-']]
    """
    return [create_row(columns)]*rows

# Вопрос 8.
def replace_elem(lst, index, elem):
    """Создаёт и возвращает новый список с теми же элементами, что и lst,
    за исключением элемента index, значение которого должно быть elem.

    >>> old = [1, 2, 3, 4, 5, 6, 7]
    >>> new = replace_elem(old, 2, 8)
    >>> new
    [1, 2, 8, 4, 5, 6, 7]
    >>> new is old         # проверяем, что replace_elem возвращает новый список
    False
    """
    assert index >= 0 and index < len(lst), 'Индекс за пределами размера списка'
    return [lst[i] for i in range(index)] + [elem] + [lst[i] for i in range(index + 1, len(lst))]
    

# Вопрос 9.
def get_piece(board, row, column):
    """Возвращает состояние поля в позиции (row, column) на доске.

    >>> rows, columns = 2, 2
    >>> board = create_board(rows, columns)
    >>> board = put_piece(board, rows, 0, 'X')[1] # Ставим "X" в столбец 0 поля и обновляем доску
    >>> board = put_piece(board, rows, 0, 'O')[1] # Ставим "O" в столбец 0 поля и обновляем доску
    >>> get_piece(board, 1, 0)
    'X'
    >>> get_piece(board, 1, 1)
    '-'
    """
    return board[row][column]

def put_piece(board, max_rows, column, player):
    """Размещает фишку игрока player в самом нижнем свободном поле заданного
    столбца. Возвращает тапл из двух элементов:

        1. Индекс строки, в которую встала фишка, или -1, если там нет мест.
        2. Новую доску.

    >>> rows, columns = 2, 2
    >>> board = create_board(rows, columns)
    >>> row, new_board = put_piece(board, rows, 0, 'X')
    >>> row
    1
    >>> row, new_board = put_piece(new_board, rows, 0, 'O')
    >>> row
    0
    >>> row, new_board = put_piece(new_board, rows, 0, 'X')
    >>> row
    -1
    """
    i = max_rows - 1
    while i>=0:
        if get_piece(board, i, column) == '-':
            return i, replace_elem(board, i, replace_elem(board[i], column, player))
        i -= 1
    return -1, board        

# Вопрос 10.
def make_move(board, max_rows, max_cols, col, player):
    """Размещает фишку игрока в столбец col доски в случае возможного хода.
    Возвращает тапл из двух значений:

        1. Если ход возможен, возвращается индекс строки, в которую попала фишка.
           Иначе возвращает -1.
        2. Обновлённая доска

    >>> rows, columns = 2, 2
    >>> board = create_board(rows, columns)
    >>> row, board = make_move(board, rows, columns, 0, 'X')
    >>> row
    1
    >>> get_piece(board, 1, 0)
    'X'
    >>> row, board = make_move(board, rows, columns, 0, 'O')
    >>> row
    0
    >>> row, board = make_move(board, rows, columns, 0, 'X')
    >>> row
    -1
    >>> row, board = make_move(board, rows, columns, -4, '0')
    >>> row
    -1
    """
    if col <= max_cols and col >= 0:
        return put_piece(board, max_rows, col, player)
    else:
        return -1, board    

# Вопрос 11.
def print_board(board, max_rows, max_cols):
    """
    Распечатывает доску. Строка 0 сверху, столбец 0 слева.

    >>> rows, columns = 2, 2
    >>> board = create_board(rows, columns)
    >>> print_board(board, rows, columns)
    - -
    - -
    >>> new_board = make_move(board, rows, columns, 0, 'X')[1]
    >>> print_board(new_board, rows, columns)
    - -
    X -
    """
    for r in range(max_rows):
        str_of_row_for_print = ''
        for c in range(max_cols):
            str_of_row_for_print += get_piece(board, r, c)
            str_of_row_for_print += ' '
        print(str_of_row_for_print.strip())        

# Вопрос 12.
def check_win_row(board, max_rows, max_cols, num_connect, row, player):
    """ 
    Возвращает True, если игрок player победил в заданной строке, иначе False.

    >>> rows, columns, num_connect = 4, 4, 2
    >>> board = create_board(rows, columns)
    >>> board = make_move(board, rows, columns, 0, 'X')[1]
    >>> board = make_move(board, rows, columns, 0, 'O')[1]
    >>> check_win_row(board, rows, columns, num_connect, 3, 'O')
    False
    >>> board = make_move(board, rows, columns, 2, 'X')[1]
    >>> board = make_move(board, rows, columns, 0, 'O')[1]
    >>> check_win_row(board, rows, columns, num_connect, 3, 'X')
    False
    >>> board = make_move(board, rows, columns, 1, 'X')[1]
    >>> check_win_row(board, rows, columns, num_connect, 3, 'X')
    True
    >>> check_win_row(board, rows, columns, 4, 3, 'X')           # Победа зависит от num_connect
    False
    >>> check_win_row(board, rows, columns, num_connect, 3, 'O') # Ищем победу только заданного игрока
    False
    """
    now_position = 0
    index_for_win = num_connect
    while now_position < max_cols and index_for_win != 0:
        if get_piece(board, row, now_position) == player:
            index_for_win -= 1
            now_position += 1
        else:
            index_for_win = num_connect
            now_position += 1      
     
    if index_for_win == 0:
        return True
    return False

        

    
        

            
def check_win_column(board, max_rows, max_cols, num_connect, col, player):
    """
    Возвращает True, если игрок player победил в заданном столбце, иначе False.

    >>> rows, columns, num_connect = 5, 5, 2
    >>> board = create_board(rows, columns)
    >>> board = make_move(board, rows, columns, 0, 'X')[1]
    >>> board = make_move(board, rows, columns, 1, 'O')[1]
    >>> check_win_column(board, rows, columns, num_connect, 0, 'X')
    False
    >>> board = make_move(board, rows, columns, 1, 'X')[1]
    >>> board = make_move(board, rows, columns, 1, 'O')[1]
    >>> check_win_column(board, rows, columns, num_connect, 1, 'O')
    False
    >>> board = make_move(board, rows, columns, 2, 'X')[1]
    >>> board = make_move(board, rows, columns, 1, 'O')[1]
    >>> check_win_column(board, rows, columns, num_connect, 1, 'O')
    True
    >>> check_win_column(board, rows, columns, 4, 1, 'O')
    False
    >>> check_win_column(board, rows, columns, num_connect, 1, 'X')
    False
    """
    now_position = 0
    index_for_win = num_connect
    while now_position < max_rows and index_for_win != 0:
        if get_piece(board, now_position, col) == player:
            index_for_win -= 1
            now_position += 1
        else:
            index_for_win = num_connect
            now_position += 1 
    if index_for_win == 0:
        return True
    return False        

# Вопрос 13.
def check_win(board, max_rows, max_cols, num_connect, row, col, player):
    """
    Возвращает True, если игрок player победил любым образом в заданных строке, 
    столбце или диагонали (row, col), иначе False.

    >>> rows, columns, num_connect = 2, 2, 2
    >>> board = create_board(rows, columns)
    >>> board = make_move(board, rows, columns, 0, 'X')[1]
    >>> board = make_move(board, rows, columns, 1, 'O')[1]
    >>> board = make_move(board, rows, columns, 0, 'X')[1]
    >>> check_win(board, rows, columns, num_connect, 0, 0, 'O')
    False
    >>> check_win(board, rows, columns, num_connect, 0, 0, 'X')
    True

    >>> board = create_board(rows, columns)
    >>> board = make_move(board, rows, columns, 0, 'X')[1]
    >>> board = make_move(board, rows, columns, 0, 'O')[1]
    >>> board = make_move(board, rows, columns, 1, 'X')[1]
    >>> check_win(board, rows, columns, num_connect, 1, 0, 'X')
    True
    >>> check_win(board, rows, columns, num_connect, 0, 0, 'X')
    False

    >>> board = create_board(rows, columns)
    >>> board = make_move(board, rows, columns, 0, 'X')[1]
    >>> board = make_move(board, rows, columns, 1, 'O')[1]
    >>> board = make_move(board, rows, columns, 1, 'X')[1]
    >>> check_win(board, rows, columns, num_connect, 0, 0, 'X')
    False
    >>> check_win(board, rows, columns, num_connect, 1, 0, 'X')
    True
    """
    diagonal_win = check_win_diagonal(board, max_rows, max_cols, num_connect,
                                      row, col, player)
    row_win = check_win_row(board, max_rows, max_cols, num_connect, row, player)
    column_win = check_win_column(board, max_rows, max_cols, num_connect, col, player)


    if row_win or column_win or diagonal_win:
        return True
    else:
        return False    


##########################################################
### Функции для решения задач, которые не надо трогать ###
##########################################################

def check_win_diagonal(board, max_rows, max_cols, num_connect, row, col, player):
    """ 
    Возвращает True, если победная диагональ заданного игрока проходит через поле
    (row, column), иначе False.
    """
    # Находит верхнее левое начало потенциально победной диагонали.
    adjacent = 0
    row_top_left, col_top_left = row, col
    while row_top_left > 0 and col_top_left > 0:
        row_top_left -= 1
        col_top_left -= 1

    # Проходит по диагонали вниз направо.
    while row_top_left < max_rows and col_top_left < max_cols:
        piece = get_piece(board, row_top_left, col_top_left)
        if piece == player:
            adjacent += 1
        else:
            adjacent = 0
        if adjacent >= num_connect:
            return True
        row_top_left += 1
        col_top_left += 1

    # Находит верхнее правое начало потенциально победной диагонали.
    adjacent = 0
    row_top_right, col_top_right = row, col
    while row_top_right > 0 and col_top_right < max_cols - 1:
        row_top_right -= 1
        col_top_right += 1

    # Проходит по диагонали вниз налево.
    while row_top_right < max_rows and col_top_right >= 0:
        piece = get_piece(board, row_top_right, col_top_right)
        if piece == player:
            adjacent += 1
        else:
            adjacent = 0
        if adjacent >= num_connect:
            return True
        row_top_right += 1
        col_top_right -= 1

    return False

###################################################################################
### Читать и понимать, что написано ниже, не нужно. Там только игровая механика. ###
###################################################################################

import sys

def other(player):
    """ Возвращает другого игрока.
    """
    if player == 'X':
        return 'O'
    return 'X'

def play(board, max_rows, max_cols, num_connect):
    max_turns = max_rows * max_cols
    print("\nИгрок 'X' начинает")
    who = 'X'
    turns = 0

    while True:
        turns += 1
        if turns > max_turns:
            print("\nНет ходов. Ничья!")
            sys.exit()

        while True:
            try:
                col_index = int(input('\nКакой столбец, игрок {}? '.format(who)))
            except ValueError as _:
                print('Неверный ввод. Попробуй ещё.')
                continue

            row_index, board = make_move(board, max_rows, max_cols, col_index, who)

            if row_index != -1:
                break

            print("Упс, сюда сунуть фишку никак")

        print_board(board, max_rows, max_cols)

        if check_win(board, max_rows, max_cols, num_connect, row_index, col_index, who):
            print("\nИгрок {} победил!".format(who))
            sys.exit()

        who = other(who)

def start_game():
    # Получаем все условия игры от пользователя.
    while True:
        # Получаем num_connect от пользователя.
        while True:
            try:
                num_connect = int(input('Размер соединения (то есть 4 для «Четыре в ряд»)? '))
            except ValueError as _:
                print('Неверный ввод. Попробуй ещё.')
                continue
            break

        # Получаем количество строк на доске.
        while True:
            try:
                 max_rows = int(input('Сколько строк? '))
            except ValueError as _:
                print('Неверный ввод. Попробуй ещё.')
                continue
            break

        # Получаем количество столбцов на доске.
        while True:
            try:
                max_cols = int(input('Сколько столбцов? '))
            except ValueError as _:
                print('Неверный ввод. Попробуй ещё.')
                continue
            break

        if max_rows >= num_connect or max_cols >= num_connect:
            break
        print("Неверный размер для минимального соединения {0}. Попробуй ещё.".format(num_connect))

    board = create_board(max_rows, max_cols)
    play(board, max_rows, max_cols, num_connect)

if __name__ == '__main__':
    import doctest, sys
    finder = doctest.DocTestFinder()
    runner = doctest.DocTestRunner(doctest.OutputChecker(), optionflags=doctest.FAIL_FAST)
    doctest.OutputChecker.output_difference = lambda a, b, c, d: ""
    m = sys.modules.get('__main__')
    for test in finder.find(m, m.__name__):
        if test.name == '__main__': continue
        if test.name.split('.')[1][:2] != '_q': continue
        for example in test.examples: example.options[doctest.SKIP] = False
        if  runner.run(test).failed != 0: break