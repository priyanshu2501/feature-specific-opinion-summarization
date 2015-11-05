import MySQLdb,json,pprint

db = MySQLdb.connect('localhost','root','priyanshu','btp')

asins = open('asins_list').read().split('\n')
cursor = db.cursor()

d = {}

count = 0
for asin in asins:
    query = 'select review,rid,summary from cell_phones_and_accessories_reviews where asin='+`asin`
    cursor.execute(query)
    reviews = cursor.fetchall()
    rev = {} 
    for review in reviews:
        rev[review[1]] = [review[0],review[2]]
        # break
    d[asin] = rev
    # print d
    # break
    count = count + 1
    print count,asin

json_d = json.dumps(d)

json.dump(json_d,open('Reviews.json','w'))
