# This will open a text file, split it into a list of each line
file = open('aoc13.txt',newline='')
inputdata = file.read().splitlines()
inputdata[1] = [i for i in inputdata[1].split(',')]
sample = [67,7,59,61]


# Part #1 Solution
bustimes = {}
time = int(inputdata[0])
for bus in inputdata[1]:
    if bus != 'x':
        bustimes[int(bus)] = (time - (time % int(bus)) + int(bus))
nextbustime = min([i for i in bustimes.values()])
nextbus = [key for key,value in bustimes.items() if value == nextbustime][0]
print('Part 1 Solution:',(nextbustime-time)*nextbus)


# List of just the bus numbers
bus_list = [int(i) for i in inputdata[1] if i != 'x']

# List of the time offsets between each bus, marked by 'x'
x_count = 0
timeoffset_list = []
for item in inputdata[1][1:]:
    if item == 'x':
        x_count += 1
    else:
        timeoffset_list.append(x_count+1)
        x_count = 0
timeoffset_list.append(1)


# This function checks through values based on the cumulative product of buses and previously returned value
def calculord(bus, cum_product, offset, timeoffset):
    i = 1
    check = False
    while check == False:
        value = i * cum_product + offset - timeoffset
        if value % bus == 0:
            return value, bus*cum_product
            check = True
        i += 1
        
        
# Loop through the list backwards, using each pass to reduce the set of values that need to be checked
offset = 0
cum_product = 1
for i in range(len(bus_list)-1,-1,-1):
    bus = bus_list[i]
    timeoffset = timeoffset_list[i]
    offset, cum_product = calculord(bus, cum_product, offset, timeoffset)
print('Final Value:',offset)
