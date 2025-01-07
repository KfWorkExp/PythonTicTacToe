import turtle

myTurtle = turtle.Turtle()
myTurtle.speed(10)   
paper = turtle.Screen()
nextTurnIsCross = False 
processing = False

SQUARES_PER_ROW = 3
SQUARE_SIZE = 100

HALF_SQUARE_SIZE = SQUARE_SIZE / 2
X_AND_O_SIZE = (SQUARE_SIZE * 0.9) / 2

# BOARD SQUARE NUMBERS LIKE THIS
# 2 5 8
# 1 4 7
# 0 3 6   

WINNING_COMBOS = [
                # Rows
                [0,3,6], [1,4,7], [2,5,8],
                # Columns
                [0,1,2], [3,4,5], [6,7,8],
                # Diagonals
                [0,4,8], [2,4,6]]

board = []

""" Creates the Tic-Tac-Toe board and draws it with the turtle """
def createBoard():

    max = int(((SQUARES_PER_ROW - 1) * SQUARE_SIZE)/2)
    min = int(max * -1)
    max = max + 1
    
    for x in range(min, max, SQUARE_SIZE):
        for y in range(min, max, SQUARE_SIZE):
            board.append({"x": x, "y": y, "state": ""})
            
    for i in range(len(board)):
        drawSquare(board[i]['x'], board[i]['y'])

    moveTo(min + SQUARE_SIZE, max + SQUARE_SIZE)    
    myTurtle.write("TIC-TAC-TOE", False, "center", ("Arial", 36, "bold"))  

""" Lifts the pen and moves it to a specific place on the board. """
def moveTo(x,y):
    
    myTurtle.penup();
    myTurtle.goto(x,y)
    myTurtle.pendown();
    myTurtle.setheading(90)
    
""" Moves the turtle to the specified location and draws a SQUARE. """
def drawSquare(x,y):
    
    moveTo(x - HALF_SQUARE_SIZE, y - HALF_SQUARE_SIZE)
    myTurtle.pencolor("black")
    myTurtle.pensize(1)
        
    for i in range(4):
        myTurtle.forward(SQUARE_SIZE)
        myTurtle.right(90)    
        
""" Moves the turtle to the specified location and draws a CIRCLE. """        
def drawNought(x,y):
    
    moveTo(x + X_AND_O_SIZE,y)
    myTurtle.pencolor("blue")
    myTurtle.pensize(4)
    
    myTurtle.circle(X_AND_O_SIZE)
    
""" Moves the turtle to the specified location and draws a CROSS. """
def drawCross(x,y):
    
    moveTo(x,y)
    myTurtle.pencolor("purple")
    myTurtle.pensize(4)
    
    myTurtle.right(45)
    
    for i in range(4):
        myTurtle.forward(X_AND_O_SIZE)
        myTurtle.back(X_AND_O_SIZE)
        myTurtle.right(90)    
 

""" Given a list of cell numnbers returns the data for those squares on the board. """    
def getRow (nos):
    
    result = []
    for i in range(len(nos)):
        result.append(board[nos[i]]['state'])      
        
    # print(nos, result)
    return result
    
""" Given a set of squares checks that all the squares have a O or an X in and returs 
    TRUE if they are all an O or an X"""
def checkLine(squares):
    # print((len(squares[0]) > 0 and len(set(squares)) == 1))
    return (len(squares[0]) > 0 and len(set(squares)) == 1)
    
    
""" Returns true if the board is in a win state otherwise returns FALSE. """
def checkForWin():

    for i in range(len(WINNING_COMBOS)):
        result = checkLine(getRow (WINNING_COMBOS[i]))
        
        if result == True:
            return result
        
    return False

""" Given the centre of the square and the co-ordinates that the user clicked, returns
    true if the co-ordinates are in the square. """
def checkClickInSquare(centreSquareDef, x, y):
    
    if (x >= centreSquareDef['x'] - HALF_SQUARE_SIZE and 
        x <= centreSquareDef['x'] + HALF_SQUARE_SIZE and
        y >= centreSquareDef['y'] - HALF_SQUARE_SIZE and 
        y <= centreSquareDef['y'] + HALF_SQUARE_SIZE):
        return True
    else:
        return False


""" When the user clicks on the board, works out which square (if any) has been clicked in. """
def getSquare(x,y):
    for i in range(len(board)):
        if (checkClickInSquare(board[i], x, y)): 
            return i
            
    return -1
    
""" Callback function.  When the user clicks on the board this function calls others to 
    work out which square has been clicked.  After this it draws a O or an X as appropriate
    and works out if the user has won or not """
def click(x,y):
    
    global nextTurnIsCross
    global board
    global processing
    
    # Only process one click at once.
    if processing:
        return
    
    processing = True
    
    square = getSquare(x,y)
    if (square >= 0 and len(board[square]['state']) == 0 ):
        
        if nextTurnIsCross:
            drawCross (board[square]['x'], board[square]['y'])
            board[square]['state'] = "X"
        else:
            drawNought(board[square]['x'], board[square]['y'])
            board[square]['state'] = "O"
            
        if checkForWin():
            myTurtle.pencolor("red")
            myTurtle.write("WIN WIN WIN!!!!!", False, "center", ("Arial", 36, "bold"))     
            turtle.exitonclick()     
        else:
            nextTurnIsCross = not nextTurnIsCross
            processing = False
  
""" Main function     
    Creates the board and then starts the listener for clicks """
def ticTacToe():
    createBoard()        
    myTurtle.hideturtle()       
    
    turtle.listen()
    paper.onclick(click)
    turtle.mainloop()     
    

ticTacToe()
#turtle.done()
