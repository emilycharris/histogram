import string

with open("sample.txt") as opened_file:
    book = opened_file.read().lower()

for p in string.punctuation:
    book = book.replace(p, "")
    book = book.replace("\n", " ")
    book = book.replace("  "," ")

histogram = {}

for word in book.split(" "):
    if word in histogram.keys():
        histogram[word] += 1
    else:
        histogram[word] = 1

import operator
sorted_hist = sorted(histogram.items(), key=operator.itemgetter(1))
for idx, item in enumerate(sorted_hist[:-21:-1]):
    word, count = item
    print(idx + 1, word, count)
#print(sorted_hist[:-21:-1])