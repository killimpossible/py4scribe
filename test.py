#coding=utf-8
'''
@author: panfei
@contact: cnweike@gmail.com
'''

from scribeutil import ScribeClient

if __name__ == '__main__':
    scribe_client = ScribeClient('127.0.0.1', 8250)
    scribe_client.log('YourCategory', 'Hello world')
