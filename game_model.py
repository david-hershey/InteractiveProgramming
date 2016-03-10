import random
from random import choice
import pygame
from pygame.locals import QUIT, KEYDOWN, MOUSEMOTION
import time
"""
    Class containing game model and all its components
"""


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
            self.rect.y  = top*height + height*2 - 1 #starts the world with a 2 block high sky
            self.width = width 
            self.height = height
            self.top =   top*height + height*2 -1 
            self.left =  left*width - width*9 
            random_seed = random.random()
            if random_seed < 0.1:
                self.color = "black"
                self.brick_type = "empty"
            elif random_seed <0.9:
                self.color = "brown"
                self.brick_type = "soil" 
            else:
                self.color = "brown"
                self.brick_type = choice(["ruby", "emerald", "amazonite", "sapphire", "watsonite"])
            if self.brick_type == "ruby":
                self.image = pygame.image.load('ruby.png').convert()
                self.image.set_colorkey((255,255,255))
            elif self.brick_type == "emerald":
                self.image = pygame.image.load('emerald.png').convert()
                self.image.set_colorkey((0,0,0))
            elif self.brick_type == "amazonite":
                self.image = pygame.image.load('amazonite.png').convert()
                self.image.set_colorkey((0,0,0))
            elif self.brick_type == "sapphire":
                self.image = pygame.image.load('sapphire.png').convert()
                self.image.set_colorkey((0,0,0))
            elif self.brick_type == "watsonite":
                self.image = pygame.image.load('watsonite.png').convert()
                self.image.set_colorkey((255,255,255))
            #self.image.fill((0,220,255))
        else:
            self.rect.x = left
            self.rect.y = top
            self.top = top
            self.left =  left
            self.width = width
            self.height = height
            random_seed = random.random()
            if random_seed < 0.1:
                self.color = "black"
                self.brick_type = "empty"
            elif random_seed <0.9:
                self.color = "brown"   
                self.brick_type = "soil" 
            else:
                self.color = "brown"
                self.brick_type = choice(["ruby", "emerald", "amazonite", "sapphire", "watsonite"])
            if self.brick_type == "ruby":
                self.image = pygame.image.load('ruby.png').convert()
                self.image.set_colorkey((255,255,255))
            elif self.brick_type == "emerald":
                self.image = pygame.image.load('emerald.png').convert()
                self.image.set_colorkey((0,0,0))
            elif self.brick_type == "amazonite":
                self.image = pygame.image.load('amazonite.png').convert()
                self.image.set_colorkey((0,0,0))
            elif self.brick_type == "sapphire":
                self.image = pygame.image.load('sapphire.png').convert()
                self.image.set_colorkey((0,0,0))
            elif self.brick_type == "watsonite":
                self.image = pygame.image.load('watsonite.png').convert()
                self.image.set_colorkey((255,255,255))
            #self.image.fill((0,220,255))


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
        self.image = pygame.image.load('fuel_station.gif').convert()

        self.left = 400
        self.top = 40
        self.width = 40
        self.height = 40
        #self.image.fill((0,255,255))

       # Fetch the rectangle object that has the dimensions of the image
       # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 40





class Shop(pygame.sprite.Sprite):

    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self):
       # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

       # Create an image of the block, and fill it with a color.
       # This could also be an image loaded from the disk.
        self.image = pygame.image.load('store.jpg').convert()
        self.rect = self.image.get_rect()

        self.left = 480
        self.top = 40
        self.width = 40
        self.height = 40
        self.rect.x = 480
        self.rect.y = 40

       # Fetch the rectangle object that has the dimensions of the image
       # Update the position of this object by setting the values of rect.x and rect.y
        

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
        self.can_drill_left = False
        self.can_drill_right = False
        self.can_drill_down = False

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
        self.can_move_down = True  #checks if the blocks free to fall downward
        self.world = [] 
        self.MARGIN = 0
        self.BRICK_WIDTH = 40
        self.BRICK_HEIGHT = 40
        self.SCREEN_WIDTH = 640
        self.SCREEN_HEIGHT = 480 
        self.FAR_LEFT = 320 
        self.FAR_RIGHT = 320
        self.FAR_BOTTOM = self.SCREEN_HEIGHT + self.BRICK_HEIGHT*4 #the threshold for adding more blocks is 5 blocks from the bottom of the screen

      
        self.init_height_dist = 32 #number of rows of blocks
        self.init_width_dist = 34 #number of columns of blocks

        self.sprite_list = pygame.sprite.Group() #a list of sprites to be drawn
        #initialize world
        for top in range(0,self.init_height_dist):
            self.world.append([])
            for left in range(0,self.init_width_dist):
                brick = Brick(left, top, self.BRICK_WIDTH, self.BRICK_HEIGHT, True)
                self.world[top].append(brick)
                if brick.brick_type != "empty" and brick.brick_type != "soil":
                    self.sprite_list.add(brick)
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
        self.vehicle = Vehicle(40*8,30, 30, 30, cheatcode)

        self.fuel_station = FuelStation()
        self.sprite_list.add(self.fuel_station)
        self.shop = Shop()
        self.sprite_list.add(self.shop)

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
                    if brick.brick_type != "soil" and brick.brick_type != "empty":
                        self.sprite_list.add(brick)

    def get_elapsed_time(self):
        return pygame.time.get_ticks()
