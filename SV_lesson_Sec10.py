# # メモリ上でどんどん増えていくのであまりよくない
# long_word = ""
# for word in ['fdagtew','das','ga']:
#     long_word += "{}adasgs".format(word)
#
# #メモリ管理上、こちらのほうがよい
# long_word = []
# for word in  ['fdagtew','das','ga']:
#     long_word.append("{}adasgs".format(word))
# new_longword =  ''.join(long_word)
#
# print()

d= {'key1':'value1','key2':'value2'}
ranking= {'key1':'value1','key2':'value2'}
if 'key1' in d:
    print('test')
# 結果は同じになるが、そもそもinはキーから読みに行くので必要がない

# 実際のコードでは変数は分かりやすいものにすること！
for name,count in ranking.items():
    print(name,count)
if 'key1' in d.keys():
    print('test')