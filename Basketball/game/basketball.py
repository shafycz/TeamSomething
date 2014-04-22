import spyral
import random
import math
from spyral import Animation, easing
import time
import test

WIDTH = 1200
HEIGHT = 900
BG_COLOR = (0,0,0)
WHITE = (255, 255, 255)
SIZE = (WIDTH, HEIGHT)


	

class Basket(spyral.Sprite):
  def __init__(self, scene, x,y,correct,num):
   super(Basket,self).__init__(scene)
   
   counter = 0

  

   self.image = spyral.Image(filename="game/newbasket.png")
   self.anchor = 'center'
   self.x = x
   self.y = y
   self.correct = correct
   self.num = num

class One(spyral.Sprite):
  def __init__(self, scene, x,y):
   super(One,self).__init__(scene)
   self.image = spyral.Image(filename="game/1.png")
   self.anchor = 'center'
   self.x = x
   self.y = y
  
		 
class Two(spyral.Sprite):
  def __init__(self, scene, x,y):
   super(Two,self).__init__(scene)
   self.image = spyral.Image(filename="game/2.png")
   self.anchor = 'center'
   self.x = x
   self.y = y
 
		 
class Three(spyral.Sprite):
  def __init__(self, scene, x,y):
   super(Three,self).__init__(scene)
   self.image = spyral.Image(filename="game/3.png")
   self.anchor = 'center'
   self.x = x
   self.y = y

class questionMessage(spyral.Sprite):
	def __init__(self,scene,img,x,y):
		spyral.Sprite.__init__(self,scene)
		self.image = img
		self.x = x
		self.y = y
class choiceMessage(spyral.Sprite):
	def __init__(self,scene,img,x,y):
		spyral.Sprite.__init__(self,scene)
		self.image = img
		self.x = x
		self.y = y

class Basketball(spyral.Scene):
    def __init__(self, *args, **kwargs):
        global manager
        spyral.Scene.__init__(self, SIZE)
  
        self.background = spyral.Image(filename= "game/background.png")
        
        global counter 
	counter = 0
        self.b1 = Basket(self, 150,400, False,1)
	self.b2 = Basket(self, 600, 400, False,2)
	self.b3 = Basket(self, 1050,400, False,3) 
	self.ball1 = One(self,150,250)
	self.ball2 = Two(self,600, 250)
	self.ball3 = Three(self, 1050,250)
	spyral.event.register("system.quit", spyral.director.pop)
	spyral.event.register("input.keyboard.down.q", spyral.director.pop)
	spyral.event.register("input.mouse.down.left", self.handle_clicked) 
   	question_array = ["There are __ many people in the mall.", "I wish I had __ dogs."]
	choices_array =["1. to 2. two 3. too","1. to 2. two 3. too"]
	global x_array
	x_array = [800]
	font = spyral.Font("/usr/share/fonts/truetype/freefont/FreeMono.ttf",36,(255,255,255))
	message = font.render(question_array[0]);
	message2 =font.render(choices_array[0]);
	questionMessage(self,message,(0),10)
	choiceMessage(self,message2,(0),50)
	

    def handle_clicked(self, pos):
	global x_array   	
	global counter
	
	if x_array[0] == 0:
		if pos.x >400 and pos.x<=800 and pos.y>300:
			self.b2.kill()
			self.ball2.kill()
		elif pos.x>800 and pos.y>300:
			self.b3.kill()
			self.ball3.kill()
		elif pos.x <400 and pos.y>300:
			counter = counter +1
			spyral.director.push(test.Test())

	elif x_array[0] == 400:
		if pos.x <400 and pos.y>300:
			self.b1.kill()
			self.ball1.kill()
		elif pos.x>800 and pos.y>300:
			self.b3.kill()
			self.ball3.kill()
		elif pos.x >400 and pos.x <800 and pos.y>300:
			counter = counter +1			
			spyral.director.push(test.Test())
	elif x_array[0] == 800:
		if pos.x <400 and pos.y>300:
			self.b1.kill()
			self.ball1.kill()
		elif pos.x<800 and pos.x>400 and pos.y>300:
			self.b2.kill()
			self.ball2.kill()
		elif pos.x >800 and pos.y>300:
			counter = counter + 1
			spyral.director.push(test.Test())
		

