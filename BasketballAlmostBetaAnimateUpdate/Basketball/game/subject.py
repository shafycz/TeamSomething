import spyral
import random
import math
from spyral import Animation, easing
import time
import test
import game
import question
WIDTH = 1200
HEIGHT = 900
BG_COLOR = (0,0,0)
WHITE = (255, 255, 255)
SIZE = (WIDTH, HEIGHT)




class Subject(spyral.Scene):
    def __init__(self, *args, **kwargs):
        global manager
        spyral.Scene.__init__(self, SIZE)
  	self.background = spyral.Image(filename= "game/colors/subjectB.png")
	spyral.event.register('input.keyboard.down.q', spyral.director.quit)

        spyral.event.register("system.quit", spyral.director.quit)
	spyral.event.register("input.mouse.down.left", self.handle_clicked)
    
    def handle_clicked(self, pos):
	spyral.director.replace(question.Question())
