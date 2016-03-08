import random
from random import choice
import pygame
from pygame.locals import QUIT, KEYDOWN, MOUSEMOTION
import time
"""
    Class containing game model and all its components
"""

class Brick(object):
    """ Represents a brick in our brick breaker game """
    def __init__(self, left, top, width, height, first):
        if first:
            self.left = left*width - width*9 #renders 9 extra columns of blocks off screen to the left
            self.top = top*height + height*2 #starts the world with a 2 block high sky
            self.width = width
            self.height = height
            random_seed = random.random()
            if random_seed < 0.1:
                self.color = "black"
            elif random_seed <0.9:
                self.color = "brown"    
            else:
                self.color = choice(["red", "green", "orange", "blue", "purple"])
        else:
            self.left = left 
            self.top = top*height + height*2  #starts the world with a 2 block high sky
            self.width = width
            self.height = height
            self.color = choice(["red", "green", "orange", "blue", "purple"])

class FuelStation(object):
    """ Represents a fuel station as a pink block at fixed point"""
    def __init__(self):
        self.left = 400
        self.top = 40
        self.width = 40
        self.height = 40

class Vehicle(object):
    """ Represents the paddle in our brick breaker game """
    def __init__(self, left, top, width, height):
        """ Initialize the paddle with the specified geometry """
        self.left = left
        self.top = top
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

      
        self.init_height_dist = 32
        self.init_width_dist = 34

        #initialize world
        for top in range(0,self.init_height_dist):
            self.world.append([])
            for left in range(0,self.init_width_dist):
                brick = Brick(left, top, self.BRICK_WIDTH, self.BRICK_HEIGHT, True)
                self.world[top].append(brick)
        self.temp_world = self.world        

        self.fuel = 5
        self.max_fuel = 10
    
        self.vehicle = Vehicle(40*8,40, 40, 40)
        self.fuel_station = FuelStation()

    def world_enlarger(self, what_side):
        

        if what_side == "left":
            pass
    

            # for top in range (len(self.world)):
      #         for left in range(0,5):
      #             brick = Brick(self.FAR_LEFT - self.BRICK_WIDTH*(left+1), top, self.BRICK_WIDTH, self.BRICK_HEIGHT, False)
      #             self.world[top].insert(0,brick)

      #     self.temp_world = self.world[:][0:34]
      #     self.FAR_LEFT = self.world[0][4].left #makes the threshold for creating more leftward blocks at 5 blocks from the leftmost column of blocks


        elif what_side == "right":
            pass
        
            # for top in range (len(self.world)):
      #         for right in range(0,5):
      #             brick = Brick(self.FAR_RIGHT + self.BRICK_WIDTH*(right+1), top, self.BRICK_WIDTH, self.BRICK_HEIGHT, False)
      #             self.world[top].append(brick)

      #     start_right = len(self.world[0]) - 34

      #     self.temp_world = self.world[:][start_right:-1]
      #     self.FAR_RIGHT = self.world[0][-5].left #makes the threshold for creating more rightward blocks at 5 blocks from the rightmost column of blocks
      #     print "new self.right ", self.FAR_RIGHT


        elif what_side == "down":
            pass

    def get_fuel(self):
        return self.fuel*1000 - pygame.time.get_ticks()

    def get_elapsed_time(self):
        return pygame.time.get_ticks()
