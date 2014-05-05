import spyral
import random

import math
#import wallbreaker
import test2



WIDTH = 1200

HEIGHT = 900
BG_COLOR = (0,0,0)

WHITE = (255, 255, 255)

SIZE = (WIDTH, HEIGHT)

DEF_FONT = "libraries/spyral/resources/fonts/DejaVuSans.ttf"


class BasketBall2(spyral.Scene):

    def __init__(self):

        super(BasketBall2, self).__init__(SIZE)

	global counter
        spyral.event.register('input.keyboard.down.q', spyral.director.quit)

        spyral.event.register("system.quit", spyral.director.quit)
	spyral.event.register("input.mouse.down.left", self.handle_clicked) 

        self.background = spyral.Image(filename= "game/background2.png")
	
	font = spyral.Font("/usr/share/fonts/truetype/freefont/FreeMono.ttf",100,(255,255,255))
	#message = font.render("Click to Start");
	#StartMessage(self,message,(200),10)
   	
	global x2_array
	question_array = ["I love to write papers __ I __ would write one every __ day if I had the time."]
	choices_array =["Where should the period go?"]
	x2_array = [0]
	font = spyral.Font("/usr/share/fonts/truetype/freefont/FreeMono.ttf",20,(255,255,255))
	message = font.render(question_array[0]);
	message2 =font.render(choices_array[0]);
	self.s1=StartMessage(self,message,(0),10)
	self.s2=StartMessage(self,message2,(0),50)
    
    def handle_clicked(self, pos):
	
	spyral.director.push(test2.Test2())

 
class StartMessage(spyral.Sprite):
	def __init__(self,scene,img,x,y):
		spyral.Sprite.__init__(self,scene)
		self.image = img
		self.x = x
		self.y = y






