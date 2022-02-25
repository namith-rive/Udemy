#import  lesson_package.utilis
#from lesson_package import utilis
#from lesson_package.utilis import say_twice
# あまり好まれない

#from lesson_package import utilis as u
#from lesson_package.talk import human # 回想が増えたらドットでつなぐ
#from lesson_package.talk import animal

#from lesson_package.talk import *
# アスタリスクを使った場合は、init.pyのallを使って定義する
#r= lesson_package.utilis.say_twice('hello')
#r= utilis.say_twice('hello')

#r= say_twice('hello')
# モジュールまたはフルパスでの読み込みが推奨される
#r= u.say_twice('hello')
#print(r)

#print(human.sing())
#print(animal.sing())

#パッケージが新でも旧でも良いようにする処置
# try:
#     from lesson_package import utilis
# except ImportError:
#     from lesson_package.tools import  utilis
# utilis.say_twice('word')
#
# import  builtins
# builtins.print()
# ranking ={
#     'A':100,
#     'B':85,
#     'C':95
# }
# r = ranking.get('B')
# print(r)
# print(sorted(ranking,key=ranking.get,reverse=True))
#
# print('################################')
#
# s="hbgvaohgaqw4e:gnao:gagrgq;vhzsdv"
#
# d={}
# for c in s:
#     if c not in d:
#         d[c]=0
#     d[c] += 1
# print(d)
#
# d={}
# for c in s:
#     d.setdefault(c,0)
#     d[c] += 1
# print(d)
#
# from collections import defaultdict
# d= defaultdict(int)
# for c in s:
#     d[c] +=1
# print(d)
#
# print(d['h'])


# from termcolor import colored
# print('test')
# print(colored('test','red'))
# print(help(colored))
#
# print('################')
#
# import collections
# import  os
# import sys # アルファベット順で書く
#
# import termcolor # 3rdパーティ製パッケージは一行開ける
#
# print(collections.__file__)
# print(termcolor.__file__)
#
# print(sys.path)
print('################')

