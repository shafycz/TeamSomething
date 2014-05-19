import spyral
import random
import math
from spyral import Animation, easing
import time
import test
import game

WIDTH = 1200
HEIGHT = 900
BG_COLOR = (0,0,0)
WHITE = (255, 255, 255)
SIZE = (WIDTH, HEIGHT)


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
  
        self.background = spyral.Image(filename= "game/background1.png")
        
        
        self.ball1 = One(self,150,250)
	self.ball2 = Two(self,600, 250)
	self.ball3 = Three(self, 1050,250)
	spyral.event.register("system.quit", spyral.director.pop)
	spyral.event.register("input.keyboard.down.q", spyral.director.pop)
	spyral.event.register("input.mouse.down.left", self.handle_clicked) 
   	question_array = ["There are __ many people in the mall.", "I wish I had __ dogs.", "He is ___ young.", "She had ___ teaspoons of sugar in her tea.",
	 "I like ___ be in the mountains.", "Mary saw a movie yesterday. I saw one ____.", "His house is near ___ rivers.", "Who are you going to give the present ___?",
	  "Can I have one of those ___?", "We live close ___ here.",
	
	"According to legend, ___ is treasure buried on the island.", "John and Jake said ___ coming for dinner.", "___ is a mouse in my closet.",
	"I wonder if ___ still planning on going to the park today.", "I can't wait to see the look on ___ faces.", "It is still ___ decision.",
	"I think Deb left her glasses over ___.", "I don't know what ___ doing to cause all that noise.", "Can you check over ___?", "I wish ___ stay in town was longer."]
	choices_array =["1. to 2. two 3. too","1. to 2. two 3. too", "1. to 2. two 3. too", "1. to 2. two 3. too", "1. to 2. two 3. too",
	"1. to 2. two 3. too", "1. to 2. two 3. too", "1. to 2. two 3. too", "1. to 2. two 3. too", "1. to 2. two 3. too",
	
	"1. their 2. there 3. they're", "1. their 2. there 3. they're", "1. their 2. there 3. they're", "1. their 2. there 3. they're", "1. their 2. there 3. they're",
	 "1. their 2. there 3. they're", "1. their 2. there 3. they're", "1. their 2. there 3. they're", "1. their 2. there 3. they're", "1. their 2. there 3. they're"]
	global x_array
	x_array = [800]
	font = spyral.Font("/usr/share/fonts/truetype/freefont/FreeMono.ttf",36,(255,255,255))
	message = font.render(question_array[0]);
	message2 =font.render(choices_array[0]);
	questionMessage(self,message,(0),10)
	choiceMessage(self,message2,(0),50)
	m2 = font.render(str(game.Counter))
	choiceMessage(self,m2,(960),20)
	m3 = font.render(str(game.Counter1))
	choiceMessage(self,m3,(1150),20)
	

    def handle_clicked(self, pos):
	global x_array   	
	
	
	if x_array[0] == 0:
		if pos.x >400 and pos.x<=800 and pos.y>300:
			#self.b2.kill()
			self.ball2.kill()
		elif pos.x>800 and pos.y>300:
			#self.b3.kill()
			self.ball3.kill()
		elif pos.x <400 and pos.y>300:
			Game.counter = Game.counter +1
			spyral.director.push(test.Test())
			spyral.director.pop()

	elif x_array[0] == 400:
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
		if pos.x <400 and pos.y>300:
			#self.b1.kill()
			self.ball1.kill()
		elif pos.x<800 and pos.x>400 and pos.y>300:
			#self.b2.kill()
			self.ball2.kill()
		elif pos.x >800 and pos.y>300:
			counter = counter + 1
			
			game.Counter = game.Counter +1
		
			spyral.director.push(test.Test())
			#spyral.director.pop()		

