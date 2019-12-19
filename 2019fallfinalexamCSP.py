#2019-20 Fall Computer Science Principles Final Exam

#Ms. Haubold


#Name
#
#Date
#


#### INSTRUCTIONS ####
#Create an etch a sketch turtle game
#The turtle should move with the arrow keys (up, down, left and right), and draw
#Space should clear the screen
#o and p should make the pen size bigger and smaller
#u should pick the pen up or put the pen down
#All code must be commented
#BONUS
#Add a feature to change colors
#

#import required libraries
import turtle as trtl

#create turtle
juan = trtl.Turtle()




#movement functions
juan.speed(0)
size = 5
juan.pensize(size)



#define
def up():
    juan.setheading(90)
    juan.forward(5)

def left():
    juan.setheading(180)
    juan.forward(5)
def down():
    juan.setheading(270)
    juan.forward(5)

def right():
    juan.setheading(0)
    juan.forward(5)

def pen_size_bigger():
    global size
    size += 1
    juan.pensize(size)

def pen_size_smaller():
    global size
    size -= 1
    juan.pensize(size)
    

def erase():
    juan.clear()

def color_blue():
    juan.color("blue")

def color_pink():
    juan.color("pink")

def color_orange():
    juan.color("orange")

def color_purple():
    juan.color("purple")

def color_red():
    juan.color("red")




#color/drawing functions
#1 = blue
#2 = orange
#3 = red
#4 = purple
#5 = pink

#create screen
wn = trtl.Screen()

#bind to keypresses
wn.onkeypress(up,"Up")
wn.onkeypress(left,"Left")
wn.onkeypress(down,"Down")
wn.onkeypress(right,"Right")
wn.onkeypress(pen_size_bigger,"o")
wn.onkeypress(pen_size_smaller,"p")
wn.onkeypress(erase,"space")
#wn.onkeypress(penup/down,"u")
wn.onkeypress(color_blue,"1")
wn.onkeypress(color_orange,"2")
wn.onkeypress(color_red,"3")
wn.onkeypress(color_purple,"4")
wn.onkeypress(color_pink,"5")

#listen
wn.listen()



#mainloop
wn.mainloop()