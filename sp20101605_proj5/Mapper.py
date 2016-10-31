#!/usr/bin/python
#-*- coding: utf-8 -*-


from sys import stdin, stdout

while True:

    line = stdin.readline().strip() #문장 양 끝의 공백 제거 
    if line == "":          #while 종료 조건
        break


    words = line.split()    #공백으로 split 하여 words에 list로 저장

    if len(words) == 1:
        continue

    for word in range(0, len(words)-1): 
        stdout.write(words[word] + " " + words[word+1] + "\t1\n")


