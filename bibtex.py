import re
from datetime import datetime

def printbibtex(url='', author='', title='', key=''):
    if title == '':
        print('titleは必須ですが，このページにはタイトルがありません．')
        exit

    if key == '':
        day = datetime.now()
        key = author + str(day.year)+str(day.month)+str(day.day)+str(day.hour)+str(day.minute)+str(day.second)+str(day.microsecond)

    print('@MISC{' + key + ',')
    print('    howpublished = {\\url{' + url + '}},')
    if author != '':
        print('    author = {' + author + '},')
    print('    title = {' + title + '}')
    print('}')
