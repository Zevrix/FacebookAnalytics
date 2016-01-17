#reads txt database and allows me to query info in IDLE

f = open('Facebookmessages.txt',"r")

lines = f.readlines()

L1 = []

for line in lines:
    words = line.split('|')
    L1.append([words[0].rstrip(),words[1].rstrip(),words[2].rstrip()])

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

L2 = []
L3 = []

for x in L1:
    if x[0] == 'Arashdeep Rai':
        L2.append(x)

