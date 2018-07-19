#import stuff up here

import random
from tkinter import *

class Dot(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.r = random.randint(20,50)
        self.fill = random.choice(["pink","orange","yellow","green",
                                   "cyan","purple"])
        self.clickCount = 0

    def containsPoint(self, x, y):
        d = ((self.x - x)**2 + (self.y - y)**2)**0.5
        return (d <= self.r)

    def draw(self, canvas):
        canvas.create_oval(self.x-self.r, self.y-self.r,
                           self.x+self.r, self.y+self.r,
                           fill=self.fill)
        canvas.create_text(self.x, self.y, text=str(self.clickCount))

class Car(object):
    def __init__(self, x, y, carString):
        self.CenterX = x
        self.centerY = y
        self.halfWidth = 20
        self.halfHeight = 7
        self.topHeight = 10
        self.topBotWidth = 19
        self.topTopWidth = 14
        self.tireFromCenter = 12
        self.tireWidth = self.halfWidth/4
        self.tireHeight = self.halfWidth/2
        self.carString = carString
        self.carImage = None
        self.carWidth = 35
        self.carHeight = 36

    def drawCar(self, canvas):
        #we draw the car?
        # canvas.create_rectangle(self.CenterX-self.halfWidth, self.centerY-self.halfHeight,
        #                   self.CenterX+self.halfWidth, self.centerY+self.halfHeight, fill="red",
        #                   outline="red")
        # canvas.create_polygon(self.CenterX-self.topBotWidth, self.centerY-self.halfHeight,
        #                     self.CenterX-self.topTopWidth, self.centerY-self.halfHeight-self.topHeight,
        #                     self.CenterX+self.topTopWidth, self.centerY-self.halfHeight-self.topHeight,
        #                     self.CenterX+self.topBotWidth, self.centerY-self.halfHeight,
        #                     fill="red")
        # #rear window
        # canvas.create_polygon(self.CenterX-self.topBotWidth+3, self.centerY-self.halfHeight-2,
        #                     self.CenterX-self.topTopWidth+2, self.centerY-self.halfHeight-self.topHeight+2,
        #                     self.CenterX+self.topTopWidth-2, self.centerY-self.halfHeight-self.topHeight+2,
        #                     self.CenterX+self.topBotWidth-3, self.centerY-self.halfHeight-2,
        #                     fill="black")
        # #tires!
        # #canvas.create_rectangle(self.CenterX-self.tireFromCenter, self.centerY+self.halfHeight,)
        #how about an actual car image???
        if(self.carImage == None):
            self.carImage = PhotoImage(file=self.carString)
        canvas.create_image(self.CenterX+(self.carWidth/2),
                            self.centerY+(self.carHeight/2),image=self.carImage)

    def moveCar(self, moves):
        #moving the car side to side
        if(moves == "Left"):
            self.CenterX -= 10
        elif(moves == "Right"):
            self.CenterX += 10

    def checkCollision(self, x, y):
        #check if point (x, y) has collided with our car
        if(((self.CenterX-(self.carWidth/2)) <= x) and (x <= (self.CenterX+(self.carWidth/2)))):
            if(((self.centerY-(self.carHeight/2)) <= y) and (y <= (self.centerY+(self.carHeight/2)))):
                return True
        return False

class Obstacle(object):
    def __init__(self, x, y, width, height, imageString):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.imageString = imageString
        self.image = None

    def drawObstacle(self, canvas):
        #here we draw it!
        if(self.image == None):
            self.image = PhotoImage(file=self.imageString)
        canvas.create_image(self.x, self.y, image=self.image)

    def moveObstacle(self, data):
        #here we give it it's motion
        if(self.y >= data.height):
            self.y = data.horizon
            self.x = random.randint((data.width/3),((data.width/3)*2))
        else:
            self.y = self.y+4


def init(data):
    data.dots = [ ]
    data.horizon = (data.height*3)/5 #either 3/5 or 11/16 (but probably 3/5)
    # data.leftCurb = data.width/5
    # data.rightCurb = (data.width/5)*4
    data.farLeftCurb = data.width/3
    data.farRightCurb = (data.width/3)*2     #we'll use these if we make it more complicated
    data.simpleLeftCurb = data.width/4
    data.simpleRightCurb = (data.width/4)*3
    data.carCenterXDefault = data.width/2
    data.carCenterY = (data.height/10)*9
    data.carImageString = "C:/Users/austinm/Documents/sideAttemptGameFolder/rsz_car.png"
    data.thisCar = Car(data.carCenterXDefault,data.carCenterY, data.carImageString)
    data.sunString = "C:/Users/austinm/Documents/sideAttemptGameFolder/rsz_teletubbies_sun.png"
    data.fatCactusString = "C:/Users/austinm/Documents/sideAttemptGameFolder/rsz_cactusSprite.png"
    data.cattleCactusString = "C:/Users/austinm/Documents/sideAttemptGameFolder/rsz_cattlecactus.png"
    data.runningCactusString = "C:/Users/austinm/Documents/sideAttemptGameFolder/rsz_runningcactus.png"
    data.theSun = None
    data.cactus1 = None
    data.cactus2 = None
    data.obstacle1 = Obstacle(314, data.horizon, 25, 34, data.runningCactusString)

def placeScenery(canvas, data):
    #let's draw some scenery!
    if(data.cactus1 == None):
        data.cactus1 = PhotoImage(file=data.fatCactusString)
    canvas.create_image(80,315,image=data.cactus1)
    if(data.cactus2 == None):
        data.cactus2 = PhotoImage(file=data.cattleCactusString)
    canvas.create_image(505,260,image=data.cactus2)

def mousePressed(event, data):
    # for dot in reversed(data.dots):
    #     if (dot.containsPoint(event.x, event.y)):
    #         dot.clickCount += 1
    #         return
    # data.dots.append(Dot(event.x, event.y))
    pass

def redrawAll(canvas, data):
    for dot in data.dots:
        dot.draw(canvas)
    #making the sky

    canvas.create_rectangle(0,0,data.width, data.horizon, fill="DeepSkyBlue2", outline="DeepSkyBlue2")
    #making the desert next to the road
    canvas.create_polygon(0,data.horizon,data.farLeftCurb,data.horizon,
                          data.simpleLeftCurb,data.height,0,data.height, fill="LightGoldenrod3")
    canvas.create_polygon(data.width,data.horizon,data.farRightCurb,data.horizon,
                          data.simpleRightCurb,data.height,data.width,data.height, fill="LightGoldenrod3")
    #let's draw the sun!
    if(data.theSun == None):
        data.theSun = PhotoImage(file=data.sunString)
    canvas.create_image(100,75,image=data.theSun) #the dimensions of the sun pic so it's in the corner
    #canvas.create_rectangle(data.width/2, (data.height/8)*7, data.width/2+5, (data.height/8)*7+5, fill="red")
    placeScenery(canvas, data)
    data.thisCar.drawCar(canvas)
    data.obstacle1.drawObstacle(canvas)

def keyPressed(event, data):
    if (event.keysym == "Left"): 
        data.thisCar.moveCar("Left")
    if(event.keysym == "Right"):
        data.thisCar.moveCar("Right")
    #pass

def timerFired(data):
    data.obstacle1.moveObstacle(data)

####################################
# use the run function as-is
####################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    init(data)
    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(600, 400)
