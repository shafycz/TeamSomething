import spyral
import random

import math
import basketball
import basketball2
import question



WIDTH = 1200

HEIGHT = 900
BG_COLOR = (0,0,0)

WHITE = (255, 255, 255)

SIZE = (WIDTH, HEIGHT)

DEF_FONT = "libraries/spyral/resources/fonts/DejaVuSans.ttf"


class Test2(spyral.Scene):

    def __init__(self):
	global counter
        super(Test2, self).__init__(SIZE)

	self.background = spyral.Image(filename= "game/background.png")
        spyral.event.register('input.keyboard.down.q', spyral.director.quit)

        spyral.event.register("system.quit", spyral.director.quit)
	spyral.event.register("input.mouse.down.left", self.handle_clicked) 

        
	
	font = spyral.Font("/usr/share/fonts/truetype/freefont/FreeMono.ttf",280,(255,255,255))
	message = font.render("Correct");
	StartMessage(self,message,(0),200)
	
    def handle_clicked(self, pos):
	   	
	
		spyral.director.push(basketball.Basketball())

 
class StartMessage(spyral.Sprite):
	def __init__(self,scene,img,x,y):
		spyral.Sprite.__init__(self,scene)
		self.image = img
		self.x = x
		self.y = y

