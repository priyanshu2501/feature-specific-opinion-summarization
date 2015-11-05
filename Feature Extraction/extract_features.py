import os,sys,re
import nltk
from nltk.collocations import *
from nltk.tokenize import *
from pos_tagger import *
import identify_entities
from feature_reduction import *
from feature_clustering import *
import pickle

bigram_measures = nltk.collocations.BigramAssocMeasures()
trigram_measures = nltk.collocations.TrigramAssocMeasures()


def get_asins(Product):
    asins = open('../'+ Product + '/asins_list','r').read().split('\n')
    return asins

def get_review_text(Product,asin):
    review_text = open('../'+Product+'/Reviews/'+asin+'.txt','r').read()
    return review_text

def convert_review_text_to_nltk_text(review_text):
    tokens = word_tokenize(review_text)
    return tokens

def get_collocations(nltk_text):
    finder = BigramCollocationFinder.from_words(nltk_text)
    finder.apply_freq_filter(3)
    collocations = finder.nbest(bigram_measures.pmi,20)
    # collocations = [' '.join(i) for i in collocations]
    # finder.score_ngrams(bigram_measures.pmi)
    # print collocations
    return collocations

# def assign_sentence_to_collocations(collocations,review_text_tokenized):
#     collocations_sentences = {}
#     for collocation in collocations:
#         word = collocation[len(collocation)-1]
#         tmp = []
#         reviewCount = 0
#         for review in review_text_tokenized:
#             sentenceCount = 0
#             for sentence in review:
#                 if word in sentence:
#                     tmp.append((reviewCount,sentenceCount))
#                 sentenceCount = sentenceCount+1
#             reviewCount = reviewCount + 1
#         collocations_sentences[collocation] = tmp
#     return collocations_sentences

def analyse_one_product(review_text):
    review_text = re.sub('([.,;!?])\s*(\w)',r'\1 \2',review_text)
    review_text_copy = review_text
    review_text = review_text.lower()
    features = []
    nltk_text = convert_review_text_to_nltk_text(review_text)
    collocations = get_collocations(nltk_text)
    # for j in collocations:
    #     print j
    Title = ''
    entities = identify_entities.main(review_text,Title)
    entities = [tuple(word_tokenize(i)) for i in entities]
    # print len(entities)
    reviews = review_text_copy.split('\n')
    reviews = [i for i in reviews if len(i) > 1]
    review_text_tokenized = [sent_tokenize(review) for review in reviews]
    # collocations_sentences = assign_sentence_to_collocations(collocations,review_text_tokenized)
    nouns,verbs,adjectives,adverbs,candidate_sentences,collocation_tagged,entities_tagged = pos_tagger(review_text_tokenized,collocations,entities)
    # print 'Collocations:'
    # for collocation in collocation_tagged:
    #     print collocation
    # raw_input()
    # for i in candidate_sentences:
        # print review_text_tokenized[i[0]][i[1]]
    features = feature_reduction(collocation_tagged,candidate_sentences,entities_tagged, review_text_tokenized)
    features = cluster_features(features)
    feature_list = [i for i in features]
    # for feature in features:
    #     # print feature
    #     for sentence in features[feature]:
    #         rc,sc,score,ad = sentence
    #         # print review_text_tokenized[rc][sc]
    #         # print score
    #     # raw_input()
    return feature_list,features

def get_features():
    done = os.listdir('Features')
    Product = 'Cell_Phones'
    # print 'Input Product?'
    # Product = raw_input()
    asins = get_asins(Product)
    # asins = ['B00009PGN0']
    for asin in asins:
        if asin+'_features' in done and False:
            print asin + ' Done'
            continue
        review_text = get_review_text(Product,asin)
        feature_list,features = analyse_one_product(review_text)
        f = open('FeatureList/'+asin+'_feature_list','w')
        for i in feature_list:
            f.write(`i`+'\n')
        pickle.dump(features,open('Features/'+asin+'_features','w')) 
        print asin + ' Done'
        f.close()
        # break

if __name__ == "__main__":
    get_features()
