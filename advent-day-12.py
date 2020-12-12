# This will open a text file, split it into a list of each line
file = open('advent-day-12.txt',newline='')
inputdata = file.read().splitlines()
instructions = [(i[0],int(i[1:])) for i in inputdata]
sample = [('F',10),('N',3),('F',7),('R',90),('F',11)]


def naiveshipmovement(directions, pos = None, facing = None):
    if pos == None:
        pos = [0,0]
    if facing == None:
        facing = 0  # facing of 0 is east, 90 is south, etc.
    move_dict = {'E':(1,0), 'W':(-1,0), 'N':(0,1), 'S':(0,-1)}
    facing_dict = {0:'E', 180:'W', 270:'N', 90:'S'}
    turn_dict = {'R':+1,'L':-1}

    for ins in directions:
        if ins[0] in ['R','L']:
            facing = (facing + turn_dict[ins[0]] * ins[1]) % 360
        elif ins[0] == 'F':
            direction = facing_dict[facing]
            pos[0] += move_dict[direction][0] * ins[1]
            pos[1] += move_dict[direction][1] * ins[1]
        else:
            pos[0] += move_dict[ins[0]][0] * ins[1]
            pos[1] += move_dict[ins[0]][1] * ins[1]

    print('Manhattan Distance:\n',abs(pos[0])+abs(pos[1]))


def smartshipmovement(directions, pos = None, waypoint = None):
    if pos == None:
        pos = [0,0]
    if waypoint == None:
        waypoint = [10,1] #waypoints are always relative to the ship position
    facing_dict = {0:lambda x,y:[x,y], #this rotates the waypoints on 'R' or 'L'
                   90:lambda x,y:[y,-x],
                   180:lambda x,y:[-x,-y],
                   270:lambda x,y:[-y,x]}
    move_dict = {'E':(1,0), 'W':(-1,0), 'N':(0,1), 'S':(0,-1)}
    turn_dict = {'R':(+1),'L':-1}

    for ins in directions:
        if ins[0] in ['R','L']:
            facing = (turn_dict[ins[0]] * ins[1]) % 360
            waypoint = facing_dict[facing](waypoint[0],waypoint[1])
        elif ins[0] in ['N','S','E','W']:
            waypoint[0] += move_dict[ins[0]][0] * ins[1]
            waypoint[1] += move_dict[ins[0]][1] * ins[1]
        else:
            pos[0] += waypoint[0] * ins[1]
            pos[1] += waypoint[1] * ins[1]

    print('Manhattan Distance:\n',abs(pos[0])+abs(pos[1]))


# Solution to part #1
naiveshipmovement(instructions)

# Solution to part #2
smartshipmovement(instructions)
