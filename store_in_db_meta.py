import MySQLdb, sys, os, json
import gzip

def parse(path):
    g = gzip.open(path,'r') 
    for l in g:
        yield json.dumps(eval(l))


db = MySQLdb.connect("localhost","root","priyanshu","btp")

cursor = db.cursor()
cursor2 = db.cursor()
cursor3 = db.cursor()


y = 0
for l in parse('meta_Cell_Phones_and_Accessories.json.gz'):
    # print l
    l = json.loads(l)
    asin = title = price = related = brand = categories = ''
    if 'asin' in l:
        asin = l['asin'].encode('ascii')
    if 'title' in l:
        title = l['title'].encode('ascii')
    if 'price' in l:
        price = l['price']
    if 'related' in l:
        related = l['related']
    if 'brand' in l:
        brand = l['brand'].encode('ascii')
    if 'categories' in l:
        categories = l['categories']
    # print '\n' 
    query = 'insert into cell_phones_and_accessories_meta(asin,title,price,brand) values('+`asin`+','+`title`+','+`price`+','+`brand`+')'
    # print query
    cursor.execute(query)

    for category in categories:
        for cat in category:
            cat = cat.encode('ascii')

            query = 'insert into cell_phones_and_accessories_categories(asin,category) values('+`asin`+','+`cat`+')'
            cursor2.execute(query)
            # print query

    for i in related:
        for j in related[i]:
            i = i.encode('ascii')
            j = j.encode('ascii')
            query = 'insert into cell_phones_and_accessories_related(asin,related,relation) values('+`asin`+','+`j`+','+`i`+')'
            # print query
            cursor3.execute(query)

    y = y+1
    print y
    if y % 10000 == 0:
        db.commit()
        print 'Committted!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
    # raw_input()

db.commit()
