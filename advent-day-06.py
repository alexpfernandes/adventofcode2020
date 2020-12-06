# This will open a text file, split it into a list of each line
file = open('aoc6.txt',newline='')
questions = file.read().splitlines()
file.close()


# This will parse the list of individual question responses into a parent list of parties, with child lists of individuals
def questionparser(questions):
    group = []
    parties = []
    for line in questions:
        if line == '':
            parties.append(group)
            group = []        
        else:
            group.append(line)
    if group not in []:
        parties.append(group)
    return parties
    
    
# This will count the unique letters in each party and sum the parties for Solution #1
def partyscore1(parties):    
    total = []
    for party in parties:
        total.append(len(set(''.join(party))))
    return sum(total)


# Solution to part #1
parties = questionparser(questions)
total = partyscore1(parties)
print(total)


# This will count the letters that are shared across all party members and provide a total sum for Solution #2
def partyscore2(parties):
    total = []
    for party in parties:
        partysize = len(party)
        partyanswers = ''.join(party)
        partyscore = 0
        for letter in party[0]:
            if partyanswers.count(letter) == partysize:
                partyscore += 1
        total.append(partyscore)
    return sum(total)


# Solution to part #2
parties = questionparser(questions)
total2 = partyscore2(parties)
print(total2)
