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

import collections

a = {'a':'a','c':'c','num':0}
b = {'b':'b','c':'cc'}
c = {'b':'bbb','c':'ccc'}
# print(a)
# a.update(b)
# print(a)
# a.update(c)
# print(a)

m = collections.ChainMap(a,b,c)
print(m)
print('######')
print(m.maps)
print('######')
m.maps.reverse()
print(m.maps)
print('######')
m.maps.insert(0, {'c':'cccccc'})
print(m.maps)
print('######')
print(m['c'])