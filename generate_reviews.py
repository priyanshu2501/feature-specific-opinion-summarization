import os,sys,MySQLdb
import nltk
# For using Multi - grain Latent Dirichlet Analysis
sys.path.insert(0,'/home/priyanshu2501/BTP_Final/REPOS/m-ochi/mglda')
from mglda import *

db = MySQLdb.connect('localhost','root','priyanshu','btp')

cursor = db.cursor()
cursor2 = db.cursor()
cursor3 = db.cursor()
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

print 'Number of Iterations : ?'
Iter = int(raw_input())

num_reviews_low_limit = 2
query = 'select distinct asin from ' + ch + '_asins where count >= ' + `num_reviews_low_limit`

cursor.execute(query)
asins = cursor.fetchall()
asins = [i[0] for i in asins]

for asin in asins:
    query = 'select title,price from '+ch+'_meta where asin = '+`asin`
    cursor3.execute(query)
    result = cursor3.fetchall()
    title = result[0][0]
    price = result[0][1]


    query = 'select review,summary from ' +ch + '_reviews where asin = '+ `asin`
    cursor2.execute(query)
    reviews = cursor2.fetchall()
    summaries = [i[1] for i in reviews]
    reviews = [i[0] for i in reviews]
    reviews2 = reviews

    #Printing Details 
    print 'Id : ' + asin
    print 'Title : ' + title
    print 'Price : ' + `price`
    print len(reviews),' Reviews'
    print '\nReviews :'
    for review in reviews:
        print review
    print
    reviews.append(title)
    reviews = []
    for review in reviews2:
        review2 = []
        review = review + '.'
        sentences = review.split('.')
        sentences2 = []
        for sentence in sentences:
            print sentence
            sentence = nltk.word_tokenize(sentence)
            print nltk.pos_tag(sentence)
            raw_input()
            if len(sentence) >= 1:
                sentences2.append(sentence)
        reviews.append(sentences2)

    # print 'Send Format :'
    # print reviews
    # print
    # raw_input()
    # print 'Analysis__________________________________'
    # gt,lt = do_mglda(reviews,Iter)
    # print 'Global Topics : '
    # print gt
    # print
    # print 'local Topics : '
    # print lt 
    # print
    # print 'Analysis Done_____________________________'
    # raw_input()


