# Python Tic Tac Toe game

## Introduction

The initial script in this repo contains a working TicTacToe game.
Students should be familiar with basic Python coding before commencing.
The exercise enhances the original game before moving on to create a connect 4 type game.

## Initial setup

### Step 1 - The following software needs to be installed on your laptop:

- [Visual Studio Code](https://code.visualstudio.com/) - Code Editor/Compiler
- [Python](https://www.python.org/downloads/) - compiler and runner for Python code.
- [Git](https://git-scm.com/) - Scource code management.

### Step 2 - Fork the Master Repo and create a working copy on your laptop.

1) First on your local machine, create a directory where you are going to work (e.g. c:\code).
2) Go to [GitHub](https://github.com/) and create yourself an account (don't forget to verify your email address).
3) Go to our seed repository and create a copy in your own account by clicking the 'fork' button.
4) In your new repo  click the green 'Code' button, and copy the url on the https tab.
5) In windows open a command prompt, 
      a) Create a 'code' folder: mkdir code
      b) Navigate to it: cd code
      c) Copy the code to your laptop: git clone <url>  (where the url is the one you copied in 4).

Note that 'forking' only copies the code and not the Wiki with the user stories etc in.  You will need to refer to the original url for these.

### Step 3 - Open in VS Code and run up the code.

1) Open VS Code.
2) Goto File -> Open Folder and select the top level folder that was exported from Git.
3) This opens up the source code in VS Code.
4) Next go to Terminal -> New Terminal.
5) In the terminal window type 'cd <path>' where path is the path to the top level folder you just opened (you can copy it from Windows Explorer)
6) Type: 'python <file name>' and press return.

### Step 4 - Push your changes into your repository

1) Open a new terminal by going to Terminal -> New Terminal.
2) Check that you have your git credentials set
   `git config --list` is the command
3) Set up your username and email if it is missing from the git config list
   `git config --global user.name "Your Name"`
   `git config --global user.email "your.email@email.com"`
4) Commit your local changes on your machine
   `git add .` Adds all local changes for committing
   `git commit -m"enter message here"` Commits the changes so they can be pushed under a message you set
5) Push your changes to your GitHub remote repository
   `git push origin HEAD` 

## Challenges

1) Run the TicTacToe game and review the code to see how it works.  Once you are happy make a copy of the file and make the following changes.
    - Change the colours of the O's and the X's
    - Change the shapes so that both players have filled in O's of different colours.
    - Change who starts.
    - Change it to be 4x4 Tic Tac Toe (getting a line of 4 in any direction to win)

2) Take a new copy of the original file and change the game to be connect 4 rather than tic tac toe.
     - The grid size will need to be 7 columns by 6 rows.  You may need to make the squares smaller so it fits on a screen.
     - The grid will need to be blue.
     - Counters are filled O's in red and yellow
     - To play a counter a player clicks a column and it is placed in the highest empty square.
     - To win the user must get 4 counters in a straight line in any direction.

3) Make a version of your connect 4 game where you can play against the computer.  Having it pick a random empty square is the easiest solution, but can you put some basic 'AI' in to make it play more like a person?
   
4) (Advanced) If you didn't do it as part of 2, try and make a generic version of either the Connect 4 or TicTacToe game.
    - It should hold the vertical and horizontal grid sizes and the number of counters needed for a win in constants.
    - Changing these constants ONLY should make the game automatically work with those parameters (making no other code changes).
        - The grid drawing as well as the win detection code will be the main parts needing updating.
     
## Extension Task

Use what you have learned here to programme a different game from scratch. Feel free to pick your own idea, but some examples of ones you might want to try are:
  - Hangman
  - Pairs/Memory Game
  - Dots and Boxes [https://mathsweek.scot/news/how-to-play-dots-boxes](https://mathsweek.scot/news/how-to-play-dots-boxes)  
  - Battleships
  - Mine Sweeper
  - Towers of Hanoi. ([https://youtu.be/rf6uf3jNjbo](https://youtu.be/rf6uf3jNjbo))

## Python Help

- [https://www.w3schools.com/python/](https://www.w3schools.com/python/)
- [https://www.w3schools.com/python/python_user_input.asp](https://www.w3schools.com/python/python_user_input.asp)
- [https://www.geeksforgeeks.org/python-turtle-tutorial/](https://www.geeksforgeeks.org/python-turtle-tutorial/)
- See the Python Basics exercise for a list of turtle commands.
