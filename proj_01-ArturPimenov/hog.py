"""Игра в Свинью."""

from dice import six_sided, four_sided, make_test_dice
from operator import mul

GOAL_SCORE = 100  # Цель игры — набрать 100 очков.

######################
# Часть 1: Симулятор #
######################


def roll_dice(num_rolls, dice=six_sided):
    """Симулирует бросание игральной кости DICE в точности NUM_ROLLS > 0 раз.
    Возвращает либо сумму результатов, либо 1, если хоть раз выпала 1.

    num_rolls:  Число бросков кости, которые нужно сделать.
    dice:       Функция без аргументов, возвращает результат отдельного броска.
    
    >>> roll_dice(4, make_test_dice(2,2,2,2))
    8
    """
    # Эти assert-инструкции проверяют, что num_rolls является положительным
    # целым.
    assert type(num_rolls) == int, 'Значение num_rolls должно быть целым.'
    assert num_rolls > 0, 'Значение num_rolls должно быть больше нуля.'
    # НАЧАЛО ЗАДАЧИ 1

    index, total, is_bool, current_dice = 1, 0, False, 0
    # total - сумма очков за один бросок num_rolls костей
    # is_bool - булевая переменная, которая проверяет один бросок кости dice для правила "Обжора"
    # current_dice - результат броска одной кости (нужна для is_bool)

    while index <= num_rolls:
        current_dice = dice()
        if current_dice == 1:
           is_bool = True 
        total += current_dice
        index += 1
    return total if is_bool == False else 1    


    # КОНЕЦ ЗАДАЧИ 1


