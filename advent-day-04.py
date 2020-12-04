# This will open a text file, split it into a list of each line
file = open('input4.txt',newline='')
rawpassports = file.read().splitlines()


# This will parse that input file as a list of lists of items,
# where each child-level list delimited by spaces, and each parent-level list is delimited by ''
cleanpassports = []
temp = ''
for line in rawpassports:
    if line == '':
        cleanpassports.append(temp[1:].split(sep=' '))
        temp = ''
    else:
        temp = ' '.join([temp,line])
# One final pass because the file does not end on an empty line -- this is lazy        
cleanpassports.append(temp[1:].split(sep=' '))


# This will split the child lists into dictionaries based on the : separator
passportlist = []
for passport in cleanpassports:
    tempdict = {}
    for item in passport:
        temp = item.split(sep=':')
        tempdict[temp[0]] = temp[1]
    passportlist.append(tempdict)
    
    
def validpassports1(inputlist):
    # This takes a list of dictionaries, and counts the number of keys in each, ignoring 'cid', for problem #1
    validcount = 0
    for passport in inputlist:
        fieldcount = sum(1 for i in passport if i != 'cid')
        if fieldcount == 7:
            validcount += 1
    return validcount


def validpassports2(inputlist):
    # This function first defines a series of functions to test each field on a passport,
    # then it iterates through each passport and counts those which have 7 valid fields, for problem #2
    
    # Each year field must be within a specific range like '2010'
    def year(value, lowerbound, upperbound):
        if value.isdigit() and lowerbound <= int(value) <= upperbound:
            return True
        return False
    
    # Heights must be in a form like '160cm' or '76in' and be in the appropriate range
    def height(value, in_lower, in_upper, cm_lower, cm_upper):
        if value[-2:] == 'in':
             if value[:-2].isdigit() and in_lower <= int(value[:-2]) <= in_upper:
                    return True
        elif value[-2:] == 'cm':
            if value[:-2].isdigit() and cm_lower <= int(value[:-2]) <= cm_upper:
                    return True
        return False
    
    # Hair color must be a hex value with a specified length, and the string must start with #, as in '#13f456'
    def hair(value, length):
        if value[0] == '#' and len(value) == length + 1:
            try:
                int(value[1:], 16)
            except:
                return False
            else:
                return True
        return False
    
    # Eye color must be in a specific list of strings like 'blu'
    def eye(value, colors):
        if value in colors:
            return True
        return False
    
    # PID must be a series of digits of a specified length like '009192332'
    def passportid(value, length):
        if len(value) == length and value.isdigit():
            return True
        return False
    
    validcount = 0
    for passport in inputlist:
        fieldcount = 0
        for field in passport:
            if field == 'byr' and year(passport[field], 1920, 2002) is True:
                fieldcount += 1
            if field == 'iyr' and year(passport[field], 2010, 2020) is True:
                fieldcount += 1    
            if field == 'eyr' and year(passport[field], 2020, 2030) is True:
                fieldcount += 1    
            if field == 'hgt' and height(passport[field], 59, 76, 150, 193) is True:
                fieldcount += 1    
            if field == 'hcl' and hair(passport[field], 6) is True:
                fieldcount += 1    
            if field == 'ecl' and eye(passport[field], ['amb','blu','brn','gry','grn','hzl','oth']) is True:
                fieldcount += 1    
            if field == 'pid' and passportid(passport[field], 9) is True:
                fieldcount += 1       
        if fieldcount == 7:
            validcount += 1
    
    return validcount
