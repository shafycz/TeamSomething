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
class X(spyral.Sprite):
  def __init__(self, scene, x,y):
   super(X,self).__init__(scene)
   self.image = spyral.Image(filename="game/x.png")
   self.anchor = 'center'
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
        
		class selectDifficultyForm(spyral.Form) 
		easy = spyral.widgets.Button("easy", "Easy")
		medium = spyral.widgets.Button("medium", "Medium")
		hard = spyral.widgets.Button("Hard", "Hard")
		if easy = "down":
			easyquestion = random.randrange(question1_array[0], question1_array[9])
			#easyrand = random.getstate()
			easysubject = random.randrange(subject1_array[easyrand, easyrand]
			easyverb = random.randrange(verb1_array[easyrand, easyrand]
			easynumber = random.randrange(number1_array[easyrand, easyrand]
			message4 = font.render(easyquestion);
			message5 = sont.render(easysubject);
			message6 = sont.render(easyverb);
			message7 = sont.render(easynumber);
		
			elif medium = "down":
			
			mediumquestion = random.randrange(question2_array[0], question2_array[9])
			#mediumrand = random.getstate() 
			mediumsubject = random.randrange(subject2_array[mediumrand, mediumrand]
			mediumverb = random.randrange(verb2_array[mediumrand, mediumrand]
			mediumnumber = random.randrange(number2_array[mediumrand, mediumrand]
			message4 = font.render(mediumquestion);
			message5 = sont.render(mediumsubject);
			message6 = sont.render(mediumverb);
			message7 = sont.render(mediumnumber);
			
			elif hard = "down":
        
			hardquestion = random.randrange(question3_array[0], question3_array[9])
			#hardrand = random.getstate()
			hardquestion = random.randrange(subject3_array[hardrand, hardrand]
			hardquestion = random.randrange(verb3_array[hardrand, hardrand]
			hardquestion = random.randrange(number3_array[hardrand, hardrand]
			message4 = font.render(hardquestion);
			message5 = sont.render(hardsubject);
			message6 = sont.render(hardverb);
			message7 = sont.render(hardnumber);
			
		#message4 = font.render(question_array[0]);
		#message5 =sont.render(subject_array[0]);
		#message6 = sont.render(verb_array[0]);
		#message7 = sont.render(number_array[0]);
		
	spyral.event.register("input.mouse.down.left", self.handle_clicked) 
	spyral.event.register("system.quit", spyral.director.pop)
	spyral.event.register("input.keyboard.down.q", spyral.director.pop)
 	font = spyral.Font("/usr/share/fonts/truetype/freefont/FreeMono.ttf",36,(255,255,255))
	question1_array = ["The cat ___ the bird around the room.", "John is ___ to school.", "You are ___ right now.", "Lions ___ after their prey.",
	 "Can I ___ to your house?", "People ___ when they are sad.", "An iPhone ___ a cellphone.", "The player ___ the basketball.",
	  "Beyonce ___ on stage with Jay Z.", "We will ___ in class because it is fun."]
	
	#Increased difficulty by making sentence structure slightly more complex
	question2_array=["I ___ March Madness on my television.", "___ a paper can be stressful.", "I ___ my homework to my room.", 
	"He was ___ daydreaming in class.", "You probably should not be ___ in class.", "The student ___ in his art class yesterday.", "___ up is hard.", 
	"I ___ The Eagles will win the Superbowl.", "All CCCS students ___ awesome!", "Anthony ___ school early because he was sick."]
	
	#Made sentences more complex by making the nouns and verbs somewhat harder to find/more vague, as well as subject, requires more thought
	question3_array=["He ___ because he got a papercut.", "He ___ breakfast, even though he knew he should not have.", "The quarterback ___ the ball to his teammate quickly.", 
	"Dorothy prefers ___ in the morning instead of at night.", "He ___ his sister, even though she had been mean.", "Broccoli ___ a delicious food.",
	"What is your favorite place to ___ about?", "Would you like to ___ to the zoo?", "Sunday is the best day for ___ a nap.", "I would like to ___ a hike today."]
	
	subject1_array =["The subject is 1. cat 2. bird 3. room ", "The subject is 1. John 2. school 3. is", "The subject is 1. now 2. you 3. right", 
	"The subject is 1. prey 2. after 3. lions", "The subject is 1. I 2. house 3. your ", "The subject is 1. when 2. sad 3. people", 
	"The subject is 1. cellphone 2. iPhone 3. a", "The subject is 1. the 2. player 3. basketball", "The subject is 1. Jay Z 2. Beyonce 3. stage", 
	"The subject is 1. we 2. class 3. fun"]
	#cat, John, you, lions, I, people, iPhone, player, Beyonce, we
	
	subject2_array =["The subject is 1. I 2. television 3. March Madness", "The subject is 1. paper 2. can 3. stressful", "The subject is 1. room 2. I 3. homework", 
	"The subject is 1. caught 2. he 3. class", "The subject is 1. you 2. class 3. should", "The subject is 1. art class 2. student 3. yesterday", 
	"The subject is 1. is 2. hard 3. up", "The subject is 1. Superbowl 2. The Eagles 3. win", "The subject is 1. awesome 2. all 3. students", 
	"The subject is 1. school 2. because 3. Anthony"]
	#I, paper, I, he, you, student, waking, The Eagles, students, Anthony
	
	subject3_array =["The subject is 1. got 2. he 3. papercut", "The subject is 1. have 2. breakfast 3. he", "The subject is 1. quarterback 2. teammate 3. ball", 
	"The subject is 1. morning 2. Dorothy 3. night", "The subject is 1. sister 2. he 3. she",
	"The subject is 1. food 2. delicious 3. broccoli", "The subject is 1. your 2. place 3. about", "The subject is 1. like 2. zoo 3. go",
	"The subject is 1. nap 2. day 3. Sunday", "The subject is 1. today 2. hike 3. would"]
	#he, he, quarterback, Dorothy, he, broccoli, place, you, Sunday, I
	
	verb1_array = ["The correct form of the verb is 1. chase  2. chased  3. chasing", "The correct form of the verb is 1. walk 2. walking 3. walked",
	"The correct form of the verb is 1. sit 2. sat 3. sitting", "The correct form of the verb is 1. ran 2. run 3. running", 
	"The correct form of the verb is 1. come 2. came 3. coming", "The correct form of the verb is 1. cried 2. cry 3. crying", 
	"The correct form of the verb is 1. is 2. has 3. are", "The correct form of the verb is 1. shoot 2. shooting 3. shot", 
	"The correct form of the verb is 1. dancing 2. danced 3. dance", "The correct form of the verb is 1. learning 2. learn 3. learned"]
	#chased, walking, sitting, run, come, cry, is, shot, danced, learn
	
	verb2_array=["The correct form of the verb is 1. watched 2. watch  3. watching ", "The correct form of the verb is 1. write 2. wrote 3. writing ", 
	"The correct form of the verb is 1. bring 2. bringing 3. brought", "The correct form of the verb is 1. catching 2. catch 3. caught",
	"The correct form of the verb is 1. talked 2. talking 3. talk", "The correct form of the verb is 1. draw 2. drew 3. drawing",
	"The correct form of the verb is 1. wake 2. waking 3. woke", "The correct form of the verb is 1. swore 2. swear 3. swearing", 
	"The correct form of the verb is 1. are 2. is 3. am", "The correct form of the verb is 1. learned 2. learn 3. learning"]
	#watched, writing, brought, caught, talking, drew, waking, swear, are, left
	
	#Used non existant forms of words to increase difficulty, as well as more irregular verbs
	verb3_array=["The correct form of the verb is 1. bleed 2. bled 3. bleeded", "The correct form of the verb is 1. skipped 2. skept 3. skip",
	"The correct form of the verb is 1. throw 2. through 3. threw", "The correct form of the verb is 1. shower 2. showering 3. showing", 
	"The correct form of the verb is 1. forgave 2. forgived 3. forgiven", "The correct form of the verb is 1. is 2. are 3. am",
	"The correct form of the verb is 1. think 2. thought 3. thinking", "The correct form of the verb is 1. go 2. goes 3. going", 
	"The correct form of the verb is 1. having 2. haved 3. have", "The correct form of the verb is 1. take 2. took 3. taked"]
	#bled, skipped, threw, showering, forgave, is, think, go, having, take
	
	number1_array = ["How many proper nouns are there A. 1 B. 2 C. 3", "How many proper nouns are there A. 1 B. 2 C. 3", "How many proper nouns are there A. 0 B. 1 C. 2", 
	"How many proper nouns are there A. 1 B. 2 C. 3", "How many proper nouns are there A. 1 B. 2 C. 3", "How many proper nouns are there A. 1 B. 2 C. 3", "How many proper nouns are there A. 1 B. 2 C. 3",
	"How many proper nouns are there A. 0 B. 1 C. 2", "How many proper nouns are there A. 1 B. 2 C. 3", "How many proper nouns are there A. 0 B. 1 C. 2"] 
	# 3, 2, 0, 2, 1, 1, 2, 2, 3, 1 
	
	number2_array =["How many proper nouns are there A. 2 B. 0 C. 1", "How many proper nouns are there A. 0 B. 2 C. 1", "How many proper nouns are there A. 1 B. 2 C. 3", "How many proper nouns are there A. 2 B. 3 C. 1",
	"How many proper nouns are there A. 4 B. 1 C. 2", "How many proper nouns are there A. 5 B. 1 C. 2", "How many proper nouns are there A. 0 B. 2 C. 1", "How many proper nouns are there A. 4 B. 3 C. 2",
	"How many proper nouns are there A. 3 B. 2 C. 0", "How many proper nouns are there A. 0 B. 2 C. 3"]
	#2, 1, 2, 1, 1, 2, 0, 2, 2, 2
	
	number3_array=["How many proper nouns are there A. 5 B. 2 C. 1", "How many proper nouns are there A. 4 B. 1 C. 7", "How many proper nouns are there A. 3 B. 1 C. 6", "How many proper nouns are there A. 3 B. 4 C. 2",
	"How many proper nouns are there A. 8 B. 1 C. 3", "How many proper nouns are there A. 5 B. 3 C. 2", "How many proper nouns are there A. 1 B. 6 C. 2", "How many proper nouns are there A. 5 B. 1 C. 2",
	"How many proper nouns are there A. 0 B. 3 C. 1", "How many proper nouns are there A. 2 B. 1 C. 6"]
	#1, 1, 3, 3, 1, 2, 1, 1, 3, 1

#Possible hint: A noun is a person, place, or thing, while a proper noun is the more specific name of a person, place, or thing. 

	verb1_answer_array = ["chased", "walking", "sitting", "run", "come", "cry", "is", "shot", "danced", "learn"]
	verb2_answer_array = ["watched", "writing", "brought", "caught", "talking", "drew", "waking", "swear", "are", "left"]
	verb3_answer_array = ["bled", "skipped", "threw", "showering", "forgave", "is", "think", "go", "having", "take"]
	number1_answer_array = ["3", "2", "0", "2", "1", "1", "2", "2", "3", "1"]
	number2_answer_array = ["2", "1", "2", "1", "1", "2", "0", "2", "2", "2"]
	number3_answer_array = ["1", "1", "3", "3", "1", "2", "1", "1", "3", "1"]
	subject1_answer_array = ["cat", "John", "you", "lions", "I", "people", "iPhone", "player", "Beyonce", "we"]
	subject2_answer_array = ["I", "paper", "I", "he", "you", "student", "waking", "The Eagles", "students", "Anthony"]
	subject3_answer_array = ["he", "he", "quarterback", "Dorothy", "he", "broccoli", "place", "you", "Sunday", "I"]

	global x_array
	x_array = [1,1]
	global y_array
	y_array = [2,1]
	global z_array
	z_array = [3,1]
	sont = spyral.Font("/usr/share/fonts/truetype/freefont/FreeMono.ttf",30,(50,50,60))
	#message4 = font.render(question_array[0]);
	#message5 =sont.render(subject_array[0]);
	#message6 = sont.render(verb_array[0]);
	#message7 = sont.render(number_array[0]);
	self.diff_form = selectDifficultyForm(self)
	self.diff_form.focus()
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
	self.c1 = Check(self,-10,-100)
	self.x1 = X(self,-10,-100)
	self.c2 = Check(self,-10,-100)
	self.x2 = X(self,-10,-100)
	self.c3 = Check(self,-10,-100)
	self.x3 = X(self,-10,-100)
	m2 = font.render(str(game.Counter))
	questionMessage(self,m2,(960),20)
	m3 = font.render(str(game.Counter1))
	questionMessage(self,m3,(1150),20)	

	print game.Balls 
	#self.c1 = Check(self,500,500)
	#message3 = font.render(counter);
	#self.c1 = questionMessage(self,message3,(1100),10)
    def handle_clicked(self, pos):
	global x_array
	global z_array
	global y_array
	if pos.y>700:
		spyral.director.replace(basketball2.BasketBall2())
	if x_array[0] == 1 and self.c1.x<0:
		if pos.x < 350 and pos.y < 250:
			self.c1.x = 160
			self.c1.y = 195 
			game.Balls = game.Balls +1
			print game.Balls 
			game.Counter = game.Counter +1
		elif pos.x< 750 and pos.x >350 and pos.y<250:
			self.x1.x = 550
			self.x1.y = 195
			self.c1.x = 165
			self.c1.y = 200
			game.Counter1 = game.Counter1 +1
		elif pos.x> 750 and pos.y<250:
			self.x1.x = 1000
			self.x1.y = 195
			self.c1.x = 165
			self.c1.y = 200
			game.Counter1 = game.Counter1 +1
	elif x_array[0] == 2 and self.c1.x<0:
		if pos.x < 350 and pos.y < 250:
			self.x1.x = 160
			self.x1.y = 195 
			self.c1.x = 550
			self.c1.y = 195
			game.Counter1 = game.Counter1 +1
		elif pos.x< 750 and pos.x >350 and pos.y<250:
			self.c1.x = 550
			self.c1.y = 195
			game.Balls = game.Balls +1
			print game.Balls 
			game.Counter = game.Counter +1
		elif pos.x> 750 and pos.y<250:
			self.x1.x = 1000
			self.x1.y = 195
			self.c1.x = 550
			self.c1.y = 195
			game.Counter1 = game.Counter1 +1
	elif x_array[0] == 3 and self.c1.x<0:
		if pos.x < 350 and pos.y < 250:
			self.x1.x = 160
			self.x1.y = 195 
			self.c1.x = 1000 
			self.c1.y = 195
			game.Counter1 = game.Counter1 +1
		elif pos.x< 750 and pos.x >350 and pos.y<250:
			self.x1.x = 550
			self.x1.y = 195
			self.c1.x = 1000
			self.c1.y = 195
			game.Counter1 = game.Counter1 +1
		elif pos.x> 750 and pos.y<250:
			self.c1.x = 1000
			self.c1.y = 195
			game.Balls = game.Balls + 1
			print game.Balls 
			game.Counter = game.Counter +1

		
	if y_array[0] == 1 and self.c2.x<0:
		if pos.x < 350 and pos.y > 250 and pos.y< 400:
			self.c2.x = 160
			self.c2.y = 350 
			game.Balls = game.Balls +1
			print game.Balls 
			game.Counter = game.Counter +1
		elif pos.x< 750 and pos.x >350 and pos.y>250 and pos.y< 400:
			self.x2.x = 550
			self.x2.y = 350
			self.c2.x = 165
			self.c2.y = 350
			game.Counter1 = game.Counter1 +1
		elif pos.x> 750 and pos.y>250 and pos.y< 400:
			self.x2.x = 1000
			self.x2.y = 350
			self.c2.x = 165
			self.c2.y = 350
			game.Counter1 = game.Counter1 +1
	elif y_array[0] == 2 and self.c2.x<0:
		if pos.x < 350 and pos.y > 250 and pos.y< 400:
			self.x2.x = 160
			self.x2.y = 350 
			self.c2.x = 550
			self.c2.y = 350
			game.Counter1 = game.Counter1 +1
		elif pos.x< 750 and pos.x >350 and pos.y>250 and pos.y< 400:
			self.c2.x = 550
			self.c2.y = 350
			game.Balls = game.Balls +1
			print game.Balls 
			game.Counter = game.Counter +1
		elif pos.x> 750 and pos.y>250 and pos.y< 400:
			self.x2.x = 1000
			self.x2.y = 350
			self.c2.x = 550
			self.c2.y = 350
			game.Counter1 = game.Counter1 +1
	elif y_array[0] == 3 and self.c2.x<0:
		if pos.x < 350 and pos.y > 250 and pos.y< 400:
			self.x2.x = 160
			self.x2.y = 350 
			self.c2.x = 1000 
			self.c2.y = 350
			game.Counter1 = game.Counter1 +1
		elif pos.x< 750 and pos.x >350 and pos.y>250 and pos.y< 400:
			self.x2.x = 550
			self.x2.y = 350
			self.c2.x = 1000
			self.c2.y = 350
			game.Counter1 = game.Counter1 +1
		elif pos.x> 750 and pos.y>250 and pos.y< 400:
			self.c2.x = 1000
			self.c2.y = 350
			game.Balls = game.Balls + 1
			print game.Balls 
			game.Counter = game.Counter +1
			
	if z_array[0] == 1 and self.c3.x<0:
		if pos.x < 350 and pos.y > 400:
			self.c3.x = 160
			self.c3.y = 500 
			game.Balls = game.Balls +1
			print game.Balls 
			game.Counter = game.Counter +1
		elif pos.x< 750 and pos.x >350 and pos.y>400:
			self.x3.x = 550
			self.x3.y = 500
			self.c3.x = 165
			self.c3.y = 500
			game.Counter1 = game.Counter1 +1
		elif pos.x> 750 and pos.y>400:
			self.x3.x = 1000
			self.x3.y = 195
			self.c3.x = 165
			self.c3.y = 200
			game.Counter1 = game.Counter1 +1
	elif z_array[0] == 2 and self.c3.x<0:
		if pos.x < 350 and pos.y > 400:
			self.x3.x = 160
			self.x3.y = 500 
			self.c3.x = 550
			self.c3.y = 500
			game.Counter1 = game.Counter1 +1
		elif pos.x< 750 and pos.x >350 and pos.y>400:
			self.c3.x = 550
			self.c3.y = 500
			game.Balls = game.Balls +1
			print game.Balls 
			game.Counter = game.Counter +1
		elif pos.x> 750 and pos.y>400:
			self.x3.x = 1000
			self.x3.y = 500
			self.c3.x = 550
			self.c3.y = 500
			game.Counter1 = game.Counter1 +1
	elif z_array[0] == 3 and self.c3.x<0:
		if pos.x < 350 and pos.y > 400:
			self.x3.x = 160
			self.x3.y = 500 
			self.c3.x = 1000 
			self.c3.y = 500
			game.Counter1 = game.Counter1 +1
		elif pos.x< 750 and pos.x >350 and pos.y>400:
			self.x3.x = 550
			self.x3.y = 500
			self.c3.x = 1000
			self.c3.y = 500
			game.Counter1 = game.Counter1 +1
		elif pos.x> 750 and pos.y>400:
			self.c3.x = 1000
			self.c3.y = 500
			game.Balls = game.Balls + 1
			print game.Balls 
			game.Counter = game.Counter +1
'''
		if pos.x > 
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
	
