#import random module
import random
side = 3
#ask for sides
while side < 4 or side > 20:
    side = int(input('How many sides on your dice (4-20)? '))
    if side < 4 or side > 20:
        print('Sorry, that\'s not a valid size value.')
print()
print('Thanks! Here we go ...')
print()
#rolling dice
double = 0
snake = 0
count = 0
first_sum = 0
second_sum = 0
while snake == 0:
    first_roll = random.randint(1,side)
    second_roll = random.randint(1,side)
    count += 1
    first_sum += first_roll
    second_sum += second_roll
    if first_roll == second_roll:
        double +=1
        if first_roll == 1:
            snake +=1
    print(count,'. die number 1 is ', first_roll, ' and die number 2 is ', second_roll, '.', sep='')
#breaks if snake eyes is achieved.
print()
print('You got snake eyes! Finally! On try number ',count,'!', sep='')
print('Along the way you rolled doubles ',double,' times (',format(double/count*100,'.2f'), '% of all rolls were doubles)', sep='')
print('The average roll for die #1 was',format(first_sum/count,'.2f'))
print('The average roll for die #2 was',format(second_sum/count,'.2f'))
