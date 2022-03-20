import contextlib

# def tag(name):
#     def _tag(f):
#         def _wrapper(content):
#             print('<{}>'.format(name))
#             r = f(content)
#             print('</{}>'.format(name))
#             return r
#         return _wrapper
#     return _tag
#
# @tag('h2')
# def f(content):
#     print(content)
#
# f = tag('h2')(f)
# f('test')

# @contextlib.contextmanager
# def tag(name):
#     print('<{}>'.format(name))
#     yield
#     print('</{}>'.format(name))
#
# @tag('h2')
# def f(content):
#     print(content)
#
# def f():
#     print('test0')
#     with tag('h2'):
#         print('test')
#     with tag('a'):
#         print('test2')
#
#
# f()

# @contextlib.contextmanager
# def tag(name):
#      print('<{}>'.format(name))
#      yield
#      print('</{}>'.format(name))

# class tag(contextlib.ContextDecorator):
#     def __init__(self, name):
#         self.name = name
#         self.start_tag = '<{}>'.format(name)
#         self.end_tag = '<{}>'.format(name)
#
#     def __enter__(self):
#         print(self.start_tag + self.end_tag)
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print(exc_type)
#         print(exc_val)
#         print(exc_tb)
#         print(self.end_tag)
#
# with tag('h2'):
#     raise Exception('error')
#      print('test')

# import contextlib
# import os
# try:
#     os.remove('somefile.tmp')
# except FileNotFoundError:
#     pass
#
# with contextlib.suppress(FileNotFoundError):
#     os.remove('somefile.tmp')
# import logging
#
# import sys
#
# # x= input('Enter:')
# # print(x)
#
# # for line in sys.stdin:
# #     print(line)
#
# # print('hello')
# # sys.stdout.write('hello')
#
# # logging.error('Error')
# # sys.stderr.write('Error!')
# with open('stdout.log','w') as f:
#     with contextlib.redirect_stdout(f):
#         help(sys.stdout)
#

# import contextlib
#
# def is_ok_job():
#     try:
#         print('do something')
#         return True
#     except Exception:
#         return False
# def cleanup():
#     print('clean up')
#
# is_ok = is_ok_job()
# print('more task')
# if not is_ok:
#     cleanup()
#
# import io
#
# f=io.StringIO()
# f.write('string io test')
# f.seek(0)
# print(f.read())

# import collections
#
# a = {'a':'a','c':'c','num':0}
# b = {'b':'b','c':'cc'}
# c = {'b':'bbb','c':'ccc'}
# # print(a)
# # a.update(b)
# # print(a)
# # a.update(c)
# # print(a)
#
# m = collections.ChainMap(a,b,c)
# print(m)
# print('######')
# print(m.maps)
# print('######')
# m.maps.reverse()
# print(m.maps)
# print('######')
# m.maps.insert(0, {'c':'cccccc'})
# print(m.maps)
# print('######')
# print(m['c'])

# import collections
#
# d = {}
# l = ['a','a','a','b','b','c']
# for word in l:
#     if word not in d:
#         d[word] = 0
#     d[word] += 1
# print(d)
#
# d = {}
# l = ['a','a','a','b','b','c']
# for word in l:
#     d.setdefault(word, 0)
#     d[word] += 1
# print(d)
#
# d = collections.defaultdict(int)
# l = ['a','a','a','b','b','c']
# for word in l :
#     d[word] += 1
# print(d)
#
# d = collections.defaultdict(set)
# s = [('red',1) , ('blue', 2), ('red','3'), ('blue', 4),
#         ('red',1) , ('blue', 4)]
# print("######################")
#
# for k,v in s:
#     d[k].add(v)
# print(d)
#
# c= collections.Counter()
# for word in l:
#     c[word] += 1
# print(c)
# print(c.most_common(3))
# print(sum(c.values()))
# print("######################")
#
# import re
# with open('lessen.py') as f:
#     words = re.findall(r'\w+', f.read().lower())
#     print(collections.Counter(words).most_common(5))

import collections
import queue

#Doubl-end queue
collections.deque

q = queue.Queue()
lq = queue.LifoQueue() #[1, 2, 3]
l = []
d = collections.deque()

for i in range(3):
    q.put(i)
    lq.put(i)
    l.append(i)
    d.append(i)

# for _ in range(3):
#     print('FIFO queue = {}'.format(q.get()))
#     print('LIFO queue = {}'.format(lq.get()))
#     print('list                = {}'.format(l.pop()))
#     print('deque           = {}'.format(d.popleft()))
#     print()
#
# print(d)
# d.extendleft('x')
# d.extend('y')
# print(d)
# d.clear()
# print(d)
# # d.rotate()
# print(d[1])
# print(d[-1])

print('###### named tuple ######')
import collections

# p= (10, 20)
# print(p[0])
# class Point(object):
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
# p = Point(10,20)
# print(p.x)

# Point = collections.namedtuple('Point', ['x','y'])
# p = Point(10,20)
# print(p.x)
# # 変更できないクラスを作る事が出来る
# #p.x = 100
#
# p._replace(x = 500)
# print(p)
#
# import re
# """
# match   文字列の先頭で正規表現とマッチするか判定
# search  文字列を操作して、正規表現がどこにマッチするか調べる
# findall   正規表現にマッチする部分文字列をすべて探し出しリストとして返す
# finditer 重複しないマッチオブジェクトのイテレータを返す
# """
# m = re.match('a.c','abc')
# print(m)
# print(m.group())
# m = re.search('a.c','test abc test')
# m = re.match('[a-c]', 'x')
# m = re.match('[a-zA-Z]', 'x')
# m = re.match('[\w]', '@')
# print(m)
#
# print('###### format ######')
# f = '{:+f}{:+f}'.format(3.14,-3.14)
# f = '{:,}'.format(123456789)
# print(f)
# print(int(100),hex(100),oct(100))

