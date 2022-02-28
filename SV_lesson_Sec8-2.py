# import tempfile
#
# with tempfile.TemporaryFile(mode='w+') as t:
#     t.write('hello')
#     t.seek(0)
#     print(t.read())
#
# with tempfile.NamedTemporaryFile(delete=False) as t:
#     print(t.name)
#     with open(t.name, 'w+') as f:
#         f.write('test\n')
#         f.seek(0)
#         print(f.read())
#
# with tempfile.TemporaryDirectory() as td:
#     print(td )
#
# temp_dir = tempfile.mkdtemp()
# print(temp_dir)

# import os
# import subprocess
#
# #subprocess.run(['ls -al'])
# subprocess.run('ls -al', shell=True)
import datetime

import datetime

now = datetime.datetime.now()
print(now)
print(now.isoformat())
print(now.strftime('%d/%m/%y-%H %S %f'))

today = datetime.date.today()
print(today)
print(today.isoformat() )
print(today.strftime('%d/%m/%y'))

t = datetime.time(hour=1, minute=10,microsecond=100)
print(t)
print(t.isoformat())
print(t.strftime('%H_%M_%S_%f'))

print(now)
d = datetime.timedelta(weeks= 1)
print(now - d)

import time
print(time.time())


import os
import shutil

file_name= 'test.txt'
if os.path.exists(file_name):
    shutil.copy(file_name,"{}.{}".format(
        file_name,now.strftime('%Y_%m_%d-%H%M%S%f'))
    )
with open(file_name, 'w') as f:
    f.write('test')