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

print(d)
d.extendleft('x')
d.extend('y')
print(d)
d.clear()
print(d)
# d.rotate()
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

import re
"""
match   文字列の先頭で正規表現とマッチするか判定
search  文字列を操作して、正規表現がどこにマッチするか調べる
findall   正規表現にマッチする部分文字列をすべて探し出しリストとして返す
finditer 重複しないマッチオブジェクトのイテレータを返す
"""
m = re.match('a.c','abc')
print(m)
print(m.group())
m = re.search('a.c','test abc test')
m = re.match('[a-c]', 'x')
m = re.match('[a-zA-Z]', 'x')
m = re.match('[\w]', '@')
print(m)

print('###### format ######')
f = '{:+f}{:+f}'.format(3.14,-3.14)
f = '{:,}'.format(123456789)
print(f)
print(int(100),hex(100),oct(100))