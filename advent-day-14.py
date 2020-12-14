# This will open a text file, split it into a list of each line
file = open('advent-day-14.txt',newline='')
inputdata = file.read().splitlines()
sample = ['mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X','mem[8] = 11','mem[7] = 101','mem[8] = 0']
sample2 = ['mask = 000000000000000000000000000000X1001X','mem[42] = 100','mask = 00000000000000000000000000000000X0XX','mem[26] = 1']


# This looks through the input list and creates a data structure like:
# ['mem', [address, value]]
# ['mask', [bit number (starting from right), value]] skipping any 'X' because I thought it might be more efficient
def parsecommandlist(inputlist):
    commands = []
    for line in inputlist:
        if line[:3] == 'mas':
            templist = [[i,int(line[-i-1])] for i in range(36) if line[-i-1] != 'X']
            commands.append(['mask',templist])
        elif line[:3] == 'mem':
            temp = line.split(' ')
            templist = [int(temp[0][4:-1]), int(temp[2])]
            commands.append(['mem',templist])
    return commands


# This function takes the command list and builds a dictionary with the memory addresses and values
# Because I didn't know about bitwise operators, or really much about binary encoding, I did this all as string manipulations
# by looping through the mask and rebuilding the string one bit at a time, ouch
def applymask(commands):
    memory_dict = {}
    mask = []
    for line in commands:
        if line[0] == 'mem':
            value = bin(line[1][1])
            value = value[:2] + (38 - len(value)) * '0' + value[2:]
            for bit in mask:
                value = value[:37-bit[0]] + str(bit[1]) + value[38-bit[0]:]
            memory_dict[line[1][0]] = eval(value)
        elif line[0] == 'mask':
            mask = line[1]
    memory_sum = sum([i for i in memory_dict.values()])
    return memory_dict, memory_sum


# Solution to Part #1
commands = parsecommandlist(inputdata)
memory_dict, memory_sum = applymask(commands)
memory_sum


# This function converts a binary string containing 'X's and uses itertools.product
# to return a list of all permutations of that string with the X replaced with 0 or 1
# This works fine for the puzzle input, because there are at most 9 X, which is 2**9 permutations
# But it grows exponentially as the number of 'X's in the input masks increases
from itertools import product
def unfloater(string):
    value_list = []
    floatcount = string.count('X')
    floatvalues = product('01', repeat = floatcount)
    for f_value in floatvalues:
        newstring = ''
        i = 0
        for let in string:
            if let == 'X':
                newstring = newstring + f_value[i]
                i += 1
            else:
                newstring = newstring + let
        value_list.append(newstring)
    return value_list


# This is a simpler version of the command list parser:
# ['mem', [address, value]] or ['mask', mask string]
def parsecommandlist_v2(inputlist):
    commands = []
    for line in inputlist:
        if line[:3] == 'mas':
            commands.append(['mask',line[7:]])
        elif line[:3] == 'mem':
            temp = line.split(' ')
            templist = [int(temp[0][4:-1]), int(temp[2])]
            commands.append(['mem',templist])
    return commands


# This function uses unfloater to explode the mem command into a list of the affected addresses,
# then loops over those addresses to replace the dictionary value.
def applymask_v2(commands):
    from itertools import product
    memory_dict = {}
    mask = []
    for line in commands:
        if line[0] == 'mem':
            address = bin(line[1][0])
            address = address[:2] + (38 - len(address)) * '0' + address[2:]
            for i in range(36):
                if mask[i] in ['1','X']:
                    address = address[:i+2] + mask[i] + address[i+3:]
            address_list = unfloater(address)
            for add in address_list:
                memory_dict[eval(add)] = line[1][1] 
        elif line[0] == 'mask':
            mask = line[1]
    memory_sum = sum([i for i in memory_dict.values()])
    return memory_dict, memory_sum


# Solution to Part #2
commands = parsecommandlist_v2(inputdata)
memory_dict, memory_sum = applymask_v2(commands)
memory_sum
