'''

Note this is still very very early into development and might become unstable at some points until its officially released

'''

# import pygame
# from utils import Button

# class eButton(Button):
#     showImg = False
#     showColor = True
#     def __init__(self, width=100, height=50, imgPath="", color=(255,255,255), onClickImg="", onClickColor=(255,255,255), onHoverImg="", onHoverColor=(255,255,255)):
#         super().__init__(width, height)
#         if len(imgPath) > 0:
#             self.img = pygame.image.load(imgPath).convert()
#             if len(onClickImg) > 0:
#                 self.onclickimg = pygame.image.load(onClickImg).convert()
#             else:
#                 self.onclickimg = self.img
#             if len(onHoverImg) > 0:
#                 self.onhoverimg = pygame.image.load(onHoverImg).convert()
#         self.onclickcolor = onClickColor
#         self.color = color
#         self.onhovercolor = onHoverColor
#     def action(self, objWindow, events) -> None:
#         if len(events) > 0:
#             mpos = pygame.mouse.get_pos()
#             if mpos[0] < self.x + self.width and mpos[0] > self.x and mpos[1] < self.y + self.height and mpos[1] > self.y:
#                 if pygame.mouse.get_pressed()[0]:
#                     self.leftClicked(objWindow)
#                 if pygame.mouse.get_pressed()[1]:
#                     self.middleClicked(objWindow)
#                 if pygame.mouse.get_pressed()[2]:
#                     self.rightClicked(objWindow)
                    
        
        
        
    