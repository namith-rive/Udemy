"""
[DEFAULT]
debug = False
[web_server]
host = 127.0.0.1
port80
"""

import configparser

# config = configparser.ConfigParser()
# config['DEFAULT'] = {
#     'debug': 'TRUE',
# }
# config['web_server'] = {
#     'host' : '127.0.0.1',
#     'port' : 80
# }
# config['db_server'] = {
#     'host' : '127.0.0.1',
#     'port' : 3306
# }
# with open('config.ini','w') as config_file:
#     config.write(config_file)

# config = configparser.ConfigParser()
# config.read('config.ini')
# print(config['web_server'])
# print(config['web_server']['host'])
# print(config['web_server']['port'])
# print(config['DEFAULT']['debug'])

# print('########################')
# import yaml
# with open('config.yml','w') as yaml_file:
#     yaml.dump({
#         'web_server':{
#             'host':'127.0.0.1',
#             'port':80
#         },
#         'db_server': {
#             'host': '127.0.0.1',
#             'port': 3306
#         }
#     },yaml_file, default_flow_style=False)
#
# with open('config.yml','r') as yaml_file:
#     data = yaml.load(yaml_file)
#     print(data, type(data))
#     print(data['web_server']['host'])
#     print(data['web_server']['port'])

# import logging
# logging.basicConfig(level=logging.INFO)
# # logging.basicConfig(filename='test.log', level=logging.INFO)
# # formatter = '%(asctime)s:%(message)s'
# # logging.basicConfig(level=logging.INFO,format=formatter)
#
# # logging.critical('critical')
# # logging.error('error')
# # logging.warning('warning')
# # logging.info('info')
# # logging.debug('debug')
# # logging.info('info %s %s ','test' , 'Test2')
#
# logging.info('info')
# #ロガーに名前を設定して、それをsetlevelで出力する
# logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)
# logger.debug('debug')

# print('********************')
# import logging
# logger = logging.getLogger(__name__)
#
# logger.error('API call is failed')
# logger.error({
#     'action':'create',
#     'status': 'fail',
#     'message': 'API call is failed',
# })
#
# print('**********hotmailへの送信方法**********')
# from email import message
#
# import smtplib
#
# smtp_host = 'smtp.live.com'
# smtp_port = 587
# from_email = 'xxxx@hotmail.com'
#
# fto_email = config.to_email
#
# msg = message.EmailMessage()
# msg.set_content('Test email')
# msg['Subject'] = 'test email sub'
# msg['From'] = from_email
# msg['To'] = fto_email
#
# server = smtplib.SMTP(smtp_host,smtp_port)
# server.ehlo()
# server.starttls()
# server.ehlo()
# server.login(username,password)
# server.send_message()
# server.quit()

from optparse import OptionParser

def main():
    usage = 'usage:%prog [options] arg1 arg2'
    parser = OptionParser(usage=usage)
    parser .add_options('-f','--file',action='store',type='string',
                        dest='filename', help='File name')
    options, args = parser.parse_args()
    print(options)
    print(args)

if __name__ == '__main__':
    main()