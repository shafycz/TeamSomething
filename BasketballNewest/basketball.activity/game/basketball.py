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
dist = 0
speed = 2.0


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
   	question_array = ["There are __ many people in the mall.", "I wish I had __ dogs.", "He is ___ young.", "She had ___ teaspoons of sugar in her tea.",
	"I like ___ be in the mountains.", "Mary saw a movie yesterday. I saw one ____.", "His house is near ___ rivers.", "Who are you going to give the present ___?",
	"Can I have one of those ___?", "We live close ___ here.",
	#2, 1, 2, 1, 0, 2, 1, 0, 2, 0
	
	"According to legend, ___ is treasure buried on the island.", "John and Jake said ___ coming for dinner.", "___ is a mouse in my closet.",
	"I wonder if ___ still planning on going to the park today.", "I can't wait to see the look on ___ faces.", "It is still ___ decision.",
	"I think Deb left her glasses over ___.", "I don't know what ___ doing to cause all that noise.", "Can you check over ___?", "I wish ___ stay in town was longer.",  
	#1, 2, 1, 2, 0, 0, 1, 2, 1, 0
	
	"He ___ a package to her in the mail.", "There was an odd ___ that the dog gave off.", "I will not pay you a single ___ for this food.", 
	"Can I borrow one ___? I need it for lunch.", "James was ___ to the nurses office because he had a runny nose.", "The teacher knew how the parent would respond even before she ___ the email.", 
	"Each animal has a different ___, which makes other animals able to detect them.", "A ___ is worth less than a nickel.", "Roses have a wonderful ___.", "Why would he ever have ___ that text to her?",
	#1, 2, 0, 0, 1, 1, 2, 0, 2, 1 
	
	"The ___ to the grocery store was too long to walk.", "He hasn't ___ a the ferris wheel in a few years.", "You're on a narrow ___ with a sheer cliff on your side.", "People ___ horses, but they also drove pick-up trucks.", 
	"That afternoon, we ___ leisurely up the stream.", "I ___ my boat to the dock.", "At some point in the trip he got on a bus and ___ home.", 
	"Did you know the government collects money in many ways, such as using a toll ___.", "Jim was tired, so he ___ his canoe back to camp.", "Many people ___ on trains as a main form of transportation.",
	#0, 2, 0, 2, 1, 1, 2, 0, 1, 2
	
	"To build muscle, bodybuilders use ___ protein.", "In the cheese making process, milk is separated out into solids, also called curds, and liquid, also called ___.", 
	"I think I have gained a few pounds, maybe I should ___ myself.", "There is no ___ I'm going into that haunted house.", "Do you know the ___ home from school?", 
	"The cashier had to ___ the fruit to be able to know it's price.", "You should ___ the pros and cons before making decisions.", 
	"Some whales ___ as much as 150 tons.", "Get out of my ___, I need to go to the emergency room!", "Taking the elevator to the second floor is a much easier ___ than taking the stairs.",
	#2, 2, 1, 0, 0, 1, 1, 1, 0, 0
	
	"A wound will ___ after a few days if you wash and treat it correctly.", "My ___ got scraped when I was skateboarding.", 
	"Having a shoe cushion for a bruised ___ is helpful.", "We can only hope that ___ come to the birthday party on time.", "Do you think ___ ask for your number tonight?", 
	"Putting salt on a mouth sore will help your mouth ___ itself.", "A broken bone will take a lot longer to ___ than a cut.", "___ pain can usually be explained by shoe choice.",
	"Don't worry, ___ let you know when your mom gets home.", "If ___ pick you up, I can drop you off.",
	#0, 2, 2, 1, 1, 0, 0, 2, 1, 1
	
	"The weather channel predicted ___ all weekend.", "___ forests now cover less than 6% of Earth's land surface.", "Did you know that acid ___ can contaminate lakes?", 
	"The king had ___ over the entire continent.", "Keeping a tight ___ on your employees is a good work strategy.", "If you walk a horse on a loose ___ it will help them relax.", 
	"Loyalty will always ___ supreme.", "The queen had a ___ of terror over the tribe, because she was cruel.", "Heavy ___ is very dangerous since it can cause flooding.", "Why don't you let me take the ___ now?",
	#0, 0, 0, 1, 2, 2, 1, 1, 0, 2
	
	"The poor old man was losing his sense of ___.", "I'm going to the construction ___ later today.", "A sunset is a great ___ to see.", 
	"I have to make sure to ___ my sources when writing a paper.", "The work ___ is very dirty now because of lazy workers not cleaning up.", 
	"On his resume, Anthony would like to ___ his father as his biggest influence.", "___ seeing in other countries is very exciting.", 
	"I was overwhelmed at the ___ of my long lost cat coming home.", "A web ___ is something you visit on the Internet.", "A stadium is a ___ usually used for sporting events and concerts.",
	#0, 1, 0, 2, 1, 2, 0, 0, 1, 1
	
	"Spy ___ is something you should try to avoid on your computer.", "Do you know ___ I put my glasses?", "I can't believe Jenny is going to ___ that to the prom!", 
	"Let us take some time to inspect your ___ that you crafted.", "Could you try to find ___ the computer's power cord is?", "Take me to the clothing store ___ I can shop.", 
	"The florist only had one item left, and he waited all day to sell that lone ___.", "I wish I knew ___ the gas station was.", "Could you hurry up and choose what you're going to ___ please?",
	 "I never like to ___ sandals."]
	#0, 2, 1, 0, 2, 2, 0, 2, 1, 1
	
	choices_array =["1. to 2. two 3. too","1. to 2. two 3. too", "1. to 2. two 3. too", "1. to 2. two 3. too", "1. to 2. two 3. too",
	"1. to 2. two 3. too", "1. to 2. two 3. too", "1. to 2. two 3. too", "1. to 2. two 3. too", "1. to 2. two 3. too",
	
	"1. their 2. there 3. they're", "1. their 2. there 3. they're", "1. their 2. there 3. they're", "1. their 2. there 3. they're", "1. their 2. there 3. they're",
	"1. their 2. there 3. they're", "1. their 2. there 3. they're", "1. their 2. there 3. they're", "1. their 2. there 3. they're", "1. their 2. there 3. they're",
	
	"1. cent 2. sent 3. scent", "1. cent 2. sent 3. scent", "1. cent 2. sent 3. scent", "1. cent 2. sent 3. scent", "1. cent 2. sent 3. scent", "1. cent 2. sent 3. scent",
	"1. cent 2. sent 3. scent", "1. cent 2. sent 3. scent", "1. cent 2. sent 3. scent", "1. cent 2. sent 3. scent",
	 
	"1. road 2. rowed 3. rode", "1. road 2. rowed 3. rode", "1. road 2. rowed 3. rode", "1. road 2. rowed 3. rode", "1. road 2. rowed 3. rode", "1. road 2. rowed 3. rode", 
	"1. road 2. rowed 3. rode", "1. road 2. rowed 3. rode", "1. road 2. rowed 3. rode", "1. road 2. rowed 3. rode",
	
	"1. way 2. weigh 3. whey", "1. way 2. weigh 3. whey", "1. way 2. weigh 3. whey", "1. way 2. weigh 3. whey", "1. way 2. weigh 3. whey", 
	"1. way 2. weigh 3. whey", "1. way 2. weigh 3. whey", "1. way 2. weigh 3. whey", "1. way 2. weigh 3. whey", "1. way 2. weigh 3. whey",
	
	"1. heal 2. he'll 3. heel", "1. heal 2. he'll 3. heel", "1. heal 2. he'll 3. heel", "1. heal 2. he'll 3. heel", "1. heal 2. he'll 3. heel", 
	"1. heal 2. he'll 3. heel", "1. heal 2. he'll 3. heel", "1. heal 2. he'll 3. heel", "1. heal 2. he'll 3. heel", "1. heal 2. he'll 3. heel",
	
	"1. rain 2. reign 3. rein", "1. rain 2. reign 3. rein", "1. rain 2. reign 3. rein", "1. rain 2. reign 3. rein", "1. rain 2. reign 3. rein", 
	"1. rain 2. reign 3. rein", "1. rain 2. reign 3. rein", "1. rain 2. reign 3. rein", "1. rain 2. reign 3. rein", "1. rain 2. reign 3. rein",
	
	"1. sight 2. site 3. cite", "1. sight 2. site 3. cite", "1. sight 2. site 3. cite", "1. sight 2. site 3. cite", "1. sight 2. site 3. cite", 
	"1. sight 2. site 3. cite", "1. sight 2. site 3. cite", "1. sight 2. site 3. cite", "1. sight 2. site 3. cite", "1. sight 2. site 3. cite",
	
	"1. ware 2. wear 3. where", "1. ware 2. wear 3. where", "1. ware 2. wear 3. where", "1. ware 2. wear 3. where", "1. ware 2. wear 3. where", 
	"1. ware 2. wear 3. where", "1. ware 2. wear 3. where", "1. ware 2. wear 3. where", "1. ware 2. wear 3. where", "1. ware 2. wear 3. where"]
	global x_array
	x_array = [2, 1, 2, 1, 0, 2, 1, 0, 2, 0, 
	1, 2, 1, 2, 0, 0, 1, 2, 1, 0, 
	1, 2, 0, 0, 1, 1, 2, 0, 2, 1,
	0, 2, 0, 2, 1, 1, 2, 0, 1, 2,
	2, 2, 1, 0, 0, 1, 1, 1, 0, 0,
	0, 2, 2, 1, 1, 0, 0, 2, 1, 1,
	0, 0, 0, 1, 2, 2, 1, 1, 0, 2,
	0, 1, 0, 2, 1, 2, 0, 0, 1, 1,
	0, 2, 1, 0, 2, 2, 0, 2, 1, 1]

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
			dist = BASKETX - initX
			#self.b2.kill()
			xCoordAnim = Animation('x', easing.Linear(initX, initX+dist/2), duration = speed)
			yCoordAnim1 = Animation('y', easing.QuadraticOut(HEIGHT, BASKETY-100),duration=speed)
			xCoordAnim2 = Animation('x', easing.Linear(initX+dist/2, initX+dist), duration = speed)
			yCoordAnim2 = Animation('y', easing.QuadraticIn(BASKETY-100,BASKETY), duration = speed)
			missAnim = Animation('x', easing.Linear(BASKETX, math.random.randint(400,800)), duration = speed)
			missAnim2 = Animation('y', easing.Linear(BASKETY, 0), duration = 4)
			
			anim = ((xCoordAnim & yCoordAnim1)+(xCoordAnim2+yCoordAnim2)+(missAnim&missAnim2))
		
			self.ball2.animate(anim)
			i =random.randint(1,2)
			if i == 1:
				BASKETX = 145
				dist = BASKETX - WIDTH
				print "computer scores on 1"
				xCoordAnim = Animation('x', easing.Linear(WIDTH, WIDTH+dist/2), duration = speed)
				yCoordAnim1 = Animation('y', easing.QuadraticOut(HEIGHT/4, BASKETY-100),duration=speed)
				xCoordAnim2 = Animation('x', easing.Linear(WIDTH+dist/2, WIDTH+dist), duration = speed)
				yCoordAnim2 = Animation('y', easing.QuadraticIn(BASKETY-100,BASKETY), duration = speed)

				anim = ((xCoordAnim & yCoordAnim1)+(xCoordAnim2+yCoordAnim2))
				self.ball1.animate(anim)
				game.Counter1 = game.Counter1 +2
				spyral.director.replace(subject.Subject())
		elif pos.x>800 and pos.y>300:
			#self.b3.kill()
			BASKETX = 1000
			dist = BASKETX - initX
			xCoordAnim = Animation('x', easing.Linear(initX, initX+dist/2), duration = speed)
			yCoordAnim1 = Animation('y', easing.QuadraticOut(HEIGHT, BASKETY-100),duration=speed)
			xCoordAnim2 = Animation('x', easing.Linear(initX+dist/2, initx+dist), duration = speed)
			yCoordAnim2 = Animation('y', easing.QuadraticIn(BASKETY-100,BASKETY), duration = speed)
			missAnim = Animation('x', easing.Linear(BASKETX, math.random.randint(800,1200)), duration = speed)
			missAnim2 = Animation('y', easing.Linear(BASKETY, 0), duration = speed)
			
			anim = ((xCoordAnim & yCoordAnim1)+(xCoordAnim2+yCoordAnim2)+(missAnim&missAnim2))
		
			self.ball3.animate(anim)
			i =random.randint(1,2)
			if i == 1:
				BASKETX = 145
				dist = BASKETX - WIDTH
				print "computer scores on 1"
				xCoordAnim = Animation('x', easing.Linear(WIDTH, WIDTH+dist/2), duration = speed)
				yCoordAnim1 = Animation('y', easing.QuadraticOut(HEIGHT/4, BASKETY-100),duration=speed)
				xCoordAnim2 = Animation('x', easing.Linear(WIDTH+dist/2, WIDTH+dist), duration = speed)
				yCoordAnim2 = Animation('y', easing.QuadraticIn(BASKETY-100,BASKETY), duration = speed)

				anim = ((xCoordAnim & yCoordAnim1)+(xCoordAnim2+yCoordAnim2))
				self.ball1.animate(anim)
				game.Counter1 = game.Counter1 +2
				spyral.director.replace(subject.Subject())
		elif pos.x <400 and pos.y>300:
			BASKETX = 145
			dist = BASKETX - initX
			xCoordAnim = Animation('x', easing.Linear(initX, initX+dist/2), duration = speed)
			yCoordAnim1 = Animation('y', easing.QuadraticOut(HEIGHT, BASKETY-100),duration=speed)
			xCoordAnim2 = Animation('x', easing.Linear(initX+dist/2, initX+dist), duration = speed)
			yCoordAnim2 = Animation('y', easing.QuadraticIn(BASKETY-100,BASKETY), duration = speed)
			anim = ((xCoordAnim & yCoordAnim1)+(xCoordAnim2+yCoordAnim2))
			self.ball1.animate(anim)
			game.Counter = game.Counter +2
			spyral.director.replace(subject.Subject())

	elif x_array[0] == 400:
		if pos.x <400 and pos.y>300:
			#self.b1.kill()
			BASKETX = 145
			dist = BASKETX - initX
			xCoordAnim = Animation('x', easing.Linear(initX, initX+dist/2), duration = speed)
			yCoordAnim1 = Animation('y', easing.QuadraticOut(HEIGHT, BASKETY-100),duration=speed)
			xCoordAnim2 = Animation('x', easing.Linear(initX+dist/2, initx+dist), duration = speed)
			yCoordAnim2 = Animation('y', easing.QuadraticIn(BASKETY-100,BASKETY), duration = speed)
			missAnim = Animation('x', easing.Linear(BASKETX, math.random.randint(BASKETX-200,BASKETX+200)), duration = speed)
			missAnim2 = Animation('y', easing.QuadraticIn(BASKETY, HEIGHT), duration = speed)
			
			anim = ((xCoordAnim & yCoordAnim1)+(xCoordAnim2+yCoordAnim2)+(missAnim&missAnim2))
			self.ball1.animate(anim)
			i =random.randint(1,2)
			if i == 1:
				print "computer scores on 2"
				BASKETX = 600
				dist = BASKETX - WIDTH
				xCoordAnim = Animation('x', easing.Linear(WIDTH, WIDTH+dist/2), duration = speed)
				yCoordAnim1 = Animation('y', easing.QuadraticOut(HEIGHT/4, BASKETY-100),duration=speed)
				xCoordAnim2 = Animation('x', easing.Linear(WIDTH+dist/2, WIDTH+dist), duration = speed)
				yCoordAnim2 = Animation('y', easing.QuadraticIn(BASKETY-100,BASKETY), duration = speed)

				anim = ((xCoordAnim & yCoordAnim1)+(xCoordAnim2+yCoordAnim2))
				self.ball2.animate(anim)
				game.Counter1 = game.Counter1 +2
				spyral.director.replace(subject.Subject())
		elif pos.x>800 and pos.y>300:
			#self.b3.kill()
			BASKETX = 1000
			dist = BASKETX - initX
			xCoordAnim = Animation('x', easing.Linear(initX, initX+dist/2), duration = speed)
			yCoordAnim1 = Animation('y', easing.QuadraticOut(HEIGHT, BASKETY-100),duration=speed)
			xCoordAnim2 = Animation('x', easing.Linear(initX+dist/2, initX+dist), duration = speed)
			yCoordAnim2 = Animation('y', easing.QuadraticIn(BASKETY-100,BASKETY), duration = speed)
			missAnim = Animation('x', easing.Linear(BASKETX, math.random.randint(BASKETX-200,BASKETX+200)), duration = speed)
			missAnim2 = Animation('y', easing.QuadraticIn(BASKETY, HEIGHT), duration = 3)
			
			anim = ((xCoordAnim & yCoordAnim1)+(xCoordAnim2+yCoordAnim2)+(missAnim&missAnim2))
			self.ball3.animate(anim)
			i =random.randint(1,2)
			if i == 1:
				BASKETX = 600
				print "computer scores on 2"
				dist = BASKETX - WIDTH
				xCoordAnim = Animation('x', easing.Linear(WIDTH, WIDTH+dist/2), duration = speed)
				yCoordAnim1 = Animation('y', easing.QuadraticOut(HEIGHT/4, BASKETY-100),duration=speed)
				xCoordAnim2 = Animation('x', easing.Linear(WIDTH+dist/2, BASKETX), duration = speed)
				yCoordAnim2 = Animation('y', easing.QuadraticIn(BASKETY-100,BASKETY), duration = speed)

				anim = ((xCoordAnim & yCoordAnim1)+(xCoordAnim2+yCoordAnim2))
				self.ball2.animate(anim)
				game.Counter1 = game.Counter1 +2
				spyral.director.replace(subject.Subject())
		elif pos.x >400 and pos.x <800 and pos.y>300:
			BASKETX = 600
			dist = BASKETX - initX
			xCoordAnim = Animation('x', easing.Linear(initX, initX+dist/2), duration = speed)
			yCoordAnim1 = Animation('y', easing.QuadraticOut(HEIGHT, BASKETY-100),duration=speed)
			xCoordAnim2 = Animation('x', easing.Linear(initX+dist/2, BASKETX), duration = speed)
			yCoordAnim2 = Animation('y', easing.QuadraticIn(BASKETY-100,BASKETY), duration = speed)
			anim = ((xCoordAnim & yCoordAnim1)+(xCoordAnim2+yCoordAnim2))
			self.ball2.animate(anim)
			game.Counter = game.Counter +2			
			spyral.director.replace(subject.Subject())
			
	elif x_array[0] == 800:
		if pos.x <400 and pos.y>300:
			#self.b1.kill()
			BASKETX = 145
			dist = BASKETX - initX
			xCoordAnim = Animation('x', easing.Linear(initX, initX+(dist/2)-75), duration = speed)
			yCoordAnim1 = Animation('y', easing.QuadraticOut(HEIGHT, BASKETY-100),duration=speed)
			xCoordAnim2 = Animation('x', easing.Linear(initX+(dist/2)-75, BASKETX-75), duration = speed)
			yCoordAnim2 = Animation('y', easing.QuadraticIn(BASKETY-100,BASKETY), duration = speed)

			anim = ((xCoordAnim & yCoordAnim1)+(xCoordAnim2+yCoordAnim2))						
			self.ball1.animate(anim)
			i =random.randint(1,2)
			print i
			if i == 1:
				BASKETX = 1000
				print "computer scores on 3"
				dist = BASKETX - WIDTH
				xCoordAnim = Animation('x', easing.Linear(WIDTH, WIDTH+dist/2), duration = speed)
				yCoordAnim1 = Animation('y', easing.QuadraticOut(HEIGHT/4, BASKETY-100),duration=speed)
				xCoordAnim2 = Animation('x', easing.Linear(WIDTH+dist/2, BASKETX), duration = speed)
				yCoordAnim2 = Animation('y', easing.QuadraticIn(BASKETY-100,BASKETY), duration = speed)

				anim = ((xCoordAnim & yCoordAnim1)+(xCoordAnim2+yCoordAnim2))
				self.ball3.animate(anim)
				game.Counter1 = game.Counter1 +2
				spyral.director.replace(subject.Subject())
		elif pos.x<800 and pos.x>400 and pos.y>300:
			#self.b2.kill()
			BASKETX = 600
			dist = BASKETX - initX
			xCoordAnim = Animation('x', easing.Linear(initX, initX+(dist/2)-75), duration = speed)
			yCoordAnim1 = Animation('y', easing.QuadraticOut(HEIGHT, BASKETY-100),duration=speed)
			xCoordAnim2 = Animation('x', easing.Linear(initX+(dist/2)-75, BASKETX-75), duration = speed)
			yCoordAnim2 = Animation('y', easing.QuadraticIn(BASKETY-100,BASKETY), duration = speed)

			anim = ((xCoordAnim & yCoordAnim1)+(xCoordAnim2+yCoordAnim2))			

			self.ball2.animate(anim)
			i =random.randint(1,2)
			print i
			if i == 1:
				print "computer scores on 3"
				BASKETX = 1000
				dist = BASKETX - WIDTH
				xCoordAnim = Animation('x', easing.Linear(WIDTH, WIDTH+dist/2), duration = speed)
				yCoordAnim1 = Animation('y', easing.QuadraticOut(HEIGHT/4, BASKETY-100),duration=speed)
				xCoordAnim2 = Animation('x', easing.Linear(WIDTH+dist/2, BASKETX), duration = speed)
				yCoordAnim2 = Animation('y', easing.QuadraticIn(BASKETY-100,BASKETY), duration = speed)

				anim = ((xCoordAnim & yCoordAnim1)+(xCoordAnim2+yCoordAnim2))
				self.ball3.animate(anim)
				game.Counter1 = game.Counter1 +2
				spyral.director.replace(subject.Subject())
		elif pos.x >800 and pos.y>300:
			BASKETX = 1000
			dist = BASKETX - initX
			xCoordAnim = Animation('x', easing.Linear(initX, initX+dist/2), duration = speed)
			yCoordAnim1 = Animation('y', easing.QuadraticOut(HEIGHT, BASKETY-100),duration= speed)
			xCoordAnim2 = Animation('x', easing.Linear(initX+dist/2, BASKETX), duration = speed)
			yCoordAnim2 = Animation('y', easing.QuadraticIn(BASKETY-100,BASKETY), duration = speed)
			anim = ((xCoordAnim & yCoordAnim1)+(xCoordAnim2+yCoordAnim2))
			self.ball3.animate(anim)
			
			game.Counter = game.Counter +2
		
			spyral.director.replace(subject.Subject())		

