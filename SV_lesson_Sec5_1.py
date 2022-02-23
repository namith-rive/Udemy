## 31
x = 10
if x < 0:
    print('negative')
elif x == 10:
    print('zero')
else:
    print('positive')

a =5
b = 10
if a> 0:
    print('a is positive')
    if b> 0:
        print('b is positive')

print('#########################')
a=10
b=5
if a>0:
    if b>0:
        print('a and b are positive')
if a > 0 and b>0:
    print('a and b are positive')

print('#########################')
y=[1, 2, 3]
x= 1
if x in y:
    print('in')
if 100 not in y:
    print('not in')
    a=1
    b=2
    if a != b:
        print('Not equal')

is_ok= True
'''
boolen型を使うときはnotを使うことがある。それ以外のときには算術演算子を使い、notは使わない方がよい。可読性が落ちるため
'''
if not is_ok:
    print('hello')
print('#########################')

is_ok = '' #値が入っているか確認するために使う
if is_ok:
    print('ok!') # 値に変数がある場合はTrueと判定される
else:
    print('no!')

is_ok = [1,2,3,4]
if is_ok:
    print('ok2!') # 値に変数がある場合はTrueと判定される
else:
    print('no2!')

print('#########################')

is_empty = None
#print(help(is_empty))
'''
class NoneType(object)
実体がないオブジェクト。値を入れたくないときに使う
'''
if is_empty is  None:
    print('None!!!')
# is はNoneかどうかを判定する際によく使う

print(1 == True)
print(None is None)
print('#########################')

count = 0
while True:
    if count >= 5:
        break

    if count ==2:
        count+=1
        continue

    print(count)
    count += 1

print('#########################')

count = 0
while count < 5:
    print(count)
    count   +=1
else:
    print('done')

print('#########################')
'''
while   True:
    word = input('Enter:')
    if word ==100:
        break
    print('next')
'''

print('#########################')
some_list =[5,6,7,8,9,10]
i=0
while i < len(some_list):
    print(some_list[i])
    i += 1

for i in some_list:
    print(i)

for s in 'abcde':
    print(s)
for word  in ['My','name','is','Mike']:
    if word == 'name':
       #break
        continue
    print(word)

print('#########################')
for fruit in ['apple','banana', 'orange']:
    if fruit == 'banana':
        print('stop eating')
        break
    print(fruit)
else:
    print('I ate ALL!')
print('#########################')
# range関数

# _を変数として使うことで、この変数はコード中で使われないことが一目で分かる
for _ in range(4):
    print('hello')
print('#########################')
# enumrate関数
#i=0
#for fruit in ['apple','banana', 'orange']:
    #print(i,fruit)
    #i +=1
for i, fruit in enumerate(['apple','banana', 'orange']):
    print(i,fruit)
print('#########################')
days = ['Mon', 'Tue', 'Wed']
fruits =  ['apple','banana', 'orange']
drinks =  ['coffee','tea', 'beer']

#for i in range(len(days)):
 #   print(days[i], fruits[i],drinks[i])
for day, fruit, drink in zip(days, fruits, drinks):
    print(day, fruit, drink )

print('#########################')

d={'x':100, 'y':200}
print(d.items())
for k,v in d.items():
    print(k, ':' ,v)

print('#########################')
def say_something():
    print('hi')
# 関数定義をした後で関数を使う。Pythonは上から順に読み込むため！
f = say_something
f()

def say_something_v2():
    s = 'hihi'
    return s
result =say_something_v2()
print(result)

def what_is_this(color):
    if color == 'red':
        return 'tomato'
    elif color == 'green':
        return 'green pepper'
    else:
        return "I don't know"

result= what_is_this('green')
print(result)