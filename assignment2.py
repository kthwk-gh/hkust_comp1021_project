'''
student name:   Li Wai Keung
student id:     20199546
student email:  wkli@stu.ust.hk
'''

"""
COMP1021    Turtle Graphics - Game Programming
"""

import turtle
import random
import pygame
import time
import sys
"""
    Constants and variables
"""
# Part 1
# Set up constants and variables

# Window size
window_height = 600
window_width = 600

# The screen update interval
update_interval = 25

# Parameters for controlling the width of the river
river_width = 300
minimum_river_width = 100

# Border parameters
border_height = 600

# Parameters for gradually decreasing river width
river_width_update = 0.5

# How far should we stay away from the borders
safe_distance_from_border = border_height / 2 + 3

# Parameters for crocodiles
croc_number = 17
crocs = []
croc_speeds = []
croc_width = 50
croc_height = 47
croc_speed_min, croc_speed_max = 4, 17

# How far should we stay away from the crocodiles
safe_distance_from_croc = 15

# Add sounds
pygame.init()
pygame.mixer.init(buffer=16)
bgmusic = pygame.mixer.Sound('angry_birds_bgm.wav')
hit_sound = pygame.mixer.Sound('hit_sound.wav')

#increase stack space
sys.setrecursionlimit(100000)
#set up time
current_time = 0

time_turtle = turtle.Turtle()
time_turtle.hideturtle()
time_turtle.up()
time_turtle.goto (260, 240)

time_turtle.color("white")

