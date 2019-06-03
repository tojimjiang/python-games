#variables
sticks = 9
player = int(1)
#ask for number of sticks
while sticks < 10 or sticks > 100:
    sticks = int(input('How many sticks (10-100)? '))
    if sticks < 10:
        print('Sorry, that\'s too few sticks. Try again.')
    elif sticks > 100:
        print('Sorry, that\'s too many sticks. Try again.')
    else:
        print('Great Let\'s play ...')
#game
while sticks != 0:
    print()
    if player % 2 == 1:
        print('Turn: Player 1')
    else:
        print('Turn: Player 2')
    print('There are', sticks,'sticks on the table.')
    allowed_take = 1
    #check to make sure the number of sticks removed is allowed, in while loop
    while allowed_take != 0:
        take_away = int(input('How many sticks do you want to take (1, 2, or 3)? '))
        if take_away < 1 or take_away > 3:
            print('Sorry, that\'s not a valid number.')
            print()
        elif take_away > sticks:
            print('Sorry, that\'s more than the number of sticks you have!')
            print()
        else:
            allowed_take -= 1
    #remove sticsk, and change turns
    sticks -= take_away
    player += 1
#Verification thatthere are now zero sticks
if sticks == 0:
    print()
    print('There are no sticks left on the table! Game over.')
#This winner revereses as once the while loop breaks, the player number is not updated
if player % 2 == 1:
    print('Player 1 wins!')
else:
    print('Player 2 wins!')
