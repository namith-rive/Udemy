# with open('text.txt.','w') as f:
#     # withを使うと自動的にクローズしてくれる
#    # f = open('text.txt.', 'w')
#     #w 上書き　a 追加
#     f.write('test\n')
#     print('My','name','is','Mike',sep='#', end ='!',file =f)
#     #print関数を使っても書き込み可能
#     #f.close() # 忘れてしまうとメモリの無駄遣いになる

# print('#####################')
# s = """\
# AAA
# BBB
# CCC
# DDD
# EEE
# """
# with open('text.txt.','w') as f:
#     f.write(s)

# with open('text.txt','r+') as f:
#     """
#     動かした瞬間、新ファイルを作成するため注意（旧ファイルが消える）
#      w+ : 書き込み+読み込み
#     """
#     #print(f.read())
#     # while True:
#     #     chunk =2
#     #     line = f.readline(chunk) # 一行ずつ/chunkごとに読み込む
#     #     #print(line, end = '')
#     #     print(line)
#     #     if not line:
#     #         break
#     # print(f.tell()) # 現在位置を教えてくれる
#     # print(f.read(1)) # 一文字書き出し
#     # f.seek(5)   # n番目の文字を取得
#     # print(f.read())
#     # f.write(0)
#     # #f.seek(0) # 書き込んだ後で最初に戻って(seek(0))書き出す
#     # print(f.read())
#
#     print(f.read())
#     f.seek(0)
#     f.write(s)

# print('### Template ##################')
import string
# s = """\
# Hi $name.
#
# $contents
#
# Have a good day
# """
# 文字列を読み込み専用で読み込む。他の人が書き込みなどしないようにする
# with open('design/email_template.txt') as f:
#     t = string.Template(f.read())
# contents = t.substitute(name= 'Mike', contents = 'How are you?')
# print(contents)

# import csv
# print('### CSV書き込み読み込み##############')
# with open('test.csv','w') as csv_file:
#     fieldnames = ['Name','Count']
#     writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerow({'Name':'A', 'Count':1})
#     writer.writerow({'Name': 'B', 'Count': 2})
#
# with open('test.csv', 'r') as csv_file:
#     reader = csv.DictReader(csv_file)
#     for row in reader:
#         print(row['Name'], row['Count'])

print('### ファイル操作##############')
import os
import pathlib
import glob
import shutil
# ファイルがあるかどうかを探す
#os.path.exists('test.txt')
#print(os.path.isfile('text.txt'))
# フォルダがあるかどうかを探す
#print(os.path.isdir('design'))

#ファイル名の変更
#os.rename('text.txt', 'renamed.txt')
# os.symlink( 'renamed.txt', 'symLink.txt')
#ディレクトリの作成・削除
#os.mkdir('test_dir')
#os.rmdir('test_dir') # ファイルが入っていると消せない

# pathlib.Path('empty.txt').touch()
# os.remove('empty.txt')

#os.mkdir('test_dir')
#os.mkdir('test_dir/test_dir2')
#os.mkdir('test_dir/test_dir3')
#print(os.listdir('test_dir'))
#pathlib.Path('test_dir/test_dir2/empty.txt').touch()

# shutil.copy('test_dir/test_dir2/empty.txt',
#                   'test_dir/test_dir2/empty2.txt')
# print(glob.glob('test_dir/test_dir2/*'))

shutil.rmtree('test_dir') # 指定ディレクトリをすべて削除する