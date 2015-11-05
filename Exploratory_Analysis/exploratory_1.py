import MySQLdb, sys, os
import matplotlib.pyplot as plt
import numpy as np
import math
import pylab

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

rows = [ min(100,int(i)) for i in rows] 
num = len(rows)
plt.title('Exploratory 1 : ' + ch + '\nNumber of Products : '+`len(rows)`) 
plt.xlabel('Percentage Reviews')
plt.ylabel('Number of Reviews')
plt.plot([i*100/len(rows) for i in range(1,len(rows)+1)],rows, 'b-');
plt.savefig('Exploratory/'+ch+'/exploratory_1.png')
# plt.show()
plt.close()
