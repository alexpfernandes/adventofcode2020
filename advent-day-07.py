# This will open a text file, split it into a list of each line
file = open('aoc7.txt',newline='')
inputdata = file.read().splitlines()
file.close()


# This will parse the input data into a dictionary of dictionaries
# where the top-level dictionary is the parent bag
# and the sub-level dictionary is the associated children bag as the key and bag count as the value
rulesdict = {}
for line in inputdata:
    templist = line.split(' bags contain')
    templist[1] = templist[1].split(',')
    tempdict = {}
    for bag in templist[1]:
        temp = bag.rstrip('bags.').strip().split(' ',1)
        tempdict[temp[1]] = temp[0]
    rulesdict[templist[0]] = tempdict
    
    
# This function recursively searches the rules in the given bag and collects the bags and their counts in a dictionary
def bagsearch(bag, bag_count, searchlist):
    for item in rulesdict[bag].items():
        if item[0] == 'other':
            pass
        else:
            if item[0] in searchlist:
                searchlist[item[0]] += bag_count * int(item[1])
            else:
                searchlist[item[0]] = bag_count * int(item[1])
            bagsearch(item[0], bag_count * int(item[1]), searchlist)
            
            
# This does uses the recursive function to map the total bag contents of each type of bag, evaluted as the top-level
searchedbags = {}
for topbag in rulesdict.keys():
    searchlist = {}
    bagsearch(topbag, 1, searchlist)
    searchedbags[topbag] = searchlist
    
    
# Solution to part #1, find all top level bags that contain 'shiny gold'
sum([1 for bag in searchedbags.values() if 'shiny gold' in bag])


# Solution to part #2, count all child bags inside of 'shiny gold'
sum([number for number in searchedbags['shiny gold'].values()])