def draw_timer():
    
    
    global current_time
    
    
    if current_time % 1000 == 0:
        time_turtle.clear()
        time_turtle.write(str(current_time//1000), font=("Arial", 20, "normal"), align="center")
    
    current_time = current_time + 100

#set up score
score = 0
score_turtle = turtle.Turtle()
score_turtle.hideturtle()
score_turtle.up()
score_turtle.goto(-150, 240)
score_turtle.color("white")
def draw_score_fast():
    global score
    score_turtle.clear()
    score += 100
    score_turtle.write(str(score), font=("Arial", 20, "normal"), align="center")
def draw_score_mid():
    global score
    score_turtle.clear()
    score += 50
    score_turtle.write(str(score), font=("Arial", 20, "normal"), align="center")
def draw_score_slow():
    global score
    score_turtle.clear()
    score += 10
    score_turtle.write(str(score), font=("Arial", 20, "normal"), align="center")
    

    


"""
    Helper function and event handler functions
"""

# Part 6
# Show a message when the game end
def gameover():
    #end message
    end_message = "You are dead!\n" + "You survived " + \
                  str(current_time//1000) +\
                  " seconds!\n" + "Your final score was " + str(score) + "!"
    turtle.home()
    turtle.color("white")
    turtle.write(end_message, align='center', font=("Arial", 36, "normal"))


# Part 2 (2 of 2)
# 2.2 Event handler for the turtle.ondrag() event
def moveplayerturtle(x, y):
    # Allow the turtle to move within the window only
    if x > -(window_width/2) and x < (window_width/2):
        turtle.goto(x, y)

# Event handler for the turtle.ontimer() event
def updatescreen():
    """
        This function does:
            1. Decrease the width of the river
            2. Check if the player has won the game
            3. Check if the player has hit the borders
            4. Move the crocodiles
            5. Check if the player has collided with a crocodile
            6. Update the screen
            7. Schedule the next update
    """
    
    # Global variables that will be changed in the function
    global river_width
    global score
    global croc_number
     #score label
    score_label = turtle.Turtle()
    score_label.hideturtle()
    score_label.up()
    score_label.goto(-240, 240)
    score_label.color("white")
    score_label.write("Score: ", font=("Arial", 20, "normal"), align="center")
    
    #update score
    score_turtle.write(str(score), font=("Arial", 20, "normal"), align="center")

    #time label
    label03_turtle = turtle.Turtle()
    label03_turtle.hideturtle()
    label03_turtle.up()
    label03_turtle.goto(200, 240)
    label03_turtle.color("white")
    label03_turtle.write("Time: ", font=("Arial", 20, "normal"), align="center")
    # Part 4.2
    # Decrease the width of the river by river_width_update
    if upper_river_border.ycor() > 350 :
        upper_river_border.sety(upper_river_border.ycor() - river_width_update)
    if lower_river_border.ycor() < -350:
        lower_river_border.sety(lower_river_border.ycor() + river_width_update)
    if river_width > minimum_river_width:
        river_width = river_width - (river_width_update*2)
    # Part 4.3
    # 4.3.1 Check if the player has won the game
    # If the player survives until the river gets to its narrowest 
    # width, he/she will win the game
    #if river_width <= minimum_river_width:
    #    bgmusic.stop()
    #    gameover("You survived the crocodile river!")
    #    return
    # 4.3.2 Check if the player has hit the borders
    # The vertical distance between the player's turtle and the 
    # borders must be large enough, otherwise the player loses
    # the game
    if upper_river_border.ycor() - turtle.ycor() < safe_distance_from_border or \
       (turtle.ycor() - lower_river_border.ycor()) < safe_distance_from_border:
        bgmusic.stop()
        hit_sound.play() 
        gameover()
        return
    # Part 5.2
    # Move the crocodiles
    # For every crocodile in crocodiles
    for i in range(croc_number):
        crocs[i].forward(croc_speeds[i])
        # 5.2.1. Move the crocodile to the left
        # 5.2.2. If the crocodile moves out of the screen, move it 
        #    to the right hand side and generate its speed and 
        #    position randomly
        if crocs[i].xcor() < -(window_width + croc_width) / 2:
            x = (window_width + croc_width) / 2
            y = random.uniform(-(river_width-croc_height)/2, (river_width-croc_height)/2)
            crocs[i].goto(x, y)
            croc_speeds[i]=random.uniform(croc_speed_min, croc_speed_max)
            if croc_speeds[i] > 36:
                draw_score_fast()
            if croc_speeds[i] >18 and croc_speeds[i] <=36:
                draw_score_mid()
            if croc_speeds[i] <=18:
                draw_score_slow()
        # Part 5.3
        # Check collision
        if turtle.distance(crocs[i]) < safe_distance_from_croc:
            bgmusic.stop()
            hit_sound.play()
            gameover()
            return
        
            
        
   
        
    #update the time  
    if upper_river_border.ycor() - turtle.ycor()> safe_distance_from_border and (turtle.ycor() - lower_river_border.ycor()) > safe_distance_from_border and turtle.distance(crocs[i]) > safe_distance_from_croc:
        
        draw_timer()
    
   
        
    
        

        # Part 3 (3-4 of 4)
    # 3.3. Update the screen
    # 3.4. Schedule an update in 'update_interval' milliseconds
    turtle.update()
    turtle.ontimer(updatescreen, update_interval)

    """
    Here is the entry point of the game
    
    First of all, we create turtles for each component
    in the game with turtle.Turtle().
    The components are:
        1. The player turtle
        2. Two big boxes used as borders of the river
        3. Ten crocodiles
    
    Then we set up the event handlers for:
        1. The ondrag handler to handle the player's control
        2. The ontimer handler to handle timer event for 
           regular screen update

    After all the components are ready, start the game
"""
# Part 1
turtle.setup(window_width, window_height) # Set the window size
#turtle.bgcolor("DarkBlue")
turtle.bgpic("space.gif")

# Part 3 (1 of 4)
# 3.1. Turn off the tracer here
turtle.tracer(False)


# Part 5.1
# Add the crocodile image to the pool of shapes
#turtle.addshape("crocodile.gif")
turtle.addshape("Minion_pig.gif")



# Part 4.1
# 4.1.1. Create the big boxes for upper border and lower border
upper_river_border = turtle.Turtle()
upper_river_border.up()
lower_river_border = turtle.Turtle()
lower_river_border.up()

turtle.addshape("upper_river_border.gif")
turtle.addshape("lower_river_border.gif")
upper_river_border.shape("upper_river_border.gif")
lower_river_border.shape("lower_river_border.gif")
# 4.1.2. Set the shape of the borders to "square"
#upper_river_border.shape("square")
#lower_river_border.shape("square")

# 4.1.3. Set the colour of the borders to "DarkOrange4"
#upper_river_border.color("DarkOrange4")
#lower_river_border.color("DarkOrange4")

# 4.1.4. Set the size of the borders
#upper_river_border.shapesize(30, 40)
#lower_river_border.shapesize(30, 40)

# 4.1.5. Set the initial y position of the borders
upper_river_border.sety((border_height + river_width) / 2)
lower_river_border.sety(-(border_height + river_width) / 2)

# Prepare the player turtle
#turtle.shape("turtle")
#turtle.color("GreenYellow")
home_turtle = turtle.Turtle()
turtle.addshape("angry_birds.gif")
home_turtle.shape("angry_birds.gif")
home_turtle.up()

#set up the label for the spinner(speed of the pigs)
label01_turtle = turtle.Turtle()
label01_turtle.hideturtle()
label01_turtle.up()
label01_turtle.color("white")
label01_turtle.goto(-120, -30)
label01_turtle.write("Maximum Speed of Pigs:", font=("Arial", 8, "bold"))

#Set up the turtle that write the number for the spinner
speed_turtle = turtle.Turtle()
speed_turtle.hideturtle()
speed_turtle.up()
speed_turtle.goto(80,-30)
speed_turtle.color("white")
speed_turtle.write(str(croc_speed_max), align="center")

#Set up the left arrow(speed)
left01_arrow = turtle.Turtle()
left01_arrow.shape("arrow")
left01_arrow.color("white")
left01_arrow.shapesize(0.5, 1)
left01_arrow.left(180)
left01_arrow.up()
left01_arrow.goto(60, -22)


def decrease_speed(x, y):
    global croc_speed_max
    if croc_speed_max > croc_speed_min:
        croc_speed_max -= 1
        speed_turtle.clear()
        speed_turtle.write(str(croc_speed_max), align="center")

left01_arrow.onclick(decrease_speed)

#Set up the right arrow(speed)
right01_arrow = turtle.Turtle()
right01_arrow.shape("arrow")
right01_arrow.color("white")
right01_arrow.shapesize(0.5, 1)
right01_arrow.up()
right01_arrow.goto(100, -22)


def increase_speed(x, y):
    global croc_speed_max
    if croc_speed_max < 54:
        croc_speed_max += 1
        speed_turtle.clear()
        speed_turtle.write(str(croc_speed_max), align="center")

right01_arrow.onclick(increase_speed)

# set up the maximum number of pigs
label02_turtle = turtle.Turtle()
label02_turtle.hideturtle()
label02_turtle.up()
label02_turtle.color("white")
label02_turtle.goto(-120, -45)
label02_turtle.write("Maximum Number of Pigs:", font=("Arial", 8, "bold"))

#Set up the turtle that write the number for the number of pigs
number_turtle = turtle.Turtle()
number_turtle.hideturtle()
number_turtle.up()
number_turtle.goto(80,-45)
number_turtle.color("white")
number_turtle.write(str(croc_number), align="center")

#Set up the left arrow(number)
left02_arrow = turtle.Turtle()
left02_arrow.shape("arrow")
left02_arrow.color("white")
left02_arrow.shapesize(0.5, 1)
left02_arrow.left(180)
left02_arrow.up()
left02_arrow.goto(60, -37)


def decrease_number(x, y):
    global croc_number
    if croc_number > 4:
        croc_number -= 1
        number_turtle.clear()
        number_turtle.write(str(croc_number), align="center")

left02_arrow.onclick(decrease_number)

#Set up the right arrow(number)
right02_arrow = turtle.Turtle()
right02_arrow.shape("arrow")
right02_arrow.color("white")
right02_arrow.shapesize(0.5, 1)
right02_arrow.up()
right02_arrow.goto(100, -37)


def increase_number(x, y):
    global croc_number
    if croc_number < ((2*10)+9+9+5+4+6)+1:
        croc_number += 1
        number_turtle.clear()
        number_turtle.write(str(croc_number), align="center")
        
right02_arrow.onclick(increase_number)

#Set up Title and Instructions
title = "Escape the Minion Pigs!"
instructions = "1. Please choose the number and speed of Minion Pigs.\n\
2. To start the game, please press the 'Start' button.\n\
3. You need to drag the Angry Bird using the mouse to escape the pigs.\n\
4. The Angry Bird will die when it touches a pig or a boundary."
title_turtle = turtle.Turtle()
title_turtle.hideturtle()
title_turtle.up()
title_turtle.goto(0,195)
title_turtle.color("white")
title_turtle.write(title, font=("Arial", 36, "bold"), align="center")

info_turtle =  turtle.Turtle()
info_turtle.hideturtle()
info_turtle.up()
info_turtle.goto(0,60)
info_turtle.color("white")
info_turtle.write(instructions, font=("Arial", 13, "normal"), align="center")
    
# Set up start button
start_button = turtle.Turtle()
start_button.up()
start_button.goto(-40, 20)
start_button.color("yellow")
start_button.begin_fill()
for _ in range(2):
    start_button.forward(80)
    start_button.left(90)
    start_button.forward(25)
    start_button.left(90)
start_button.end_fill()

start_button.color("black")
start_button.goto(0, 25)
start_button.write("Start", font=("Arial", 8, "bold"), align="center")

start_button.goto(0, 33)
start_button.shape("square")
start_button.shapesize(1.25, 4)
start_button.color("")

def startgame(x, y):
    home_turtle.hideturtle()
    home_turtle.goto(600, 600)
    # Create  crocodiles
    for _ in range(croc_number):

        # a. Create a new turtle instance which is facing left
        croc = turtle.Turtle()

        # b. Set the shape
        #croc.shape("crocodile.gif")
        croc.shape("Minion_pig.gif")

        # c. Rotate the crocodile
        croc.left(180)
        
        # d. Place the crocodile in the right hand side randomly
        croc.up()
        x = (window_width + croc_width) / 2
        y = random.uniform(-(river_width-croc_height)/2, (river_width-croc_height)/2)
        croc.goto(x, y)

        # e. Add the new crocodile to the list 'crocs'
        crocs.append(croc)

        # 5.1.1. Generate a random speed and store it in 'croc_speeds'
        #croc_speeds.append(random.uniform(croc_speed_min, croc_speed_max))

    
        croc_speeds.append(random.uniform(croc_speed_min, croc_speed_max))

    #create player turtle
    turtle.shape("angry_birds.gif")
    turtle.up()

    time.sleep(1)
    turtle.ondrag(moveplayerturtle)
    turtle.ontimer(updatescreen, update_interval*20)

    


    title_turtle.clear()
    info_turtle.clear()
    label01_turtle.clear()
    label02_turtle.clear()
    speed_turtle.clear()
    number_turtle.clear()
    left01_arrow.hideturtle()
    right01_arrow.hideturtle()
    left02_arrow.hideturtle()
    right02_arrow.hideturtle()
    start_button.clear()                       
    bgmusic.play(-1)

    
        

start_button.onclick(startgame)

    
    

# Part 2 (1 of 2)
# 2.1 Set up event handlers
#    The event handler for turtle.ondrag
#turtle.ondrag(moveplayerturtle)
# Part 3 (2 of 4)
# The event handler for turtle.ontimer
# 3.2. Schedule the first update
#    It starts the main loop and starts the game
#updatescreen()

# Start the main loop, start the game
turtle.update()
turtle.done()

