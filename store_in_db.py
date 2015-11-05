import MySQLdb, sys, os, json
import gzip

def parse(path):
    g = gzip.open(path,'r') 
    for l in g:
        yield json.dumps(eval(l))


db = MySQLdb.connect("localhost","root","priyanshu","btp")

cursor = db.cursor()

y = 0
for l in parse('reviews_Cell_Phones_and_Accessories.json.gz'):
    # print l
    l = json.loads(l)
    asin = rid = rname = review = overall = summary = rutime = rtime = ''
    if 'asin' in l:
        asin = l['asin'].encode('ascii')
    if 'reviewerID' in l:
        rid = l['reviewerID'].encode('ascii')
    if 'reviewerName' in l:
        rname = l['reviewerName'].encode('ascii')
    if 'reviewText' in l:
        review = l['reviewText'].encode('ascii')
    if 'overall' in l:
        overall = l['overall']
    if 'summary' in l:
        summary = l['summary'].encode('ascii')
    if 'unixReviewTime' in l:
        rutime = l['unixReviewTime']
    if 'reviewTime' in l:
        rtime = l['reviewTime'].encode('ascii')
    # print '\n' 
    query = 'insert into cell_phones_and_accessories_reviews(asin,rid,rname,review,overall,summary,rutime,rtime) values('+`asin`+','+`rid`+','+`rname`+','+`review`+','+`overall`+','+`summary`+','+`rutime`+','+`rtime`+')'
    # print query
    # raw_input()
    cursor.execute(query)
    y  = y+1
    # print y
    if y % 10000 == 0:
        print y,'Committted!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
        db.commit()
        # raw_input()
print y
db.commit()


