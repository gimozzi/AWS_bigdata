#-*- coding: utf-8 -*-
#20101605
#sp prj4

import requests
from bs4 import BeautifulSoup

url = []    # url
#################################################
def search(para_url): 
    if para_url in url:
        #만약 para_url 의 주소가 url(url.txt) 리스트에 있으면 중복이므로 return
        return
    else:
        #else 면 crawling 하고(beautifulsoup), url(url.txt)에 저장, index(global) ++, Output.txt 생성 // recursive search 한다(local hyperlink)
        r = requests.get(para_url)
        b = BeautifulSoup(r.content)
        c = b.find_all('a')
        url.append(para_url)        #global url : url.txt에 저장
        #Output_0XXX.txt 생성
        f = open("Output_" + str(len(url)).zfill(4) + ".txt", "w")
        f.write(b.text)
        f.close()
        
        hyperlink = []
        #hyperlink 생성
        #for i in hyperlink(local): #recursive function call
        for i in c:
            if len(i['href']) == 0:
                pass
            elif i['href'].find("#") == 0:
                pass
            elif i['href'].find("?") == 0:
                pass
            elif i['href'].find("http://") != -1:
                chk = requests.get(i['href'])
                if (chk.ok == True and (i['href'] in url) == False):
                    hyperlink.append(i['href'])
            else:
                chk = requests.get("http://cspro.sogang.ac.kr/~gr120150253/" + i['href'])
                if (chk.ok == True and ("http://cspro.sogang.ac.kr/~gr120150253/" + i['href'] in url) == False):
                    hyperlink.append("http://cspro.sogang.ac.kr/~gr120150253/" + i['href'])

        #recursive function call
        for i in hyperlink:
            search(i)

#################################################
search("http://cspro.sogang.ac.kr/~gr120150253/index.html")

#url.txt 저장
f = open("URL.txt", "w")
for i in url:
    if i != url:
        f.writelines(i+'\n')
    else:
        f.writelines(i)
f.close()

