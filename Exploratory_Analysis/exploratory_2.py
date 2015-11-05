import MySQLdb, sys, os
import matplotlib.pyplot as plt
import numpy as np
import math
from pylab import *

print 'Enter Type of Item :'
print '1 - Cell Phones and Accessories'
print '2 - Electronics'
print '3 - Home and Kitchen'
print 'Enter your choice'
choice = int(raw_input())
ch = ''

if choice == 1:
    ch = 'cell_phones_and_accessories'
elif choice == 2:
    ch = 'electronics'
elif choice == 3:
    ch = 'home_and_kitchen'
else:
    sys.exit(0)

# Histogram of number of reviews per item in each category
try:
    rows = open('Exploratory/'+ch+'/exploratory_1','r').read().split('[')[1].split(']')[0].split(',')
    rows = [int(i) for i in  rows]
except:
    db = MySQLdb.connect('localhost','root','priyanshu','btp')
    cursor = db.cursor()
    query = 'select count(*) from '+ch+'_reviews group by asin order by count(*)'
    cursor.execute(query)
    print '_____Query Executed'

    rows = cursor.fetchall()
    print len(rows)
    rows = [int(i[0]) for i in rows]
    f = open('Exploratory/'+ch+'/exploratory_1','w')
    f.write(str(rows))
    f.close()
    db.close()

figure(1,figsize=(7,7))
ax = axes([0.1,0.1,0.8,0.8])

labels = ['>1','<=1']
rows2 = [(i>1) for i in rows]
fracs = [rows2.count(1),rows2.count(0)]
explode = (0.1,0)
pie(fracs,explode = explode,labels = labels,autopct = '%1.1f%%',shadow = True, startangle = 90)
title(ch+'\nPercentage of Products having multiple reviews\nNumber of Reviews : '+`len(rows)`)
savefig('Exploratory/'+ch+'/exploratory_2.png')

