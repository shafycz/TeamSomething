import spyral
import random
import there
import math
import basketball
import game
import question
import basketball2



WIDTH = 1200

HEIGHT = 900
BG_COLOR = (0,0,0)

WHITE = (255, 255, 255)

SIZE = (WIDTH, HEIGHT)

DEF_FONT = "libraries/spyral/spyral/resources/fonts/FreeMono.ttf"

class Black(spyral.Sprite):
  def __init__(self, scene, x,y):
   super(Black,self).__init__(scene)
   self.image = spyral.Image(filename="game/colors/blackB.png")
   self.anchor = 'center'
   self.x = x
   self.y = y

class Blue(spyral.Sprite):
  def __init__(self, scene, x,y):
   super(Blue,self).__init__(scene)
   self.image = spyral.Image(filename="game/colors/blueB.png")
   self.anchor = 'center'
   self.x = x
   self.y = y

class Green(spyral.Sprite):
  def __init__(self, scene, x,y):
   super(Green,self).__init__(scene)
   self.image = spyral.Image(filename="game/colors/greenB.png")
   self.anchor = 'center'
   self.x = x
   self.y = y

class Pink(spyral.Sprite):
  def __init__(self, scene, x,y):
   super(Pink,self).__init__(scene)
   self.image = spyral.Image(filename="game/colors/pinkB.png")
   self.anchor = 'center'
   self.x = x
   self.y = y

class Purple(spyral.Sprite):
  def __init__(self, scene, x,y):
   super(Purple,self).__init__(scene)
   self.image = spyral.Image(filename="game/colors/purpleB.png")
   self.anchor = 'center'
   self.x = x
   self.y = y

class Red(spyral.Sprite):
  def __init__(self, scene, x,y):
   super(Red,self).__init__(scene)
   self.image = spyral.Image(filename="game/colors/redB.png")
   self.anchor = 'center'
   self.x = x
   self.y = y


class ball(spyral.Sprite):
	def __init__(self,scene,x,y):
		spyral.Sprite.__init__(self,scene)
		self.image = spyral.Image(filename= "game/colors/basketballPic3.png")
		self.x = x
		self.y = y
class hat(spyral.Sprite):
	def __init__(self,scene,x,y):
		spyral.Sprite.__init__(self,scene)
		self.image = spyral.Image(filename= "game/colors/tophat.png")
		self.x = x
		self.y = y
class sheep(spyral.Sprite):
	def __init__(self,scene,x,y):
		spyral.Sprite.__init__(self,scene)
		self.image = spyral.Image(filename= "game/colors/sheep_front2.png")
		self.x = x
		self.y = y
class phone(spyral.Sprite):
	def __init__(self,scene,x,y):
		spyral.Sprite.__init__(self,scene)
		self.image = spyral.Image(filename= "game/colors/phone.png")
		self.x = x
		self.y = y
class ball8(spyral.Sprite):
	def __init__(self,scene,x,y):
		spyral.Sprite.__init__(self,scene)
		self.image = spyral.Image(filename= "game/colors/ball8.png")
		self.x = x
		self.y = y
class burger(spyral.Sprite):
	def __init__(self,scene,x,y):
		spyral.Sprite.__init__(self,scene)
		self.image = spyral.Image(filename= "game/colors/burger.png")
		self.x = x
		self.y = y
class flower(spyral.Sprite):
	def __init__(self,scene,x,y):
		spyral.Sprite.__init__(self,scene)
		self.image = spyral.Image(filename= "game/colors/flower.png")
		self.x = x
		self.y = y

