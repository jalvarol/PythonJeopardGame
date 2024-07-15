from turtle import *
import time

tracer(0,0)
screen = Screen()
bgcolor("grey")


#THIS WILL GREET YOU TO OUR JEOPARDY GAME
def jeopardyGreet():
    pensize(5)
    hideturtle()
    speed(0)
    pencolor("white")
    write("Welcome to Jeopardy",align = "center", font =("Helvetica",60,"normal"))
    update()
    time.sleep(2)
#THIS BUILDS A TURTLE TO ASK THE JEOPARDY QUESTION(second turtle due to reset on the same turtle resets everything, this allows it to go back to previous screen with blued out sections)
def jeopardyQuestion(question):
    t = Turtle()
    tracer(0,0)
    t.up()
    t.setpos(-600,400)
    t.down()
    t.pencolor("dark blue")
    t.fillcolor("dark blue")
    t.begin_fill()
    t.forward(1200)
    t.right(90)
    t.forward(800)
    t.right(90)
    t.forward(1200)
    t.right(90)
    t.forward(800)
    t.end_fill()
    t.setpos(0,0)
    t.up()
    t.pencolor("white")
    t.write(question,align = "center", font =("Helvetica",30,"normal"))
    t.reset()
def jeopardyEnding():
    clear()
    jeopardyQuestion("Congrats!")
    jeopardyQuestion("TOTAL: "+str(overScore())+" points")

#THIS USES THE TURTLE FUNCTION "TEXTINPUT" TO ANSWER THE QUESTION
def getAnswer():
    answer = screen.textinput("Jeopardy","Type your answer")
    return answer

#THIS PRINTS THE HEADLINER
def printJeopardyTitle():
     hideturtle()
     up()
     setpos(0,400)
     pencolor("white")
     write("JEOPARDY",align = "center", font =("Helvetica",80,"normal"))
    
#BUILDS THE JEOPARDY TABLE BY GIVING THE X,Y COORDINATES
def printTable():
    UpperLeftx = -600
    UpperLefty = 400
    for column in range(0,4):
        up()
        for row in range(0,4):
            drawTable(UpperLeftx,UpperLefty,"black",column,row)
            UpperLeftx = UpperLeftx + 300
        UpperLefty = UpperLefty - 200
        UpperLeftx = -600
    
#DRAWS RECTANGLES OF THE JEOPARDY TABLE
def drawTable(x,y,color,column,row):
    #This will be used for the width of a rectangle
    SIDE = 200
    #We start the table at this x,y coordinate
    setpos(x,y)
    down()
    #We color the outline 'black' and the
    #fill color 'blue'
    pencolor('black')
    fillcolor("dark blue")
    begin_fill()
    #The square begins
    for i in range(0,4):
        #This makes the length of the rectangle longer
        if i%2==0:
            SIDE +=100
        else:
        #This does otherwise
            SIDE = 200
        forward(SIDE)
        right(90)
        
    end_fill()
    up()
    #Setpos sets up the writing to be in the middle of a rectangle
    setpos(x+150,y-100)
    pencolor("white")
    #This adjusts the text, the pos of the text, and the font
    write(labelTable(Elements,column,row),align = "center", font =("Helvetica",24,"bold"))
    update()
#This brings back the Labels and positions them at respective spots
def labelTable(Elements,column,row):
    if column >0:
        pencolor("yellow")
        pen
    if column == 0: 
        return Elements[row][column]
    elif column == 1:
        return Elements[row][column][0]
    elif column == 2:
        return Elements[row][1][1]
    elif column == 3:
        return Elements[row][1][2]


#RETURNS THE X,Y POSITION AS AN INDEX VALUE as well as limiting locations used
def getgridposition(x,y):
    if 200 > y > 0:
        row = 0
    elif -200 < y < 0:
        row = 1
    elif -400 < y < -200:
        row = 2
    else:
        row =  3
    
    if -600 < x < -300:
        col = 0
    elif -300 < x < 0:
        col = 1
    elif 0 < x < 300:
        col = 2
    elif 300 < x < 600:
        col = 3
    else:
        col = 4
    return [int(row),int(col)]
 
