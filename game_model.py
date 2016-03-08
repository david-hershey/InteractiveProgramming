import random
from random import choice
import pygame
from pygame.locals import QUIT, KEYDOWN, MOUSEMOTION
import time
"""
    Class containing game model and all its components
"""

# class Brick(object):
#     """ Represents a brick in our brick breaker game """
#     def __init__(self, left, top, width, height, first):
#         if first:
#             self.left = left*width - width*9 #renders 9 extra columns of blocks off screen to the left
#             self.top = top*height + height*2  #starts the world with a 2 block high sky
#             self.width = width
#             self.height = height
#             random_seed = random.random()
#             if random_seed < 0.1:
#                 self.color = "black"
#             elif random_seed <0.9:
#                 self.color = "brown"    
#             else:
#                 self.color = choice(["red", "green", "orange", "blue", "purple"])
#         else:
#             self.left = left
#             self.top = top 
#             self.width = width
#             self.height = height
#             random_seed = random.random()
#             if random_seed < 0.1:
#                 self.color = "black"
#             elif random_seed <0.9:
#                 self.color = "brown"    
#             else:
#                 self.color = choice(["red", "green", "orange", "blue", "purple"])

class Brick(pygame.sprite.Sprite):

    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, left, top, width, height, first):
       # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

       # Create an image of the block, and fill it with a color.
       # This could also be an image loaded from the disk.
        self.image = pygame.Surface([width, height])
       

       # Fetch the rectangle object that has the dimensions of the image
       # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()
       
        if first:
            self.rect.x  = left*width - width*9 #renders 9 extra columns of blocks off screen to the left
            self.rect.y  = top*height + height*2  #starts the world with a 2 block high sky
            self.width = width
            self.height = height
            self.top =   top*height + height*2
            self.left =  left*width - width*9 
            random_seed = random.random()
            if random_seed < 0.1:
                self.color = "black"
            elif random_seed <0.9:
                self.color = "brown"    
            else:
                self.color = choice(["red", "green", "orange", "blue", "purple"])
            self.image.fill((0,220,255))
        else:
            self.rect.x = left
            self.rext.y = top
            self.top = left
            self.left =  top
            self.width = width
            self.height = height
            random_seed = random.random()
            if random_seed < 0.1:
                self.color = "black"
            elif random_seed <0.9:
                self.color = "brown"    
            else:
                self.color = choice(["red", "green", "orange", "blue", "purple"])
            self.image.fill((0,220,255))


# class FuelStation(object):
#     """ Represents a fuel station as a pink block at fixed point"""
#     def __init__(self):
#         self.left = 400
#         self.top = 40
#         self.width = 40
#         self.height = 40

class FuelStation(pygame.sprite.Sprite):

    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self):
       # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

       # Create an image of the block, and fill it with a color.
       # This could also be an image loaded from the disk.
        self.image = pygame.Surface([40, 40])

        self.left = 400
        self.top = 40
        self.width = 40
        self.height = 40
        self.image.fill((0,255,255))

       # Fetch the rectangle object that has the dimensions of the image
       # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 404



class Shop(object):
    """ Represents a shop where the vehicle can sell a mineral"""
    def __init__(self):
        self.left = 480
        self.top = 40
        self.width = 40
        self.height = 40

class Vehicle(pygame.sprite.Sprite):

    """ Represents the paddle in our brick breaker game """

    def __init__(self, left, top, width, height, cheatcode):
       # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

       # Create an image of the block, and fill it with a color.
       # This could also be an image loaded from the disk.
        self.image = pygame.Surface([width, height])
      

       # Fetch the rectangle object that has the dimensions of the image
       # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()

        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.thruster = False
        self.cheatcode = cheatcode
        self.speed = 0

        self.gravity = .1
        self.thruster_veloc = -.1
        
        self.rect.x = left
        self.rect.y = top
        self.image.fill((0,220,255))


class BrickBreakerModel(object):
    """ Stores the game state for our brick breaker game """
    def __init__(self):
       #self.bricks = [][]
        self.enlarger_helper = None
        self.can_move_down = False  #checks if the blocks free to fall downward
        self.world = [] 
        self.MARGIN = 0
        self.BRICK_WIDTH = 40
        self.BRICK_HEIGHT = 40
        self.SCREEN_WIDTH = 640
        self.SCREEN_HEIGHT = 480 
        self.FAR_LEFT = 320 
        self.FAR_RIGHT = 320
        self.FAR_BOTTOM = self.SCREEN_HEIGHT + self.BRICK_HEIGHT*4 #the threshold for adding more blocks is 5 blocks from the bottom of the screen

      
        self.init_height_dist = 34 #number of rows of blocks
        self.init_width_dist = 32 #number of columns of blocks

        #initialize world
        for top in range(0,self.init_height_dist):
            self.world.append([])
            for left in range(0,self.init_width_dist):
                brick = Brick(left, top, self.BRICK_WIDTH, self.BRICK_HEIGHT, True)
                self.world[top].append(brick)
        self.temp_world = self.world        

        self.fuel = 500
        self.max_fuel = 1000

        #counter for minerals
        self.red_block = 0
        self.green_block = 0
        self.orange_block = 0    
        self.blue_block = 0
        self.purple_block = 0
        
        self.money = 0 
       
        cheatcode = "dpapp"
        self.vehicle = Vehicle(40*8,40, 40, 40, cheatcode)
        self.fuel_station = FuelStation()
        self.shop = Shop()

    def world_enlarger(self, what_side):
        
        if what_side == "left":
            pass

        elif what_side == "right":
            pass

        elif what_side == "down":
          
            for top in range(0,5): # cycles through 5 blocks 
                self.world.append([]) #creates a row (list) to be filled with bricks
                for left in range(0,self.init_width_dist):


                    brick = Brick(self.world[0][0].left+left*self.BRICK_WIDTH, self.world[-2][0].top + self.BRICK_HEIGHT, self.BRICK_WIDTH, self.BRICK_HEIGHT, False)
                    self.world[-1].append(brick)

    def get_elapsed_time(self):
        return pygame.time.get_ticks()
