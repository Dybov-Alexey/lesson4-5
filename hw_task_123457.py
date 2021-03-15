from functools import reduce

def factorial(n):
    proiz = 1
    while n != 1:
        proiz *= n
        n -= 1
    return proiz

fact = lambda x: 1 if x == 0 else x * fact(x-1)

# n=int(input())
# print(reduce(lambda x,y:x*y,range(1,n+1)))
# a = lambda x,y:x*y,range(1,n+1)

def usealpha(stroka):
    stroka = str(stroka)
    print(f'Введенная строка: {stroka}')
    while len(stroka) != 0:
        print(f'Символ {stroka[0]} встречается {stroka.count(stroka[0])} раз(а)')
        stroka = stroka.replace(stroka[0],'')

useal = lambda str: [print(f'Символ {str[i]} встречается {str.count(str[i])} раз(а) ') for i in range(0,len(str))]

def usealpha():
    while True:
        try:
            n = int(input('''
    Выберете:
    1.Подсчет частоты вхождений символов в текст.
    2.Подсчета количества слов в тексте. 
    3.Посчета количества предложений в тексте.
    4.Выход.\n'''))
        except:
            print('Еще раз')
            continue
        if n == 1:
            stroka = str(input('Введите строку: '))
            while len(stroka) != 0:
                print(f'Символ {stroka[0]} встречается {stroka.count(stroka[0])} раз(а)')
                stroka = stroka.replace(stroka[0],'')
        if n == 2:
            stroka = str(input('Введите текст: '))
            helper = stroka.split(' ' or '\n')
            print(len(helper))
        if n == 3:
            stroka = str(input('Введите текст: '))
            helper = stroka.split('.' or '!' or '?')#только не работает с ! ?
            for i in range(1,len(helper)):
                if helper[i][len(helper[i])-1].isupper():
                    helper.pop(i)
            print(len(helper))
        if n == 4:
            print('Goodbye!')
            break
    
def bank():
    while True:
        try:
            how = int(input('''
    Сколько взнос?\n
    '''))   
            proc = int(input('''
    Сколько процент?\n
    '''))
            date = int(input('''
    На сколько месяцев?\n
    '''))
        except:
            print('Еще раз')
            continue
        break
    print(f'К {date} ваша сумма будет равна {rec(how,proc,date)} ')

def rec(how,proc,date):
    if date == 1:
        how = how * (proc/100+1)
        return how
    return rec(how * (proc/100+1),proc,date-1)

while True:
        try:
            n = int(input('''
    Выберете:
    1.Факториал.
    2.Факториал лямбдой без рекурсии. 
    3.Факториал лямбдой с рекурсией.
    4.Функция с функциями посчета слов/символов/предловжений.
    5.Лямбда функция с подсчетом вхождения символов.
    6.Функция про банк.
    7.Выход.\n'''))
        except:
            print('Еще раз')
            continue
        if n == 1:
            while True:
                try:
                    a = int(input('Введите число для которого посчитать факториал: '))
                except:
                    print('Еще раз!')
                    continue
                break
            print(f'Факториал {a} равен {factorial(a)}')
        if n == 2:
            while True:
                try:
                    a = int(input('Введите число для которого посчитать факториал: '))
                except:
                    print('Еще раз!')
                    continue
                break
            print(f'Факториал {a} равен {reduce(lambda x,y:x*y,range(1,a+1))}')
        if n == 3:
            while True:
                try:
                    a = int(input('Введите число для которого посчитать факториал: '))
                except:
                    print('Еще раз!')
                    continue
                break
            print(f'Факториал {a} равен {fact(a)}')
        if n == 4:
            usealpha()
        if n == 5:
            stroka = input('Введите строку: ')
            useal(stroka)
        if n == 6:
            bank()
        if n == 7:
            print('Остальное скину попозже, думал во вторник практика, хотел вечером доделать все, извините пожалуйста :)')
            break