#this will blue out the whole grid regardless of where you click in the specific grid
def blueout(x,y):
  home()
  row = (200-y)//200 
  col = (x+600)//300
  b = 200+(row*(-200))
  a = -600+(col*(300))
  up()
  goto(a,b)
  color("dark blue")
  fd(10)
  rt(90)
  fd(10)
  down()
  pensize(1)
  fillcolor("dark blue")
  begin_fill()
  #this loop is to create a rectangle
  for i in range(4):
    if (i%2)==0:
      fd(180)
      lt(90)
    else:
      fd(280)
      lt(90)
  end_fill()
  up()

#scoring system using list
#this function adds points to a list
def addPoints(points):
  f.append(int(points))
#this function sums up the list values for a total score value
def overScore():
  sum = 0
  for num in f:
    sum += num
  return (sum)

#CALLS GETGRIDPOSITION TO GET INDEX VALUES
#COMPARES USER INPUT TO LIST OF ANSWERS
#IF CORRECT, USER GETS $$$
def screenclicked(x,y):
  #this converts the amount of entries in the score box to number of questions answered
  count = len(f)
  # This function runs when the screen is clicked
  pos = getgridposition(x, y)
  #this loop is created to limit grids to game tiles only based on row and col position
  if ((pos[0] <0 or pos[0]>2) or (pos[1]<0 or pos[1]>3)):
      print("Please select a box within the square")
  else:
      blueout(x,y)
      row = pos[0]
      col = pos[1]
      coordinates_tmp = [pos[0], pos[1]]
      if coordinates_tmp in coordinates:
          print("Please select another box")
      else:
          coordinates.append(coordinates_tmp)
          jeopardyQuestion(categories[col][row][0])
          a=getAnswer()
          s=(categories[col][row][1])
          #if a.lower() == (categories[col][row][1])):
          #this loop is used to compare answers with the solution
          if a.lower()== s.lower():
            points= (row+1)*500
            print("Correct, you achieved " + str(points )+ " points")
            addPoints(points)
            print("Total score: " ,overScore(),  " click on another box.")
          else:
            points= (row+1)*-500
            print("Not even close buddy, you lost " + str(points))
            addPoints(points)
            print("Total score: " ,overScore(), ", click on another box.")
          #this loop limits the game to 12 tries (uses len() to count amount of tries)
          if count == 11:
              jeopardyEnding()
              exit()


if __name__ == "__main__":
    
    Elements = [
        ("Python", ["$500", "$1000","$1500"]),
        ("Jeopardy", ["$500", "$1000","$1500"]),
        ("PyTurtle", ["$500", "$1000","$1500"]),
        ("Random", ["$500", "$1000","$1500"])]

    
    # Question/Answer Content
    #Please enter your questions and your answers, and consider the context of Jeopardy when
    #answering said questions i.e. "What is..., Who is..."
    categories = [
    # Python
    [
    ["Question", "Answer"],
    ["Question", "Answer"],
    ["Question'","Answer"],
    ],
    # Jeopardy
    [
    ["Question","Answer"],
    ["Question","Answer"],
    ["Question","Answer"],
    ],

    # PyTurtle
    [
    ["Question", "Answer"],
    ["Question", "Answer"],
    ["Question", "Answer"],
    ],
    # Random
    [
    ["This a character who lives in a pineapple under the sea.", "Who is spongebob?"],
    ["This character is usually associated with a red and striped shirt.", "Who is Waldo?"],
    ["This an area above our heads and is considered a void.", "What is space?"],
    ["This is not a valid question press okay to continue", ""],
    ],

    ]

    jeopardyGreet()
    printJeopardyTitle()
    printTable()
    f = []
    coordinates = []
    screen.onclick(screenclicked)


