#-*- coding: utf-8 -*-
execfile('20101605.conf')


from sys import stdin
from boto.dynamodb2.table import Table
myTable = Table('test_120')


from boto.dynamodb2.exceptions import ItemNotFound, ValidationException

def CLI(word):
    try:                        #조회된 단어 출력 
        got = myTable.get_item(words = word)    
        print got['counts']
    except ItemNotFound:        #table에 단어 가 없는 경우 0 출력
        #got = None
        got = 0
        print got
    except ValidationException: #공백을 입력받을 경우 종료
        exit()
        
while True:
    search = raw_input()    #조회할 단어 입력
    #print "["+search+"]"
    CLI(search)             #CLI함수에서 단어 조회

