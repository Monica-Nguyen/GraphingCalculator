#Name: Monica Nguyen
#Date: Oct 18, 2019
#The following code draws mathematical expressions determined by the user and plots them using a coordinate system where (0,0) is the bottom left corner and (800,600) is the top right corner. The user determine the spacing between ticks on the graph. The colors of the graphs alternate between red, green and blue. 

#Import the turtle and math library so that we can use the drawing function and do calculations
import turtle
from math import* #When trigonometry functions are used, the user can just use sin(x), for example

#Constants used for the having the screen within the specified boundaries. 
WIDTH = 800 
HEIGHT = 600 
TEXTGAP = 20 #Used for Distance of the labels from the axes 
TICKSIZE = 5 
STEP = 1
AXISCOLOR = "black" #Color for the axis

#Purpose: Returns the screen (pixel based) coordinates of some (x, y) graph location based on configuration
        # Usage -> screenCoor(xo, yo, ratio, 1, 0)
#Parameters: xo, yo : pixel location of the origin of the graph
             #ratio: ratio of pixels to single step in graph (i.e 1 step is ratio amount of pixels)
             #x, y: graph location to change into a screen (pixel-based) location
#Returns: (screenX, screenY) which is the pixel location (x,y) in the window
def screenCoor(xo, yo, ratio, x, y): #x,y are coordinate values 
    pointer = setup()
    pointer.color(AXISCOLOR)
    screenX = xo + ratio * x
    screenY = yo + ratio * y
    return screenX, screenY  #Returns the pixel value of the screenX and screenY to plot on the window


#Purpose: Returns a string of colors to allow graphs to cycle through red, green then blue. 
#Parameters: counter - integer where the value is a count (starting at 0) of the expressions drawn
#Return: 0 is "red", 1 is "green", 2 is "blue" and the numbers keep repeating itself, to repeat the colors.
def getColor(counter): #The counter is the number associated to each additional expression entered.   
    if counter % 3 == 0: #When there is no remainder, the color is red.
        return "red"
    if counter % 3 == 1: #When remainder = 1, the pen color is green.
        return "green"
    if counter % 3 == 2: #When remainder = 2, the pen color is blue. 
        return "blue"

#Purpose: Draw xaxis label (text) for a point at (screenX, screenY) on the window. 
        # the actual drawing points will be offset from this location as necessary
        # Ex. for (x,y) = (1,0) or x-axis tick/label spot 1, draw a tick mark and the label 1
        # Usage -> drawXAxisLabelTick(pointer, 1, 0, "1")
#Parameters: pointer: the turtle drawing object
            #screenX, screenY): the pixel screen location to drawn the label and tick mark for
            #text: the text of the label to draw
#Returns: Nothing
def drawXAxisLabelTick(pointer, screenX, screenY, text): #
		pointer.goto(screenX, screenY + TICKSIZE) #Moving location to top of tick
		pointer.down()
		pointer.goto(screenX, screenY - TICKSIZE) #Moving location to bottom of tick
		pointer.up()
		pointer.goto(screenX, screenY - TEXTGAP) 
		if text != 0: #Only if the text does not equal zero, then the x-labels will be drawn (To not write 0 on the turtle screen)
			pointer.write(text, False, align= 'center')
		pointer.goto(screenX+STEP,screenY) #Allows the next tick and label to be drawn one ratio of pixels away horizontally, so we add a STEP to the xaxis.
		pointer.down()
    
#Purpose: Draw yaxis label (text) for a point at (screenX, screenY) on the window.
        # the actual drawing points will be offset from this location as necessary
        # Ex. for (x,y) = (0,1) or y-axis tick/label spot 1, draw a tick mark and the label 1
        # Usage -> drawXAxisLabelTick(pointer, 0, 1, "1")
#Parameters: pointer: the turtle drawing object
            #(screenX, screenY): the pixel screen location to drawn the label and tick mark for
            #text: the text of the label to draw
