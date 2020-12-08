# This will open a text file, split it into a list of each line
file = open('advent-day-08.txt',newline='')
inputdata = file.read().splitlines()
file.close()


# This will parse the inputdata into a list of 2 elements: the command and the value
codelist = [[item[0], int(item[1])] for item in [line.split() for line in inputdata]]


# This function recursively follows the commands given in the codelist.
# It tracks the total accumulator value and uses the instructions list to track if it hits the same command line twice
def run_op(index, accumulator, instructions):
    if index in instructions or index == len(codelist):
        print(accumulator)
    else:
        instructions.append(index)
        command = codelist[index][0]
        value = codelist[index][1]
        if command == 'acc':
            accumulator += value
            run_op(index+1, accumulator, instructions)
        elif command == 'nop':
            run_op(index+1, accumulator, instructions)
        else:
            run_op(index+value, accumulator, instructions)


# This is the solution to part #1
run_op(0,0,[])


# This function recursively follows the commands given in the codelist.
# It returns 'Success' if it finds an instruction to run the very next command line after the end of the list.
def bug_search(index, instructions):
    if index in instructions:
        return 'Loop at command line '+ str(index)
    elif index == len(templist):
        return 'Success'
    else:
        instructions.append(index)
        command = templist[index][0]
        value = templist[index][1]
        if command in ['acc','nop']:
            return bug_search(index+1, instructions)
        else:
            return bug_search(index+value, instructions)


# This will iterate through the command list, flipping the command between nop and jmp if appropriate,
# and run the bug_search recursion on each modified list.
# It will describe the line to be changed when it finds a successful change.
from copy import deepcopy
commandflip = {'nop':'jmp', 'jmp':'nop'}

for num, line in enumerate(codelist):
    templist = deepcopy(codelist)
    if line[0] in commandflip:
        templist[num][0] = commandflip[templist[num][0]]
        if bug_search(0,[]) == 'Success':
            print('Command line ' + str(num) + ' should be changed to ' + str(templist[num]))
            
            
# Solution to part #2
codelist[264] = ['nop', 60]
run_op(0,0,[])
