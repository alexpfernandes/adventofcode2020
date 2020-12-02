def parse_password_data(string):
    # This function the password data into the 4 usable components: e.g. "1-9 x: xwjgxtmrzxzmkx"
    
    minbound, maxbound, letter, passwords = [], [], [], []
    for line in string:
        firstpart = line.split(sep = '-')
        secondpart = firstpart[-1].split(sep = ' ', maxsplit = 1)
        thirdpart = secondpart[-1].split(sep = ': ')
        minbound.append(int(firstpart[0]))
        maxbound.append(int(secondpart[0]))
        letter.append(str(thirdpart[0]))
        passwords.append(str(thirdpart[-1]))

    return minbound, maxbound, letter, passwords

def password_analyzer_one(minbound, maxbound, letter, passwords):
    # This function test the validity of the password based on the rules:
        # Each line gives the password policy and then the password.
        # The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid.
        # For example, "1-3 a" means that the password must contain a at least 1 time and at most 3 times.
        
    valid_count = 0
    for i in range(len(passwords)):
        occurances = passwords[i].count(letter[i])
        if minbound[i] <= occurances <= maxbound[i]:
            valid_count += 1
    
    return valid_count

def password_analyzer_two(minbound, maxbound, letter, passwords):
    # This function test the validity of the password based on the rules:
        # Each policy actually describes two positions in the password, where 1 means the first character, 2 means the second character, and so on.
        # (Be careful; Toboggan Corporate Policies have no concept of "index zero"!)
        # Exactly one of these positions must contain the given letter.
        # Other occurrences of the letter are irrelevant for the purposes of policy enforcement.
        
    valid_count = 0
    for i in range(len(passwords)):
        firstpos = passwords[i][minbound[i]-1] == letter[i]
        secondpos = passwords[i][maxbound[i]-1] == letter[i]
        # XOR hack
        if firstpos != secondpos:
            valid_count += 1
    
    return valid_count