#Returns: Nothing
def drawYAxisLabelTick(pointer, screenX, screenY, text):
		pointer.up()
		pointer.goto(screenX + TICKSIZE, screenY) #Moving location to right of tick
		pointer.down()
		pointer.goto(screenX - TICKSIZE, screenY) #Moving location to left of tick
		pointer.up()
		pointer.goto(screenX - TEXTGAP, screenY)
		if text != 0: #Only if the text does not equal zero, then the y-labels will be drawn
			pointer.write(text, False, align= 'center')
		pointer.goto(screenX,screenY+STEP) #Allows the next tick and label to be drawn one ratio of pixels away vertically, so we add a STEP to the yaxis.
		pointer.down()
    
#Purpose: Draw in the window an xaxis (secondary function is to return the minimum and maximum graph locations drawn at)
        # Usage -> drawXAxis(pointer, xo, yo, ratio)
#Parameters: pointer:the turtle drawing object
           # xo, yo : the pixel location of the origin of the  graph
           # ratio: the ratio of pixels to single step in graph (i.e 1 step is ratio amount of pixels)
#Returns: (xmin, ymin) where xmin is minimum x location drawn at and xmax is maximum x location drawn at
def drawXAxis(pointer, xo, yo, ratio):
    xmin = 0
    xmax = 0 
    x = 0 #Making x negative so that one step can be made in the left direction
    screenX, screenY = screenCoor(xo, yo, ratio, x, 0)
    while screenX > 0 : #Drawing the negative x axis to be above 0
        pointer.up()
        pointer.goto(xo,yo) #Start at origin, then draw left. 
        pointer.down()
        screenX, screenY = screenCoor(xo, yo, ratio, x, 0) #y is 0 in the screenCoor because yo (the origin that the user inputs) must stay constant as we draw the x-axis. However, x value is changing as the axis is progressing. Later on, one ratio (one step) worth of pixels is subtracted to keep moving. 
        pointer.goto(screenX,screenY)
        drawXAxisLabelTick(pointer, screenX, screenY, x) #Calling function to draw x-axis ticks. The text box is replaced with x, so that the x values can be labeled on the graph. 
        pointer.up()
        x = x - STEP #To allow loop to move one coordinate left at a time 
    xmin = x #xmin changes based on the ratio the user inputs
    x = 0
    screenX, screenY = screenCoor(xo, yo, ratio, x, 0)
    while screenX < WIDTH: #Drawing the positive x-axis to be below 800
        pointer.up()
        pointer.goto(xo,yo) #Start at origin, then draw right. 
        pointer.down()
        screenX, screenY = screenCoor(xo, yo, ratio, x, 0) 
        pointer.goto(screenX,screenY)
        drawXAxisLabelTick(pointer, screenX, screenY, x) #Calling function to draw x-axis ticks. The text box is replaced with x, so that the x values can be labeled on the graph. 
        pointer.up()
        x = x + STEP #To allow loop to move one coordinate right at a time 
    xmax = x #xmax changes based on the ratio the user inputs
    
    return xmin, xmax #return these values to be used for drawing expressions and limiting where they are drawn in the turtle window
     
#Purpose: Draw a y-axis in the window 
        # Usage -> drawYAxis(pointer, xo, yo, ratio)
#Parameters: pointer: the turtle drawing object
        # xo, yo : the pixel location of the origin of the  graph
        # ratio: the ratio of pixels to single step in graph (i.e 1 step is ratio amount of pixels)
#Returns: Nothing
def drawYAxis(pointer, xo, yo, ratio):
    y = 0
    screenX, screenY = screenCoor(xo, yo, ratio, 0, y)
    while screenY > 0: #Drawing the negative y axis to be above 0
        pointer.up()
        pointer.goto(xo,yo)
        pointer.down()
        screenX, screenY = screenCoor(xo, yo, ratio, 0, y) #x is 0 in the screenCoor because xo (the origin that the user inputs) must stay constant as we draw the y-axis. However, y value is changing as the axis is progressing. Later on, one ratio (one step) worth of pixels is subtracted to keep moving. 
        pointer.goto(screenX, screenY)
        drawYAxisLabelTick(pointer, screenX, screenY, y) #Calling function to draw y-axis ticks. The text box is replaced with y, so that the y values can be labeled on the graph. 
        pointer.down()
        y = y - STEP #To allow loop to move one coordinate down at a time 
    ymin = y
    y=-STEP
    screenX, screenY = screenCoor(xo, yo, ratio, 0, y)
    while screenY < HEIGHT: #Drawing the positive y-axis to be below pixel 600
        pointer.up()
        pointer.goto(xo,yo)
        pointer.down()
        screenX, screenY = screenCoor(xo, yo, ratio, 0, y) #x is 0 in the screenCoor because xo (the origin that the user inputs) must stay constant as we draw the y-axis. However, y value is changing as the axis is progressing. Later on, one ratio (one step) worth of pixels is subtracted to keep moving. 
        pointer.goto(screenX, screenY)
        drawYAxisLabelTick(pointer, screenX, screenY, y) #Calling function to draw y-axis ticks. The text box is replaced with y, so that the y values can be labeled on the graph. 
        pointer.down()
        y = y + STEP #To allow loop to move one coordinate up at a time 
    pointer.up()
    return ymin

