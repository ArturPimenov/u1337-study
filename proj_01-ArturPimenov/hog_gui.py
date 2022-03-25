"""Графический интерфейс (GUI) для игры в Свинью.

В файле могут встретиться возможности Python, выходящие за рамки курса.
"""

from tkinter import *
import argparse
import sys
import tkinter as tk

import hog
import dice


##########################
# Вспомогательные классы #
##########################

class BetterWidget(object):
    """Возвращает себя при вызовах pack и config для цепоки вызовов."""
    def pack(self, **kwargs):
        super().pack(**kwargs)
        return self

    def config(self, **kwargs):
        super().config(**kwargs)
        return self

class TextWidget(BetterWidget):
    """Содержит изменяемую строку текста."""
    def __init__(self, **kwargs):
        self.textvar = kwargs.get('textvariable', tk.StringVar())
        self.config(textvariable=self.textvar)
        if 'text' in kwargs:
            self.textvar.set(kwargs['text'])

    @property
    def text(self):
        return self.textvar.get()

    @text.setter
    def text(self, value):
        return self.textvar.set(str(value))

class Text(tk.Text):
    """Текстовое поле."""
    def __init__(self, parent, **kwargs):
        kwargs.update(text_theme)
        tk.Text.__init__(self, parent, **kwargs)

class Label(TextWidget, tk.Label):
    """Текстовая метка."""
    def __init__(self, parent, **kwargs):
        kwargs.update(label_theme)
        tk.Label.__init__(self, parent, **kwargs)
        TextWidget.__init__(self, **kwargs)

class Button(BetterWidget, tk.Button):
    """Интерактивная кнопка."""
    def __init__(self, *args, **kwargs):
        kwargs.update(button_theme)
        tk.Button.__init__(self, *args, **kwargs)

class Entry(TextWidget, tk.Entry):
    """Виджет ввода текста."""
    def __init__(self, parent, **kwargs):
        kwargs.update(entry_theme)
        tk.Entry.__init__(self, parent, **kwargs)
        TextWidget.__init__(self, **kwargs)

class Frame(BetterWidget, tk.Frame):
    """Контейнер для других виджетов."""
    def __init__(self, *args, **kwargs):
        kwargs.update(frame_theme)
        tk.Frame.__init__(self, *args, **kwargs)

class IORedirector(object):
    """Общий класс для перенаправления ввода/вывода в текстовое поле."""
    def __init__(self, text_area):
        self.text_area = text_area

class StdoutRedirector(IORedirector):
    """Класс для перенаправления stdout в текстовое поле."""
    def write(self, text):
        self.text_area.insert(END, text)
        self.text_area.see(END)

    def flush(self):
        pass  # Пустая инструкция для предотвращения креша
              # (https://stackoverflow.com/a/43014145).

def name(who):
    """Возвращает имя игрока."""
    return "Игрок {0}".format(who)

#######
# GUI #
#######

class HogGUIException(BaseException):
    """Особое HogGUI-исключение. Используется для досрочного выхода из игры."""
    pass

