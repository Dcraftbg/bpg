# from libs.bpg import *
# from utils import *
# from utils_2 import *

from lib.bpg import *
window = bpg.Window((500,500))
window.setTitle("SUSSY GAME")
testTextBox = utils.textBox("BRO NAH THIS SHIT IS GARBAGE",20,colorText=(255,255,255),colorBackground=(0,0,0,0))
testTextBox.x = 100
window.add(testTextBox)
amplifierX = 5
amplifierY = 5
isfacingRight = True
isfacingDown = True
running = True
while running:
  window.fetchEvents()
  for event in window.events:
    if event.type == pygame.QUIT:
      running = False
    if event.type == pygame.MOUSEBUTTONDOWN:
      if pygame.mouse.get_pressed()[0]:
        if isfacingRight:
          if testTextBox.x+amplifierX+testTextBox.width <= window.width:
            testTextBox.x += amplifierX
          else:
            #print("Hi!")
            #print(isfacingRight)
            isfacingRight = False
            #print(isfacingRight)
        else:
          if testTextBox.x-amplifierX >= 0:
            #print("what?")
            testTextBox.x -= amplifierX
          else:
            #print("bruh WHY")
            isfacingRight = True
        
      
      if pygame.mouse.get_pressed()[2]:
        # if testTextBox.y+amplifierY+testTextBox.height <= window.height:
        #   testTextBox.y += amplifierY
        if isfacingDown:
          if testTextBox.y+amplifierY+testTextBox.height <= window.height:
            testTextBox.y += amplifierY
          else:
            
            isfacingDown = False
        else:
          if testTextBox.y-amplifierY >= 0:
            testTextBox.y -= amplifierY
          else:
            isfacingDown = True
      if pygame.mouse.get_pressed()[1]:
        amplifierX += 1
        amplifierY += 1
        
  window.update()