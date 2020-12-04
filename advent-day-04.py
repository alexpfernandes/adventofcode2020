file = open('aoc4.txt',newline='')
rawpassports = file.read().splitlines()

cleanpassports = []
temp = ''
for line in rawpassports:
    if line == '':
        cleanpassports.append(temp[1:].split(sep=' '))
        temp = ''
    else:
        temp = ' '.join([temp,line])
        
cleanpassports.append(temp[1:].split(sep=' '))

passportlist = []
for passport in cleanpassports:
    tempdict = {}
    for item in passport:
        temp = item.split(sep=':')
        tempdict[temp[0]] = temp[1]
    passportlist.append(tempdict)
    
validcount = 0

for passport in passportlist:
    fieldcount = sum(1 for i in passport if i != 'cid')
    if fieldcount == 7:
        validcount += 1

print(validcount)