class HogGUI(Frame):
    """Графический интерфейс игры на Tkinter."""

    KILL = -9   # сигнал kill для останова игры

    ##########################
    # Инициализация виджетов #
    ##########################

    def __init__(self, parent, computer=False):
        """Заменяет dice из модуля hog на версию с GUI-хуками и запускает игру.

        parent   — родительский виджет (должен быть корнем root)
        computer — True, если игра против компьютера
        """
        super().__init__(parent)
        self.pack(fill=BOTH)
        self.parent = parent
        self.who = 0

        self.init_scores()
        self.init_rolls()
        self.init_dice()
        self.init_status()
        self.init_messages()
        self.init_restart()

        self.computer, self.turn = computer, 0
        self.play()

    def init_scores(self):
        """Создаёт дочерние виджеты для подсчёта очков.

        У каждого игрока имеется метка Label для показа количества очков,
        которая обновляется каждый ход. Количество очков может быть получено и
        изменено через переменные Tkinter в self.score_vars.
        """
        self.score_frame = Frame(self).pack()

        self.p_frames = [None, None]
        self.p_labels = [None, None]
        self.s_labels = [None, None]
        for i in (0, 1):
            self.p_frames[i] = Frame(self.score_frame, padx=25).pack(side=LEFT)
            self.p_labels[i] = Label(self.p_frames[i],
                        text=name(i) + ':').pack()
            self.s_labels[i] = Label(self.p_frames[i]).pack()

    def init_rolls(self):
        """Создаёт родительские виджеты для показа количества бросков.

        Основной виджет — Entry — для ввода текста. Значение промежуточной
        Tkinter-переменной self.roll_verified устанавливается в соответствии с
        количеством бросков. Как только значение переменной обновляется — игрок
        немедленно совершает ход, основываясь на этом значении.
        """
        self.roll_frame = Frame(self).pack()

        self.roll_label = Label(self.roll_frame).pack()
        self.roll_entry = Entry(self.roll_frame,
                                justify=CENTER).pack()
        self.roll_entry.bind('<Return>',
                             lambda event: self.roll_button.invoke())
        self.roll_verified = IntVar()
        self.roll_button = Button(self.roll_frame,
                                  text='Бросок!',
                                  command=self.roll).pack()

    def init_dice(self):
        """
        Создаёт дочерние виджеты для отображения игральных костей. Каждая
        игральная кость хранится в объекте Label. Объекты Label могут быть
        «запакованы» или «распакованы» в зависимости от количества брошенных
        костей.
        """
        self.dice_frames = [
            Frame(self).pack(),
            Frame(self).pack(),
            Frame(self).pack(),
            Frame(self).pack()
        ]
        self.dice = {
            i: Label(self.dice_frames[i//5]).
                    config(image=HogGUI.IMAGES[6]).
                    pack(side=LEFT)
            for i in range(10)
        }

    def init_status(self):
        """Создаёт дочерние виджеты для отображения игрового состояния.
        Например, для отображения надписи «Дикий кабан»."""
        self.status_label = Label(self).pack()

    def init_messages(self):
        """Создаёт дочерние виджеты для вывода сообщений."""
        self.messages = Text(self)
        self.messages.pack()
        sys.stdout = StdoutRedirector(self.messages)

    def init_restart(self):
        """Создаёт дочерние виджеты для перезапуска игры."""
        self.restart_button = Button(self, text='Заново!',
                                     command=self.restart).pack()

    ##################
    # Игровая логика #
    ##################

    def make_dice(self, sides):
        """Создаёт функцию dice с GUI-хуками и обёртывает dice.make_fair_dice.

        sides — количество сторон у кости
        """
        fair_dice = dice.make_fair_dice(sides)
        def gui_dice():
            """Делает бросок fair_dice и выставляет соответствующее изображение
            в self.dice."""
            result = fair_dice()
            img = HogGUI.IMAGES[result]
            self.dice[self.dice_count].config(image=img).pack(side=LEFT)
            self.dice_count += 1
            return result
        return gui_dice

    def clear_dice(self):
        """Распаковывает (прячет) все метки игральных костей."""
        for i in range(10):
            self.dice[i].pack_forget()

    def clear_messages(self):
        self.messages.delete(1.0, END)

    def roll(self):
        """Проверяет и устанавливает количество бросков на основании ввода
        пользователя. В соответствии с правилами игры корректным значением
        является неотрицательное целое число.
        """
        self.clear_messages()
        result = self.roll_entry.text
        try:
            rolls = 10 >= int(result) >= 0
            assert rolls, 'Значение должно быть между 0 и 10 включительно.'
            self.roll_verified.set(int(result))
        except (ValueError, AssertionError) as e:
            print(e)

    def switch(self, who=None):
        """Меняет игроков. Значение self.who либо 0, либо 1."""
        self.p_frames[self.who].config(bg=bg)
        self.p_labels[self.who].config(bg=bg)
        self.s_labels[self.who].config(bg=bg)
        self.who = 1 - self.who if who is None else who
        self.p_frames[self.who].config(bg=select_bg)
        self.p_labels[self.who].config(bg=select_bg)
        self.s_labels[self.who].config(bg=select_bg)

    def strategy(self, score, opp_score):
        """Стратегия с GUI-хуком. Эта стратегия передаётся в функцию play модуля
        hog. Стратегия ожидает ввода числа бросков, его проверки и возврат этого
        числа. Игровая информация также обновляется.

        score     — очки игрока
        opp_score — очки противника
        """
        s0 = score if self.who == 0 else opp_score
        s1 = opp_score if self.who == 0 else score
        self.s_labels[0].text = s0
        self.s_labels[1].text = s1
        self.roll_label.text = 'Ходит {0}. Число костей:'.format(name(self.who))
        status = self.status_label.text
        self.status_label.text = status

        if self.computer and self.who == self.turn:
            self.update()
            self.after(DELAY)
            result = hog.final_strategy(score, opp_score)
        else:
            self.roll_entry.focus_set()
            self.wait_variable(self.roll_verified)
            result = self.roll_verified.get()
            self.roll_entry.text = ''
        if result == HogGUI.KILL:
            raise HogGUIException

        self.clear_dice()
        self.dice_count = 0
        self.status_label.text = '{} использовал {} костей (кость).'.format(name(self.who),
                                                               result)
        self.switch()
        return result

    def play(self):
        """Симулирует игру в Свинью, вызывая hog.play с GUI-стратегиями.

        Если игрок внезапно закрывает окно (например в середине игры), то
        поднимается HogGUIException для выхода из игрового цикла.

        В противном случае при уничтожении виджета стратегия продолжила бы
        ожидание.
        """
        self.turn = 1 - self.turn
        self.switch(0)
        self.s_labels[0].text = '0'
        self.s_labels[1].text = '0'
        self.status_label.text = ''
        try:
            commentary = hog.both(hog.announce_highest(0),
                         hog.both(hog.announce_highest(1),
                                  hog.announce_lead_changes()))
            score, opponent_score, _ = trace_play(hog.play, self.strategy,
                                                  self.strategy,
                                                  score0=0,
                                                  score1=0,
                                                  dice=self.make_dice(6),
                                                  goal=100,
                                                  say=commentary,
                                                  feral_hogs=True)
        except HogGUIException:
            pass
        else:
            self.s_labels[0].text = score
            self.s_labels[1].text = opponent_score
            winner = 0 if score > opponent_score else 1
            self.status_label.text = 'Игра окончена! {} победил!'.format(
                                        name(winner))

    def restart(self):
        """Уничтожает текущую игру и запускает новую."""
        self.roll_verified.set(HogGUI.KILL)
        self.status_label.text = ''
        self.clear_dice()
        self.clear_messages()
        self.play()

    def destroy(self):
        """Переопределяет метод destroy для завершения текущей игры."""
        self.roll_verified.set(HogGUI.KILL)
        super().destroy()

def trace_play(play, strategy0, strategy1, score0, score1, dice, goal, say, feral_hogs):
    """Обёртывает пользовательскую функцию play и
        (1) удостоверяет, что strategy0 и strategy1 вызываются единственный раз
            за ход
        (2) записывает последовательность ходов в виде списка словарей, каждый
            из которых имеет ключи "s0_start", "s1_start", "who", "num_dice",
            "dice_values"

    Возвращает (s0, s1, trace), где s0, s1 — это возвращаемые значения из play,
    а trace — это последовательность ходов в указанном выше виде.
    """
    game_trace = []

    def mod_strategy(who, my_score, opponent_score):
        if game_trace:
            prev_total_score = game_trace[-1]["s0_start"] + game_trace[-1]["s1_start"]
            if prev_total_score == my_score + opponent_score:
                # игра всё ещё на последнем ходу, поскольку общее число баллов
                # растёт каждый ход
                return game_trace[-1]["num_dice"]
        current_num_dice = (strategy0, strategy1)[who](my_score, opponent_score)
        current_turn = {
            "s0_start" : [my_score, opponent_score][who],
            "s1_start" : [my_score, opponent_score][1 - who],
            "who" : who,
            "num_dice" : current_num_dice,
            "dice_values" : [] # кости ещё не брошены
        }
        game_trace.append(current_turn)
        return current_num_dice

    def mod_dice():
        roll = dice()
        if not game_trace:
            raise RuntimeError("roll_dice вызвана до функции strategy")
        game_trace[-1]["dice_values"].append(roll)
        return roll

    s0, s1 = play(
        lambda a, b: mod_strategy(0, a, b),
        lambda a, b: mod_strategy(1, a, b),
        score0,
        score1,
        dice=mod_dice,
        goal=goal,
        say=say,
        feral_hogs=feral_hogs)

    return s0, s1, game_trace

def run_GUI(computer=False):
    """Запуск графического интерфейса.

    computer — True означает игру против компьютера
    """
    root = Tk()
    root.title('Игра в Свинью')
    root.minsize(520, 600)
    root.geometry("520x600")

    # Tkinter работает только GIF'ками
    HogGUI.IMAGES = {
        1: PhotoImage(file='images/die1.gif'),
        2: PhotoImage(file='images/die2.gif'),
        3: PhotoImage(file='images/die3.gif'),
        4: PhotoImage(file='images/die4.gif'),
        5: PhotoImage(file='images/die5.gif'),
        6: PhotoImage(file='images/die6.gif'),
    }

    app = HogGUI(root, computer)
    root.mainloop()

########
# ТЕМЫ #
########

select_bg = '#a6d785'
bg='#ffffff'
fg='#000000'
font=('Arial', 14)
height=5

frame_theme = {
    'bg': bg,
}

label_theme = {
    'font': font,
    'bg': bg,
    'fg': fg,
}

text_theme = {
    'font': font,
    'bg': bg,
    'fg': fg,
    'height': height,
}

button_theme = {
    'font': font,
    'activebackground': select_bg,
    'bg': bg,
    'fg': fg,
}

entry_theme = {
    'fg': fg,
    'bg': bg,
    'font': font,
    'insertbackground': fg,
}

##############################
# Интерфейс командной строки #
##############################

DELAY=2000

def run(*args):
    parser = argparse.ArgumentParser(description='GUI-Свинья')
    parser.add_argument('-f', '--final',
                        help='игра против финальной стратегии из hog.py. '
                             'Компьютер играет за обоих игроков.',
                        action='store_true')
    parser.add_argument('-d', '--delay',
                        help='задержка хода игрока в секундах', type=int,
                        default=2)
    args = parser.parse_args()
    global DELAY
    DELAY = args.delay * 1000
    run_GUI(computer=args.final)

if __name__ == '__main__':
    import sys
    args = sys.argv[1:]
    run(*args)