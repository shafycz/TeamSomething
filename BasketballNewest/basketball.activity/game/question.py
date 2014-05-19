import spyral
import random

import math
#import wallbreaker
import basketball2
import game
import question


WIDTH = 1200

HEIGHT = 900
BG_COLOR = (0,0,0)

WHITE = (255, 255, 255)

SIZE = (WIDTH, HEIGHT)

DEF_FONT = "libraries/spyral/resources/fonts/DejaVuSans.ttf"

  
 
		 
class Check(spyral.Sprite):
  def __init__(self, scene, x,y):
   super(Check,self).__init__(scene)
   self.image = spyral.Image(filename="game/colors/check.png")
   self.anchor = 'center'
   self.x = x
   self.y = y
class X(spyral.Sprite):
  def __init__(self, scene, x,y):
   super(X,self).__init__(scene)
   self.image = spyral.Image(filename="game/colors/x.png")
   self.anchor = 'center'
   self.x = x
   self.y = y
class ball(spyral.Sprite):
	def __init__(self,scene,x,y):
		spyral.Sprite.__init__(self,scene)
		self.image = spyral.Image(filename= "game/colors/basketballPic2.png")
		self.x = x
		self.y = y
class One(spyral.Sprite):
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

class Question(spyral.Scene):
    def __init__(self, *args, **kwargs):
        global manager
	
        spyral.Scene.__init__(self, SIZE)
        if game.Color == 0:
        	self.background = spyral.Image(filename= "game/colors/blackb3.png")
        elif game.Color==1:
        	self.background = spyral.Image(filename= "game/colors/blueb3.png")
	if game.Color == 2:
        	self.background = spyral.Image(filename= "game/colors/greenb3.png")
        elif game.Color==3:
        	self.background = spyral.Image(filename= "game/colors/pinkb3.png")
	if game.Color == 4:
        	self.background = spyral.Image(filename= "game/colors/purpleb3.png")
        elif game.Color==5:
        	self.background = spyral.Image(filename= "game/colors/redb3.png")
       	spyral.event.register('input.keyboard.down.space', self.go_Next) 
	spyral.event.register("input.mouse.down.left", self.handle_clicked) 
	spyral.event.register("system.quit", spyral.director.pop)
	spyral.event.register("input.keyboard.down.q", spyral.director.pop)
 	font = spyral.Font("/usr/share/fonts/truetype/freefont/FreeMono.ttf",36,(255,255,255))



	question_array = ["The cat ___ the bird around the room.", "John is ___ to school.", "You are ___ right now.", "Lions ___ after their prey.",
	"Can I ___ to your house?", "People ___ when they are sad.", "An iPhone ___ a cellphone.", "The player ___ the basketball.",
	"Beyonce ___ on stage with Jay Z.", "We will ___ in class because it is fun.",
	
	#Increased difficulty by making sentence structure slightly more complex
	"I ___ March Madness on my television.", "___ a paper can be stressful.", "I ___ my homework to my room.", 
	"He was ___ daydreaming in class.", "You probably should not be ___ in class.", "The student ___ in his art class yesterday.", "___ up is hard today.", 
	"I ___ The Eagles will win the Superbowl.", "All CCCS students ___ awesome!", "Anthony ___ school early because he was sick.",
	
	#Made sentences more complex by making the nouns and verbs somewhat harder to find/more vague, as well as subject, requires more thought
	"He ___ because he got a papercut.", "He ___ breakfast, even though he knew he should not have.", "The quarterback ___ the ball to his teammate quickly.", 
	"Dorothy prefers ___ in the morning instead of at night.", "He ___ his sister, even though she had been mean.", "Broccoli ___ a delicious food.",
	"What is your favorite place to ___ about?", "Would you like to ___ to the zoo?", "Sunday is the best day for ___ a nap.", "I would like to ___ a hike today."]
	
	subject_array =["The subject is 1. cat 2. bird 3. room ", "The subject is 1. John 2. school 3. is", "The subject is 1. now 2. you 3. right", 
	"The subject is 1. prey 2. after 3. lions", "The subject is 1. I 2. house 3. your ", "The subject is 1. when 2. sad 3. people", 
	"The subject is 1. cellphone 2. iPhone 3. a", "The subject is 1. the 2. player 3. basketball", "The subject is 1. Jay Z 2. Beyonce 3. stage", 
	"The subject is 1. we 2. class 3. fun",
	#cat, John, you, lions, I, people, iPhone, player, Beyonce, we
	#0, 0, 1, 2, 0, 2, 1, 1, 1, 0
	
	"The subject is 1. I 2. television 3. March Madness", "The subject is 1. paper 2. can 3. stressful", "The subject is 1. room 2. I 3. homework", 
	"The subject is 1. caught 2. he 3. class", "The subject is 1. you 2. class 3. should", "The subject is 1. art class 2. student 3. yesterday", 
	"The subject is 1. today 2. hard 3. up", "The subject is 1. Superbowl 2. The Eagles 3. win", "The subject is 1. awesome 2. all 3. students", 
	"The subject is 1. school 2. because 3. Anthony",
	#I, paper, I, he, you, student, today, The Eagles, students, Anthony
	#0, 0, 1, 1, 0, 1, 0, 1, 2, 2
	
	"The subject is 1. got 2. he 3. papercut", "The subject is 1. have 2. breakfast 3. he", "The subject is 1. quarterback 2. teammate 3. ball", 
	"The subject is 1. morning 2. Dorothy 3. night", "The subject is 1. sister 2. he 3. she",
	"The subject is 1. food 2. delicious 3. broccoli", "The subject is 1. your 2. place 3. about", "The subject is 1. you 2. zoo 3. go",
	"The subject is 1. nap 2. day 3. Sunday", "The subject is 1. I 2. hike 3. would"]
	#he, he, quarterback, Dorothy, he, broccoli, place, you, Sunday, I
	#1, 2, 0, 1, 1, 2, 1, 0, 2, 0
	
	verb_array = ["The correct form of the verb is 1. chase  2. chased  3. chasing", "The correct form of the verb is 1. walk 2. walking 3. walked",
	"The correct form of the verb is 1. sit 2. sat 3. sitting", "The correct form of the verb is 1. ran 2. run 3. running", 
	"The correct form of the verb is 1. come 2. came 3. coming", "The correct form of the verb is 1. cried 2. cry 3. crying", 
	"The correct form of the verb is 1. is 2. has 3. are", "The correct form of the verb is 1. shoot 2. shooting 3. shot", 
	"The correct form of the verb is 1. dancing 2. danced 3. dance", "The correct form of the verb is 1. learning 2. learn 3. learned",
	#chased, walking, sitting, run, come, cry, is, shot, danced, learn
	#1, 1, 2, 1, 0, 1, 0, 2, 1, 1
	
	"The correct form of the verb is 1. watched 2. watch  3. watching ", "The correct form of the verb is 1. write 2. wrote 3. writing ", 
	"The correct form of the verb is 1. bring 2. bringing 3. brought", "The correct form of the verb is 1. catching 2. catch 3. caught",
	"The correct form of the verb is 1. talked 2. talking 3. talk", "The correct form of the verb is 1. draw 2. drew 3. drawing",
	"The correct form of the verb is 1. wake 2. waking 3. woke", "The correct form of the verb is 1. swore 2. swear 3. swearing", 
	"The correct form of the verb is 1. are 2. is 3. am", "The correct form of the verb is 1. leave 2. left 3. leaving",
	#watched, writing, brought, caught, talking, drew, waking, swear, are, left
	#0, 2, 2, 2, 1, 1, 1, 1, 0, 1
	
	#Used non existant forms of words to increase difficulty, as well as more irregular verbs
	"The correct form of the verb is 1. bleed 2. bled 3. bleeded", "The correct form of the verb is 1. skipped 2. skept 3. skip",
	"The correct form of the verb is 1. throw 2. through 3. threw", "The correct form of the verb is 1. shower 2. showering 3. showing", 
	"The correct form of the verb is 1. forgave 2. forgived 3. forgiven", "The correct form of the verb is 1. is 2. are 3. am",
	"The correct form of the verb is 1. think 2. thought 3. thinking", "The correct form of the verb is 1. going 2. goes 3. go", 
	"The correct form of the verb is 1. had 2. having 3. have", "The correct form of the verb is 1. took 2. take 3. taked"]
	#bled, skipped, threw, showering, forgave, is, think, go, having, take
	#1, 0, 2, 1, 0, 0, 0, 2, 1, 1
	
	number_array = ["How many nouns are there A. 1 B. 2 C. 3", "How many nouns are there A. 1 B. 2 C. 3", "How many nouns are there A. 0 B. 1 C. 2", 
	"How many nouns are there A. 1 B. 2 C. 3", "How many nouns are there A. 1 B. 2 C. 3", "How many nouns are there A. 1 B. 2 C. 3", "How many nouns are there A. 1 B. 2 C. 3",
	"How many nouns are there A. 0 B. 1 C. 2", "How many nouns are there A. 1 B. 2 C. 3", "How many nouns are there A. 0 B. 1 C. 2",
	#2, 1, 0, 1, 0, 0, 1, 2, 2, 1
	
	"How many nouns are there A. 2 B. 0 C. 1", "How many nouns are there A. 0 B. 2 C. 1", "How many nouns are there A. 1 B. 2 C. 3", "How many nouns are there A. 2 B. 3 C. 1",
	"How many nouns are there A. 4 B. 1 C. 2", "How many nouns are there A. 5 B. 1 C. 2", "How many nouns are there A. 0 B. 2 C. 1", "How many nouns are there A. 4 B. 3 C. 2",
	"How many nouns are there A. 3 B. 2 C. 0", "How many nouns are there A. 0 B. 2 C. 3",
	#0, 2, 1, 2, 1, 1, 1, 2, 1, 1
	
	"How many nouns are there A. 5 B. 2 C. 1", "How many nouns are there A. 4 B. 1 C. 7", "How many nouns are there A. 3 B. 1 C. 6", "How many nouns are there A. 3 B. 4 C. 2",
	"How many nouns are there A. 8 B. 1 C. 3", "How many nouns are there A. 5 B. 3 C. 2", "How many nouns are there A. 1 B. 6 C. 2", "How many nouns are there A. 5 B. 1 C. 2",
	"How many nouns are there A. 0 B. 3 C. 1", "How many nouns are there A. 2 B. 1 C. 6"]
	#2, 1, 0, 0, 1, 2, 0, 1, 1, 1




	global x_array
	x_array = [0, 0, 1, 2, 0, 2, 1, 1, 1, 0,
	0, 0, 1, 1, 0, 1, 0, 1, 2, 2,
	1, 2, 0, 1, 1, 2, 1, 0, 2, 0]
	global y_array
	y_array = [1, 1, 2, 1, 0, 1, 0, 2, 1, 1,
	0, 2, 2, 2, 1, 1, 1, 1, 0, 1,
	1, 0, 2, 1, 0, 0, 0, 2, 1, 1]
	global z_array
	z_array = [2, 1, 0, 1, 0, 0, 1, 2, 2, 1,
	0, 2, 1, 2, 1, 1, 1, 2, 1, 1,
	2, 1, 0, 0, 1, 2, 0, 1, 1, 1]
	
	global rnd
	rnd = random.randint(0,30)
	sont = spyral.Font("/usr/share/fonts/truetype/freefont/FreeMono.ttf",20,(255,255,255))
	#message4 = font.render(str(game.Balls));	
	message4 = sont.render(question_array[rnd]);
	message5 =sont.render(subject_array[rnd]);
	message6 = sont.render(verb_array[rnd]);
	message7 = sont.render(number_array[rnd]);
	questionMessage(self,message4,(0),10)
	questionMessage(self,message5,(0),150)
	questionMessage(self,message6,(0),200)	
	questionMessage(self,message7,(0),250)
	message = font.render("");
	message1 = font.render("2.");
	message2 = font.render("1.");
	message3 = font.render("3.");
	message10 = font.render("a.");
	message11 = font.render("b.");
	message12 = font.render("c.");
	questionMessage(self,message10, 220, 360) 
	questionMessage(self,message11, 570, 360) 
	questionMessage(self,message12, 920, 360) 
	self.q1 = questionMessage(self,message,(0),10)
	self.q2 = questionMessage(self,message1,(10),550)
	self.q3 = questionMessage(self,message2,(10),400)
	self.q4 = questionMessage(self,message3,(10),700)
	
	game.NumAnsw = 0
	self.c1 = Check(self,-10,-100)
	self.x1 = X(self,-10,-100)
	self.c2 = Check(self,-10,-100)
	self.x2 = X(self,-10,-100)
	self.c3 = Check(self,-10,-100)
	self.x3 = X(self,-10,-100)
	if game.Pic == 0:
        	self.b1 = One(self,200,390)
		self.b2 = One(self,200,540)
		self.b3 = One (self,200, 690)
		self.b4 = One(self,550, 390)
		self.b5 = One(self,550,540)
		self.b6 = One(self,550,690)
		self.b7 = One(self,900,390)
		self.b8 = One(self,900,540)
		self.b9 = One(self,900,690)
	
	if game.Pic == 1:
        	self.b1 = hat(self,200,390)
		self.b2 = hat(self,200,540)
		self.b3 = hat (self,200, 690)
		self.b4 = hat(self,550, 390)
		self.b5 = hat(self,550,540)
		self.b6 = hat(self,550,690)
		self.b7 = hat(self,900,390)
		self.b8 = hat(self,900,540)
		self.b9 = hat(self,900,690)
	if game.Pic == 4:
        	self.b1 = sheep(self,200,390)
		self.b2 = sheep(self,200,540)
		self.b3 = sheep (self,200, 690)
		self.b4 = sheep(self,550, 390)
		self.b5 = sheep(self,550,540)
		self.b6 = sheep(self,550,690)
		self.b7 = sheep(self,900,390)
		self.b8 = sheep(self,900,540)
		self.b9 = sheep(self,900,690)
	if game.Pic == 3:
        	self.b1 = phone(self,200,390)
		self.b2 = phone(self,200,540)
		self.b3 = phone (self,200, 690)
		self.b4 = phone(self,550, 390)
		self.b5 = phone(self,550,540)
		self.b6 = phone(self,550,690)
		self.b7 = phone(self,900,390)
		self.b8 = phone(self,900,540)
		self.b9 = phone(self,900,690)
	if game.Pic == 5:
        	self.b1 = ball8(self,200,390)
		self.b2 = ball8(self,200,540)
		self.b3 = ball8 (self,200, 690)
		self.b4 = ball8(self,550, 390)
		self.b5 = ball8(self,550,540)
		self.b6 = ball8(self,550,690)
		self.b7 = ball8(self,900,390)
		self.b8 = ball8(self,900,540)
		self.b9 = ball8(self,900,690)
	if game.Pic == 2:
        	self.b1 = burger(self,200,390)
		self.b2 = burger(self,200,540)
		self.b3 = burger (self,200, 690)
		self.b4 = burger(self,550, 390)
		self.b5 = burger(self,550,540)
		self.b6 = burger(self,550,690)
		self.b7 = burger(self,900,390)
		self.b8 = burger(self,900,540)
		self.b9 = burger(self,900,690)
	if game.Pic == 6:
        	self.b1 = flower(self,200,390)
		self.b2 = flower(self,200,540)
		self.b3 = flower (self,200, 690)
		self.b4 = flower(self,550, 390)
		self.b5 = flower(self,550,540)
		self.b6 = flower(self,550,690)
		self.b7 = flower(self,900,390)
		self.b8 = flower(self,900,540)
		self.b9 = flower(self,900,690)
	
	m2 = font.render(str(game.Counter))
	self.s1=questionMessage(self,m2,(940),35)
	m3 = font.render(str(game.Counter1))
	self.s2 =questionMessage(self,m3,(1140),35)	
	self.font1 = spyral.Font("/usr/share/fonts/truetype/freefont/FreeMono.ttf",36,(255,255,255))
	print game.Balls 
	
	self.n1 = 0
	self.n2 = 0
	#self.c1 = Check(self,500,500)
	#message3 = font.render(counter);
	#self.c1 = questionMessage(self,message3,(1100),10)
    def go_Next(self):
	if game.NumAnsw == 3:

		spyral.director.pop
		#spyral.director.replace(pong.Pong())		
		spyral.director.replace(basketball2.BasketBall2())
		#spyral.director.replace(question.Question())
    def handle_clicked(self, pos):
	global x_array
	global z_array
	global y_array
	
	if x_array[rnd] == 0 and self.c1.x<0:
		if pos.x < 350 and pos.y < 525:
			self.c1.x = 250
			self.c1.y = 400 
			game.Balls = game.Balls +1
			print game.Balls 
			game.Counter = game.Counter +1
			self.s1.kill()
			q = self.font1.render(str(game.Counter))
			self.s1=questionMessage(self,q,(940),35)
			game.NumAnsw = game.NumAnsw +1
		elif pos.x< 750 and pos.x >350 and pos.y<525:
			self.x1.x = 570
			self.x1.y = 450
			self.c1.x = 250
			self.c1.y = 400
			game.Counter1 = game.Counter1 +1
			self.s2.kill()
			q = self.font1.render(str(game.Counter1))
			self.s2=questionMessage(self,q,(1140),35)
			game.NumAnsw = game.NumAnsw +1
		elif pos.x> 750 and pos.y<525:
			self.x1.x = 960
			self.x1.y = 450
			self.c1.x = 250
			self.c1.y = 400
			game.Counter1 = game.Counter1 +1
			self.s2.kill()
			q = self.font1.render(str(game.Counter1))
			self.s2=questionMessage(self,q,(1140),35)
			game.NumAnsw = game.NumAnsw +1
	elif x_array[rnd] == 1 and self.c1.x<0:
		if pos.x < 350 and pos.y < 525:
			self.x1.x = 250
			self.x1.y = 450 
			self.c1.x = 570
			self.c1.y = 400
			game.Counter1 = game.Counter1 +1
			self.s2.kill()
			q = self.font1.render(str(game.Counter1))
			self.s2=questionMessage(self,q,(1140),35)
			game.NumAnsw = game.NumAnsw +1
		elif pos.x< 750 and pos.x >350 and pos.y<525:
			self.c1.x = 570
			self.c1.y = 400
			game.Balls = game.Balls +1
			print game.Balls 
			game.Counter = game.Counter +1
			self.s1.kill()
			q = self.font1.render(str(game.Counter))
			self.s1=questionMessage(self,q,(940),35)
			game.NumAnsw = game.NumAnsw +1
	
		elif pos.x> 750 and pos.y<525:
			self.x1.x = 960
			self.x1.y = 450
			self.c1.x = 570
			self.c1.y = 400
			game.Counter1 = game.Counter1 +1
			self.s2.kill()
			q = self.font1.render(str(game.Counter1))
			self.s2=questionMessage(self,q,(1140),35)
			game.NumAnsw = game.NumAnsw +1
	elif x_array[rnd] == 2 and self.c1.x<0:
		if pos.x < 350 and pos.y < 525:
			self.x1.x = 250
			self.x1.y = 450 
			self.c1.x = 980 
			self.c1.y = 400
			game.Counter1 = game.Counter1 +1
			self.s2.kill()
			q = self.font1.render(str(game.Counter1))
			self.s2=questionMessage(self,q,(1140),35)
			game.NumAnsw = game.NumAnsw +1
		elif pos.x< 750 and pos.x >350 and pos.y<525:
			self.x1.x = 570
			self.x1.y = 450
			self.c1.x = 980
			self.c1.y = 400
			game.Counter1 = game.Counter1 +1
			self.s2.kill()
			q = self.font1.render(str(game.Counter1))
			self.s2=questionMessage(self,q,(1140),35)
			game.NumAnsw = game.NumAnsw +1
		elif pos.x> 750 and pos.y<525:
			self.c1.x = 980
			self.c1.y = 400
			game.Balls = game.Balls + 1
			print game.Balls 
			game.Counter = game.Counter +1
			self.s1.kill()
			q = self.font1.render(str(game.Counter))
			self.s1=questionMessage(self,q,(940),35)
			game.NumAnsw = game.NumAnsw +1

		
	if y_array[rnd] == 0 and self.c2.x<0:
		if pos.x < 350 and pos.y > 525 and pos.y< 675:
			self.c2.x = 250
			self.c2.y = 550
			game.Balls = game.Balls +1
			print game.Balls 
			game.Counter = game.Counter +1
			self.s1.kill()
			q = self.font1.render(str(game.Counter))
			self.s1=questionMessage(self,q,(940),35)
			game.NumAnsw = game.NumAnsw +1
		elif pos.x< 750 and pos.x >350 and pos.y>525 and pos.y< 675:
			self.x2.x = 550
			self.x2.y = 600
			self.c2.x = 250
			self.c2.y = 550
			game.Counter1 = game.Counter1 +1
			self.s2.kill()
			q = self.font1.render(str(game.Counter1))
			self.s2=questionMessage(self,q,(1140),35)
			game.NumAnsw = game.NumAnsw +1
		elif pos.x> 750 and pos.y>525 and pos.y< 675:
			self.x2.x = 960
			self.x2.y = 600
			self.c2.x = 250
			self.c2.y = 550
			game.Counter1 = game.Counter1 +1
			self.s2.kill()
			q = self.font1.render(str(game.Counter1))
			self.s2=questionMessage(self,q,(1140),35)
			game.NumAnsw = game.NumAnsw +1
	elif y_array[rnd] == 1 and self.c2.x<0:
		if pos.x < 350 and pos.y > 525 and pos.y< 675:
			self.x2.x = 250
			self.x2.y = 600 
			self.c2.x = 570
			self.c2.y = 550
			game.Counter1 = game.Counter1 +1
			self.s2.kill()
			q = self.font1.render(str(game.Counter1))
			self.s2=questionMessage(self,q,(1140),35)
			game.NumAnsw = game.NumAnsw +1
		elif pos.x< 750 and pos.x >350 and pos.y>525 and pos.y< 675:
			self.c2.x = 570
			self.c2.y = 550
			game.Balls = game.Balls +1
			print game.Balls 
			game.Counter = game.Counter +1
			self.s1.kill()
			q = self.font1.render(str(game.Counter))
			self.s1=questionMessage(self,q,(940),35)
			game.NumAnsw = game.NumAnsw +1
		elif pos.x> 750 and pos.y>525 and pos.y< 675:
			self.x2.x = 1000
			self.x2.y = 600
			self.c2.x = 570
			self.c2.y = 550
			game.Counter1 = game.Counter1 +1
			self.s2.kill()
			q = self.font1.render(str(game.Counter1))
			self.s2=questionMessage(self,q,(1140),35)
			game.NumAnsw = game.NumAnsw +1
	elif y_array[rnd] == 2 and self.c2.x<0:
		if pos.x < 350 and pos.y > 525 and pos.y< 675:
			self.x2.x = 250
			self.x2.y = 600 
			self.c2.x = 960 
			self.c2.y = 550
			game.Counter1 = game.Counter1 +1
			self.s2.kill()
			q = self.font1.render(str(game.Counter1))
			self.s2=questionMessage(self,q,(1140),35)
			game.NumAnsw = game.NumAnsw +1
		elif pos.x< 750 and pos.x >350 and pos.y>525 and pos.y< 675:
			self.x2.x = 570
			self.x2.y = 600
			self.c2.x = 960
			self.c2.y = 550
			game.Counter1 = game.Counter1 +1
			self.s2.kill()
			q = self.font1.render(str(game.Counter1))
			self.s2=questionMessage(self,q,(1140),35)
			game.NumAnsw = game.NumAnsw +1
		elif pos.x> 750 and pos.y>525 and pos.y< 675:
			self.c2.x = 960
			self.c2.y = 550
			game.Balls = game.Balls + 1
			print game.Balls 
			game.Counter = game.Counter +1
			self.s1.kill()
			q = self.font1.render(str(game.Counter))
			self.s1=questionMessage(self,q,(940),35)
			game.NumAnsw = game.NumAnsw +1
			
	if z_array[rnd] == 0 and self.c3.x<0:
		if pos.x < 350 and pos.y > 675:
			self.c3.x = 250
			self.c3.y = 700 
			game.Balls = game.Balls +1
			print game.Balls 
			game.Counter = game.Counter +1
			self.s1.kill()
			q = self.font1.render(str(game.Counter))
			self.s1=questionMessage(self,q,(940),35)
			game.NumAnsw = game.NumAnsw +1
		elif pos.x< 750 and pos.x >350 and pos.y>675:
			self.x3.x = 570
			self.x3.y = 750
			self.c3.x = 250
			self.c3.y = 700
			game.Counter1 = game.Counter1 +1
			self.s2.kill()
			q = self.font1.render(str(game.Counter1))
			self.s2=questionMessage(self,q,(1140),35)
			game.NumAnsw = game.NumAnsw +1
		elif pos.x> 750 and pos.y>675:
			self.x3.x = 960
			self.x3.y = 750
			self.c3.x = 250
			self.c3.y = 700
			game.Counter1 = game.Counter1 +1
			self.s2.kill()
			q = self.font1.render(str(game.Counter1))
			self.s2=questionMessage(self,q,(1140),35)
			game.NumAnsw = game.NumAnsw +1
	elif z_array[rnd] == 1 and self.c3.x<0:
		if pos.x < 350 and pos.y > 675:
			self.x3.x = 250
			self.x3.y = 750 
			self.c3.x = 570
			self.c3.y = 700
			game.Counter1 = game.Counter1 +1
			self.s2.kill()
			q = self.font1.render(str(game.Counter1))
			self.s2=questionMessage(self,q,(1140),35)
			game.NumAnsw = game.NumAnsw +1
		elif pos.x< 750 and pos.x >350 and pos.y>675:
			self.c3.x = 570
			self.c3.y = 700
			game.Balls = game.Balls +1
			print game.Balls 
			game.Counter = game.Counter +1
			self.s1.kill()
			q = self.font1.render(str(game.Counter))
			self.s1=questionMessage(self,q,(940),35)
			game.NumAnsw = game.NumAnsw +1
		elif pos.x> 750 and pos.y>675:
			self.x3.x = 960
			self.x3.y = 750
			self.c3.x = 570
			self.c3.y = 700
			game.Counter1 = game.Counter1 +1
			self.s2.kill()
			q = self.font1.render(str(game.Counter1))
			self.s2=questionMessage(self,q,(1140),35)
			game.NumAnsw = game.NumAnsw +1
	elif z_array[rnd] == 2 and self.c3.x<0:
		if pos.x < 350 and pos.y > 675:
			self.x3.x = 250
			self.x3.y = 750 
			self.c3.x = 960 
			self.c3.y = 700
			game.Counter1 = game.Counter1 +1
			self.s2.kill()
			q = self.font1.render(str(game.Counter1))
			self.s2=questionMessage(self,q,(1140),35)
			game.NumAnsw = game.NumAnsw +1
		elif pos.x< 750 and pos.x >350 and pos.y>675:
			self.x3.x = 570
			self.x3.y = 750
			self.c3.x = 960
			self.c3.y = 700
			game.Counter1 = game.Counter1 +1
			self.s2.kill()
			q = self.font1.render(str(game.Counter1))
			self.s2=questionMessage(self,q,(1140),35)
			game.NumAnsw = game.NumAnsw +1
		elif pos.x> 750 and pos.y>675:
			self.c3.x = 960
			self.c3.y = 700
			game.Balls = game.Balls + 1
			print game.Balls 
			game.Counter = game.Counter +1
			self.s1.kill()
			q = self.font1.render(str(game.Counter))
			self.s1=questionMessage(self,q,(940),35)
			game.NumAnsw = game.NumAnsw +1
	
#class checl(spyral.Sprite):
#	def __init__(self,scene,img,x,y):
	
class questionMessage(spyral.Sprite):
	def __init__(self,scene,img,x,y):
		spyral.Sprite.__init__(self,scene)
		self.image = img
		self.x = x
		self.y = y

	
