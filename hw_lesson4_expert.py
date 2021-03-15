'''
Изначально думал, что дерево должно храниться в списке например _list = [2, [1], [1, [0], [1]]], соответсвенно какждый новый вложенный
список - это соответственно "потомки", и пытался для этой идеи реалтзовать, однако столкнулся с проблемой что при при присвоении списку
списка получалось, что мы присваиваем строку элементу с индексом 0. Если же делать через цикл, то т.к в список вложен список некоторые 
элементы все равно становятся строками.(все что закомментированно - это для этого способа) 
Но на занятии вы показали, что оказывается можно с классами, так что я переделал и это что не закомменированно.
'''
# _list = [2, [1], [1, [0], [1]]]
# def tree(label, branches=[]):
#     for branch in branches:
#         assert is_tree(branch), 'ветви должны быть деревьями'
#     return [label] + list(branches)

# def label(tree):
#     return tree[0]

# def branches(tree):
#     return tree[1:]

# def is_tree(tree):
#     if type(tree) != list or len(tree) < 1:
#         return False
#     for branch in branches(tree):
#         if not is_tree(branch):
#             return False
#     return True

# def is_leaf(tree):
#     return not branches(tree)

# # d = _list
# # while len(_list)!=0:
# #     print(label(_list))
# #     for b in branches(_list):
# #         print(b)
# #     _list.clear()
# #     _list.append(label(branches(d)))
# #     print(_list[0])

# def print_tree(t,indent=0):
#     print(' ' * indent + str(label(t)))
#     for b in branches(t):
#         print_tree(b,indent + 1)

# print_tree(_list)
# d = branches(_list)
# print(label(d))
# print(type(label(d)))
# indent=0
# while len(_list)!=0:
#     print(' ' * indent + str(label(_list)))
#     print(type(_list[0]))
#     print(_list)
#     _list = branches(_list)
#     #_list = list(_list[0])
#     indent += 1

class Node:
    def __init__(self, value):
        self.left = None
        self.value = value
        self.right = None

class Tree:
    def create(self, value):
        return Node(value)

    def add(self, node , value):
        if node is None:
            return self.create(value)
        if value < node.value:
            node.left = self.add(node.left, value)
        elif value > node.value:
            node.right = self.add(node.right, value)

        return node

def preorder(unit):
        if not unit:
            return
        stack = []
        stack.append(unit)
        while stack:
            unit = stack.pop()
            print(unit.value,end=' ')
            if unit.right:
                stack.append(unit.right)
            if unit.left:
                stack.append (unit.left)

def inorder(unit):
    stack = []
    while stack or unit:
        if unit:
            stack.append(unit)
            unit = unit.left
        else:
            unit = stack.pop()
            print(unit.value,end=' ')
            unit = unit.right

root = None
tree = Tree()
root = tree.add(root, 1)
tree.add(root, 2)
tree.add(root, 3)
tree.add(root, 4)
tree.add(root, 7)
tree.add(root, 6)
tree.add(root, 8)


'''
    Идею взял с объяснения в четверг
'''
def calculation(str):
    if correct(str):
        stack = []
        stack = str.split()
        postfix = []
        helper = []
        priority = {"(": 1, "-": 2, "+": 2, "/": 3, "*": 3}
        for i in stack:
            if is_digit(i):
                postfix.append(i)
            elif i == '(':
                helper.append(i)
            elif i == ')':
                temp = helper.pop()
                while temp != '(':
                    postfix.append(temp)
                    temp = helper.pop()
            else:
                while helper and priority[helper[len(helper) - 1]] >= priority[i]:
                    postfix.append(helper.pop())
                helper.append(i)
        while helper:
            postfix.append(helper.pop())
        stack = postfix
        print(f"Результат вычисления равен: {connection(stack)}")
    else:
        print('Скобки расставлены неверно.')
        return

def is_digit(number):
    if number.isdigit():
        return True
    elif number[0] == '-' and number[1:].isdigit():
        return True
    else:
        return False

def connection(stack):
    helper = []
    for i in stack:
        if is_digit(i):
            helper.append(int(i))
        else:
            a = helper.pop()
            b = helper.pop()
            res = operation(b, a, i)
            helper.append(res)
    return helper.pop()


def operation(a, b, sign):
    if sign == '+':
        return a + b
    elif sign == '-':
        return a - b
    elif sign == '*':
        return a * b
    elif sign == '/':
        return a / b

def correct(str):
    stack = []
    brackets = {'(': ')', '[': ']', '{': '}', '<': '>'}
    for i in str:
        if i in brackets.keys():
            stack.append(i)
        elif i in brackets.values():
            if stack:
                bracket = stack.pop()
                if brackets.get(bracket) != i:
                    return False
            else:
                return False
    if stack:
        return False
    return True

while True:
        n = input(
    """
    Выберите задачу.
    Обход дерева:           1
    Решение мат. примера:   2
    Выход:                  3
    """
        )
        if n == '1':
            print('Центрированный обход: ',end='')
            inorder(root)
            print('\nПрямой обход: ',end='')
            preorder(root)
        elif n == '2':
            calculation(input('Введите пример, в котором между каждыми символами пробел: '))
        elif n == '3':
            print("Goodbye!")
            break
        else: 
            print("Неверный символ") 
