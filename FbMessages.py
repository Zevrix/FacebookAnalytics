#reads txt database and allows me to query info in IDLE

f = open('Facebookmessages.txt',"r")

lines = f.readlines()

L1 = []
friends = {}

for line in lines:
    words = line.split('|')
    L1.append([words[0].rstrip(),words[1].rstrip(),words[2].rstrip()])
    if words[0].rstrip() not in friends:
        friends[words[0].rstrip()] = 0
    friends[words[0].rstrip()] += 1

def look(name,message):
    count = 0
    for x in L1:
        if name in x[0] and message in x[2]:
            print(x)
            count += 1
    return count

def date(date):
    count = 0
    for x in L1:
        if date in x[1]:
            print(x)
            count += 1
    return count

def wordFrequency(word,name):
    totalMessages = 0
    totalWord = 0
    for x in L1:
        if name in x[0]:
            totalMessages += 1
        totalWord += x[2].count(word)
    print(totalWord/totalMessages*100,"% of",name,"'s messages contain the word '",word,"'.")

def averageWordLength(L2):
    letters = 0
    words = 0
    for x in L2:
        m = x[2].split(" ")
        for y in m:
            letters += len(y)
        words += len(m)
    return letters/words

def generateMessages(name):
    L2 = []
    for x in L1:
        if name in x[0]:
            L2.append(x)
    return L2

L2 = generateMessages("Arash")
wordLength = 0

