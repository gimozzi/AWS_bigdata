#-*- coding: utf-8 -*-
execfile('20101605.conf')


from boto.s3.connection import S3Connection

s3 = S3Connection()

bucket = s3.get_bucket('sgcs15spproj6tokyo')    #조교의 bucket


from boto.dynamodb2.table import Table

ngram = Table('test_120')                       #bigram이 저장될 table

#for s3object in bucket.list():
#    print s3object.key

for s3object in bucket.list():
    if 'output' in s3object.key and 'part-' in s3object.key:
        content = s3object.get_contents_as_string()
        for each_line in content.split('\n'):
            if each_line =="":                  #예외 조건 검사
                continue
            words, counts = each_line.split('\t')
            ngram.put_item(data = {'words': words, 'counts': counts})   #table에 bigram 입력

