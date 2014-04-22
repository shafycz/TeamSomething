import spyral
import random

import math
import basketball



WIDTH = 1200

HEIGHT = 900
BG_COLOR = (0,0,0)

WHITE = (255, 255, 255)

SIZE = (WIDTH, HEIGHT)

DEF_FONT = "libraries/spyral/resources/fonts/DejaVuSans.ttf"


class MainMenu(spyral.Scene):

    def __init__(self):

        super(MainMenu, self).__init__(SIZE)


        spyral.event.register('input.keyboard.down.q', spyral.director.quit)

        spyral.event.register("system.quit", spyral.director.quit)
	spyral.event.register("input.mouse.down.left", self.handle_clicked) 

        self.background = spyral.Image(filename= "game/background.png")
	self.start = Start(self,600,300)
	
	font = spyral.Font("/usr/share/fonts/truetype/freefont/FreeMono.ttf",100,(255,255,255))
	message = font.render("Click to Start");
	StartMessage(self,message,(200),10)
   
    def handle_clicked(self, pos):
	   	
	if pos.y <450:
		spyral.director.push(basketball.Basketball())
	 
class Start(spyral.Sprite):
  def __init__(self, scene, x,y):
   super(Start,self).__init__(scene)

  

   self.image = spyral.Image(filename="game/newbasket.png")
   self.anchor = 'center'
   self.x = x
   self.y = y
 
class StartMessage(spyral.Sprite):
	def __init__(self,scene,img,x,y):
		spyral.Sprite.__init__(self,scene)
		self.image = img
		self.x = x
		self.y = y






