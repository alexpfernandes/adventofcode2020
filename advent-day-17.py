# This will open a text file, split it into a list of each line
file = open('advent-day-17.txt',newline='')
inputdata = [file.read().splitlines()]
sample = [['.#.','..#','###']]


from copy import deepcopy
from itertools import product


neighbors = list(product([-1,0,1],repeat=3))
del neighbors[neighbors.index((0,0,0))]


def print_state(array, step):
    print('Step =',step)
    total = 0
    for num, z in enumerate(array):
        print('z =',num-(len(array)-1)//2)
        for line in z:
            print(line)
            total += line.count('#')
        print('\n')
    print('Active Cells =',total,'\n')


def pad_array(array):
    padded_array = deepcopy(array)
    side = len(array[0])
    for znum, z in enumerate(array):
        for ynum, y in enumerate(z):
            padded_array[znum][ynum] = '.' + array[znum][ynum] + '.'
        padded_array[znum] = [''.join('.'*(side+2))] + padded_array[znum] + [''.join('.'*(side+2))]
    z_padding = [''.join('.'*(side+2)) for i in range(side+2)]
    padded_array = [z_padding] + padded_array + [z_padding]
    return padded_array


def growth_step(array):
    nextarray = deepcopy(array)
    max_z = len(nextarray) - 1
    max_xy = len(nextarray[0]) - 1
    for znum, zslice in enumerate(array):
        for ynum, yslice in enumerate(zslice):
            for xnum, xslice in enumerate(yslice):
                count = 0
                for z,y,x in neighbors:
                    if (0 <= znum+z <= max_z) and (0 <= ynum+y <= max_xy) and (0 <= xnum+x <= max_xy):
                        if array[znum+z][ynum+y][xnum+x] == '#':
                            count += 1
                if count == 3:
                    nextarray[znum][ynum] = nextarray[znum][ynum][:xnum] + '#' + nextarray[znum][ynum][xnum+1:]
                elif count == 2 and xslice == '#':
                    nextarray[znum][ynum] = nextarray[znum][ynum][:xnum] + '#' + nextarray[znum][ynum][xnum+1:]
                else:
                    nextarray[znum][ynum] = nextarray[znum][ynum][:xnum] + '.' + nextarray[znum][ynum][xnum+1:]
    return nextarray            


def conway_cube(array,steps,show=False):
    if show == True:
        print_state(array,0)
    for step in range(1,steps+1):
        array = pad_array(array)
        array = growth_step(array)
        if show == True:
            print_state(array,step)
    print_state(array,steps)


# Solution to Part 1
conway_cube(inputdata,6)


neighbors_4d = list(product([-1,0,1],repeat=4))
del neighbors_4d[neighbors_4d.index((0,0,0,0))]


def print_state_4d(array, step):
    print('Step =',step)
    total = 0
    for wnum, w in enumerate(array):
        for znum, z in enumerate(w):
            print('w =',wnum-(len(array)-1)//2)
            print('z =',znum-(len(array[0])-1)//2)
            for line in z:
                print(line)
                total += line.count('#')
            print('\n')
    print('Active Cells =',total,'\n')


def mydeepcopy_4d(inputarray):
    copiedarray = []
    for wnum, w in enumerate(inputarray):
        tempz = []
        for znum, z in enumerate(w):
            tempy = []
            for ynum, y in enumerate(z):
                tempy.append(y)
            tempz.append(tempy)
        copiedarray.append(tempz)
    return copiedarray


def pad_array_4d(array):
    padded_array = deepcopy(array)
    zsize = len(array[0])
    ysize = len(array[0][0])
    for wnum, w in enumerate(array):
        for znum, z in enumerate(w):
            for ynum, y in enumerate(z):
                padded_array[wnum][znum][ynum] = '.' + array[wnum][znum][ynum] + '.'
            padded_array[wnum][znum] = [''.join('.'*(ysize+2))] + padded_array[wnum][znum] + [''.join('.'*(ysize+2))]
        z_padding = [''.join('.'*(ysize+2)) for i in range(ysize+2)]
        padded_array[wnum] = [z_padding] + padded_array[wnum] + [z_padding]
    w_padding = [[''.join('.'*(ysize+2)) for i in range(ysize+2)] for j in range(zsize+2)]
    padded_array = [w_padding] + padded_array + [w_padding]   
    return padded_array


def growth_step_4d(array):
    nextarray = mydeepcopy_4d(array)
    max_w = len(array) - 1
    max_z = len(array[0]) - 1
    max_xy = len(array[0][0]) - 1
    for wnum, wslice in enumerate(array):
        for znum, zslice in enumerate(wslice):
            for ynum, yslice in enumerate(zslice):
                for xnum, xslice in enumerate(yslice):
                    count = 0
                    if nextarray[wnum][znum][ynum][xnum] != array[wnum][znum][ynum][xnum]:
                        print(f"{wnum} {znum} {ynum} {xnum} WAS CHANGED BEFORE WE GOT TO IT!!!")
                    for w,z,y,x in neighbors_4d:
                        if (0 <= wnum+w <= max_w) and (0 <= znum+z <= max_z) and (0 <= ynum+y <= max_xy) and (0 <= xnum+x <= max_xy):
                            if array[wnum+w][znum+z][ynum+y][xnum+x] == '#':
                                count += 1
                    if count == 3:
                        nextarray[wnum][znum][ynum] = nextarray[wnum][znum][ynum][:xnum] + '#' + nextarray[wnum][znum][ynum][xnum+1:]
                    elif count == 2 and xslice == '#':
                        nextarray[wnum][znum][ynum] = nextarray[wnum][znum][ynum][:xnum] + '#' + nextarray[wnum][znum][ynum][xnum+1:]
                    else:
                        nextarray[wnum][znum][ynum] = nextarray[wnum][znum][ynum][:xnum] + '.' + nextarray[wnum][znum][ynum][xnum+1:]
    return nextarray            
    
    
def conway_hypercube(array,steps,show=False):
    if show == True:
        print_state_4d(array,0)
    for step in range(1,steps+1):
        padded_array = pad_array_4d(array)
        array = growth_step_4d(padded_array)
        if show == True:
            print_state_4d(array,step)
    print_state_4d(array,steps)


# Solution to Part 2
conway_hypercube([inputdata],6)
