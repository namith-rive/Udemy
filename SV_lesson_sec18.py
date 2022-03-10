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
import logging

import sys

# x= input('Enter:')
# print(x)

# for line in sys.stdin:
#     print(line)

# print('hello')
# sys.stdout.write('hello')

# logging.error('Error')
# sys.stderr.write('Error!')
with open('stdout.log','w') as f:
    with contextlib.redirect_stdout(f):
        help(sys.stdout)

