import spyral
import random
import there
import math
import basketball
import game



WIDTH = 1200

HEIGHT = 900
BG_COLOR = (0,0,0)

WHITE = (255, 255, 255)

SIZE = (WIDTH, HEIGHT)

DEF_FONT = "libraries/spyral/resources/fonts/DejaVuSans.ttf"

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


class MainMenu(spyral.Scene):

    def __init__(self):

        super(MainMenu, self).__init__(SIZE)


        spyral.event.register('input.keyboard.down.q', spyral.director.quit)

        spyral.event.register("system.quit", spyral.director.quit)
	spyral.event.register("input.mouse.down.left", self.handle_clicked) 

        self.background = spyral.Image(filename= "game/background1.png")
	#self.start = Start(self,600,300)
	self.b1 = Black(self, 0,100)
	self.b2 = Blue(self,150,100)
	self.g1 = Green(self,300,100)
	self.p1 = Pink(self,450,100)
	self.p2 = Purple(self, 600,100)
	self.r1 = Red(self, 750,100)	
	font = spyral.Font("/usr/share/fonts/truetype/freefont/FreeMono.ttf",60,(255,255,255))
	m1 = font.render("Basketball Grammar");
	StartMessage(self,m1,(200),200)
	m2 = font.render(str(game.Counter))
	StartMessage(self,m2,(960),20)
	m3 = font.render(str(game.Counter1))
	StartMessage(self,m3,(1150),20)
	
   
    def handle_clicked(self, pos):
	   	
	

	if pos.y > 40 and pos.y <150:
		if pos.x< 92:
			 self.background = spyral.Image(filename= "game/colors/blackb1.png")
			 game.Color = 0
		elif pos.x >92 and pos.x <203:
			self.background = spyral.Image(filename= "game/colors/blueb1.png")
			game.Color = 1
		elif pos.x>243 and pos.x < 352:
			self.background = spyral.Image(filename= "game/colors/greenb1.png")
			game.Color = 2
		elif pos.x>400 and pos.x< 506:
			self.background = spyral.Image(filename= "game/colors/pinkb1.png")
			game.Color = 3
		elif pos.x>540 and pos.x< 655:
			self.background = spyral.Image(filename= "game/colors/purpleb1.png")
			game.Color = 4
		elif pos.x>700 and pos.x< 800:
			self.background = spyral.Image(filename= "game/colors/redb1.png")
			game.Color = 5
	if pos.y > 450:
		spyral.director.replace(there.There())
class StartMessage(spyral.Sprite):
	def __init__(self,scene,img,x,y):
		spyral.Sprite.__init__(self,scene)
		self.image = img
		self.x = x
		self.y = y






