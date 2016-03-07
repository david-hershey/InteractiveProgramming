import pygame
from pygame.locals import QUIT, KEYDOWN, MOUSEMOTION
import time
from random import choice

class PygameBrickBreakerView(object):
    """ Visualizes a brick breaker game in a pygame window """
    def __init__(self, model, screen):
        """ Initialize the view with the specified model
            and screen. """
        self.model = model
        self.screen = screen


    def draw(self):
        """ Draw the game state to the screen """
        self.screen.fill(pygame.Color('black'))
        # draw the bricks to the screen
        for top in range(len(self.model.temp_world)):
        	for left in range(len(self.model.temp_world[top])):

        		#pulls the appropriate brick model from the list
        		brick = self.model.temp_world[top][left]

        		r = pygame.Rect(brick.left, brick.top, brick.width, brick.height)
           		pygame.draw.rect(self.screen, pygame.Color(brick.color), r)

        
        r = pygame.Rect(40*8,40,40,40) #the mining vehicle
                     
        pygame.draw.rect(self.screen, pygame.Color('white'), r)
       
        pygame.display.update()




class Brick(object):
    """ Represents a brick in our brick breaker game """
    def __init__(self, left, top, width, height, first):
	    if first:
	        self.left = left*width - width*9 #renders 9 extra columns of blocks off screen to the left
	        self.top = top*height + height*2 #starts the world with a 2 block high sky
	        self.width = width
	        self.height = height
	        self.color = choice(["red", "green", "orange", "blue", "purple"])
	    else:
	    	self.left = left 
	        self.top = top*height + height*2  #starts the world with a 2 block high sky
	        self.width = width
	        self.height = height
	        self.color = choice(["red", "green", "orange", "blue", "purple"])


class Vehicle(object):
    """ Represents the paddle in our brick breaker game """
    def __init__(self, left, top, width, height):
        """ Initialize the paddle with the specified geometry """
        self.left = left*width
        self.top = top*height + height*4
        self.width = width
        self.height = height

class BrickBreakerModel(object):
    """ Stores the game state for our brick breaker game """
    def __init__(self):
       #self.bricks = [][]
        self.world = []	
        self.MARGIN = 0
        self.BRICK_WIDTH = 40
        self.BRICK_HEIGHT = 40
        self.SCREEN_WIDTH = 640
        self.SCREEN_HEIGHT = 480 
        self.FAR_LEFT = 320 
        self.FAR_RIGHT = 320
        self.FAR_BOTTOM = -680

      
        self.init_height_dist = 34
        self.init_width_dist = 34

        #initialize world
        for top in range(0,self.init_height_dist):
        	self.world.append([])
        	for left in range(0,self.init_width_dist):
        		brick = Brick(left, top, self.BRICK_WIDTH, self.BRICK_HEIGHT, True)
        		self.world[top].append(brick)
        self.temp_world = self.world		


        #self.vehicle = Vehicle(0,0, 40, 40)

    def world_enlarger(self, what_side):
    	

    	if what_side == "left":
    		pass
    		
    		# for top in range (len(self.world)):
      #   		for left in range(0,5):
      #   			brick = Brick(self.FAR_LEFT - self.BRICK_WIDTH*(left+1), top, self.BRICK_WIDTH, self.BRICK_HEIGHT, False)
      #   			self.world[top].insert(0,brick)

      #   	self.temp_world = self.world[:][0:34]
      #   	self.FAR_LEFT = self.world[0][4].left #makes the threshold for creating more leftward blocks at 5 blocks from the leftmost column of blocks


    	elif what_side == "right":
    		pass
    	
    		# for top in range (len(self.world)):
      #   		for right in range(0,5):
      #   			brick = Brick(self.FAR_RIGHT + self.BRICK_WIDTH*(right+1), top, self.BRICK_WIDTH, self.BRICK_HEIGHT, False)
      #   			self.world[top].append(brick)

      #   	start_right = len(self.world[0]) - 34

      #   	self.temp_world = self.world[:][start_right:-1]
      #   	self.FAR_RIGHT = self.world[0][-5].left #makes the threshold for creating more rightward blocks at 5 blocks from the rightmost column of blocks
      #   	print "new self.right ", self.FAR_RIGHT


        elif what_side == "down":
        	for top in range (len(self.world)):
    			for right in range(0,5):
        			brick = Brick(self.FAR_RIGHT + self.BRICK_WIDTH*(right+1), top, self.BRICK_WIDTH, self.BRICK_HEIGHT, False)
        			self.world[top].append(brick)
        	start_right = len(self.world[0]) - 34

        	self.temp_world = self.world[:][start_right:-1]
        	self.FAR_RIGHT = self.world[0][-5].left #makes the threshold for creating more rightward blocks at 5 blocks from the rightmost column of blocks
        	print "new self.right ", self.FAR_RIGHT


class PyGameKeyboardController(object):
    def __init__(self, model):
        self.model = model

    def handle_event(self, event):
        """ Look for left and right keypresses to
            modify the x position of the paddle """
        if event.type != KEYDOWN:
            return

        if event.key == pygame.K_UP:
        	for top in range(len(self.model.temp_world)):
        		for left in range(len(self.model.temp_world[top])):
        			brick = self.model.temp_world[top][left]
        			brick.top += brick.height
        #	if self.model.bricks[0][0].top	

        

        if event.key == pygame.K_DOWN:
        	for top in range(len(self.model.temp_world)):
        		for left in range(len(self.model.temp_world[top])):
        			brick = self.model.temp_world[top][left]
        			brick.top -= brick.height
        print self.model.temp_world[0][0].top

           

        if event.key == pygame.K_LEFT:
	        if self.model.temp_world[0][0].left != self.model.FAR_LEFT: 
	        	

	        	for top in range(len(self.model.temp_world)):
	        		for left in range(len(self.model.temp_world[top])):
	        			brick = self.model.temp_world[top][left]
	        			brick.left += brick.width
	        else:
	        	return

        	#if farthest block to left reachest threshold, add more blocks to left
        	if self.model.temp_world[0][0].left == self.model.FAR_LEFT: 
        		self.model.world_enlarger("left")

        	# print "left, ", self.model.temp_world[0][0].left	
        	# print "right, ", self.model.temp_world[0][-1].left	

        	

        if event.key == pygame.K_RIGHT:
        	if self.model.world[0][-1].left != self.model.FAR_RIGHT: 
	        	for top in range(len(self.model.temp_world)):
	        		for left in range(len(self.model.temp_world[top])):
	        			brick = self.model.temp_world[top][left]
	        			brick.left -= brick.width
	        else:
	        	return
        	if self.model.world[0][-1].left == self.model.FAR_RIGHT: 
        		self.model.world_enlarger("right")

        	# print "left, ", self.model.temp_world[0][0].left	
        	# print "right, ", self.model.temp_world[0][-1].left	
        


class PyGameMouseController(object):
    def __init__(self, model):
        self.model = model

    def handle_event(self, event):
        """ Look for mouse movements and respond appropriately """
        if event.type != MOUSEMOTION:
            return
        self.model.paddle.left = event.pos[0]

if __name__ == '__main__':
    pygame.init()
    size = (640, 480)
    screen = pygame.display.set_mode(size)

    model = BrickBreakerModel()
    view = PygameBrickBreakerView(model, screen)
    controller = PyGameKeyboardController(model)
    #controller = PyGameMouseController(model)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            controller.handle_event(event)
        view.draw()
        time.sleep(.001)