sample = [0,3,6]
inputdata = [0,8,15,2,12,1,4]


# This functions naively builds a list of the spoken numbers and searches backwards through the list
# This is O(n^2) because the index() function serves as a growing loop within the turn loop
def memorygame_naive(start_nums, end_turn):
    spoken = start_nums[:]
    turn = len(spoken) + 1
    while turn <= end_turn:
        last = spoken[-1]
        history = spoken[:-1]
        if last in history:
            distance = list(reversed(history)).index(last) + 1
            spoken.append(distance)
        else:
            spoken.append(0)
        turn += 1
    return spoken[end_turn-1]


# Solution 1
memorygame_naive(inputdata,2020)


# This function is smarter, and it uses a dictionary to remember the turn count of the last time each value was seen
# Because pulling a value from a dictionary is constant, this is now a O(n) solution
def memorygame_hashed(start_nums, end_turn):
    history = {}
    for value, num in enumerate(start_nums[:-1]):
        history[num] = value + 1
    turn = len(start_nums) + 1
    last = start_nums[-1]
    while turn <= end_turn:
        if last in history:
            distance = turn - history[last] - 1
            history[last] = turn - 1
            last = distance
        else:
            history[last] = turn - 1
            last = 0
        turn += 1
    return last


# Solution 2
memorygame_hashed(inputdata,30000000)


# Just a little time test to prove that the hashed solution is better than the naive approach
import time
print('Turns','Naive','Hashed')
for i in range(1,6):
    start1 = time.time()
    memorygame_naive(inputdata,10**i)
    end1 = time.time()
    memorygame_hashed(inputdata,10**i)
    end2 = time.time()
    print('10^' + str(i), ' {:.2f}'.format(end1-start1), ' {:.2f}'.format(end2-end1))
