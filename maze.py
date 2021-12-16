#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
#sol_1
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def right():
    if front_is_clear():
            move()                       
    if wall_in_front():
        if not wall_on_right():
            turn_right()
        turn_left()
        if front_is_clear():
            move()
                
def no_right():
    turn_right()
    if not wall_in_front():
        move()
    
while not at_goal():
    if wall_on_right():
        right()
    else:
        no_right()

#sol_2

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while front_is_clear():
    move()
turn_left()    
    
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()


#sol_3

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def right():
    if front_is_clear():
            move()                       
    if wall_in_front():
        if not wall_on_right():
            turn_right()
        turn_left()
        if front_is_clear():
            move()
                
def no_right():
    if count >=13:
        turn_right()
        turn_right()
    turn_right()
    if not wall_in_front():
        move()
count = 1    
while not at_goal():
    if wall_on_right():
        right()
        count=0
    else:                    
        count+=1   
        no_right()


    
    