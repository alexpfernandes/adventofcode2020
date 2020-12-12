# <This solution does not use dynamic programming / memoization during its recursion, and only fails to time-out because of the simplicity of the puzzle input>

# This will open a text file, split it into a list of each line
file = open('advent-day-10.txt',newline='')
inputdata = [int(item) for item in file.read().splitlines()]
file.close()
sample = [16,10,15,5,1,11,7,19,6,12,4]
sample2 = [28,33,18,42,31,14,46,20,48,47,24,23,49,45,19,38,39,11,1,32,25,35,8,17,7,9,4,2,34,10,3]
sample3 = [i for i in range(1,30)]


# This functions preps the input by adding the starting joltage [0] and the final device joltage [max+3] and sorting
def chargeprepper(inputdata):
    chargelist = inputdata.copy()
    chargelist.append(max(chargelist) + 3)
    chargelist.append(0)
    return sorted(chargelist)


# This function takes the prepped input and calculates the joltage differences used in the solution to part #1
def diffcounts(chargelist):
    diffs = []
    for item in chargelist:
        if item == 0:
            prev = 0
        else:
            diffs.append(item - prev)
            prev = item
    for num in set(diffs):
        print(num, diffs.count(num))
        
       
# This function takes the ordered list of charges and counts the number of values it can 'reach' --
# that is, how many values are 1, 2, or 3 jolts higher.
# The actual absolute value of each charger is unimportant for counting the number of possible paths,
# so instead I make a list of the number of possible choices from each value in the set of jolts.
def neighbormaker(chargelist):
    neighborlist = []
    for index, charge in enumerate(chargelist):
        if index == len(chargelist)-1:
            break
        else: 
            rem_list = [item - 3 for item in chargelist[index+1:]]
            neighborlist.append(sum(1 if x <= charge else 0 for x in rem_list))
    return neighborlist
    
    
# This function needs some explaination.
# I was daunted by the idea of trying to recursively search the entire chain of values,
# so instead I noticed that in trying to resolve a simple example by hand
# that the list of neighborcounts could be subdivided into units that could be multiplied together.
# As there is only one path through a [1] node, these can be ignored.
# a [3] or [2] mark the beginning of a subdivision chain, and they do not converge back to 1 path
# until they encounter one of this terminal pattern: [2,1,1]
# Each of those terminal patterns MUST pass through the final [1] in the list, and therefore reduce to a single path.
# By example: [0,1,2,3,6,9,12,15,16,17,18,19,22] 
# converts to this neighborlist [3,2,1,1,1,1,1,3,3,2,1,1]
# can be reduced to [3,2,1,1][1,1,1][3,3,2,1,1]
# which have the following number of paths: (4)(1)(7)
# and therefore 28 total options
def chargesplitter(difflist):
    chargeunits = []
    snipflag = False
    for index, charge in enumerate(difflist):
        if snipflag is False and charge != 1:
            snipflag = True
            startindex = index
        if snipflag is True and index >= 2:
            if difflist[index-2:index+1] == [2,1,1]:
                chargeunits.append(difflist[startindex:index+1])
                snipflag = False
    return chargeunits
    
    
# This is the recursive function that appends a 1 to a list every time there's a unique path.
# This is a bad way to do it, because it ought to use memoization, and I can't figure out a way
# to do that without completely rewriting my recursion method.
def chargesearch(sublist, accum):
    for i in range(1, sublist[0] + 1):
        if sublist[i] == 1:
            accum.append(1)
        else:
            chargesearch(sublist[i:], accum)


# This totals the number of paths by running each subdivision through the recursive loop and tallying their products
def chargepathcount(chargeunits):
    total = 1
    for unit in chargeunits:
        accum = []
        chargesearch(unit, accum)
        total *= sum(accum)
    return total
    
    
# This wraps together all these seperate functions and prints the (kinda) solution to part #1 and part #2
def analyzechargers(inputdata):
    chargelist = chargeprepper(inputdata)
    print('Counts for Solution #1')
    diffcounts(chargelist)
    neighborlist = neighbormaker(chargelist)
    chargeunits = chargesplitter(neighborlist)
    print('Path count for Solution #2')
    print(chargepathcount(chargeunits))
    
    
analyzechargers(inputdata)