import re
#
# s = ('arn:aws:cloudformation:bha:rhgarghaoirghauireog:stack/'
#      'mystack-mynestendstack-sgg/khgareuga-gaeaga-gaergaeg-gaweaerase')
#
# #m = re.match(r' arn:aws:cloudformation:[\w-]+:[\d]+:stack/[\w-]+/[\w-]+'+, s)
# m = re.match(r'arn:aws:cloudformation:(?P<region>[\w-]+):[\d]+:stack/[\w-]+/[\w-]+'+, s)
#
# if m:
#     print(m.group('region'))
# else:
#     raise Exception
#
# print(m)

# s = 'My name is ... Mike'
# print(s.split())
#
# p = re.compile(r'\W+')
# print(p.split(s))

# p = re.compile('(blue|white|red)')
# print(p.sub('color','blue socks and red shoes'))
# print(p.subn('color','blue socks and red shoes'))

#
# def hexrepl(match):
#     value = int(match.group())
#     return hex(value)
#
# p = re.compile(r'\d')
# print(p.sub(hexrepl,'12345 55 11 test test2'))

# import re
# # Greedy
#
# s='<html><head><title>Title</title></head></html>'
#
# print(re.match('<.*>',s))
# print(re.match('<.*?>',s))

#repr representation 表示
# print('s')
# print(str('s'))
# print(repr('s'))
#
# import datetime
# d = datetime.datetime.now()
# print(d)
# print(str(d))
# print(repr(d))

# print('###### pprint ######')
# import json
# import pprint
# l = ['apple','orange','banana','peach','mango']
# l.insert(0,l[:])
# l.insert(0,l[:])
# l.insert(0,l[:])
# l.insert(0,l[:])
# # print(l)
# pp = pprint.PrettyPrinter(
#     indent = 4, width = 40, compact=True, depth=3)
# pp.pprint(l)
# 論理和
# print( 0|0)
# print( 0|1)
# print( 1|0)
# print( 1|1)
#
# # 論理積
# print( 192 & 255)
# print( 0 & 1)
# print( 1 & 0)
# print( 1 & 1)
#
# # 排他的論理和
# print('排他的論理和')
# print( 0 ^ 0)
# print( 0 ^ 1)
# print( 1 ^ 0)
# print( 1 ^ 1)
#
# print('反転')
# print( bin(0))
# print( bin(~0))
# print( bin(1))
# print( bin(~1))
# print( bin(~~1))
#
# print('シフト')
# print( bin(1 << 0))
# print( bin(1 << 1))
# print( bin(1 << 2))
# print( bin(5 << 1))
#
# # 論理積
# print( 192 & 255)
# print( 168 & 255)
# print( 192 | 0)
# print( 168 | 0)
# print( 10 ^255)

import enum

# db = {
#     # 'stack1':'active',
#     # 'stack2':'inactive'
#     'stack1': 2,
#     'stack2': 2,
# }
# if db['stack1'] == 'active':
#     print('shutdown')
# elif db['stack2'] == 'inactive':
#     print('terminate')
# STATUS_ACTIVE =1
# STATUS_INACTIVE =2
# if db['stack1'] == STATUS_ACTIVE:
#     print('shutdown')
# elif db['stack2'] == STATUS_INACTIVE:
#     print('terminate')

print('#################')
# class Status(enum.Enum):
#     ACTIVE = 1
#     RENAME_ACTIVE = 1
#     INACTIVE = 2
#     RUNNING = 3
#
# if Status(db['stack1']) == Status.ACTIVE:
#     print('shutdown')
# elif Status(db['stack2']) == Status.INACTIVE:
#     print('terminate')
#
# # print(Status.ACTIVE)
# print(repr(Status.ACTIVE))
# print(Status.ACTIVE.name)
# print(Status.ACTIVE.value)

# for s in Status:
#     print(s)
#     print(type(s))
# print('#################')
# print((Status(1)))
#
# print('#################')

# class Perm(enum.IntFlag):
#     R =4
#     W = 2
#     X = 1
#
# print(Perm.R | Perm.W)
# print(repr(Perm.R | Perm.W | Perm.X))


# def memorize(f):
#     memo = {}
#     def _wrapper(n):
#         if n not in memo:
#             memo[n] = f(n)
#         return memo[n]
#     return _wrapper
#
# import functools
#
# # @memorize
# @functools.lru_cache()
# def long_func(n):
#     r = 0
#     for i in range(1000000):
#         r += n * i
#     return r
#
# for i in range(10):
#     print(long_func(i))
#
# print(long_func.cache_info())
#
# print('next run')
# for i in range(10):
#     print(long_func(i))
#
# print(long_func.cache_info())

print('#################')
#
# import functools
#
# def d(f):
#     def w():
#         """ Wrapper docstring"""
#         return f()
#     return w
# @d
# def example():
#     """ Example docstring"""
#     print('example')
#
# #example()
# print(example.__doc__)
#
# help(example)
print('### functools.partioal #############')
import functools
def f(x, y):
    return x+y

def task(f):
    print('start')
    print(f())

# def outer(x, y):
#     def inner():
#         return x+y
#     return inner

# f = outer(10,20)
p = functools.partial(f, 10, 20)
task(p)
#task(lambda x,y: x+y)