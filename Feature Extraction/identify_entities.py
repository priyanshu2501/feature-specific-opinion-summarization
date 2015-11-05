from nltk.probability import FreqDist
from nltk.util import ngrams
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import re
sw = stopwords.words('english')
rem_words = ['quot','this','is','my','I','You','will','would','should','that','the','if','but','am','it']
#Keep editing these words
p = re.compile(r'\b(this|is|my|I|You|will|would|should|that|the|if|but|am|it)\b',re.IGNORECASE)

def isMostlyStopwords(c,x,Title):
	count = 0
	for i in range(0,len(x)):
		if x[i] in sw:
			count += 1	
        if count > 1 or count == 1 and len(x) <= 2 or len(' '.join(x)) < 4:
		return True
	if len(x) == 1 and c < 10:
		return True
	if len(x) == 2 and c < 5:
		return True
	if len(x) == 3 and c < 4:
		return True
        # print x,len(x),c
	return False

def identify_entities(corpus,Title):
	maxTagLen = 3
	n = maxTagLen #Length of n grams
	corpus_freq = []
	corpus = re.sub(p,'',corpus)
	corpus = re.findall("[A-Z]{2,}(?![a-z])|[A-Z][a-z]+(?=[A-Z])|[\'\w]+",corpus)
	for i in range(1,n+1):
		grams = FreqDist(ngrams(corpus,i)).most_common(200)
		grams = [(i[1],i[0]) for i in grams if not isMostlyStopwords(i[1],i[0],Title) ]	
		# print len(grams)
                grams = sorted(grams,reverse = True)
		for j in grams:
	                corpus_freq.append(j)
	entity_list = corpus_freq
	return entity_list
	
def main(reviews,Title):
	entity_list = identify_entities(reviews,Title)
	entity_list2 = [' '.join(i[1]) for i in entity_list]
	freqs = [i[0] for i in entity_list]
	entity_list = entity_list2
	# removedEntities,entity_list = filter_entities(tagList, entity_list,freqs=freqs)
        # print 'Entity Extraction done'
	return entity_list
