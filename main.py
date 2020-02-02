import random

def noun():
    noun = nouns[random.randint(0,len(nouns)-1)]
    noun += ' ' 
    return noun

def verb():
    verb = verbs[random.randint(0,len(verbs)-1)]
    verb += ' '
    return verb

def adj():
    adj = adjs[random.randint(0, len(adjs)-1)]
    adj += ' ' 
    return adj

def prep():
    prep = preps[random.randint(0, len(preps)-1)]
    prep += ' ' 
    return prep

#open files to obtain words
nounFile = open("nouns.txt",'r')
verbFile = open("verbs.txt",'r')
adjFile = open("adj.txt", 'r')
prepFile = open("prepositions.txt", 'r')

nouns = []
verbs = []
adjs = []
preps = []

#populate word arrays
for i in nounFile:
    nouns.append(i.replace('\n', ''))
nounFile.close()

for i in verbFile:
    verbs.append(i.replace('\n', ''))
    print(verbs)
verbFile.close()

for i in adjFile:
    adjs.append(i.replace('\n', ''))
adjFile.close()

for i in prepFile:
    preps.append(i.replace('\n', ''))
prepFile.close()

#make output file and generate sentences
output = open("output.txt", "w+")
for i in range(10):
    sentence = "The " + adj() + noun() + verb() + prep() + "the " + adj() + noun() + '\n'
    output.write(sentence)
    print(sentence)
output.close()



