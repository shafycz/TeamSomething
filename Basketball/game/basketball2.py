import spyral
import random

import math
import wallbreaker
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

        self.background = spyral.Image(filename= "game/background.png")
	self.start = Start(self,150,300)
	self.start2 = Start(self, 600,300)
	self.start3 = Start(self, 1050,300)
	font = spyral.Font("/usr/share/fonts/truetype/freefont/FreeMono.ttf",100,(255,255,255))
	#message = font.render("Click to Start");
	#StartMessage(self,message,(200),10)
   	self.v1 = Vertline(self, 225,500)
	self.v2 = Vertline(self,675,500)
	self.v3 = Vertline(self,1125,500)
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
	global x2_array   	
	#global counter
	
	if x2_array[0] == 0:
		if pos.x >400 and pos.x<=800:
			self.start2.kill()
			self.v2.kill()
		elif pos.x>800:
			self.v3.kill()
			self.start3.kill()
		elif pos.x <400:
			#counter = counter +1			
			spyral.director.push(test2.Test2())

	elif x2_array[0] == 400:
		if pos.x <400:
			self.v1.kill()
			self.start.kill()
		elif pos.x>800:
			self.v3.kill()
			self.start3.kill()
		elif pos.x >400 and pos.x <800:
			#counter = counter +1
			spyral.director.push(test2.Test2())
	elif x2_array[0] == 800:
		if pos.x <400:
			self.v1.kill()
			self.start.kill()
		elif pos.x<800 and pos.x>400:
			self.v2.kill()
			self.start2.kill()
		elif pos.x >800 and pos.y>300:
			#counter = counter +1
			spyral.director.push(test2.Test2())
class Vertline(spyral.Sprite):
    def __init__(self, scene, x, y):
        spyral.Sprite.__init__(self, scene)
        self.image = spyral.Image(size=(10, 600)).fill((40, 50, 255))
	self.anchor = 'midleft'
	self.x = x
	self.y = y
		 
class Start(spyral.Sprite):
  def __init__(self, scene, x,y):
   super(Start,self).__init__(scene)

  

   self.image = spyral.Image(filename="game/basket3.png")
   self.anchor = 'center'
   self.x = x
   self.y = y
 
class StartMessage(spyral.Sprite):
	def __init__(self,scene,img,x,y):
		spyral.Sprite.__init__(self,scene)
		self.image = img
		self.x = x
		self.y = y






