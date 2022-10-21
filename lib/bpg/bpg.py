import pygame
pygame.init()

class Position:
    x = 0
    y = 0
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y
class Component:
    x = 0
    y = 0
    actionEvents = []
    def __init__(self):
        pass
    def redraw(self,objWindow) -> None:
        pass
    def onAdd(self,objWindow) -> None:
        '''
        !!!!THIS SHOULD NOT BE USED OUTSIDE OF THE WINDOW CLASS WITH add() METHOD!!!!
        '''
        pass
    def setPos(self,arg) -> None:
        if type(arg) == tuple:
            x = arg[0]
            y = arg[1]
        elif type(arg) == Position:
            x = arg.x
            y = arg.y
        else:
            raise Exception("Parameter Object Not Recognised. List of posible arguments:\n- tuple\n- Position")
        self.x = x
        self.y = y
    def action(self,objWindow,events = []) -> None:
        pass
    
class Window:
    window = None
    components = []
    events = []
    
    
    updateWindowOnAdd = True
    redrawSpritesOnUpdate = True
    
    
    
    def __init__(self,*args) -> None:
        self.window = pygame.display.set_mode(args)
        self.size = args[0]
    def add(self,objComponent) -> None:
        objComponent.onAdd(self)
        self.components.append(objComponent)
        if self.updateWindowOnAdd:
            self.update()
    def redrawSprites(self,i=0,all=False) -> None:
        if all:
            for comp in self.components:
                comp.redraw(self) 
        else:
            self.components[i].redraw(self)
    def fetchEvents(self) -> None:
        '''
        Not to get confused with events, fetch events just updates the list of concurrent events it DOESN'T RETURN THEM.
        '''
        self.events = pygame.event.get()
        
    #update elements 
    def update(self) -> None:
        self.window.fill((0,0,0))
        if self.redrawSpritesOnUpdate:
            self.redrawSprites(all=True)
        for c in self.components:
            if len(c.actionEvents) > 0:
                if len(self.events) > 0:
                    e = []
                    for event in self.events:
                        for actionEvent in c.actionEvents:
                            if event.type == actionEvent:
                                e.append(event)
                    c.action(self,e)
                        # if c.actionEvents[co] == event.type:
                        #     e.append(event)
                        # if co >= len(c.actionEvents)-1:
                        #     c.action(self,e)
                        #     break
                            
            else:
                c.action(self,[])
        pygame.display.update()    
        
    
    
    
    #syntax sugar
    def setIcon(self,iconPath) -> None:
        a = pygame.image.load(iconPath).convert()
        pygame.display.set_icon(a)
    def setTitle(self,title) -> None:
        pygame.display.set_caption(title)
    @property
    def width(self) -> int:
        return self.window.get_width()
    @property
    def height(self) -> int:
        return self.window.get_height()
