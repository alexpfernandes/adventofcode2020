samplecard = 5764801
sampledoor = 17807724
card = 14012298
door = 74241
subject = 7
modulator = 20201227


# This function returns the number of modulation loops required for each of the public keys
def loopcount(card,door,subject,modulator):
    value = 1
    loopsize_card = 0
    loopsize_door = 0
    loop = 1
    while loopsize_card == 0 or loopsize_door == 0:
        value = (value * subject) % modulator
        if value == card:
            loopsize_card = loop
        if value == door:
            loopsize_door = loop
        loop += 1
    return loopsize_card, loopsize_door        


# This function figures out the encrypted key based on the loop size from the loopcount function
def hack(card,door,loopsize_card,loopsize_door,modulator):
    value_card = 1
    value_door = 1
    loop = 1
    while loop <= loopsize_card or loop <= loopsize_door:
        value_card = (value_card * card) % modulator
        value_door = (value_door * door) % modulator
        if loop == loopsize_card:
            key_door = value_door
        if loop == loopsize_door:
            key_card = value_card
        loop += 1
    if key_card == key_door:
        print('Success! Encrypted key is')
        print(key_card)
    else:
        print('Hacking failure! Something went wrong.')


loopsize_card, loopsize_door = loopcount(card,door,subject,modulator)
hack(card,door,loopsize_card,loopsize_door,modulator)
