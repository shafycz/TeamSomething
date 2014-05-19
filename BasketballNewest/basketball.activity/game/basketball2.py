import spyral
import random
import math
from spyral import Animation, easing
import time
import test
import game
import subject
import basketball
import win
WIDTH = 1200
HEIGHT = 900
BG_COLOR = (0,0,0)
WHITE = (255, 255, 255)
SIZE = (WIDTH, HEIGHT)

class ball(spyral.Sprite):
	def __init__(self,scene,x,y):
		spyral.Sprite.__init__(self,scene)
		self.image = spyral.Image(filename= "game/colors/basketballPic3.png")
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
class Ball(spyral.Sprite):
    def __init__(self, scene):
        super(Ball, self).__init__(scene)
        self.image = spyral.Image("game/colors/basketballPic3.png")
        self.anchor = 'center'
        self.pos = (WIDTH-1100, HEIGHT-50)

    def collide_Comp(self, comp):
        if self.collide_sprite(comp):
            print "I collided!"
            self.stop_all_animations()
            self.pos = (-1100, -50)
	    
	    

class Comp(spyral.Sprite):
    def __init__(self, scene, x, y, vel):
        super(Comp, self).__init__(scene)
        self.image = spyral.Image("game/colors/basketballPic3.png")
        self.anchor = 'center'
        self.pos = (x, y)
        self.vel_y = vel
        spyral.event.register('director.update', self.update)
    def update(self, delta):
        self.y -= delta*self.vel_y
        r = self.rect
        if r.top <= 50+100:
            r.top = 100
            self.vel_y = -self.vel_y
        if r.bottom >= HEIGHT-100:
            r.bottom = HEIGHT
            self.vel_y = -self.vel_y
class BasketBall2(spyral.Scene):
    def __init__(self, *args, **kwargs):
        global manager
        spyral.Scene.__init__(self, SIZE)
	font1 = spyral.Font("libraries/spyral/spyral/resources/fonts/FreeMono.ttf",70,(255,0,0))
	font2 = spyral.Font("libraries/spyral/spyral/resources/fonts/FreeMono.ttf",90,(0,255,0))
  	if game.Color == 0:
        	self.background = spyral.Image(filename= "game/colors/blackb2.png")
        elif game.Color==1:
        	self.background = spyral.Image(filename= "game/colors/blueb2.png")
	if game.Color == 2:
        	self.background = spyral.Image(filename= "game/colors/greenb2.png")
		#font2 = spyral.Font("libraries/spyral/spyral/resources/fonts/FreeMono.ttf",90,(255,255,255))
        elif game.Color==3:
        	self.background = spyral.Image(filename= "game/colors/pinkb2.png")
	if game.Color == 4:
        	self.background = spyral.Image(filename= "game/colors/purpleb2.png")
        elif game.Color==5:
        	self.background = spyral.Image(filename= "game/colors/redb2.png")
        	#font1 = spyral.Font("libraries/spyral/spyral/resources/fonts/FreeMono.ttf",70,(255,255,255))
	
	spyral.event.register('input.keyboard.down.space', self.go_Next)
	spyral.event.register("system.quit", spyral.director.pop)
	spyral.event.register("input.keyboard.down.q", spyral.director.pop)
	#spyral.event.register("input.mouse.down.left", self.handle_clicked) 
	#spyral.event.register('input.keyboard.down.s', self.shoot)
	spyral.event.register('director.update', self.update)
   	self.font = spyral.Font("libraries/spyral/spyral/resources/fonts/FreeMono.ttf",36,(255,255,255))
	self.m2 = self.font.render(str(game.Counter))
	self.s1 = choiceMessage(self,self.m2,(960),30)
	self.m3 = self.font.render(str(game.Counter1))
	self.s2 = choiceMessage(self,self.m3,(1150),30)


	self.d = self.font.render("Click to Shoot")
	self.d1 = choiceMessage(self,self.d,(400),400)
	self.d2 = self.font.render("Press Space to Continue")
	self.d3 = choiceMessage(self,self.d2,(400),500)
	

	self.ball = Ball(self)
        self.comp1 = Comp(self, WIDTH/2 - 150, HEIGHT-50, 300)
        self.comp2 = Comp(self, WIDTH/2 + 150, HEIGHT-50, 500)
	n2=self.font.render(str(game.Balls))
        self.b1 = choiceMessage(self,n2,(1050),13)
	#self.comp2 = Comp(self, 600, 300, 500)
        spyral.event.register("input.mouse.down.left", self.handle_clicked)
    def update(self, delta):
        self.ball.collide_Comp(self.comp1)
        self.ball.collide_Comp(self.comp2)
	
	if self.ball.pos == (-1100, -50):
	    #self.s1.kill()
	    if game.Shooting == 1:
		print "called shooting"
		game.Counter = game.Counter -3 
		
		self.s1.kill()
		n1=self.font.render(str(game.Counter))
		self.s1 = choiceMessage(self,n1,(960),30)
	 #   n1=self.font.render(str(game.Counter))
	  #  self.s1 = choiceMessage(self,n1,(960),30)
                self.ball.pos = (WIDTH-1100, HEIGHT-50)
	    else:
		self.ball.pos = (WIDTH-1100, HEIGHT-50)
