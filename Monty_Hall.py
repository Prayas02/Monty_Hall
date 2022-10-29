import random

i=0
county=0      # pointer to count the number of time he switches 
countn=0      # pointer to count the number of times he does'nt switch
countywin=0   # pointer to count the number of times he wins when he switches
countnwin=0   # pointer to count the number of times he wins when he does'nt switch

while i<1000:      # we test it for 1000 inputs 
    
    choice=random.randint(1,3)             # choice is random between 1-3 indicating the 3 doors
    print(f'The choice is {choice}')

    jackpot=random.randint(1,3)            # jackpot is random between 1-3 indicating the car
    print(f'The jackpot is {jackpot}')

    goat=random.randint(1,3)               # one goat which monty opens which can't be the jackpot or the choice 
    while goat==jackpot or goat==choice:
        goat=random.randint(1,3)

    print(f'One goat is opened {goat}')

    switch=random.randint(1,3)               # the swicting option which monty gives to the player
    while switch==choice or switch==goat:    # the switch should not be equal to the choice or the goat(already opened)
        switch=random.randint(1,3)
        
    list1=['y','n']          # list to store yes or no option
    

    option=random.choice(list1)
    print(f"Do you want to switch y/n, the option is {option}")

    if option=='y':
        county+=1       # it increments as the option is yes 
        choice=switch   # as the option is yes the switch has been made
        
    else:
        countn+=1       # it increments as the option is no


    if choice==jackpot:    
        print('Congo you won')
        if option=='y':    
            countywin+=1     # it increments if the option is yes and he wins
        else:
            countnwin+=1     # it increments if the option is no and he wins

    else:
        print('Sorry you lost')
    
    i+=1
    print('-------------')

print(f'The number of times he switches is {county} and the number of times he does not switch is {countn}')
print(f'Win % when he switches = {(countywin*100)/county}%')
print(f'Win % when he does not switch = {(countnwin*100)/countn}%')
