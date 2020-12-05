# This will open a text file, split it into a list of each line
file = open('aoc5.txt',newline='')
boardingpasses = file.read().splitlines()


def boardingpassconverter(boardingpasses):
    # This function reads through the list of boarding pass strings,
    # converts them to decimal, splits them into row and column,
    # and calculates the seat ID

    to_bin = {'F':'0',
             'B':'1',
             'L':'0',
             'R':'1'}

    seatnumbers = []
    for seat in boardingpasses:
        temp = seat
        for key, value in to_bin.items():
            temp = temp.replace(key, value)    
        row = int(temp[:7], 2)
        column = int(temp[-3:], 2)
        seat_id = row * 8 + column
        seatnumbers.append([row, column, seat_id])
        
    return seatnumbers
    

# This will return the largest seat_id value, solution to part #1
newlist = sorted(seatnumbers, key=lambda x: x[2])
max(newlist)[2]


def findopenseat(seatnumbers):
    # This function finds the first 'hole' in the seat_ids to identify the missing boarding pass

    temp = sorted(seatnumbers, key=lambda x: x[2])
    previous = 0
    for seat in temp:
        if previous != 0 and seat[2] - previous > 1:
            return previous + 1
        previous = seat[2]
        
        
# Solution to part 2
findopenseat(seatnumbers)
