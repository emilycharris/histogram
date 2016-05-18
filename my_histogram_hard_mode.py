import string

ignore_string = "a,able,about,across,after,all,almost,also,am,among,an,and,any,are,as,at,be,"\
"because,been,but,by,can,cannot,could,dear,did,do,does,either,else,ever,every,"\
"for,from,get,got,had,has,have,he,her,hers,him,his,how,however,i,if,in,into,is,"\
"it,its,just,least,let,like,likely,may,me,might,most,must,my,neither,no,nor,"\
"not,of,off,often,on,only,or,other,our,own,rather,said,say,says,she,should,"\
"since,so,some,than,that,the,their,them,then,there,these,they,this,tis,to,too,"\
"twas,us,wants,was,we,were,what,when,where,which,while,who,whom,why,will,with,"\
"would,yet,you,your"

ignore_list = ignore_string.split(",")

with open("sample.txt") as opened_file:
    book = opened_file.read().lower()

for p in string.punctuation:
    book = book.replace(p, "")
    book = book.replace("\n", " ")
    book = book.replace("  "," ")

histogram = {}

for word in book.split(" "):
    if word in ignore_list:
        del word
    else:
        if word in histogram.keys():
            histogram[word] += 1
        else:
            histogram[word] = 1

import operator
sorted_hist = sorted(histogram.items(), key=operator.itemgetter(1))
for idx, item in enumerate(sorted_hist[:-21:-1]):
    word, count = item
    print(idx + 1, word, count)