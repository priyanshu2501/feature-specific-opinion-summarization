import MySQLdb

db = MySQLdb.connect('localhost','root','priyanshu','btp')

cursor = db.cursor()

query = 'select asin from cell_phones_and_accessories_asins where count >= 50 and asin in (select asin from cell_phones_and_accessories_categories where category = "Cell Phones")';

cursor.execute(query)

rows = cursor.fetchall()

f = open('asins_list','w')
for asin in rows:
    f.write(asin[0]+'\n')
f.close()
    
