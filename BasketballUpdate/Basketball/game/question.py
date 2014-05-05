import spyral
import random

import math
#import wallbreaker
import basketball2
import game


WIDTH = 1200

HEIGHT = 900
BG_COLOR = (0,0,0)

WHITE = (255, 255, 255)

SIZE = (WIDTH, HEIGHT)

DEF_FONT = "libraries/spyral/resources/fonts/DejaVuSans.ttf"

  
 
		 
class Check(spyral.Sprite):
  def __init__(self, scene, x,y):
   super(Check,self).__init__(scene)
   self.image = spyral.Image(filename="game/check.png")
   self.anchor = 'center'
   self.x = x
   self.y = y

class Question(spyral.Scene):
    def __init__(self, *args, **kwargs):
        global manager
	global counter
        spyral.Scene.__init__(self, SIZE)
  
        self.background = spyral.Image(filename= "game/background5.png")
        
        global counter 
	counter = 0
        
	spyral.event.register("input.mouse.down.left", self.handle_clicked) 
	spyral.event.register("system.quit", spyral.director.pop)
	spyral.event.register("input.keyboard.down.q", spyral.director.pop)
 	font = spyral.Font("/usr/share/fonts/truetype/freefont/FreeMono.ttf",36,(255,255,255))
	question_array = ["The cat ___ the bird around the room.", "Fill in here with a new sentence"]
	subject_array =["The subject is 1. cat 2. bird 3. room ","The subject is 1. answer 2. answer 3. answer"]
	verb_array = ["The correct form of the verb is 1. chase  2. chased  3. chasing", "The correct form of the verb is 1. answer 2. answer 3. answer"]
	number_array = ["How many nouns are there 1. 1 2. 2 3. 3", "blah blah blah"]

	global x_array
	x_array = [1,0]
	global y_array
	y_array = [2,0]
	global z_array
	z_array = [3,0]
	sont = spyral.Font("/usr/share/fonts/truetype/freefont/FreeMono.ttf",30,(50,50,60))
	message4 = font.render(question_array[0]);
	message5 =sont.render(subject_array[0]);
	message6 = sont.render(verb_array[0]);
	message7 = sont.render(number_array[0]);
	questionMessage(self,message4,(0),10)
	questionMessage(self,message5,(0),575)
	questionMessage(self,message6,(0),625)	
	questionMessage(self,message7,(0),670)
	message = font.render("");
	message1 = font.render("2.");
	message2 = font.render("1.");
	message3 = font.render("3.");
	self.q1 = questionMessage(self,message,(0),10)
	self.q2 = questionMessage(self,message1,(10),310)
	self.q3 = questionMessage(self,message2,(10),200)
	self.q4 = questionMessage(self,message3,(10),450)
	self.h1 = Horline(self, 0,250)
	self.h2 = Horline(self, 0,400)
	self.h3 = Horline(self, 0,555)
	self.v3 = Vertline(self, 350, 350)
	self.v1 = Vertline(self, 750, 350)
	self.c1 = Check(self,500,500)
	#message3 = font.render(counter);
	#self.c1 = questionMessage(self,message3,(1100),10)
    def handle_clicked(self, pos):
	global x_array
	global z_array
	global y_array
	'''
	if x_array[0] = 1
		if pos.x > elif x_array[0] == 400:
		if pos.x <400 and pos.y>300:
			#self.b1.kill()
			self.ball1.kill()
		elif pos.x>800 and pos.y>300:
			#self.b3.kill()
			self.ball3.kill()
		elif pos.x >400 and pos.x <800 and pos.y>300:
			Game.counter = Game.counter +1			
			spyral.director.push(test.Test())
			spyral.director.pop()
	elif x_array[0] == 800:
	'''
#class checl(spyral.Sprite):
#	def __init__(self,scene,img,x,y):
	
class questionMessage(spyral.Sprite):
	def __init__(self,scene,img,x,y):
		spyral.Sprite.__init__(self,scene)
		self.image = img
		self.x = x
		self.y = y
class Vertline(spyral.Sprite):
    def __init__(self, scene, x, y):
        spyral.Sprite.__init__(self, scene)
        self.image = spyral.Image(size=(10, 400)).fill((255, 255, 255))
	self.anchor = 'midleft'
	self.x = x
	self.y = y
	
class Horline(spyral.Sprite):
    def __init__(self, scene,x, y):
        spyral.Sprite.__init__(self, scene)
        self.image = spyral.Image(size=(1200, 10)).fill((255, 255, 255))
	self.anchor = 'midleft'
	self.x = x
	self.y = y
	
