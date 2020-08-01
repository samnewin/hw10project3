# Exercise No.   23
# File Name:     hw10Project3
# Programmer:    Samuel Nguyen
# Date:          July 16, 2020
#
# Problem Statement: This program converts a user supplied image to grayscale
# Overall Plan:
# 1. Define calcHeight function using the gender formulas and return
# 2. set up GraphWin
# 3. Prompt user to enter parent's height (and create input boxes)
# 4. Draw the calc button
# 5. Within a while true loop, check for mouse click on box. if so, call calcHeight and print 

# Import the necessary python libraries.
#   graphics.py = Zelle's graphics library
#   cbutton.py = modifed version of Zelle's button library to include circles instead

from graphics import *
from cbutton import *

#calcHeight method to calculate the predicted height
def calcHeight(gender, heightM, heightF):
  numH=0
  #based on gender of child, apply formula and return
  if gender=="m":
    numH=((heightM*(13/12))+heightF)/2
  else:
    numH=((heightF*(12/13))+heightM)/2
  return numH

def main():
  #set up graphWin
  win = GraphWin("Height Calculator", 600, 600)
  win.setCoords (0, 0, 5, 5)
  win.setBackground ("white")

  #Prompt user
  Text(Point(2, 4), "Enter Father's Height in inches: ").draw(win)
  Text(Point(2, 3), "Enter Mother's Height in inches: ").draw(win)

  inputTextFather = Entry(Point(3.5, 3), 5)
  inputTextFather.setText("0.0")
  inputTextFather.draw(win)

  inputTextMother = Entry(Point(3.5, 4), 5)
  inputTextMother.setText("0.0")
  inputTextMother.draw(win)

  #draw button
  calcButton=CButton(win, Point(2.5, 2), .75, "Click to Calculate")
  
  # Event loop 
  calcButton.activate()
  while True:
    pt=win.getMouse()
    if calcButton.clicked(pt): 
      heightM=float (inputTextFather.getText()) 
      heightF=float (inputTextMother.getText()) 

      maleHeight=str(calcHeight("m", heightM, heightF))
      femaleHeight=str(calcHeight("f", heightM, heightF))

      message="Child's predicted height is: \n"+maleHeight+" or "+femaleHeight+" inches."
      
      Text(Point(2.35, 1), message).draw(win)

      calcButton.deactivate()
      break

main()
