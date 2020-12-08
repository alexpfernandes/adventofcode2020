# This will open a text file, split it into a list of each line
file = open('aoc8.txt',newline='')
inputdata = file.read().splitlines()


codelist = []
for line in inputdata:
    temp = line.split()
    temp[1] = int(temp[1])    
    codelist.append(temp)


def run_op(index, accumulator, instructions):
    if index in instructions:
        print(accumulator)
    else:
        instructions.append(index)
        if codelist[index][0] == 'acc':
            accumulator += codelist[index][1]
            run_op(index+1, accumulator, instructions)
        elif codelist[index][0] == 'nop':
            run_op(index+1, accumulator, instructions)
        else:
            run_op(index+codelist[index][1], accumulator, instructions)


run_op(0, 0 , [])