###### BALL ANIMATIONS ####################
    #if the player makes it
    xCoordAnim1 = Animation('x', easing.Linear(WIDTH-1100, WIDTH-65), duration = 1.0)
    xCoordAnim2 = Animation('x', easing.Linear(WIDTH-65, WIDTH-40), duration = 0.5)
    yCoordAnim1 = Animation('y', easing.QuadraticOut(HEIGHT-50, HEIGHT-750),duration= 0.75)
    yCoordAnim2 = Animation('y', easing.QuadraticIn(HEIGHT-750,HEIGHT-550), duration = 0.25)
    yCoordAnim3 = Animation('y', easing.QuadraticIn(HEIGHT-550,HEIGHT-50), duration = 0.5)
    
    anim = (xCoordAnim1 & (yCoordAnim1 + yCoordAnim2)) + (xCoordAnim2 & yCoordAnim3)


    #if the player misses it
    ##this first block is the original direction if the ball would make it###    
    missAnimX1 = Animation('x', easing.Linear(WIDTH-1100, WIDTH-45), duration = 1.0)
    missAnimY1 = Animation('y', easing.QuadraticOut(HEIGHT-50, HEIGHT-750), duration = 0.75)
    missAnimY2 = Animation('y', easing.QuadraticIn(HEIGHT-750,HEIGHT-550), duration = 0.25)
    ##this second block is after the ball hits the rim and misses####
    missAnimX2 = Animation('x', easing.Linear(WIDTH-45, WIDTH-600), duration = 0.1)
    missAnimY3 = Animation('y', easing.Linear(HEIGHT-550,HEIGHT-950), duration = 0.1)
        
    missAnim2X2 = Animation('x', easing.Linear(WIDTH-45, WIDTH+250), duration = 0.1)
    missAnim2Y3 = Animation('y', easing.Linear(HEIGHT-550,HEIGHT-950), duration = 0.1)

    missAnim3Y3 = missAnimY3 = Animation('y', easing.Linear(HEIGHT-550,HEIGHT-950), duration = 0.1)

    missAnim1 = (missAnimX1 & (missAnimY1 + missAnimY2)) + (missAnimX2 & missAnimY3)
    missAnim2 = (missAnimX1 & (missAnimY1 + missAnimY2)) + (missAnim2X2 & missAnim2Y3)
    missAnim3 = (missAnimX1 & (missAnimY1 + missAnimY2)) + missAnim3Y3
    
###########END BALL ANIMATIONS##############

###########Comp Animations###########
#    compAnimY1 = Animation('y', easing.QuadraticOut(HEIGHT-50, HEIGHT-750),duration=2.0)
#    compAnimY2 = Animation('y', easing.QuadraticIn(HEIGHT-750, HEIGHT-50),duration=2.0, loop = True)
#    compJump = compAnimY1 + compAnimY2
###########End Comp Animations#######    

    

    #self.comp.animate(compJump)
    #spyral.event.register("self.comp.animation.end", self.comp.animate(compJump))
    
    def handle_clicked(self):
     if game.Balls != 0:
	game.Shooting = 0
	game.Balls = game.Balls -1
	self.b1.kill()
	n2=self.font.render(str(game.Balls))
	self.b1 = choiceMessage(self,n2,(1050),13)
        rando = random.randrange(0,1)
        self.ball.stop_all_animations()
        if (rando == 0):   
	    game.Shooting = 1
	         
            self.ball.stop_all_animations()
            self.ball.animate(self.anim)
           # self.ball.collide_Comp(self.comp)
	    self.s1.kill()
	    game.Counter = game.Counter +3
	    n1=self.font.render(str(game.Counter))
	    self.s1 = choiceMessage(self,n1,(960),30)
	    
        else: 
            ran = random.randrange(0,3)
	   # prevScore = game.Counter
	    game.shooting = 2
            if (ran == 0):
                self.ball.stop_all_animations()
                self.ball.animate(self.missAnim1)
                #self.ball.collide_Comp(self.comp)
		#if prevScore >game.Counter:
		#	game.Counter = prevScore
            if (ran == 1):    
                self.ball.stop_all_animations()
                self.ball.animate(self.missAnim2)
                #self.ball.collide_Comp(self.comp)
		#if prevScore >game.Counter:
		#	game.Counter = prevScore
            else:
                self.ball.stop_all_animations()
                self.ball.animate(self.missAnim3)
                #self.ball.collide_Comp(self.comp)
		#if prevScore >game.Counter:
			#game.Counter = prevScore



	
    
	#elif	
    def go_Next(self):
	if game.Balls == 0:
		if game.Turns <5:
			game.Turns = game.Turns +1
			spyral.director.pop
			spyral.director.replace(basketball.Basketball())
		else:
			if game.Counter > game.Counter1:
				game.Win = True
				spyral.director.replace(win.Win())
			else:
				game.Win = False
				spyral.director.replace(win.Win())
'''		
    def handle_clicked(self, pos):
	if game.Balls != 0:
		n1=self.font.render(str(game.Counter))
		self.s1.kill()
		self.s1 = choiceMessage(self,n1,(960),30)
		game.Balls = game.Balls -1
'''
