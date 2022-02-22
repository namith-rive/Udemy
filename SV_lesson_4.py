X=20
Y=X
Y=5
print(id(X))
print(id(Y))
print(Y)
print(X)

X= ['a','b']
Y=X
Y[0]='p'
print(id(X))
print(id(Y))
print(Y)
print(X)
print('########################')
##### 4-22
num_tuple=(10,20)
print(num_tuple)

x,y = num_tuple
print(x,y)
print(x)

print( type(num_tuple) )
print(type(x) )

a=100
b=200
print(a,b)
a,b=b,a     #アンパッキングによる値の入れ替え
print(a,b)
print('########################')
##### 4-23
chose_from_two = ('A','B','C')
#chose_from_two = ['A','B','C']
# タプルで宣言していると、誤ってリスト回答部分を書き換えられるような処理をやっても弾くことが出来る
answer = []

#chose_from_two.append('A')
#chose_from_two.append('A')

answer.append('A')
answer.append('C')

print(chose_from_two)
print(answer)

print('########################')
##### 4-26
x= { 'a' : 1}
y=x
y['a'] = 1000
print(x)
print(y)

x= { 'a' : 1}
y=x.copy()
y['a'] = 1000
print(x)
print(y)

print('########################')
##### 4-27
fruits = {
    'apple' : 100,
    'banana':200,
    'orange':300
}
print(fruits['apple'])

print('########################')
## 共通要素を探すような場合に集合を使う
my_friend = {'A','C','D'}
A_friend = {'B','D','E','F'}

print(my_friend & A_friend)

## 重複を削除するためにsetを使うケース
f= ['apple','banana','apple','banana']
kind = set(f)
print(kind)