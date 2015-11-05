import json, csv, gzip, sys


def parse(path):
  g = gzip.open(path, 'r')
  for l in g:
    yield eval(l)


fields = {"asin", "reviewerID", "reviewerName", "review", "overall", "summary", "unixReviewTime", "reviewTime"}
csvOut = gzip.open('reviews_'+sys.argv[1]+'.csv.gz','w')
writer = csv.writer(csvOut)

i=0
for product in parse('reviews_'+sys.argv[1]+'.json.gz'):
    line = []
    for f in fields:
        if product.has_key(f):
            line.append(str(product[f]).strip())
        else:
            line.append('')
        print i
    i = i+1
    writer.writerow(line)
