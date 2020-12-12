# This will open a text file, split it into a list of each line
file = open('advent-day-11.txt',newline='')
inputdata = file.read().splitlines()
file.close()
sample = ['L.LL.LL.LL','LLLLLLL.LL','L.L.L..L..','LLLL.LL.LL','L.LL.LL.LL',
          'L.LLLLL.LL','..L.L.....','LLLLLLLLLL','L.LLLLLL.L','L.LLLLL.LL']
          

# This function takes in the current 2d array of seats, width and height of the array, a list of which offsets qualify as neighbors, and the mode
# The mode denotes which solution is followed:
    # part 1 [prox] looks at the surrounding 8 spaces and counts occupied seats
    # part 2 [view] looks along each 8 directions, but skips over '.' spaces to count occupied seats
# In general, this method is iterating over the 2d array, and on each pass searching the space around each cell.
# One idea for improvement would be to take advantage of caching by remembering which cells have a locked-in neighbor count,
# by counting how many boundary cells, floor cells '.', or other locked-in cells it has for neighbors.
def neighbormap(seatstate, maxrow, maxcolumn, neighbors, neighborcount, mode):
    if mode == 'view':        
        for row_index, line in enumerate(seatstate):
            for col_index, value in enumerate(line):
                if value in ['#','L']:
                    for row, col in neighbors:
                        finished = False
                        multiplier = 1
                        while finished is False:
                            row_spot = row_index + row * multiplier
                            col_spot = col_index + col * multiplier
                            if 0 <= row_spot <= maxrow and 0 <= col_spot <= maxcolumn:
                                if seatstate[row_spot][col_spot] == '#':
                                    neighborcount[row_index][col_index] += 1
                                    finished = True
                                elif seatstate[row_spot][col_spot] == 'L':
                                    finished = True
                                else:
                                    pass
                            else:
                                finished = True
                            multiplier += 1   
    elif mode == 'prox':
        for row_index, line in enumerate(seatstate):
            for col_index, value in enumerate(line):
                if value == '#':
                    for row, col in neighbors:
                        if 0 <= row_index + row <= maxrow and 0 <= col_index + col <= maxcolumn:
                            neighborcount[row_index + row][col_index + col] += 1
    return neighborcount
    
    
# This function takes the same information as the neighbormap function, initializes values,
# runs the neighbormap function to figure out each cells' number of neighboring occupied seats,
# then fills a new copy of the seat state with the next iteration of the map, depending on mode.
# It also counts the changes made along the way for the purpose of finding equillibrium.
def nextseatstate(seatstate, maxrow, maxcolumn, neighbors, mode):
    nextstate = [['' for column in row] for row in seatstate]
    neighborcount = [[0 for column in row] for row in seatstate]
    changecount = 0
    seatlimit = {'prox':4,'view':5}[mode]
    
    neighborcount = neighbormap(seatstate, maxrow, maxcolumn, neighbors, neighborcount, mode)
        
    for row_index, line in enumerate(seatstate):
        for col_index, value in enumerate(line):
            if value == 'L' and neighborcount[row_index][col_index] == 0:
                nextstate[row_index][col_index] = '#'
                changecount += 1
            elif value == '#' and neighborcount[row_index][col_index] >= seatlimit:
                nextstate[row_index][col_index] = 'L'
                changecount += 1
            else:
                nextstate[row_index][col_index] = value
    return nextstate, changecount
    
    
# This function serves as the shell function to initialize the inputs for the subfunctions,
# and to run a while loop that will end when the seat state reaches equilibrium [0 changes]
# or an upper limit of loops is run. This failsafe could be made a lot more obvious.
def findequilibrium(inputchart, mode):
    maxrow = len(inputchart) - 1
    maxcolumn = len(inputchart[0]) - 1
    neighbors = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    state = [[i for i in line] for line in inputchart]
    changecount = 1
    loops = 0
    
    while changecount > 0 and loops < 1000:
        state, changecount = nextseatstate(state, maxrow, maxcolumn, neighbors, mode)
        loops += 1
    return state, loops-1
    
    
# Prints solutions to both part #1
finalstate, loopcount = findequilibrium(inputdata,'prox')
print('\nStep Count:',loopcount)
print('Filled seats:',sum([row.count('#') for row in finalstate]),'\n')
for line in finalstate:
    print(''.join(line))
    
    
# Prints solutions to both part #2
finalstate, loopcount = findequilibrium(inputdata,'view')
print('\nStep Count:',loopcount)
print('Filled seats:',sum([row.count('#') for row in finalstate]),'\n')
for line in finalstate:
    print(''.join(line))
