def turn_right():
    for left in range(3):
        turn_left()
def wall():
    turn_left()
    move()
    while wall_on_right() == True:
        move()
    turn_right()
    move()
    turn_right()
    while wall_in_front() == False:
        move()
    turn_left()
while not at_goal():
    if wall_in_front():
        wall()
    else:
        move()
    
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
