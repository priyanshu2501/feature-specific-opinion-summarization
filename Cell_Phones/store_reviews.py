import json
data = json.load(open('Reviews.json','r'))
data = json.loads(data)

for asin in data:
    if len(asin) < 2:
        continue
    f = open('Reviews/'+asin.encode('ascii')+'.txt','w')
    for rid in data[asin]:
        f.write('\n'+data[asin][rid][0]+'\n')
    f.close()
    print asin

