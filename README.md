# About
Easier Pygame. That one library to help you with all your basic needs that pygame, sometimes just doesn't provide.




# How to install library?
Well there are many ways to install the library but the easiest one is downloading the "bpg" folder from lib. You can then paste it into your projects directory or in a 
sub directory to your main source file. 
Core files:
```
lib/bpg/bpg
lib/bpg/utils
lib/bpg/__init__
```

# How to use bpg?
You can find example file/s in the top level of the repository. They are a basic showcase of a few of bpgs features.


All of the **bare bone** functions for using bpg can be accessed by doing:
```
bpg.<whatever part of the core library you are using>
```
The bpg.py file contains:
```
Window (class) -> For creating your windows
Component (class) -> The base for all components that are built on top of bpg
```

To create a basic game you do:
```py
from bpg import * #our import

window = bpg.Window((500,250)) #creating the window. Takes in the same arguments pygame does
window.setTitle("My first game!") #setting the title of the window

running = True #running variable we are going to use for our game loop
while running: #our game loop
  window.fetchEvents() #you need to call it at the start of each frame. It updates the current events the window is getting
  for event in window.events: #loop through all of the events
    if event.type == pygame.QUIT: #check if the user has clicked the red X at the top for closing the application
      running = False #close the application
   window.update() #update all sprites at the end of each frame. 
```



You can create your own Components using the component class. The component class comes with:
- Functions:
```
action(objWindow, events)
-> Is called every time a new frame is updated. Parameters:

objWindow -> Returns the current window
events -> Returns a list of all active actionEvents (you will find more about them under "variables")
```
```
onAdd(objWindow)
-> Is called at the moment the component is added to a window. Parameters:
objWindow -> Returns the current window
```
```
redraw(objWindow)
-> Is called whenever the window.redraw() method is called or when window.redrawSpritesOnUpdate is on. Parameters:
objWindow -> Returns the current window
```
- Variables:
```
x -> Current X position
y -> Current Y position
actionEvents -> Its a list of events that consists of all of the events the action function might need to run. If the event is currently active the "events" variable taken
as a parameter is going to consist of that method. If none of the events are currently active the "events" parameter is going to be an empty list of events.
```

After you create a component you can add it with the window.add(Component).

# What is bpg utils?
 
The bpg/utils.py file contains a lot of useful Components. It **currently** consists of:
```
Rectangle (class) -> For making rectangles
Image (class) -> For loading images
Button (class) -> For making buttons
textBox (class) -> For displaying text
writeBox (class) -> For getting text as input
```



