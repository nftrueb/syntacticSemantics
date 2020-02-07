# ----------------------------------------------------------------
#                   Syntactically Symantic
#
#   Original code development began on January 31, 2020
#   Orginal author: Nicholas Trueb
#
#   This code is intended for use in learning the basics
#   of python programming and computer logic by young students
#   specifically those enrolled in the NSLC Engineering Program
#
#   Use of accompanied txt files provides a list of various
#   types of words (nouns, verbs, adjectives, etc.) The program
#   builds random sentences of varying complexity that follow
#   the correct grammar rules of the English language, but
#   themselves do not carry any actual meaning.
#
# ----------------------------------------------------------------


import random

# def word(type):
# argument  -   type : integer indicating noun, verb, adj., etc.
# return    -   word : word that has been randomly selected to be subbed
#                      into the sentence that is being constructed
#               -1   : if type is not within valid bounds
#
# The correct type of word is first selected by wordTypes[type]
# A random integer index is generated to select a word of that type
# A space is added to the end for continuity in the output

def word(type):
    if(type < 0 and type >= len(wordTypes)):
        return -1
 
    word = wordTypes[type][random.randint(0, len(wordTypes[type])-1)]
    word += ' '
    return word

def concatenate(arr):
    ret = ''
    return ret.join(arr)

def getArticle(index, sentence, offset):
    print(index)
    if(random.randint(0,1) == 0):
        if(len(sentence) != 0):
            firstChar = sentence[index][0]
            if(firstChar == 'a' or firstChar == 'e' or firstChar == 'i' or firstChar == 'o' or firstChar == 'u'):
                sentence.insert(index, articles[0 + offset]) # An
            else:
                sentence.insert(index, articles[1 + offset]) # A
        else:
            sentence.insert(index, articles[2 + offset]) # The
    else:
        sentence.insert(index, articles[2 + offset]) # The 

#open files in read-only mode to load words
nounFile = open("nouns.txt",'r')
verbFile = open("verbs.txt",'r')
adjFile = open("adj.txt", 'r')
prepFile = open("prepositions.txt", 'r')

articles = ["An ", "A ", "The ", "an ", "a ", "the "] #, "A ", "the ",  "a "]
numArticles = 3
conjunctions = ["and ", "but ", "or "]
nouns = [] #0
verbs = [] #1
adjs = []  #2
preps = [] #3

wordTypes = [nouns, verbs, adjs, preps]

#populate word arrays with all words from the files
#close files after use
for i in nounFile:
    nouns.append(i.replace('\n', ''))
nounFile.close()

for i in verbFile:
    verbs.append(i.replace('\n', ''))
verbFile.close()

for i in adjFile:
    adjs.append(i.replace('\n', ''))
adjFile.close()

for i in prepFile:
    preps.append(i.replace('\n', ''))
prepFile.close()

#make varying complexity sentences
#nouns = [] #0
#verbs = [] #1
#adjs = []  #2
#preps = [] #3
sentence = []
numAdj = random.randint(1,2)

indexBeforeAdjs = len(sentence) - 1
if(indexBeforeAdjs == -1):
    indexBeforeAdjs = 0

for i in range(numAdj):
    sentence.append(word(2))

#get correct article in beginning of sentence
getArticle(indexBeforeAdjs,sentence,0)

# add noun
sentence.append(word(0))
sentence.append(word(1))
if(random.randint(0,1) == 1):
    sentence.append(word(3))
    # add preposition
    indexBeforeAdjs = len(sentence) 

    for i in range(numAdj -1):
        sentence.append(word(2))
    getArticle(indexBeforeAdjs, sentence, numArticles)
    sentence.append(word(0))

print(sentence)
final = concatenate(sentence)
final = final[:len(final)-1] + '.'
print(final)

#make output file and generate sentences
#output = open("output.txt", "w+")
#for _ in range(3):
#   paragraph = '   '
#    for i in range(10):
#        sentence = "The " + word(2) + word(0) + word(1) + word(3) + "the " + word(2) + word(0)
#        paragraph += sentence[:len(sentence)-1] + '. '
#        
#    print(paragraph)
#    print('')
#    output.write(paragraph + "\n\n")
#output.close()



