import json

print('#### XML #################')
# import xml.etree.ElementTree as ET

# root = ET.Element('root')
# tree = ET.ElementTree(element=root)

# employee = ET.SubElement(root,'employee')
# employ =ET.SubElement(employee, 'employ')
# employ_id = ET.SubElement(employee,'id')
# employ_id.text = '111'
# employ_id = ET.SubElement(employee,'name')
# employ_id.text = 'Mike'
#
# employ =ET.SubElement(employee, 'employ')
# employ_id = ET.SubElement(employee,'id')
# employ_id.text = '222'
# employ_id = ET.SubElement(employee,'name')
# employ_id.text = 'Nancy'
#
# tree.write('test.xml', encoding='utf-8',xml_declaration=True)
#
# tree = ET.ElementTree(file='test.xml')
# root = tree.getroot()
#
# for employee in root:
#     for employ in employee:
#         for person in employ:
#             print(person.tag, person.text)
#
# print('test')

print('#### JSON #################')
# j= {
#     "employee":
#         [
#             {"id":111,"name":"Mike"},
#             {"id":222,"name":"Nancy"}
#         ]
# }
# print(j)
# #jsonは""でないといけない
# print(json.dumps(j))
# #Python中でjsonを使う場合は's'がつく
# a = json.dumps(j)
# json.loads(a)
# print('＠＠＠＠＠＠＠')
# print(json.loads(a))
# print('＠＠＠＠＠＠＠')
# with open('test.json','w') as f:
#     json.dump(j,f)
# print('####JSONの読み込み###########')
# with open('test.json','r') as f:
#     print(json.load(f))

"""
REST
HTTPメソッド　クライアントが行いたい処理をサーバに伝える
GET データの参照
POST データの新規登録
PUT　データの更新
DELETE　データの削除
"""
# import urllib.request
# import  json
# payload = {'key1' : 'value1' , 'key2' : 'value2'}
# url = 'http://httpbin.org/get' + '?' + urllib.parse.urlencode(payload)
# print(url)
# # http://httpbin.org/get?key1=value1&key2=value2
#
# with urllib.request.urlopen(url) as f:
#    # print(f.read().decode('utf-8'))
#     r = json.loads(f.read().decode('utf-8'))
#     print(type(r))
# payload = json.dumps(payload).encode('utf-8')
# req = urllib.request.Request(
#     'http://httpbin.org/post',data = payload,method='POST')
# with urllib.request.urlopen(req) as f:
#     print(json.loads(f.read().decode('utf-8')))
# req = urllib.request.Request(
#     'http://httpbin.org/put',data = payload,method='PUT')
# with urllib.request.urlopen(req) as f:
#     print(json.loads(f.read().decode('utf-8')))
#
# req = urllib.request.Request(
#     'http://httpbin.org/delete',data = payload,method='DELETE')
# with urllib.request.urlopen(req) as f:
#     print(json.loads(f.read().decode('utf-8')))

print('#### Request #################')
# import requests
#
# payload = {'key1' : 'value1' , 'key2' : 'value2'}
#
# #r = requests.get( 'http://httpbin.org/get' , params=payload)
# #r = requests.post( 'http://httpbin.org/post' , data=payload)
# #r = requests.put( 'http://httpbin.org/put' , data=payload)
# #r = requests.delete( 'http://httpbin.org/delete' , data=payload)
#
# # タイムアウトでエラーを返す方法
# r= requests.get( 'http://httpbin.org/get' , params=payload, timeout=1)
#
#
# print(r.status_code)
# print(r.text)
# print(r.json())

# import  http.server
# import  socketserver
#
# with socketserver.TCPServer(('127.0.0.1', 8000),
#     http.server.SimpleHTTPRequestHandler) as httpd:
#     httpd.serve_forever()
# #  pyhton ターミナルから開く
# #  webbrowser.open('http://127.0.0.1:8000')

# import  matplotlib.pyplot as plt
# import networkx as nx
#
# G = nx.Graph()
# G.add_node(1)
# G.add_nodes_from([2,3])
# #G.add_edges(1,2)
# #G.add_edges(2,3)
#
# nx.draw(G)
# plt.show()
print('#### Flask #################')
# import sqlite3
# from  flask import Flask
# from  flask import g
# from  flask import render_template
# from flask import request
# from  flask import Response
#
# app = Flask(__name__)
# def get_db():
#     db = getattr(g, '_database', None)
#     if db is None:
#         db = g._database = sqlite3.connect('test_sqlite.db')
#         return db
#
# @app.teardown_appcontext
# def close_connection(exception):
#     db = getattr(g,'__database', None)
#     if db is not None:
#         db.close()
#
# @app.route('/employee', methods=['POST','PUT','DELETE'])
# @app.route('/employee/<name>', methods=['GET'])
# def employee(name=None):
#     db = get_db()
#     curs = db.cursor()
#     curs.execute(
#         'CREATE TABLE IF NOT EXISTS person('
#         'id INTEGER PRIMARY KEY AUTOINCREMENT, name STRING)'
#     )
#     db.commit()
#     name = request.values.get('name',name)
#     if request.method =='GET':
#         curs.execute('SELECT * FROM persons WHERE name = "{}'.format(name))
#         person = curs.fetchone()
#         if not person:
#             return "No", 404
#         user_id, name = person
#         return'{}:{}'.format(user_id,name), 200
#     if request.method == 'POST':
#         curs.execute('INSERT INFO persons(name) values("{}")'.format(name))
#         return 'created {}'.format(name), 201
#     if request.method == 'PUT':
#         new_name = request.values['new_name']
#         curs.execute('UPDATE persons set name = "{} WHERE name = "{}'''.format(
#             new_name, name
#         ))
#         db.commit()
#         return 'updated {}:{}'.format((name,new_name)), 200
#     if request.method == 'DELETE':
#         curs.execute('DELETE from persons WHERE name = "{}'.format(name))
#         return 'deleted{}'.format(name), 200
#
#
#
# @app.route('/')
# def hello_world():
#     return 'Top'
#
# @app.route('/hello')
# @app.route('/hello/<username>')
# def hello_world2(username=None):
#     return   render_template('hello.html', username=username)
#     #return 'hello world!{}'.format(username)
#
# @app.route('/post', methods = ['GET','PUT','DELETE'])
# def show_post():
#     return str(request.vales)
#
# def main():
#     app.debug = True
#     app.run()
#     #app.run(host='127.0.0.1',port= 5000)
#
# if __name__ =='__main__':
#     main()
print('### beautiful soup ########')
from bs4 import BeautifulSoup

import  requests

html =requests.get('http://www.python.org')
# print(html.text)

soup = BeautifulSoup(html.text, 'lxml')
titles = soup.find_all('title')
print(titles[0].text)

intro = soup.find_all('div', {'class':'introduction'})
print(intro[0].text)