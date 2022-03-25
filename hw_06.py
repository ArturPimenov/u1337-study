class Fib():
    """Число Фибоначчи.

    >>> start = Fib()
    >>> start
    0
    >>> start.next()
    1
    >>> start.next().next()
    1
    >>> start.next().next().next()
    2
    >>> start.next().next().next().next()
    3
    >>> start.next().next().next().next().next()
    5
    >>> start.next().next().next().next().next().next()
    8
    >>> start.next().next().next().next().next().next() # Проверка, что start не изменился
    8
    """

    def __init__(self, value=0, p_value=0):
        self.value = value
        self.p_value = p_value

    def next(self):
        return Fib(1) if self.value == 0 else Fib(self.value + self.p_value, self.value)      

    def __repr__(self):
        return str(self.value)

class VendingMachine:
    """Торговый автомат, продающий некоторый товар по некоторой цене.
    
    >>> v = VendingMachine('яблоко', 10)
    >>> v.vend()
    'Товара нет в наличии.'
    >>> v.restock(2)
    'Количество товара «яблоко»: 2'
    >>> v.vend()
    'Нужно дополнительно внести 10 ₽.'
    >>> v.deposit(7)
    'Доступно: 7 ₽'
    >>> v.vend()
    'Нужно дополнительно внести 3 ₽.'
    >>> v.deposit(5)
    'Доступно: 12 ₽'
    >>> v.vend()
    'Получите яблоко и сдачу 2 ₽.'
    >>> v.deposit(10)
    'Доступно: 10 ₽'
    >>> v.vend()
    'Получите яблоко.'
    >>> v.deposit(15)
    'Товара нет в наличии. Вот твои деньги — 15 ₽.'

    >>> w = VendingMachine('лимонад', 2)
    >>> w.restock(3)
    'Количество товара «лимонад»: 3'
    >>> w.restock(3)
    'Количество товара «лимонад»: 6'
    >>> w.deposit(2)
    'Доступно: 2 ₽'
    >>> w.vend()
    'Получите лимонад.'
    """
    def __init__(self, name, price, amount=0):
        self.name = name
        self.price = price
        self.amount = amount
        self.money = 0

    def restock(self, quantity):
        self.amount += quantity
        return 'Количество товара «{0}»: {1}'.format(self.name, self.amount)

    def deposit(self, add_money):
        self.money += add_money
        if self.amount == 0:
            self.money = 0
            return 'Товара нет в наличии. Вот твои деньги — {} ₽.'.format(add_money)
        else:
            return 'Доступно: {} ₽'.format(self.money)

    def vend(self):
        if self.amount == 0 and self.money == 0:
            return 'Товара нет в наличии.'

        elif self.money < self.price:
            return 'Нужно дополнительно внести {} ₽.'.format(self.price - self.money)
        elif self.money == self.price:
            self.amount -= 1
            return 'Получите {}.'.format(self.name)
        else:
            self.amount -= 1
            change = self.money - self.price
            self.money = 0
            return 'Получите {0} и сдачу {1} ₽.'.format(self.name, change)
                
                   

