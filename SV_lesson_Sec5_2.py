# num: int = 10
def add_num(a: int, b: int) -> int:
    # こんな書き方もできる -> int は返り値がint型ということ
    return a + b
r = add_num(10, 20)
print(r)
r = add_num('a', 'b')  # 間違ったものを入れてもPythonは動いてしまう
print(r)
print('#############################')
def menu(entree, drink, dessert):
    print('entree =', entree)
    print('drink =', drink)
    print('dessert =', dessert)

menu(entree='beef', drink='ice', dessert='beer')

print('#############################')
#def test_func(x, l=[]):
def test_func(x, l=None):
    if l is None: #空のリストや辞書を渡す場合は関数内で定義する。引数にはしない
        l=[]
    l.append(x)
    return l
# y=[1,2,3]
# r=test_func(100,y)
# print(r)
# y = [1, 2, 3]
# r = test_func(200, y)
# print(r)
r = test_func(100)
print(r)
r = test_func(100)
print(r)
# 100が二個入るような状況でバグの温床
# →Pythonではリストをデフォルト引数で与えないことが暗黙の了解とされている

print('#############################')
def say_something(word1,word2,word3):
    print(word1) # めんどくさい！

say_something('Hi','Mike', 'Nance')

def say_something(word, *args):
    # *を使うと自動的にタプルに入れてくれる
    # 最初の引数はマストだが、残りはいくつ必要か分らないようなときにはこう書くとよい
    print('word =',word)
    for arg in args:
        print(arg)
#say_something('Hi','Mike', 'Nance')

t = ('Mike', 'Nance')
say_something('Hi','Mike', *t)

print('#############################')
def menu(entree='beef', drink='wine'):
    print(entree, drink)

menu(entree='beef', drink='cofee')

def menu(**kwargs):
    print(kwargs)
    for k,v in kwargs.items():
        print(k,v)
d = {
    'entree' : 'beef',
    'drink' : 'ice coffee',
    'dessert' : 'ice'
}
menu(**d)
#menu(entree='beef', drink='cofee')

def menu(food, *args, **kwargs):
    print(food)
    print(args)
    print(kwargs)

menu('banana', 'apple', 'orrange', entree='beef')

print('#############################')

def example_func(param1,param2):
    """
    いろいろ説明を書く
    Args:
        Param1:あれこれ
        param2:あれこれ
    Returns:
        bool:あれこれ
    """
    print(param1)
    print(param2)
    return True
print(example_func.__doc__)

print('#############################')
# 関数内関数
# 関数内だけで使う関数の場合に使う、関数内で繰り返し処理を使うような場合にも使える
def outer(a,b):
    def plus(c,d):
        return c+d
    r1=plus(a,b)
    r2 = plus(r1, b)

    print(r1,r2 )
outer(1,2)

print('#############################')
# def outer(a,b):
#     def inner():
#         return a+b
#     return inner # ()が無いので、まだ実行されていない
#
# print(outer(1,2))
# f=outer(1,2)
# r=f()
# print(r)
# クロージャ―を使うケース
def circle_area_func(pi):
    def circle_area(radius):
        return pi * radius*radius
    return circle_area

cal1 = circle_area_func(3.14)
cal2 = circle_area_func(3.141592)
print(cal1(10))
print(cal2(10))
# 初めに設定した引数に対して、後々使い分けたいというようなときに使う

print('#############################')
def print_more(func):
    def wrapper(*args,**kwargs):
        print('start:', func.__name__)
        print('args:',args)
        print('kwargs:', kwargs)
        result = func(*args,**kwargs)
        print('result:',result)
        return result
    return wrapper

def print_info(func):
    def wrapper(*args,**kwargs):
        print('#start')
        result =func(*args, **kwargs)
        print('#end')
        return result
    return wrapper

@print_info
@print_more
def add_num(a,b):
    return a+b

r=add_num(10,20)
print(r)

# def add_num(a,b):
#     return a+b
# print('start')
# r= add_num(10,20)
# print('end')
# print(r)