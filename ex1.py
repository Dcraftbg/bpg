# from libs.bpg import *
# from utils import *
# from utils_2 import *

from lib.bpg import *
window = bpg.Window((500,500))
window.setTitle("Test Game")
testTextBox = utils.textBox("Some Text",20,colorText=(255,255,255),colorBackground=(0,0,0,0))
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
            isfacingRight = False
        else:
          if testTextBox.x-amplifierX >= 0:
            testTextBox.x -= amplifierX
          else:
            isfacingRight = True
        
      
      if pygame.mouse.get_pressed()[2]:
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