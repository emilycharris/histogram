# histogram
histogram homework 

_This assignment was completed as part of my coursework at The Iron Yard._

###Assignment

Write a program that opens a file called sample.txt. Your program should read this file and then return the top 20 words used in the text and the number of times they are used.

**Objectives**

This assignment is designed to understand how to open and read from a file, work with dictionaries, and sort a list. The learning objective for this assignment is to understand how to reduce a collection of text (a book) into another form (a frequency dictionary).

**Obtaining the file**

Download this file and place it into your project. sample.txt

**Normal Mode**

Your program should open sample.txt and read in the entirety of its text. You'll need to normalize the text so that words in different cases are still the same word and so it's scrubbed of punctuation. Once you've done that, go through the text and find the number of times each word is used.

After that, find the top 20 words used and output them to the console in reverse order, along with their frequency, like this:

peanut 33

racket 31

and 29

common 21

religion 15

fate 14

algorithm 10

the 9

...

**Hard Mode**

- In addition to the requirements from Normal Mode:

- Add a list of ignored words to your program and do not count those words in the word frequencies. A suggested list:

 - a,able,about,across,after,all,almost,also,am,among,an,and,any,are,as,at,be,because,been,but,by,can,cannot,could,dear,did,do,does,either,else,ever,every,for,from,get,got,had,has,have,he,her,hers,him,his,how,however,i,if,in,into,is,it,its,just,least,let,like,likely,may,me,might,most,must,my,neither,no,nor,not,of,off,often,on,only,or,other,our,own,rather,said,say,says,she,should,since,so,some,than,that,the,their,them,then,there,these,they,this,tis,to,too,twas,us,wants,was,we,wer,what,when,where,which,while,who,whom,why,will,with,would,yet,you,your

- Change your program so that you have to give it the name of the file to read on the command line, like so: python word_frequency.py sample.txt
- Output the words to the console in a simple text-based histogram format, like so:

peanut    #################################

racket    ###############################

and       #############################

common    #####################

religion  ###############

fate      ##############

algorithm ##########

the       #########

...

- Normalize the histogram so that you never have more than 50 # marks. You'll have to scale all the lines by some divisor if you have more than 50 of one word. It is ok to round down decimals with this. For example, if you have the word "the" 75 times and the word "and" 47 times, you'd have 50 # for "the" and 31 # for "and".
