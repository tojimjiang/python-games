#While loop for input:
allowed_input = 0
while allowed_input == 0:
    bottles = int(input('How many bottles of beer on the wall? '))
    if bottles > 0:
        allowed_input += 1
        print()
    else:
        print('Sorry, that\'s not a valid number of bottles. Try again.')
        print()
#Running program for any bottles of beer greater than one
while bottles != 0:
    if bottles > 1:
        plural = 'bottles'
    else:
        plural = 'bottle'
    print(bottles, plural,'of beer on the wall,',bottles, plural,'of beer.')
    bottles -= 1
    if bottles > 1:
        plural = 'bottles'
    else:
        plural = 'bottle'
    if bottles != 0:
        print('Take one down, pass it around,',bottles,plural,'of beer on the wall.')
        print()
    else:
        print('Take it down, pass it around, no more bottles of beer on the wall.')
