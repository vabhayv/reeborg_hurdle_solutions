def turn_right():
    for left in range(3):
        turn_left()
def sequence():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
while at_goal() == False:
    sequence()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
