import csv
with open('aoc3data.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    datalist = []
    for row in reader:
        for item in row:
            datalist.append(item)
            
def treecount(treemap, xslope, yslope):
    # This will count the number of trees '#' in a map of open spaces '.'
    # The path taken is a straight line from cell to cell with an X and Y slope
    # A positive X slope is movement to the right, a positive Y slope is movement down
    # Movement off the right edge can be interpreted as wrapping around to the other side
    
    width = len(treemap[0])
    totalsteps = int(len(treemap)/yslope) + (len(treemap) % yslope > 0)
    xposition = 0
    path = []
    
    for step in range(totalsteps):
        path.append(datalist[step*yslope][xposition])
        xposition += xslope
        if xposition >= width:
            xposition -= width
    
    return path.count('#')

# Solution #1
treecount(datalist, 3, 1)

# Solution #2
trees = []
for slope in slopelist:
    trees.append(treecount(datalist, slope[0], slope[1]))

solution = 1
for tree in trees:
    solution *= tree
    
print(solution)
