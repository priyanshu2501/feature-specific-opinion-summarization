import os,sys

def cluster_features(features):
    feature_list = [(len(i),i) for i in features]
    feature_list = sorted(feature_list,reverse = True)
    feature_list = [i[1] for i in feature_list]
    # print feature_list
    for i in range(0,len(feature_list)):
        if feature_list[i] == ('xxxx'):
            continue
        for j in range(i+1,len(feature_list)):
            if feature_list[j] == ('xxxx'):
                continue
            completely_present = True
            for word in feature_list[j]:
                if word not in feature_list[i]:
                    completely_present = False
            if completely_present:
                for sentence in features[feature_list[j]]:
                    features[feature_list[i]].append(sentence)
                del features[tuple(feature_list[j])]
                feature_list[j] = ('xxxx')
    # print [i for i in features]
    # print feature_list
    return features
