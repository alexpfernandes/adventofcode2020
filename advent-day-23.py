inputdata = '135468729'
sample = '389125467'


# This function builds the input into a dictionary of pointers to the next value.
# By example for the sample input, {3:8,8:9,9:1,...}
# If part2 is set to True, it also adds entries for 10-1000000
# Crucially, at the end, it makes sure the final entry points back to the beginning, making this circular
def cupstodict(cups,part2=False):
    cupdict = {}
    prev = 0
    for item in cups:
        cupdict[prev] = int(item)
        prev = int(item)
    if part2 == True:
        for num in range(10,1000001):
            cupdict[prev] = num
            prev = num
    cupdict[prev] = int(cups[0])
    del cupdict[0]
    return cupdict


# This function takes the dictionary of cups, and re-organizes the pointers for the
# three cups following the current cup
# Because the problem for part 2 is so large, I knew that I couldn't use naive list slicing methods,
# So I read online about "Linked Lists"
# I believe that this is an implementation of a linked list,
# and mapping it into a dictionary was inspired by a comment from reddit user /u/MikeyJSabin 
def cupturn(cupdict,cur_cup):
    a = cupdict[cur_cup]
    b = cupdict[a]
    c = cupdict[b]
    d = cupdict[c]
    dest_cup = cur_cup - 1
    while dest_cup in [0,a,b,c]:
        if dest_cup == 0:
            dest_cup = len(cupdict)
        else:
            dest_cup -= 1
    term_cup = cupdict[dest_cup]
    cupdict[dest_cup] = a
    cupdict[c] = term_cup
    cupdict[cur_cup] = d
    newcup = cupdict[cur_cup]
    return cupdict, newcup


# This function runs through the steps of the game and prints out a solution for each part of the puzzle
# It takes a few seconds to run on my machine, and I suspect that my implementation is far from perfect.
# I suspect that using a list (where the index is the cup label and the value is the pointer)
# might be faster because of the way python handles lists vs dictionaries, but I'm not sure.
def playcups(cups,turns,part2=False):
    cupdict = cupstodict(cups,part2)
    newcup = int(cups[0])
    for turn in range(turns):
        cupdict, newcup = cupturn(cupdict,newcup)
    if part2 == False:
        print('Solution to Part 1:')
        prev = 1
        accum = ''
        for i in range(len(cupdict)-1):
            accum += str(cupdict[prev])
            prev = cupdict[prev]
        print(accum)
    else:
        print('Solution to Part 2:')
        a = cupdict[1]
        b = cupdict[a]
        print(a*b)


playcups(inputdata,100,part2=False)
playcups(inputdata,10000000,part2=True)
