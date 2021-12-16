#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json

#sol_1

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while not at_goal():
    if wall_in_front():
        turn_left()
        count = 0
        while not right_is_clear():            
            move()
            count+=1
        turn_right()
        move()
        turn_right()
        for i in range(0,count):
            move()
        turn_left()    
    else:
        move()

 #sol_2

 def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while not at_goal():
    if wall_in_front():
        turn_left()
        while not right_is_clear():            
            move()
        turn_right()
        move()
        turn_right()
        while front_is_clear():
            move()
        turn_left()    
    else:
        move()       