#Purpose: Draw expressions from the user in the window between xmin and xmax.
#Parameters: pointer: the turtle drawing object
           # xo, yo : the pixel location of the origin of the  graph
           # ratio: the ratio of pixels to single step in graph (i.e 1 step is ratio amount of pixels)
           # expr: the expression to draw (assumed to be valid)
           # xmin, ymin : the range for which to draw the expression [xmin, xmax]
#Returns: Nothing  

def drawExpr(pointer, xo, yo, ratio, xmin, xmax, expr):
    x = float(xmin + 1) #+1 to ensure graph is drawn inside the correct parameters
    y = eval(expr) #Evaluates expression 
    screenX, screenY = screenCoor(xo, yo, ratio, x, y)
    
    while screenY > 800: #My intention is to make the graph only draw inside the vertical boundaries, and I could not do this without also skewing the drawn graph itself. I decided to let the graphs draw beyond the y axes to allow for the graphs to draw correctly to scale. 
        if screenY < ymin:
            x = x + 1 
            y = eval(expr)
            screenX, screenY = screenCoor(xo, yo, ratio, x, y) #convert values to screen coordinates
        
    screenX, screenY = screenCoor(xo, yo, ratio, x, y)
    
    pointer.goto(screenX,screenY) 
    while x < xmax -1 : #-1 to ensure graph is drawn inside the correct parameters for x axis
        
        y = eval(expr) 
        
        screenX, screenY = screenCoor(xo, yo, ratio, x, y) #convert values to screen coordinates

        #print(x, y, "I am here", screenY) I used this to track coordinates and how numbers were responding

        if(screenY < 800): #If condition to make the turtle drawings more smooth 
            pointer.down()
            pointer.goto(screenX, screenY)
            pointer.up()
        x = x + 0.1 #Delta value, allows curves to be drawn smoothly because more y-values can be plotted very close together
    pointer.up()

#Purpose: Set up Turtle window for drawing
#Returns: Nothing
def setup():
    pointer = turtle.Turtle()
    screen = turtle.getscreen()
    screen.setup(WIDTH, HEIGHT, 0, 0) #To make (0,0) bottom left and (800,600) top right 
    screen.setworldcoordinates(0, 0, WIDTH, HEIGHT) #To make (0,0) bottom left and (800,600) top right 
    pointer.hideturtle()
    screen.delay(delay=0)
    return pointer

#  Main function that attempts to graph a number of expressions entered by the user
#  The user designates the origin of the chart to be drawn, as well as the ratio of pixels to steps for both axes.
#  The window size is always 800 width by 600 height in pixels
#  DO NOT CHANGE THIS FUNCTION
#  Returns: Nothing
def main():
    #Setup window
    pointer = setup()

    #Get input from user
    xo, yo = eval(input("Enter pixel coordinates of origin: "))
    ratio = int(input("Enter ratio of pixels per step: "))

    #Set color and draw axes (store discovered visible xmin/xmax to use in drawing expressions)
    pointer.color(AXISCOLOR)
    xmin, xmax = drawXAxis(pointer, xo, yo, ratio)
    
    drawYAxis(pointer, xo, yo, ratio)

    #Loop and draw expressions until an empty string "" is entered and change expression colour based on how many expressions have been drawn
    expr = input("Enter an arithmetic expression: ")
    counter = 0
    while expr != "":
        pointer.color(getColor(counter))
        drawExpr(pointer, xo, yo, ratio, xmin, xmax, expr)
        expr = input("Enter an arithmetic expression: ")
        counter += 1
	
main() #To run the program 