def free_bacon(score):
    """Возвращает количество очков от броска 0 костей (Халявный бекон).

    score:  Текущие очки противника.
    >>> free_bacon(7)
    10
    >>> free_bacon(12)
    9
    """
    assert score < 100, 'Игра должна быть завершена.'
    # НАЧАЛО ЗАДАЧИ 2
    return 10 - min(score % 10, score // 10)
    # КОНЕЦ ЗАДАЧИ 2


def take_turn(num_rolls, opponent_score, dice=six_sided):
    """Симуляция хода с NUM_ROLLS бросками кости DICE, значение num_rolls может
    быть равно нулю (Халявный бекон). Возвращает количество очков, полученное
    текущим игроком за ход.

    num_rolls:       Число бросков кости, которые нужно сделать.
    opponent_score:  Количество очков противника.
    dice:            Функция без аргументов, возвращает результат одного броска.
    
    >>> take_turn(4, 10, make_test_dice(5, 4, 3, 2))
    14
    >>> take_turn(0, 65, make_test_dice(4, 3, 2, 1))
    5
    """
    # Не трогай эти ассерты, они помогают отыскивать ошибки.
    assert type(num_rolls) == int, 'Значение num_rolls должно быть целым.'
    assert num_rolls >= 0, 'Невозможно бросить кость отрицательное количество раз в take_turn.'
    assert num_rolls <= 10, 'Невозможно бросить кость более 10 раз.'
    assert opponent_score < 100, 'Игра должна быть завершена.'
    # НАЧАЛО ЗАДАЧИ 2
    return roll_dice(num_rolls, dice) if num_rolls else free_bacon(opponent_score)
    # КОНЕЦ ЗАДАЧИ 2

def mul_scores_for_swap(player_score):
    """
    Принимает очки одного игрока, возвращает - перемноженное значение крайних цифр очков

    >>> mul_scores_for_swap(123)
    3
    >>> mul_scores_for_swap(2)
    4
    """
    return mul(player_score // (10 ** (len(str(player_score)) - 1)), player_score % 10)

def is_swap(player_score, opponent_score):
    """
    Проверяет, что очки игроков должны поменяться местами.
    
    >>> is_swap(124, 2)
    True
    >>> is_swap(100, 15)
    False
    >>> is_swap(22, 2)
    True
    """
    # НАЧАЛО ЗАДАЧИ 4
    return mul_scores_for_swap(player_score) == mul_scores_for_swap(opponent_score)
    # КОНЕЦ ЗАДАЧИ 4

def is_mhn_xr(num_rolls0, num_rolls):
    """
    Функция, которая проверяет правило Мохнатых хрюшек

    num_rools0 - количество бросаемых костей в предыдущем ходе игрока x
    num_rools - количество бросаемых костей на данном ходе игрока x

    >> is_mhn_xr(0, 2)
    True
    >> is_mhn_xr(4, 2)
    True
    >> is_mhn_xr(1, 5)
    False
    """
    if num_rolls - 2 == num_rolls0 or num_rolls + 2 == num_rolls0:
        return True 
    return False    


def other(player):
    """Возвращает индекс противника, допустимые значения PLAYER: 0 и 1.

    >>> other(0)
    1
    >>> other(1)
    0
    """
    return 1 - player


def silence(score0, score1):
    """Ничего не сообщает (смотри Часть 2)."""
    return silence


def play(strategy0, strategy1, score0=0, score1=0, dice=six_sided,
         goal=GOAL_SCORE, say=silence, feral_hogs=True):
    """Cимулирует игру в Свинью и возвращает итоговые очки
    для обоих игроков: сначала очки игрока «0», затем очки игрока «1».

    Функция strategy принимает очки обоих игроков (текущего игрока и противника)
    и возвращает количество бросков для текущего игрока в этом ходе.

    strategy0:  Стратегия игрока 0, он ходит первым.
    strategy1:  Стратегия игрока 1, он ходит вторым.
    score0:     Начальное количество очков игрока 0.
    score1:     Начальное количество очков игрока 1.
    dice:       Функция без аргументов, возвращает результат отдельного броска.
    goal:       Игра заканчивается и кто-то побеждает при достижении этого количества очков.
    say:        Функция-комментарий для вызова в конце первого хода.
    feral_hogs: Булева величина, указывающая на включение правила Мохнатых хрюшек.
    """
    player = 0  # Хранит информацию о том, чей ход; игрока 0 или игрока 1.
    # НАЧАЛО ЗАДАЧИ 5

    #Количество костей игроков, брошенных в предыдущем ходе (изначально равны 0)
    num_rolls0_0 = 0
    num_rolls1_0 = 0   

    #Подсчитывает количество ходов в игре (нужен только для того, чтобы программа в "условии для комментариев" понимала, что это не первый ход!)
    iter_moves = 1


    num_rolls = [num_rolls0_0, num_rolls1_0]
    score = [score0, score1]
    #Функция, которая эмитирует бросок костей игрока и возвращает очки за ход и количество бросаемых костей
    def player_move_for_score(int_identity_of_player):
        if int_identity_of_player == 0:
            num_rolls = strategy0(score[0], score[1])
            score_in_the_move = take_turn(num_rolls, score[1], dice)
        else:
            num_rolls = strategy1(score[1], score[0])
            score_in_the_move = take_turn(num_rolls, score[0], dice)
        return score_in_the_move, num_rolls    


    while score[0] < goal and score[1] < goal:
        move, this_move_num_rolls = player_move_for_score(player)
        if is_mhn_xr(num_rolls[player], this_move_num_rolls) and feral_hogs:
            move += 3

        score[player] += move  

        if is_swap(score[0], score[1]):
            score[0], score[1] = score[1], score[0]

        num_rolls[player] = this_move_num_rolls    
        player = other(player) 
      
    # КОНЕЦ ЗАДАЧИ 5
    # (кстати, отступ для решения задачи 6 может быть недостаточным)
    # НАЧАЛО ЗАДАЧИ 6

        say = say(score[0], score[1])    
    # КОНЕЦ ЗАДАЧИ 6

        score0, score1 = score[0], score[1]
    return score0, score1


########################
# Часть 2: Комментарии #
########################


def say_scores(score0, score1):
    """Сообщает текущий счёт каждого игрока."""
    print("Игрок 0 набрал", score0, "очков, а Игрок 1 набрал", score1)
    return say_scores

def announce_lead_changes(previous_leader=None):
    """Возвращает функцию, которая сообщает о смене лидера.

    >>> f0 = announce_lead_changes()
    >>> f1 = f0(5, 0)
    Игрок 0 вырвался вперёд на 5
    >>> f2 = f1(5, 12)
    Игрок 1 вырвался вперёд на 7
    >>> f3 = f2(8, 12)
    >>> f4 = f3(8, 13)
    >>> f5 = f4(15, 13)
    Игрок 0 вырвался вперёд на 2
    """
    def say(score0, score1):
        if score0 > score1:
            leader = 0
        elif score1 > score0:
            leader = 1
        else:
            leader = None
        if leader != None and leader != previous_leader:
            print('Игрок', leader, 'вырвался вперёд на', abs(score0 - score1))
        return announce_lead_changes(leader)
    return say

def both(f, g):
    """Выводит два сообщения — первое с помощью f, второе с помощью g.

    NOTE: Следующие примеры не могут иметь место в реальной игре, это
    просто доктесты.

    >>> h0 = both(say_scores, announce_lead_changes())
    >>> h1 = h0(10, 0)
    Игрок 0 набрал 10 очков, а Игрок 1 набрал 0
    Игрок 0 вырвался вперёд на 10
    >>> h2 = h1(10, 6)
    Игрок 0 набрал 10 очков, а Игрок 1 набрал 6
    >>> h3 = h2(6, 17)
    Игрок 0 набрал 6 очков, а Игрок 1 набрал 17
    Игрок 1 вырвался вперёд на 11
    """
    def say(score0, score1):
        return both(f(score0, score1), g(score0, score1))
    return say


def announce_highest(who, previous_high=0, previous_score=0):
    """Выводит сообщение, когда ход приносит максимальное за игру количество
    очков игроку WHO.

    NOTE: Следующие примеры не могут иметь место в реальной игре, это
    просто доктесты.

    >>> f0 = announce_highest(1) # Сообщает только об успехах Игрока 1
    >>> f1 = f0(12, 0)
    >>> f2 = f1(12, 11)
    11 очка(ов)! Лучший результат для Игрока 1
    >>> f3 = f2(20, 11)
    >>> f4 = f3(13, 20)
    >>> f5 = f4(20, 35)
    15 очка(ов)! Лучший результат для Игрока 1
    >>> f6 = f5(20, 47) # Игрок 1 получает 12 очков; недостаточно для рекорда
    >>> f7 = f6(21, 47)
    >>> f8 = f7(21, 77)
    30 очка(ов)! Лучший результат для Игрока 1
    >>> f9 = f8(77, 22) # Swap!
    >>> f10 = f9(33, 77) # Swap!
    55 очка(ов)! Лучший результат для Игрока 1
    """
    assert who == 0 or who == 1, 'Аргумент who должен идентифицировать игрока.'
    # НАЧАЛО ЗАДАЧИ 7
    def say_record(score0, score1):
        local_previous_high = previous_high
        if who == 0:
            now_score = score0
            if now_score - previous_score > local_previous_high:
                local_previous_high = now_score - previous_score
                print(local_previous_high, "очка(ов)! Лучший результат для Игрока", who)
        else:
            now_score = score1
            if now_score - previous_score > previous_high:
                local_previous_high = now_score - previous_score
                print(local_previous_high, "очка(ов)! Лучший результат для Игрока", who)
        
        return announce_highest(who, local_previous_high, now_score)
    return say_record        

    # КОНЕЦ ЗАДАЧИ 7


######################
# Часть 3: Стратегии #
######################


def always_roll(n):
    """Возвращает стратегию, в которой всегда бросается N костей.

    Стратегия — это функция, принимающая два аргумента: количество очков
    текущего игрока и количество очков противника. Возвращает число бросков
    костей для текущего хода игрока.

    >>> strategy = always_roll(5)
    >>> strategy(0, 0)
    5
    >>> strategy(99, 99)
    5
    """
    def strategy(score, opponent_score):
        return n
    return strategy


def make_averaged(fn, num_samples=1000):
    """Возвращает функцию, которая возвращает среднее значение от NUM_SAMPLES
    вызовов функции FN.

    Для создания этой функции потребуется использовать синтаксис *args, который
    не был рассмотрен на лекциях. Так что смотри описание проекта.

    >>> dice = make_test_dice(4, 2, 5, 1)
    >>> averaged_dice = make_averaged(dice, 1000)
    >>> averaged_dice()
    3.0
    """
    # НАЧАЛО ЗАДАЧИ 8
    def averaged_dice(*args):
        int_iter = 0
        result = 0.0
        while int_iter < num_samples:
            result += fn(*args)
            int_iter += 1
        return result / num_samples
    return averaged_dice
    # КОНЕЦ ЗАДАЧИ 8


def max_scoring_num_rolls(dice=six_sided, num_samples=1000):
    """Возвращает число бросков (от 1 до 10), которое приведет в среднем
    к максимальному количеству очков за ход. Функция многократно вызывает
    roll_dice с заданной костью DICE.
    Считай, что кость DICE всегда возвращает положительные результаты.

    >>> dice = make_test_dice(1, 6)
    >>> max_scoring_num_rolls(dice)
    1
    """
    # НАЧАЛО ЗАДАЧИ 9
    int_iter = 10
    result = 0
    min_dice = 0
    maximum = 0
    while int_iter >= 1:
        maximum = make_averaged(roll_dice, num_samples)(int_iter, dice)
        if maximum >= result:
            min_dice = int_iter
            result = maximum
        int_iter -= 1    
    return min_dice
    # КОНЕЦ ЗАДАЧИ 9


def winner(strategy0, strategy1):
    """Возвращает 0, если strategy0 выигрывает против strategy1, иначе 1."""
    score0, score1 = play(strategy0, strategy1)
    if score0 > score1:
        return 0
    else:
        return 1


def average_win_rate(strategy, baseline=always_roll(4)):
    """
    Возвращает усреднённую долю побед (от 0 до 1) стратегии STRATEGY против
    другой стратегии BASELINE. Усреднение учитывает, что начинает игру любая
    из стратегий.
    """
    win_rate_as_player_0 = 1 - make_averaged(winner)(strategy, baseline)
    win_rate_as_player_1 = make_averaged(winner)(baseline, strategy)

    return (win_rate_as_player_0 + win_rate_as_player_1) / 2


def run_experiments():
    """Запускает набор экспериментов со стратегией и выводит информацию
    о результатах."""
    if False:  # Измени на False, когда закончишь вопрос про max_scoring_num_rolls
        six_sided_max = max_scoring_num_rolls(six_sided)
        print('Наиболее выгодное количество бросков для шестигранной кости:', six_sided_max)

    if False:  # Измени на True для теста always_roll(6)
        print('Доля побед для always_roll(6):', average_win_rate(always_roll(6)))

    if False:  # Измени на True для теста bacon_strategy
        print('Доля побед для bacon_strategy:', average_win_rate(bacon_strategy))

    if False:  # Измени на True для теста swap_strategy
        print('Доля побед для swap_strategy:', average_win_rate(swap_strategy))

    if True:  # Измени на True для теста final_strategy
        print('Доля побед для final_strategy:', average_win_rate(final_strategy))

    "*** Тут можешь добавить дополнительные эксперименты, если хочешь ***"


def bacon_strategy(score, opponent_score, margin=8, num_rolls=4):
    """
    Эта стратегия запустит 0 костей, если можно получить по крайней мере
    MARGIN очков, в противном случае вернёт NUM_ROLLS.
    """
    # НАЧАЛО ЗАДАЧИ 10
    return 0 if free_bacon(opponent_score) >= margin else num_rolls  # Замени эту инструкцию
    # КОНЕЦ ЗАДАЧИ 10


def swap_strategy(score, opponent_score, margin=8, num_rolls=4):
    """Эта стратегия запустит 0 костей, если она сработала как выгодный
    переворот. Также она запустит 0 костей, если можно получить по крайней мере
    MARGIN очков и не использовать невыгодный переворот. Иначе запустит
    NUM_ROLLS костей.
    """
    # НАЧАЛО ЗАДАЧИ 11

    my_score = score + free_bacon(opponent_score)
    if my_score == opponent_score and (my_score-score)>=margin:
        return 0
    elif (is_swap(my_score, opponent_score) and opponent_score > my_score):
        return 0    
    elif not is_swap(my_score, opponent_score) and (my_score-score)>=margin:
        return 0
    else:
        return num_rolls    
            

    #return 0 if (is_swap((score + free_bacon(opponent_score)) == mul_scores_for_swap(opponent_score)) and score + free_bacon(opponent_score) >= margin) else num_rolls# Замени эту инструкцию
    #return 0 if is_swap(score + free_bacon(opponent_score), opponent_score) and opponent_score > score + free_bacon(opponent_score)
    # КОНЕЦ ЗАДАЧИ 11


def final_strategy(score, opponent_score):
    """Напиши краткое описание твоей финальной стратегии.

    *** ТВОЁ ОПИСАНИЕ ЗДЕСЬ ***
    """
    # НАЧАЛО ЗАДАЧИ 12
    return 4  # Замени эту инструкцию
    # КОНЕЦ ЗАДАЧИ 12

##############################
# Интерфейс командной строки #
##############################

# Учти: Функции в этой секции не должны меняться. Здесь используются возможности
#       Python выходящие за рамки курса.

def run(*args):
    """Считывает аргументы командной строки и вызывает соответствующие
    функции.

    Эта функция использует возможности Python выходящие за пределы курса.
    """
    import argparse
    parser = argparse.ArgumentParser(description="Игра в Свинью")
    parser.add_argument('--run_experiments', '-r', action='store_true',
                        help='Запускает эксперименты со стратегиями')

    args = parser.parse_args()

    if args.run_experiments:
        run_experiments()

if __name__ == '__main__':
    import sys
    args = sys.argv[1:]
    run(*args)