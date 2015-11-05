import nltk

def pos_tagger(review_list,collocations,entities):
    candidate_sentences = []
    nouns = []
    adjectives = []
    verbs = []
    adverbs = []
    reviewCount = 0
    collocation_tagged = {}
    entities_tagged = {}
    for review in review_list:
        sentenceCount = 0
        for sentence in review:
            tokens = nltk.word_tokenize(sentence)
            tagged_tokens = nltk.pos_tag(tokens)
	    tagged_tokens = [(i.lower(),j) for (i,j) in tagged_tokens]
            a = 0
            n = 0
            nn  = []
            ad = []
            wordCount = 0
            for word,pos in tagged_tokens:
                if pos.startswith('NN'):
                    n = 1
                    nn.append((word,wordCount,pos))
                    nouns.append((word,reviewCount,sentenceCount))
                elif pos.startswith('JJ'):
                    a = 1
                    ad.append((word,wordCount,pos))
                    adjectives.append((word,reviewCount,sentenceCount))
                elif pos.startswith('VB'):
                    verbs.append((word,reviewCount,sentenceCount))
                elif pos.startswith('RB'):
                    # a = 1
                    # adj.append((word,wordCount,pos))
                    adverbs.append((word,reviewCount,sentenceCount))
                wordCount = wordCount + 1
            if a + n == 2:
                adj_nn_pairs = []
                for i in ad:
                    nchosen = ''
                    closeness = 100000
                    for j in nn:
                        if abs(j[1] - i[1]) < closeness:
                            nchosen = j[0]
                            closeness = abs(j[1] - i[1])
                    adj_nn_pairs.append((i[0],nchosen))
                candidate_sentences.append((reviewCount,sentenceCount,adj_nn_pairs))
                # print sentence 
                # print 'Nouns - ' + `nn`
                # print 'Adjectives - ' + `ad`
                # for i in adj_nn_pairs:
                #     print i
                # raw_input()
	    
	    for collocation in collocations:
		    if collocation not in collocation_tagged:
			    collocation_present = True
			    for word in collocation:
			    	if word not in sentence:
					collocation_present = False
		              		break
		    	    if collocation_present:
				for word,pos in tagged_tokens:
					if word == collocation[len(collocation) - 1] and pos.startswith('NN'):
						collocation_tagged[collocation] = True
                                        if word == collocation[0] and not (pos.startswith('NN') or pos.startswith('JJ') or pos.startswith('VB') or pos.startswith('RB')):
                                            if collocation in collocation_tagged:
                                                del collocation_tagged[collocation]
                                            break
	    for entity in entities:
		    if entity not in entities_tagged:
			    entity_present = True
			    for word in entity:
			    	if word not in sentence:
					entity_present = False
		              		break
		    	    if entity_present:
				for word,pos in tagged_tokens:
					if word == entity[len(entity) - 1] and pos.startswith('NN'):
						# print entity,pos
                                                # print '--- ' + sentence
						entities_tagged[entity] = True
                                        if word == entity[0] and not (pos.startswith('NN') or pos.startswith('JJ') ):
                                            if entity in entities_tagged:
						# print `entity`+ ' deleted'
                                                del entities_tagged[entity]
                                            break
				
            sentenceCount = sentenceCount + 1
        reviewCount = reviewCount + 1
    # print entities_tagged
    return nouns,verbs,adjectives,adverbs,candidate_sentences,collocation_tagged,entities_tagged



