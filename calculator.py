import os

helper = ['+','-','*','**','/','+-','abs',""]
def in_put():
    while True:
        try:
            t = int(input('Введите число: '))
        except:
            print('Вы ввели не число, в следующий раз вводите число')
            continue
        break
    return t

plus = lambda n,t: n + t
minus = lambda n,t: n - t
power = lambda n,t: n ** t
multiplication = lambda n,t: n * t
division = lambda n,t: n / t

print('''
Калькулятор для базовых оперций.
      Инструкция по вводу.
1.Вводите первое число больше 0 - enter
2.Выбираете операцию(если вам изначально надо было отрицательное число, меняете знак) - enter
3.При необходимости вводите число для операции - enter
4.Вы считаете новое число и снова выбираете операцию (2.)
''')
input('Для продолженя нажмите enter')
os.system("cls")

n = in_put()
os.system("cls")
while True:
    os.system("cls")
    print(f'Число - {n} ')
    while True:
        operation = input('''
    Выберете операцию или введите число:
    '+' - сложение
    '-' - вычитание 
    '*' - умножение
    '/' - деление
    '**' - возведение в стемень
    '+-' - смена знака числа
    'abs' - модуль числа
    Пустой ввод - выход
    ''')
        if operation not in helper:
            print('Вы выбрали несуществующую операцию. Попробуйте еще раз!')
            input('Для продолженя нажмите enter')
            continue
        break
    if operation == '+':
        t = in_put()
        n = plus(n,t)
    if operation == '-':
        t = in_put()
        n = minus(n,t)
    if operation == '*':
        t = in_put()
        n = multiplication(n,t)
    if operation == '/':
        while True:
            try:
                t = in_put()
                n = division(n,t)
            except:
                print('Деление на 0, так не прокатит, давайка другое число')
                continue
            break
    if operation == '**':
        t = in_put()
        n = power(n,t)
    if operation == '+-':
        n = -n
    if operation == 'abs':
        n = abs(n)
    if operation == '':
        print('Goodbye!')
        break
    os.system("cls")

