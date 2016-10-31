#!/usr/bin/python
#-*- coding: utf-8 -*-


from sys import stdin, stdout


library = {}    #dictionary 선언

while True:
    line = stdin.readline().strip() #문장 양 끝의 공백 제거
    if line == "":                  #while 종료조건
        break


    word, cnt = line.split('\t')    #tab으로 구분하여 단어 조합과 횟수로 저장
    
    if word in library:
        library[word] += int(cnt)   #단어조합이 이미 존재하면 더해준다 
    else:
        library[word] = int(cnt)    #단어조합이 없을경우 추가하여줌

for word in library:
    stdout.write(word + "\t" + str(library[word]) + "\n")


