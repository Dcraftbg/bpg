
#import bpg
import pygame
from . import bpg
class Image(bpg.Component):
    visible = True
    def __init__(self,path):
        self.image = pygame.image.load(path).convert()
    def action(self, objWindow, events=[]) -> None:
        objWindow.window.blit(self.image,(self.x,self.y))
    def onAdd(self, objWindow) -> None:
        objWindow.window.blit(self.image,(self.x,self.y))
    #sugar syntax
    @property
    def width(self) -> int:
        return self.image.get_width()
    @property
    def height(self) -> int:
        return self.image.get_height()
class textBox(bpg.Component):
    text = ""
    _tsurface = None
    colorText = (0,0,0)
    def __init__(self,text:str,textSize: int = 24,x:int = 0, y:int = 0,width: int = 0, height: int = 0,fontName: str = "Calibri",antialias=False, colorText = (0,0,0), colorBackground = (255,255,255),alphaBackGround: int = 255):
        
        font = pygame.font.SysFont(fontName, textSize)
        
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.font = font
        self.text = text
        self.antialias = antialias
        self.color = colorText
        self.colorBackground = colorBackground
        self.alphaBackGround = alphaBackGround
    def getSurface(self) -> pygame.Surface:
        return self.font.render(self.text, self.antialias,self.color,self.colorBackground)
    def updateSurface(self) -> None:
        self._tsurface = self.font.render(self.text, self.antialias,self.color,self.colorBackground)
    def updateSize(self,i: int):
        if i > 0 and i < 5:
            self.updateSurface()
            rect = self._tsurface.get_rect()
            match i:
                case 1:
                  self.x = rect.x
                case 2:
                  self.y = rect.y
                case 3:
                  self.width = rect.width
                case 4:
                  self.height = rect.height
    def action(self, objWindow, events=[]) -> None:
        self.updateSurface()
        rimg = self._tsurface.get_rect()
        
        if self.x == 0:
            self.x = rimg.x
        if self.y == 0:
            self.y = rimg.y
        if self.width == 0:
            self.width = rimg.width
        if self.height == 0:
            self.height = rimg.height
        #rimg.topright = (self.x,self.y)
        #rimg.bottomright = (self.x+self.width,self.y+self.height)
        rimg.x = self.x
        rimg.y = self.y
        rimg.width = self.width
        rimg.height = self.height
        #pygame.draw.rect(objWindow.window,self.colorBackground,rimg)
        objWindow.window.blit(self._tsurface, rimg)
        #objWindow.window.blit(self._tsurface,(20,20))
        
    
    
    
class writeBox(bpg.Component):
    allowInput = True
    selected = False
    actionEvents = [pygame.MOUSEBUTTONDOWN,pygame.KEYDOWN]
    text = ""
    def __init__(self,x=0,y=0,width=100,height=50, color=(255,255,255), startText=""):
        self.x = x
        self.y = y
        self.color = color
        self.width = width
        self.height = height
        self.text = startText
        self.textBox = textBox(startText)
        #self.testBox = Rectangle((x,y),(x+width,y+height))
        
        #self.textB = textBox(startText)
    def onAdd(self, objWindow) -> None:
        objWindow.add(self.textBox)
    def action(self, objWindow, events=[]) -> None:
        
        # if len(events) > 0:
        #     print(events)
        self.textBox.text = self.text
        if self.allowInput:
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mpos = pygame.mouse.get_pos()        
                    #print("Hi!")
                    if mpos[0] < self.x + self.width and mpos[0] > self.x and mpos[1] < self.y + self.height and mpos[1] > self.y:
                        self.selected = True
                        #print("Selected")
                    else:
                        self.selected = False
                        #print("Deselected")
                if event.type == pygame.KEYDOWN and self.selected:
                    #print(pygame.key.name(event.key))
                    if not pygame.key.name(event.key) == "backspace":
                        self.text += event.unicode
                    else:
                        self.text = self.text[:len(self.text)-1]
class Button(bpg.Component):
    width = 0
    height = 0
    def __init__(self,width=100,height=50):
        self.width = width
        self.height = height
    actionEvents = [pygame.MOUSEBUTTONDOWN]
    __hasEntered = False
    def exitedButton(self,objWindow) -> None:
        pass
    def _outHover(self,objWindow) -> None:
        pass
    def onHover(self,objWindow) -> None:
        pass
    def rightClicked(self, objWindow) -> None:
        pass
    def leftClicked(self,objWindow) -> None:
        pass
    def middleClicked(self,objWindow) -> None:
        pass
    def action(self, objWindow, events) -> None:
        mpos = pygame.mouse.get_pos()
        if mpos[0] < self.x + self.width and mpos[0] > self.x and mpos[1] < self.y + self.height and mpos[1] > self.y:
            self.__hasEntered = True
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            self.onHover(objWindow)
            if len(events) > 0:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                if pygame.mouse.get_pressed()[0]:
                    self.leftClicked(objWindow)
                if pygame.mouse.get_pressed()[1]:
                    self.middleClicked(objWindow)
                if pygame.mouse.get_pressed()[2]:
                    self.rightClicked(objWindow)
        else:
            self._outHover(objWindow)
            if self.__hasEntered:
                self.__hasEntered = False
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                self.exitedButton(objWindow)

class Rectangle(bpg.Component):
    width = 0
    height = 0
    visible = True
    def __init__(self,pos1:bpg.Position | tuple,pos2:bpg.Position | tuple,color=(255,255,255)) -> None:
        x1 = 0
        y1 = 0
        x2 = 0
        y2 = 0
        if type(pos1) is bpg.Position:
            self.pos1 = pos1
            x1 = pos1.x
            y1 = pos1.y
        elif type(pos1) is tuple:
            self.pos1 = bpg.Position(pos1[0],pos1[1])
        if type(pos2) is bpg.Position:
            self.pos2 = pos2
            x2 = pos2.x
            y2 = pos2.y
        elif type(pos2) is tuple:
            self.pos2 = bpg.Position(pos2[0],pos2[1])
        self.width = x1 - x2
        self.height = y1 - y2
        self.color = color
    def action(self,objWindow,events) -> None:
        if self.visible:
            pygame.draw.rect(objWindow.window,self.color,pygame.Rect(self.pos1.x,self.pos1.y,self.pos2.x,self.pos2.y))