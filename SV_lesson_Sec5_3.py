print('#############################')
# lambda関数
l =['Mon','tue','Wed','Thu','fri','sat','Sun']

def change_words(words, func):
    for word in words:
        print(func(word))

#def sample_func(word):
 #   return word.capitalize()
# sample_func = lambda word:word.capitalize()

change_words(l,lambda word:word.capitalize())

print('#############################')
# ジェネレーター
l =['Good morning','Good afternoon','Good night']
for i in l:
    print(i)
print('#############################')
def counter(num =10):
    for _ in range(num):
        yield 'run'
def greeting():
    yield 'Good morning'
    yield 'Good afternoon'
    yield 'Good night'
for g in greeting():
    print(g)
c=counter()
g = greeting()
print(next(g))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(g))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(g))
# 処理を保持しているので、他の処理の後で継続することが出来る

print('#############################')
t = (1,2,3,4,5)
t2 = (5,6,7,8,9,10)

r=[]
for i  in t:
    if i % 2 == 0:
        r.append(i)
print(r)

r= [i for i in t if i % 2 == 0]
print(r)

r = []
for i in t:
    for j in t2:
        r.append(i*j)
print(r)

r = [i*j for i in t for j in t2]
print(r)

print('#############################')
w=['mon','tue','wed']
f =['cpfee','milk','water']

d = {}
for x,y in zip(w,f):
    d[x] = y
print(d)

d = {x:y for x,y in zip(w,f)}
print(d)

print('#############################')
s = set()
for i in range(10):
    s.add(i)
print(s)

s={i for i in range(10)}
print(s)

print('#############################')
def g():
    for i in range(10):
        yield i

g = g()

g = tuple(i for i in range(10))
print(type(g))
print(g)

print('#############################')
animal = 'cat'
def f():
    # print(animal)
    #global animal
    ##animal = 'dog'
    ##print('local :', locals())
    print(f.__name__)
    print(f.__doc__)

f( )
print('global :', globals())

print('#############################')
l =[1,2,3]
j = 5

try:
    l[0]
except IndexError as ex:
    print("Dont't worry: {}".format(ex))
except NameError as ex:
    print(ex)
except Exception as ex:
    print("other : {}".format(ex))
else:
    print('done') # 何も問題なく抜けた場合に表示される。最後に描くのとは意味合いが少し違う
finally:
    print('clean up')

print('#############################')
class UppercaseError(Exception):
    pass
def check():
    words = ['APPLE','orange','banana']
    for word in words:
        if word.isupper():
                raise UppercaseError(word)
try:
    check()
except UppercaseError as exc:
    print('This is my fault. Go next')