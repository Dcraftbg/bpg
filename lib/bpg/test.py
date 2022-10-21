from bpg import *
from utils import *
from utils_2 import *
inputBox = writeBox()
print(f"{inputBox.x},{inputBox.y} {inputBox.width},{inputBox.height}")
window = Window((500,500))
window.setTitle("SUSSY GAME")
window.add(inputBox)
running = True
counter = 1
print(pygame.KEYDOWN)
while running:
  window.fetchEvents()
  # if len(window.events) > 0:
  #   counter += 1
  #   print(window.events)
  if counter >= 1000:
    running = False
  for event in window.events:
    if event.type == pygame.QUIT:
      running = False
  window.update()