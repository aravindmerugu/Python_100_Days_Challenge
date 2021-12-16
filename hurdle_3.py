#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json

#sol_1
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    while front_is_clear():
        if not at_goal():
            move()
        else:
            break
    while wall_in_front():
        turn_left()
        move()
        turn_right()
        move()
        turn_right()
        move()
        turn_left()
    
while not at_goal():
    jump()


#sol_2
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    while wall_in_front():
        turn_left()
        move()
        turn_right()
        move()
        turn_right()
        move()
        turn_left()
    
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()