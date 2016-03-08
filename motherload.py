import pygame
from pygame.locals import QUIT, KEYDOWN, MOUSEMOTION
import time
from random import choice
import random
import game_model

class PygameBrickBreakerView(object):
    """ Visualizes a brick breaker game in a pygame window """
    def __init__(self, model, screen):
        """ Initialize the view with the specified model
            and screen. """
        self.model = model
        self.screen = screen


    def draw(self):
        """ Draw the game state to the screen """
        myFont = pygame.font.SysFont("monospace",15)
        game_over_font = pygame.font.SysFont("monospace",100)
    
        self.screen.fill(pygame.Color('black'))
        # draw the bricks to the screen
        for top in range(len(self.model.temp_world)):
            for left in range(len(self.model.temp_world[top])):

                #pulls the appropriate brick model from the list
                brick = self.model.temp_world[top][left]

                r = pygame.Rect(brick.left, brick.top, brick.width, brick.height)
               
               
                if brick.left == self.model.vehicle.left and brick.top <= self.model.vehicle.top + brick.height and brick.top + brick.height > self.model.vehicle.top + brick.height:  #checks if the vehicle overlaps a block, if so change block to black
                    if brick.color != "black":
                        model.can_move_down = False
                    else:
                    	model.can_move_down = True

                if brick.left == self.model.vehicle.left and self.model.vehicle.top > brick.top and self.model.vehicle.top + brick.height < brick.top + brick.height*2: #checks if the vehicle overlaps a block, if so change block to black
                    if brick.color != "black" and brick.color != "brown":
                        print "I am eating ...", brick.color

                    brick.color = "black"
                    pygame.draw.rect(self.screen, pygame.Color(brick.color), r)

                else:
                    pygame.draw.rect(self.screen, pygame.Color(brick.color), r)
                    
        
        r = pygame.Rect(self.model.vehicle.left,self.model.vehicle.top,self.model.vehicle.width,self.model.vehicle.height) #the mining vehicle
                     
        pygame.draw.rect(self.screen, pygame.Color('white'), r)

        r = pygame.Rect(self.model.fuel_station.left,self.model.fuel_station.top,self.model.fuel_station.width,self.model.fuel_station.height)
        pygame.draw.rect(self.screen, pygame.Color('deep pink'),r) 

        if self.model.fuel_station.left == self.model.vehicle.left and self.model.fuel_station.top == self.model.vehicle.top and self.model.get_fuel < self.model.max_fuel:
            self.model.fuel += 5
 
        # if self.model.get_fuel() <= 0:
        #  #   msg = game_over_font.render("GAME OVER",1,(255,255,0))
        #     #screen.blit(msg, (0, 240))
        # else:
        #     timer = myFont.render(str(self.model.get_fuel()), 1, (255,255,0))
        #     screen.blit(timer, (20,20))
        pygame.display.update()




class PyGameKeyboardController(object):
    def __init__(self, model):
        self.model = model

    def handle_event(self, event):
        """ Look for left and right keypresses to
            modify the x position of the paddle """
        if event.type != KEYDOWN:
            return

        # if event.key == pygame.K_UP:
        #     for top in range(len(self.model.temp_world)):
        #         for left in range(len(self.model.temp_world[top])):
        #             brick = self.model.temp_world[top][left]
        #             brick.top += brick.height*2
        # #   if self.model.bricks[0][0].top  
        #     self.model.fuel_station.top += self.model.BRICK_HEIGHT
        

        # if event.key == pygame.K_DOWN:
        # 	print self.model.temp_world[-1][0].top
        # 	if self.model.temp_world[-1][0].top != self.model.FAR_BOTTOM: 
	       #      for top in range(len(self.model.temp_world)):
	       #          for left in range(len(self.model.temp_world[top])):
	       #              brick = self.model.temp_world[top][left]
	       #              brick.top -= brick.height
	       #      self.model.fuel_station.top -= self.model.BRICK_HEIGHT
	       #  else:
	       #      self.model.fuel_station.top -= self.model.BRICK_HEIGHT
	       #      self.model.world_enlarger("down")
	       #      for top in range(len(self.model.temp_world)):
	       #          for left in range(len(self.model.temp_world[top])):
	       #              brick = self.model.temp_world[top][left]
	       #              brick.top -= brick.height
        # #print self.model.temp_world[0][0].top

           

       #checking pressed keys
      

        if event.key == pygame.K_LEFT:
            if self.model.temp_world[0][0].left != self.model.FAR_LEFT: 
                

                for top in range(len(self.model.temp_world)):
                    for left in range(len(self.model.temp_world[top])):
                        brick = self.model.temp_world[top][left]
                        brick.left += brick.width
                self.model.fuel_station.left += self.model.BRICK_HEIGHT
            else:
                return

            #if farthest block to left reachest threshold, add more blocks to left
            if self.model.temp_world[0][0].left == self.model.FAR_LEFT: 
                self.model.world_enlarger("left")
            

        if event.key == pygame.K_RIGHT:
            if self.model.world[0][-1].left != self.model.FAR_RIGHT: 
                for top in range(len(self.model.temp_world)):
                    for left in range(len(self.model.temp_world[top])):
                        brick = self.model.temp_world[top][left]
                        brick.left -= brick.width
                self.model.fuel_station.left -= self.model.BRICK_HEIGHT
            else:
                return
            if self.model.world[0][-1].left == self.model.FAR_RIGHT: 
                self.model.world_enlarger("right")



class PyGameMouseController(object):
    def __init__(self, model):
        self.model = model

    def handle_event(self, event):
        """ Look for mouse movements and respond appropriately """
        if event.type != MOUSEMOTION:
            return
        self.model.paddle.left = event.pos[0]

clock = pygame.time.Clock()

if __name__ == '__main__':
    
  
  
    speed = 0;
    gravity = 0.1;
    thruster = -0.1
    pygame.init()
    size = (640, 480)
    screen = pygame.display.set_mode(size)
    model = game_model.BrickBreakerModel()
    view = PygameBrickBreakerView(model, screen)
    controller = PyGameKeyboardController(model)
    #controller = PyGameMouseController(model)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            controller.handle_event(event)

        if model.temp_world[-1][0].top >= model.FAR_BOTTOM and model.temp_world[-1][0].top < model.FAR_BOTTOM + 40: 
        	mistake = model.FAR_BOTTOM - model.temp_world[-1][0].top
        	print "enlarging world"
        	model.world_enlarger("down")


        keys = pygame.key.get_pressed()  
    	if keys[pygame.K_UP]:
    		for top in range(len(model.temp_world)):
	            for left in range(len(model.temp_world[top])):
	                    brick = model.temp_world[top][left]
	                    brick.top -= speed
	        model.fuel_station.top -= speed

	        speed = speed + thruster;	

	        if speed > 1:
	            speed = 0

        elif keys[pygame.K_DOWN] and not model.can_move_down:
        #	print "juss drilling"
	    	speed = .7
	    	for top in range(len(model.temp_world)):
	            for left in range(len(model.temp_world[top])):
	                    brick = model.temp_world[top][left]
	                    brick.top -= speed
	        model.fuel_station.top -= speed

    	elif model.can_move_down:    
	        for top in range(len(model.temp_world)):
	            for left in range(len(model.temp_world[top])):
	                    brick = model.temp_world[top][left]
	                    brick.top -= speed
	        model.fuel_station.top -= speed
	        speed = speed + gravity
	        if speed > 5:
	        	speed = 5
        if not model.can_move_down and event.type != KEYDOWN:
        	speed = 0

	   	

        view.draw()
     #   clock.tick(500000000)
