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
r=[]
for i  in t:
    if i % 2 == 0:
        r.append(i)
print(r)

r= [i for i in t if i % 2 == 0]
print(r)