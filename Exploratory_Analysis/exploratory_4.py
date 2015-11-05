import MySQLdb, sys, os
import matplotlib.pyplot as plt
import numpy as np
import math
import pylab
import pickle # For reading and writing python objects

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
d = {}
try:
    rows = pickle.loads(open('Exploratory/'+ch+'/exploratory_4','r'))
except:
    db = MySQLdb.connect('localhost','root','priyanshu','btp')

    cursor = db.cursor()
    query = 'select review from '+ch+'_reviews limit 100000'
    cursor.execute(query)
    print '_____Query Executed'
    
    rows = cursor.fetchall()
    print len(rows)
    words = []
    rows2 = []
    f = open('Exploratory/'+ch+'/exploratory_4','w')
    for i in rows:
        num_words = min(300,i[0].count(' '))
        
        if num_words in d:
            d[num_words] = d[num_words] + 1
        else:
            d[num_words] = 1
    rows = d
    pickle.dump(d,f)
    f.close()
    db.close()
print len(rows),'$$'
max_words = 0
for i in d:
    max_words = max(max_words,i)
d[300] = 0
plt.title('Exploratory 4 : ' + ch + '\nNumber of Words per review') 
plt.ylabel('Number of Reviews')
plt.xlabel('Number of words in reviews')
# print rows
bins = max_words
rows2 = []
for i in rows:
    for j in range(0,rows[i]):
        rows2.append(int(i))
# print rows2
n,bins,patches = plt.hist(rows2,bins, facecolor = 'r')


plt.savefig('Exploratory/'+ch+'/exploratory_4.png')
plt.show()
plt.close()
