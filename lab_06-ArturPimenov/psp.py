from car import Car, MonsterTruck

def _q_01():
    """
    ============================================================================
    Часть 1
    ----------------------------------------------------------------------------
    >>> apalkoff_car = Car('Tesla', 'Model S')                  # doctest: +SKIP
    >>> apalkoff_car.color                                      # doctest: +SKIP
    'Без цвета. Покрась меня.'

    >>> apalkoff_car.paint('чёрный')                            # doctest: +SKIP
    'Цвет Tesla Model S теперь чёрный'

    >>> apalkoff_car.color                                      # doctest: +SKIP
    'чёрный'

    ============================================================================
    Часть 2
    ----------------------------------------------------------------------------
    >>> apalkoff_car = Car('Tesla', 'Model S')                  # doctest: +SKIP
    >>> apalkoff_car.model                                      # doctest: +SKIP
    'Model S'

    >>> apalkoff_car.gas = 10                                   # doctest: +SKIP
    >>> apalkoff_car.drive()                                    # doctest: +SKIP
    'Tesla Model S делает врум-врум!'

    >>> apalkoff_car.drive()                                    # doctest: +SKIP
    'Tesla Model S не может ехать!'

    >>> apalkoff_car.fill_gas()                                 # doctest: +SKIP
    'Количество бензина в Tesla Model S: 20'

    >>> apalkoff_car.gas                                        # doctest: +SKIP
    20

    >>> Car.gas                                                 # doctest: +SKIP
    30

    ============================================================================
    Часть 3
    ----------------------------------------------------------------------------
    >>> Car.headlights                                          # doctest: +SKIP
    2

    >>> apalkoff_car.headlights                                 # doctest: +SKIP
    2

    >>> Car.headlights = 3                                      # doctest: +SKIP
    >>> apalkoff_car.headlights                                 # doctest: +SKIP
    3

    >>> apalkoff_car.headlights = 2                             # doctest: +SKIP
    >>> Car.headlights                                          # doctest: +SKIP
    3

    ============================================================================
    Часть 4
    ----------------------------------------------------------------------------
    >>> apalkoff_car.wheels = 2                                 # doctest: +SKIP
    >>> apalkoff_car.wheels                                     # doctest: +SKIP
    2

    >>> Car.num_wheels                                          # doctest: +SKIP
    4

    >>> apalkoff_car.drive()                                    # doctest: +SKIP
    'Tesla Model S не может ехать!'

    >>> Car.drive()                                             # doctest: +SKIP
    Traceback (most recent call last):
      File "C:\Python39\lib\doctest.py", line 1336, in __run
        exec(compile(example.source, filename, "single",
      File "<doctest __main__._q_01[22]>", line 1, in <module>
        Car.drive()                                             # doctest: +SKIP
    TypeError: drive() missing 1 required positional argument: 'self'

    >>> Car.drive(apalkoff_car)                                 # doctest: +SKIP
    'Tesla Model S не может ехать!'

    ============================================================================
    Часть 5
    ----------------------------------------------------------------------------
    >>> apalkoff_car = MonsterTruck('Монстр', 'Бэтмобиль')      # doctest: +SKIP
    >>> apalkoff_car.drive()                                    # doctest: +SKIP
    ДРЫН-ДЫН-ДЫН! Этот монстр-трак просто огромный!
    'Монстр Бэтмобиль делает врум-врум!'
    >>> Car.drive(apalkoff_car)                                 # doctest: +SKIP
    'Монстр Бэтмобиль делает врум-врум!'

    >>> MonsterTruck.drive(apalkoff_car)                        # doctest: +SKIP
    ДРЫН-ДЫН-ДЫН! Этот монстр-трак просто огромный!
    'Монстр Бэтмобиль делает врум-врум!'

    >>> Car.rev(apalkoff_car)                                   # doctest: +SKIP
    Traceback (most recent call last):
      File "C:\Python39\lib\doctest.py", line 1336, in __run
        exec(compile(example.source, filename, "single",
      File "<doctest __main__._q_01[28]>", line 1, in <module>
        Car.rev(apalkoff_car)                                   # doctest: +SKIP
    AttributeError: type object 'Car' has no attribute 'rev'
    """
    return 0

# Ниже этого места трогать ничего не нужно.

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