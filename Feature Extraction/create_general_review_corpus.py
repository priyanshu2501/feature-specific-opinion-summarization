import MySQLdb
import os,sys

con = MySQLdb.connect('localhost','root','priyanshu','btp')

cursor = con.cursor()
cursor2 = con.cursor()
f = open('General_Corpus_for_Cell_Phones','w')

query = 'select review from electronics_reviews limit 1000'
cursor.execute(query)

rows = cursor.fetchall()
for row in rows:
    f.write(row[0] + '\n')


query = 'select review from home_and_kitchen_reviews limit 1000'
cursor2.execute(query)

rows = cursor2.fetchall()
for row in rows:
    f.write(row[0] + '\n')
f.close()

con.close()
