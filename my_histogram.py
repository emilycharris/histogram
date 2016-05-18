import string

with open("sample.txt") as opened_file:
    book = opened_file.read()

for p in string.punctuation:
    book = book.replace(p, "")
    book = book.replace("/n", "")


histogram = {}

for word in book.split(" "):
    if word in histogram.keys():
        histogram[word] += 1
    else:
        histogram[word] = 1

for key, value in histogram.items():
    print(key, value)

#print(histogram)

#hard mode - you have to sort smallest to largest occurence *you can sort a list, not dictionary
#also to draw out the amount of # signs for that
#string multiplication print("#" * 20)