# This will open a text file, split it into a list of each line
file = open('advent-day-09.txt',newline='')
inputdata = file.read().splitlines()
file.close()


# This function searches a window of values for a pair that sum to the next value to the right of the window
def xmas_bug_finder(valuelist, preamblesize):
    for index, value in enumerate(valuelist[preamblesize:]):
        preamble = [item for item in valuelist[index : index + preamblesize]]
        for pre in preamble:
            diff = value - pre
            if diff in preamble and diff != pre:
                break
        else:
            return value


# This function loops through each value in the list searching for a cumulative sum that equals the target value
# This is bad way to do it, as it's O(n2) and we're looping through the same values repeatedly
def xmas_hack_naive(valuelist, targetvalue):
    for i in range(len(valuelist)):
        temp = 0
        for j in range(len(valuelist)):
            temp += valuelist[i+j]
            if temp == targetvalue:
                return min(valuelist[i:i+j+1]) + max(valuelist[i:i+j+1])
            elif temp > targetvalue:
                break


# This approach for solution #2 uses a 'sliding window' approach, cribbed from github user: elvinyhlee
# Because we're looking for sequential values, when our cumulative sum grows past the target value,
# instead of starting over with the next value in the outer loop,
# we can instead move the left bound on the cumulative list to the right and save a ton of needless iteration.
def xmas_hack_slidingwindow(valuelist, targetvalue):
    leftindex = 0
    rightindex = 0
    windowsum = 0
    while leftindex <= rightindex < len(valuelist):
        nextvalue = valuelist[rightindex]
        if windowsum + nextvalue < targetvalue:
            windowsum += nextvalue
            rightindex += 1
        elif windowsum + nextvalue > targetvalue:
            while windowsum + nextvalue > targetvalue:
                windowsum -= valuelist[leftindex]
                leftindex += 1        
        else:    
            return min(valuelist[leftindex : rightindex + 1]) + max(valuelist[leftindex : rightindex + 1])


# Set parameters and runs the functions for solution #1 and solution #2
preamblesize = 25
valuelist = [int(item) for item in inputdata]
print('Solution 1: ', xmas_bug_finder(valuelist, preamblesize))
print('Solution 2: ', xmas_hack_naive(valuelist, xmas_bug_finder(valuelist, preamblesize)))
