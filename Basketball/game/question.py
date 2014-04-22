import spyral
import random

import math
import wallbreaker
import basketball2



WIDTH = 1200

HEIGHT = 900
BG_COLOR = (0,0,0)

WHITE = (255, 255, 255)

SIZE = (WIDTH, HEIGHT)

DEF_FONT = "libraries/spyral/resources/fonts/DejaVuSans.ttf"


class Question(spyral.Scene):
    def __init__(self, *args, **kwargs):
        global manager
	global counter
        spyral.Scene.__init__(self, SIZE)
  
        self.background = spyral.Image(filename= "game/background.png")
        
        global counter 
	counter = 0
        self.b1 = Basket(self, 150,400, False,1)
	self.b2 = Basket(self, 600, 400, False,2)
	self.b3 = Basket(self, 1050,400, False,3) 
	spyral.event.register("input.mouse.down.left", self.handle_clicked) 
	spyral.event.register("system.quit", spyral.director.pop)
	spyral.event.register("input.keyboard.down.q", spyral.director.pop)
 	font = spyral.Font("/usr/share/fonts/truetype/freefont/FreeMono.ttf",36,(255,255,255))
	message = font.render("Pick one of the options");
	message1 = font.render("Easy");
	message2 = font.render("Medium");
	message3 = font.render("Hard");
	self.q1 = questionMessage(self,message,(0),10)
	self.q2 = questionMessage(self,message1,(100),600)
	self.q3 = questionMessage(self,message2,(550),600)
	self.q4 = questionMessage(self,message3,(1000),600)

	#message3 = font.render(counter);
	#self.c1 = questionMessage(self,message3,(1100),10)
    def handle_clicked(self, pos):
	if pos.x >400 and pos.x<=800 and pos.y>300:
		spyral.director.push(basketball2.BasketBall2())	
	elif pos.x>800 and pos.y>300:
		 spyral.director.push(basketball2.BasketBall2())	
	elif pos.x <400 and pos.y>300:
		spyral.director.push(basketball2.BasketBall2())
class Basket(spyral.Sprite):
  def __init__(self, scene, x,y,correct,num):
   super(Basket,self).__init__(scene)
   self.image = spyral.Image(filename="game/newbasket.png")
   self.anchor = 'center'
   self.x = x
   self.y = y
   self.correct = correct
   self.num = num

class questionMessage(spyral.Sprite):
	def __init__(self,scene,img,x,y):
		spyral.Sprite.__init__(self,scene)
		self.image = img
		self.x = x
		self.y = y

