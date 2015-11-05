import os,sys
import pickle
from nltk.tokenize import *

neg_words =[" too ","never","nothing","nowhere","noone","none","not","havent","hasnt","hadnt","cant","couldnt","shouldnt","wont","wouldnt","dont","doesnt","didnt","isnt","arent","aint","n't"] 
def generate_feature_sentiments(feature_details,review_text_tokenized):
    reviews = {}
    features = []
    for key in feature_details: 
        features.append(key)
        pos_reviews = []
        neg_reviews = []
        # print key,":"
        reviews[key] = {}
        reviews[key]['pos'] = []
        reviews[key]['neg'] = []
        for i in feature_details[key]:
            neg = False
            for j in neg_words:
                if j in review_text_tokenized[i[0]][i[1]]:
                    neg = True
                    break
            if not neg:
                if i[2] > 0:
                    # print "Positive : ",review_text_tokenized[i[0]][i[1]]," -- ", i[3]
                    pos_reviews.append((i[0],i[1],i[2],i[3]))
                elif i[2] < 0:
                    # print "Negative : ",review_text_tokenized[i[0]][i[1]]," -- ",i[3]
                    neg_reviews.append((i[0],i[1],i[2],i[3]))
            else:
                if i[2] > 0:
                    # print "Negative : ",review_text_tokenized[i[0]][i[1]]," -- ",i[3]
                    neg_reviews.append((i[0],i[1],i[2],i[3]))
                elif i[2] < 0:
                    # print "Positive : ",review_text_tokenized[i[0]][i[1]]," -- ", i[3]
                    pos_reviews.append((i[0],i[1],i[2],i[3]))
        # print "Positive Reviews:"
        # for review in pos_reviews:
        #     print review_text_tokenized[review[0]][review[1]]
        # print 
        # print "Negative Reviews:"
        # for review in neg_reviews:
        #     print review_text_tokenized[review[0]][review[1]]
        # print
        reviews[key]['pos'] = pos_reviews
        reviews[key]['neg'] = neg_reviews
    return features,reviews

if __name__ == "__main__":
    product = "Cell_Phones"
    asins = open('../'+product+'/asins_list').read().split('\n')
    for asin in asins :
        print asin
        review_text = open('../'+product+'/Reviews/'+asin+'.txt','r').read().lower()
        reviews = review_text.split('\n')
        reviews = [i for i in reviews if len(i) >= 1]
        review_text_tokenized = [sent_tokenize(review) for review in reviews]
     
        # print [len(i) for i in reviews]
        feature_details = pickle.load(open('../Feature Extraction/Features/'+asin+'_features','r'))
        features,reviews = generate_feature_sentiments(feature_details,review_text_tokenized)
        f = open('Reviews_Analysed/'+asin+'_Reviews_Analysed','w')
        x = ''
        for feature in features:
            f.write('__________' + `feature` + '__________\n\n\n')
            f.write('Positive Reviews:\n\n')
            for i in reviews[feature]['pos']:
                f.write('---'+`review_text_tokenized[i[0]][i[1]]` + ' **** ' + `i[3]` +  '\n')
            f.write('\nNegative Reviews:\n\n')
            for i in reviews[feature]['neg']:
                f.write('---'+`review_text_tokenized[i[0]][i[1]]` + ' **** ' + `i[3]` + '\n')
            f.write('\n')
            f.write('\n================================================================================================================\n')
        # f.write(x)
        f.close()
        print asin + ' Done'
