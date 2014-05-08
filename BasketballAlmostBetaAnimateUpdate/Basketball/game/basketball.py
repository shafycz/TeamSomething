import spyral
import random
import math
from spyral import Animation, easing
import time
import test
import game
import subject
WIDTH = 1200
HEIGHT = 900
BG_COLOR = (0,0,0)
WHITE = (255, 255, 255)
SIZE = (WIDTH, HEIGHT)
BASKETX = 0 #x,y pos of the chose basket
BASKETY = 375
initX = WIDTH/2 


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
  	if game.Color == 0:
        	self.background = spyral.Image(filename= "game/colors/blackb1.png")
        elif game.Color==1:
        	self.background = spyral.Image(filename= "game/colors/blueb1.png")
	if game.Color == 2:
        	self.background = spyral.Image(filename= "game/colors/greenb1.png")
        elif game.Color==3:
        	self.background = spyral.Image(filename= "game/colors/pinkb1.png")
	if game.Color == 4:
        	self.background = spyral.Image(filename= "game/colors/purpleb1.png")
        elif game.Color==5:
        	self.background = spyral.Image(filename= "game/colors/redb1.png")
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
	m2 = font.render(str(game.Counter))
	choiceMessage(self,m2,(960),20)
	m3 = font.render(str(game.Counter1))
	choiceMessage(self,m3,(1150),20)
	

    def handle_clicked(self, pos):
	global x_array   	
	
	
	if x_array[0] == 0:
		if pos.x >400 and pos.x<=800 and pos.y>300:
			BASKETX = 600
			#self.b2.kill()
			xCoordAnim = Animation('x', easing.Linear(initX, ((initX+BASKETX)/2)), duration = 4.0)
			yCoordAnim1 = Animation('y', easing.QuadraticOut(HEIGHT, BASKETY-100),duration=2.0)
			xCoordAnim2 = Animation('x', easing.Linear(((initX+BASKETX)/2), BASKETX), duration = 4.0)
			yCoordAnim2 = Animation('y', easing.QuadraticIn(BASKETY-100,BASKETY), duration = 2.0)
			missAnim = Animation('x', easing.Linear(BASKETX, math.random.randint(0,1200)), duration = 4)
			missAnim2 = Animation('y', easing.Linear(BASKETY, 0), duration = 4)
			
			anim = ((xCoordAnim & yCoordAnim1)+(xCoordAnim2+yCoordAnim2)+(missAnim&missAnim2))
		
			self.ball2.animate(anim)
			i =random.randint(1,2)
			if i == 1:
				BASKETX = 145
				print "computer scores on 1"
				xCoordAnim = Animation('x', easing.Linear(WIDTH, ((WIDTH+BASKETX)/2)), duration = 4.0)
				yCoordAnim1 = Animation('y', easing.QuadraticOut(HEIGHT/3, BASKETY-100),duration=2.0)
				xCoordAnim2 = Animation('x', easing.Linear(((WIDTH+BASKETX)/2), BASKETX), duration = 4.0)
				yCoordAnim2 = Animation('y', easing.QuadraticIn(BASKETY-100,BASKETY), duration = 2.0)

				anim = ((xCoordAnim & yCoordAnim1)+(xCoordAnim2+yCoordAnim2))
				self.ball1.animate(anim)
				game.Counter1 = game.Counter1 +2
				if ( self.ball1.x == BASKETX and self.ball1.y == BASKETY):
					spyral.director.replace(subject.Subject())
		elif pos.x>800 and pos.y>300:
			#self.b3.kill()
			BASKETX = 1000
			xCoordAnim = Animation('x', easing.Linear(initX, WIDTH-((initX+BASKETX)/2)), duration = 4.0)
			yCoordAnim1 = Animation('y', easing.QuadraticOut(HEIGHT, BASKETY-100),duration=2.0)
			xCoordAnim2 = Animation('x', easing.Linear(WIDTH-((initX+BASKETX)/2), BASKETX), duration = 4.0)
			yCoordAnim2 = Animation('y', easing.QuadraticIn(BASKETY-100,BASKETY), duration = 2.0)
			missAnim = Animation('x', easing.Linear(BASKETX, math.random.randint(0,1200)), duration = 4)
			missAnim2 = Animation('y', easing.Linear(BASKETY, 0), duration = 4)
			
			anim = ((xCoordAnim & yCoordAnim1)+(xCoordAnim2+yCoordAnim2)+(missAnim&missAnim2))

			self.ball3.animate(anim)
			i =random.randint(1,2)
			if i == 1:
				BASKETX = 145
				print "computer scores on 1"
				xCoordAnim = Animation('x', easing.Linear(WIDTH, WIDTH-((WIDTH+BASKETX)/2)), duration = 4.0)
				yCoordAnim1 = Animation('y', easing.QuadraticOut(HEIGHT/3, BASKETY-100),duration=2.0)
				xCoordAnim2 = Animation('x', easing.Linear(WIDTH-((WIDTH+BASKETX)/2), BASKETX), duration = 4.0)
				yCoordAnim2 = Animation('y', easing.QuadraticIn(BASKETY-100,BASKETY), duration = 2.0)

				anim = ((xCoordAnim & yCoordAnim1)+(xCoordAnim2+yCoordAnim2))
				self.ball1.animate(anim)
				game.Counter1 = game.Counter1 +2
				if (self.ball1.x == BASKETX and  self.ball1.y == BASKETY):
					spyral.director.replace(subject.Subject())
		elif pos.x <400 and pos.y>300:
			BASKETX = 145
			xCoordAnim = Animation('x', easing.Linear(initX, WIDTH-((initX+BASKETX)/2)), duration = speed)
			yCoordAnim1 = Animation('y', easing.QuadraticOut(HEIGHT, BASKETY-100),duration=2.0)
			xCoordAnim2 = Animation('x', easing.Linear(WIDTH-((initX+BASKETX)/2), BASKETX), duration = 4.0)
			yCoordAnim2 = Animation('y', easing.QuadraticIn(BASKETY-100,BASKETY), duration = 2.0)
			anim = ((xCoordAnim & yCoordAnim1)+(xCoordAnim2+yCoordAnim2))
			self.ball1.animate(anim)
			game.Counter = game.Counter +2
			if (self.ball1.x == BASKETX and  self.ball1.y == BASKETY):
				spyral.director.replace(subject.Subject())

	elif x_array[0] == 400:
		if pos.x <400 and pos.y>300:
			#self.b1.kill()
			BASKETX = 145
			xCoordAnim = Animation('x', easing.Linear(initX, WIDTH-((initX+BASKETX)/2)), duration = 4.0)
			yCoordAnim1 = Animation('y', easing.QuadraticOut(HEIGHT, BASKETY-100),duration=2.0)
			xCoordAnim2 = Animation('x', easing.Linear(WIDTH-((initX+BASKETX)/2), BASKETX), duration = 4.0)
			yCoordAnim2 = Animation('y', easing.QuadraticIn(BASKETY-100,BASKETY), duration = 2.0)
			missAnim = Animation('x', easing.Linear(BASKETX, math.random.randint(BASKETX-200,BASKETX+200)), duration = 4)
			missAnim2 = Animation('y', easing.QuadraticIn(BASKETY, HEIGHT), duration = 3)
			
			anim = ((xCoordAnim & yCoordAnim1)+(xCoordAnim2+yCoordAnim2)+(missAnim&missAnim2))
			self.ball1.animate(anim)
			i =random.randint(1,2)
			if i == 1:
				print "computer scores on 2"
				BASKETX = 600
				xCoordAnim = Animation('x', easing.Linear(WIDTH, WIDTH-((WIDTH+BASKETX)/2)), duration = 4.0)
				yCoordAnim1 = Animation('y', easing.QuadraticOut(HEIGHT/3, BASKETY-100),duration=2.0)
				xCoordAnim2 = Animation('x', easing.Linear(WIDTH-((WIDTH+BASKETX)/2), BASKETX), duration = 4.0)
				yCoordAnim2 = Animation('y', easing.QuadraticIn(BASKETY-100,BASKETY), duration = 2.0)

				anim = ((xCoordAnim & yCoordAnim1)+(xCoordAnim2+yCoordAnim2))
				self.ball2.animate(anim)
				game.Counter1 = game.Counter1 +2
				if (self.ball2.x == BASKETX and  self.ball2.y == BASKETY):
					spyral.director.replace(subject.Subject())
		elif pos.x>800 and pos.y>300:
			#self.b3.kill()
			BASKETX = 1000
			xCoordAnim = Animation('x', easing.Linear(WIDTH, WIDTH-((WIDTH+BASKETX)/2)), duration = 4.0)
			yCoordAnim1 = Animation('y', easing.QuadraticOut(HEIGHT/3, BASKETY-100),duration=2.0)
			xCoordAnim2 = Animation('x', easing.Linear(WIDTH-((WIDTH+BASKETX)/2), BASKETX), duration = 4.0)
			yCoordAnim2 = Animation('y', easing.QuadraticIn(BASKETY-100,BASKETY), duration = 2.0)
			missAnim = Animation('x', easing.Linear(BASKETX, math.random.randint(BASKETX-200,BASKETX+200)), duration = 4)
			missAnim2 = Animation('y', easing.QuadraticIn(BASKETY, HEIGHT), duration = 3)
			
			anim = ((xCoordAnim & yCoordAnim1)+(xCoordAnim2+yCoordAnim2)+(missAnim&missAnim2))
			self.ball3.animate(anim)
			i =random.randint(1,2)
			if i == 1:
				BASKETX = 600
				print "computer scores on 2"
				xCoordAnim = Animation('x', easing.Linear(WIDTH, WIDTH-((WIDTH+BASKETX)/2)), duration = 4.0)
				yCoordAnim1 = Animation('y', easing.QuadraticOut(HEIGHT/3, BASKETY-100),duration=2.0)
				xCoordAnim2 = Animation('x', easing.Linear(WIDTH-((WIDTH+BASKETX)/2), BASKETX), duration = 4.0)
				yCoordAnim2 = Animation('y', easing.QuadraticIn(BASKETY-100,BASKETY), duration = 2.0)

				anim = ((xCoordAnim & yCoordAnim1)+(xCoordAnim2+yCoordAnim2))
				self.ball2.animate(anim)
				game.Counter1 = game.Counter1 +2
				if (self.ball2.x == BASKETX and  self.ball2.y == BASKETY):
					spyral.director.replace(subject.Subject())
		elif pos.x >400 and pos.x <800 and pos.y>300:
			BASKETX = 600
			xCoordAnim = Animation('x', easing.Linear(initX, WIDTH-((initX+BASKETX)/2)), duration = 4.0)
			yCoordAnim1 = Animation('y', easing.QuadraticOut(HEIGHT, BASKETY-100),duration=2.0)
			xCoordAnim2 = Animation('x', easing.Linear(WIDTH-((initX+BASKETX)/2), BASKETX), duration = 4.0)
			yCoordAnim2 = Animation('y', easing.QuadraticIn(BASKETY-100,BASKETY), duration = 2.0)
			anim = ((xCoordAnim & yCoordAnim1)+(xCoordAnim2+yCoordAnim2))
			self.ball2.animate(anim)
			game.Counter = game.Counter +2
			if (self.ball2.x == BASKETX and self.ball2.y == BASKETY):		
				spyral.director.replace(subject.Subject())
			
	elif x_array[0] == 800:
		if pos.x <400 and pos.y>300:
			#self.b1.kill()
			BASKETX = 145
			xCoordAnim = Animation('x', easing.Linear(initX, WIDTH-((initX+BASKETX)/2)-75), duration = 4.0)
			yCoordAnim1 = Animation('y', easing.QuadraticOut(HEIGHT, BASKETY-100),duration=2.0)
			xCoordAnim2 = Animation('x', easing.Linear(WIDTH-((initX+BASKETX)/2)-75, BASKETX-75), duration = 4.0)
			yCoordAnim2 = Animation('y', easing.QuadraticIn(BASKETY-100,BASKETY), duration = 2)

			anim = ((xCoordAnim & yCoordAnim1)+(xCoordAnim2+yCoordAnim2))						
			self.ball1.animate(anim)
			i =random.randint(1,2)
			print i
			if i == 1:
				BASKETX = 1000
				print "computer scores on 3"
				xCoordAnim = Animation('x', easing.Linear(WIDTH, WIDTH-((WIDTH+BASKETX)/2)), duration = 4.0)
				yCoordAnim1 = Animation('y', easing.QuadraticOut(HEIGHT/3, BASKETY-100),duration=2.0)
				xCoordAnim2 = Animation('x', easing.Linear(WIDTH-((WIDTH+BASKETX)/2), BASKETX), duration = 4.0)
				yCoordAnim2 = Animation('y', easing.QuadraticIn(BASKETY-100,BASKETY), duration = 2.0)

				anim = ((xCoordAnim & yCoordAnim1)+(xCoordAnim2+yCoordAnim2))
				self.ball3.animate(anim)
				game.Counter1 = game.Counter1 +2
				if (self.ball3.x == BASKETX and  self.ball3.y == BASKETY):
					spyral.director.replace(subject.Subject())
		elif pos.x<800 and pos.x>400 and pos.y>300:
			#self.b2.kill()
			BASKETX = 600
			xCoordAnim = Animation('x', easing.Linear(initX, ((initX+BASKETX)/2)-75), duration = 4.0)
			yCoordAnim1 = Animation('y', easing.QuadraticOut(HEIGHT, BASKETY-100),duration=4.0)
			xCoordAnim2 = Animation('x', easing.Linear(((initX+BASKETX)/2)-75, BASKETX-75), duration = 4.0)
			yCoordAnim2 = Animation('y', easing.QuadraticIn(BASKETY-100,BASKETY), duration = 4.0)

			anim = ((xCoordAnim & yCoordAnim1)+(xCoordAnim2+yCoordAnim2))			

			self.ball2.animate(anim)
			i =random.randint(1,2)
			print i
			if i == 1:
				print "computer scores on 3"
				BASKETX = 1000
				xCoordAnim = Animation('x', easing.Linear(WIDTH, ((WIDTH+BASKETX)/2)), duration = 4.0)
				yCoordAnim1 = Animation('y', easing.QuadraticOut(HEIGHT/3, BASKETY-100),duration=4.0)
				xCoordAnim2 = Animation('x', easing.Linear(((WIDTH+BASKETX)/2), BASKETX), duration = 4.0)
				yCoordAnim2 = Animation('y', easing.QuadraticIn(BASKETY-100,BASKETY), duration = 4.0)

				anim = ((xCoordAnim & yCoordAnim1)+(xCoordAnim2+yCoordAnim2))
				self.ball3.animate(anim)
				game.Counter1 = game.Counter1 +2
				if (self.ball3.x == BASKETX and self.ball3.y == BASKETY):
					spyral.director.replace(subject.Subject())
		elif pos.x >800 and pos.y>300:
			BASKETX = 1000
			xCoordAnim = Animation('x', easing.Linear(initX, WIDTH-((initX+BASKETX)/2)), duration = 4.0)
			yCoordAnim1 = Animation('y', easing.QuadraticOut(HEIGHT, BASKETY-100),duration=4.0)
			xCoordAnim2 = Animation('x', easing.Linear(WIDTH-((initX+BASKETX)/2), BASKETX), duration = 4.0)
			yCoordAnim2 = Animation('y', easing.QuadraticIn(BASKETY-100,BASKETY), duration = 4.0)
			anim = ((xCoordAnim & yCoordAnim1)+(xCoordAnim2+yCoordAnim2))
			self.ball3.animate(anim)
			
			game.Counter = game.Counter +2
			if ( self.ball3.x <= BASKETX and self.ball3.y <= BASKETY):
				spyral.director.replace(subject.Subject())		