class MainMenu(spyral.Scene):

    def __init__(self):
	game.Counter = 0
	game.Counter1 = 0
	game.Turns = 0
        super(MainMenu, self).__init__(SIZE)
	self.font1 = spyral.Font("libraries/spyral/spyral/resources/fonts/FreeMono.ttf",30,(240,240,255))
	game.Pic = 0
        spyral.event.register('input.keyboard.down.q', spyral.director.quit)
	#self.b2 = ball(self, 500,500)
        spyral.event.register("system.quit", spyral.director.quit)
	spyral.event.register("input.mouse.down.left", self.handle_clicked) 
	spyral.event.register('input.keyboard.down.space', self.go_Next)
        self.background = spyral.Image(filename= "game/colors/blackb3.png")
	#self.start = Start(self,600,300)
	self.i1 = ball(self, 0,700)
	self.i7 = hat(self, 150,700)
	self.i6 = burger(self, 300,700)
	self.i5 = phone(self, 450,700)
	self.i4 = sheep(self, 600,700)
	self.i3 = ball8(self, 750,700)
	self.i2 = flower(self, 900,700)	
	self.image = spyral.Image(filename= "game/colors/basketballPic3.png")
	#self.i8 = pic(self,1050,700,self.image)
	m3 = self.font1.render("Basketball");
	self.ballThing = StartMessage(self,m3,(1000),700)
	
	self.b1 = Black(self, 0,100)
	self.b2 = Blue(self,150,100)
	self.g1 = Green(self,300,100)
	self.p1 = Pink(self,450,100)
	self.p2 = Purple(self, 600,100)
	self.r1 = Red(self, 750,100)

	m0 = self.font1.render("Easy");
	self.easy = StartMessage(self,m0,(400),400)
	m31 = self.font1.render("Medium");
	self.medium = StartMessage(self,m31,(550),400)
	m67 = self.font1.render("Hard");
	self.hard = StartMessage(self,m67,(700),400)	

	self.e1 = Red(self, 450,350)
	self.m9 = Red(self, 600,350)
	self.h1 = Red(self, 750,350)
	font = spyral.Font("libraries/spyral/spyral/resources/fonts/FreeMono.ttf",60,(255,255,255))
	m1 = font.render("Basketball Grammar");
	StartMessage(self,m1,(200),200)
	m2 = font.render(str(game.Counter))
	StartMessage(self,m2,(930),20)
	m3 = font.render(str(game.Counter1))
	StartMessage(self,m3,(1150),20)
	z3 = self.font1.render("Easy");
	self.difficult = StartMessage(self,z3,(1000),300)
	
    def go_Next(self):
	
	spyral.director.replace(basketball.Basketball())
	#spyral.director.replace(question.Question())
	#spyral.director.replace(basketball2.BasketBall2())
    def handle_clicked(self, pos):
	   	
	print pos.y
	
	if pos.y > 291 and pos.y <413:
		if pos.x> 400 and pos.x <506:
			 self.difficult.kill()
			 z3 = self.font1.render("Easy");
			 self.difficult = StartMessage(self,z3,(1000),300)
			 game.Difficult = 0
		elif pos.x >540 and pos.x <655:
			self.difficult.kill()
			z3 = self.font1.render("Medium");
			self.difficult = StartMessage(self,z3,(1000),300)
			game.Difficult = 2
		elif pos.x>700 and pos.x < 800:
			self.difficult.kill()
			z3 = self.font1.render("Hard");
			self.difficult = StartMessage(self,z3,(1000),300)
			game.Difficult = 3
	if pos.y > 40 and pos.y <150:
		if pos.x< 92:
			 self.background = spyral.Image(filename= "game/colors/blackb3.png")
			 game.Color = 0
		elif pos.x >92 and pos.x <203:
			self.background = spyral.Image(filename= "game/colors/blueb3.png")
			game.Color = 1
		elif pos.x>243 and pos.x < 352:
			self.background = spyral.Image(filename= "game/colors/greenb3.png")
			game.Color = 2
		elif pos.x>400 and pos.x< 506:
			self.background = spyral.Image(filename= "game/colors/pinkb3.png")
			game.Color = 3
		elif pos.x>540 and pos.x< 655:
			self.background = spyral.Image(filename= "game/colors/purpleb3.png")
			game.Color = 4
		elif pos.x>700 and pos.x< 800:
			self.background = spyral.Image(filename= "game/colors/redb3.png")
			game.Color = 5

	if pos.y > 697 and pos.y <785:
		if pos.x< 93:
			 self.image = spyral.Image(filename= "game/colors/basketballPic3.png")
			 self.ballThing.kill()
			 m3 = self.font1.render("Basketball");
			 self.ballThing = StartMessage(self,m3,(1000),700)
			 game.Pic = 0
		elif pos.x >93 and pos.x <257:
			self.image = spyral.Image(filename= "game/colors/tophat.png")
			game.Pic = 1
		        self.ballThing.kill()
			m3 = self.font1.render("Tophat");
			self.ballThing = StartMessage(self,m3,(1000),700)
		elif pos.x>257 and pos.x < 423:
			self.image = spyral.Image(filename= "game/colors/sheep_front2.png")
			game.Pic = 2
			self.ballThing.kill()
			m3 = self.font1.render("Burger");
			self.ballThing = StartMessage(self,m3,(1000),700)
		elif pos.x>423 and pos.x< 562:
			self.image = spyral.Image(filename= "game/colors/phone.png")
			game.Pic = 3
			self.ballThing.kill()
			m3 = self.font1.render("Phone");
			self.ballThing = StartMessage(self,m3,(1000),700)
		elif pos.x>562 and pos.x< 705:
			self.image = spyral.Image(filename= "game/colors/ball8.png")
			game.Pic = 4
			self.ballThing.kill()
			m3 = self.font1.render("Sheep");
			self.ballThing = StartMessage(self,m3,(1000),700)
		elif pos.x>705 and pos.x< 861:
			
			game.Pic = 5
			self.ballThing.kill()
			m3 = self.font1.render("8Ball");
			self.ballThing = StartMessage(self,m3,(1000),700)
		elif pos.x>861 and pos.x< 990:
			self.image = spyral.Image(filename= "game/colors/flower.png")
			game.Pic = 6
			self.ballThing.kill()
			m3 = self.font1.render("Flower");
			self.ballThing = StartMessage(self,m3,(1000),700)
	
	
class StartMessage(spyral.Sprite):
	def __init__(self,scene,img,x,y):
		spyral.Sprite.__init__(self,scene)
		self.image = img
		self.x = x
		self.y = y






