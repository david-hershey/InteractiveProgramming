import pygame, os, sys
from pygame.locals import *
import time
from random import choice
import random
import game_model
import pygame, os, sys
import math 


class GameViewer(object):
    """ Visualizes the game world defined by the brick objects, vehicle, shop, workshop and fuel station"""
    def __init__(self, model, screen):
        """ Initialize the view with the specified model
            and screen. """
        self.model = model
        self.screen = screen
        self.running = True


    def draw(self):
        """ Draws the game state to the screen """

        myFont = pygame.font.SysFont("monospace",15)
        game_over_font = pygame.font.SysFont("monospace",100)
    
        self.screen.fill(pygame.Color('black'))

        # draw the block to the screen
        for top in range(len(self.model.temp_world)):
            for left in range(len(self.model.temp_world[top])):

                #pulls the appropriate block model from the list
                brick = self.model.temp_world[top][left]

                #if there are bricks surrounding the current block, then continue 
                if not (left == 0 or top == 0 or top == len(self.model.temp_world) -1 or left == len(self.model.temp_world[0])-1) and pygame.sprite.collide_rect(brick,self.model.vehicle):

                    #define the 8 surrounding bricks
                    brick_left = self.model.temp_world[top][left-1]
                    brick_top_left =  self.model.temp_world[top-1][left-1]
                    brick_top_right = self.model.temp_world[top-1][left+1]
                    brick_bottom_left = self.model.temp_world[top+1][left-1]
                    brick_bottom_right = self.model.temp_world[top+1][left+1]
                    brick_right = self.model.temp_world[top][left+1]
                    brick_bottom = self.model.temp_world[top+1][left]
                    brick_top = self.model.temp_world[top-1][left]
                      
                    #predefines collision which the surrounding blocks as True  
                    t = True
                    tl = True
                    tr = True

                    l = True
                    r = True

                    bl = True
                    b = True
                    br = True

                    #checks collision with each surround block, and if touching, sets the collision variable to True, else false 
                    if pygame.sprite.collide_rect(brick,self.model.vehicle):

                        if pygame.sprite.collide_rect(self.model.vehicle,brick_left):  #checks collision with left brick
                            l = True
                        elif not pygame.sprite.collide_rect(self.model.vehicle,brick_left):
                            l = False

                        if pygame.sprite.collide_rect(self.model.vehicle,brick_right): #checks collision with right 
                            r = True
                        elif not pygame.sprite.collide_rect(self.model.vehicle,brick_right):
                            r = False
                        
                        if pygame.sprite.collide_rect(self.model.vehicle,brick_top):  #checks collision with top
                            t = True
                        elif not pygame.sprite.collide_rect(self.model.vehicle,brick_top):
                            t = False
                        
                        if pygame.sprite.collide_rect(self.model.vehicle,brick_bottom): #checks collision with bottom
                            b = True
                        elif not pygame.sprite.collide_rect(self.model.vehicle,brick_bottom):
                            b = False
                        
                        if pygame.sprite.collide_rect(self.model.vehicle,brick_bottom_left): #checks collision with bottom left
                            bl = True
                        elif not pygame.sprite.collide_rect(self.model.vehicle,brick_bottom_left):
                            bl = False
                        
                        if pygame.sprite.collide_rect(self.model.vehicle,brick_bottom_right): #checks collision with bottom right
                            br = True
                        elif not pygame.sprite.collide_rect(self.model.vehicle,brick_bottom_right):
                            br = False
                        
                        if pygame.sprite.collide_rect(self.model.vehicle,brick_top_left): #checks collision with top left
                            tl = True
                        elif not pygame.sprite.collide_rect(self.model.vehicle,brick_top_left):
                            tl = False
                        
                        if pygame.sprite.collide_rect(self.model.vehicle,brick_top_right):  #checks collision with top right
                            tr = True
                        elif not pygame.sprite.collide_rect(self.model.vehicle,brick_top_right):
                            tr = False

              

                        #checks if there are blocks above, and if so, dissallow the user from traveling upwards
                        if t and not tl and not tr:
                      
                            if brick_top.color == "black":
                                self.model.vehicle.can_move_up = True
                            else:
                                self.model.vehicle.can_move_up = False
                        elif (tl and t):
                            if brick_top.color == "black" and brick_top_left.color == "black":
                                self.model.vehicle.can_move_up = True
                            else:
                                self.model.vehicle.can_move_up = False
                        elif (t and tr):
                            if brick_top.color == "black" and brick_top_right.color == "black":
                                self.model.vehicle.can_move_up = True
                            else:
                                self.model.vehicle.can_move_up = False
                        else:
                            self.model.vehicle.can_move_up = True

                        #checks if there are blocks below, if not, allow for free fall 
                        if b and not bl and not br:
                            if brick_bottom.color == "black":
                                self.model.can_move_down = True
                            else:
                                self.model.can_move_down = False
                        elif b and bl:
                            if brick_bottom.color == "black" and brick_bottom_left == "black":
                                self.model.can_move_down = True
                            else:
                                self.model.can_move_down = False
                        elif b and br:
                            if brick_bottom.color == "black" and brick_bottom_right.color == "black":
                                self.model.can_move_down = True
                            else:
                                self.model.can_move_down = False
                        elif brick.color == "black" and not b and not bl and not br:
                            self.model.can_move_down = True
                
                        #checks if there are bricks touching to the left and bottom, if so turn on drilling 
                        if l and bl:
                            if brick_left.color == "black":
                                self.model.vehicle.can_move_left = True
                            else:
                                self.model.vehicle.can_move_left = False

                        if r and br:
                            if brick_right.color == "black":
                                self.model.vehicle.can_move_right = True
                            else:
                                self.model.vehicle.can_move_right = False

                        #checks for drilling to the right, True if there are blocks to the right 
                        if l and b and not self.model.can_move_down:
                            if brick_left.color != "black" and brick_bottom.color != "black":
                             
                                self.model.vehicle.can_drill_left = True
                            else:
                                self.model.vehicle.can_drill_left = False

                        if r and b and not self.model.can_move_down:
                            if brick_right.color != "black" and brick_bottom.color != "black":
                                self.model.vehicle.can_drill_right = True
                            else:
                                self.model.vehicle.can_drill_right = False

                        if b:
                            if brick_bottom.color != "black":
                                self.model.vehicle.can_drill_down = True
                            else:
                                self.model.vehicle.can_drill_down = False                        
                

                r = pygame.Rect(brick.left, brick.top, brick.width, brick.height)
             
                #checks if player has mined a mineral, if so increments the mineral count 
                if not (top == 0 or top ==1):
                    if math.fabs(brick.left - self.model.vehicle.left) < 20 and math.fabs(self.model.vehicle.top - brick.top)<20: #checks if the vehicle overlaps a block, if so change block to black (empty)
                        if brick.brick_type == "ruby":
                            self.model.red_block += 1
                            self.model.score += 100
                            brick.image.fill((0,0,0))
                            brick.image.set_colorkey((0,0,0))
                        elif brick.brick_type == "emerald":
                            self.model.green_block += 1
                            self.model.score += 100
                            brick.image.fill((0,0,0))
                            brick.image.set_colorkey((0,0,0))
                        elif brick.brick_type == "amazonite":
                            self.model.orange_block += 1
                            self.model.score += 100
                            brick.image.fill((0,0,0))
                            brick.image.set_colorkey((0,0,0))
                        elif brick.brick_type == "sapphire":
                            self.model.blue_block += 1
                            self.model.score += 100
                            brick.image.fill((0,0,0))
                            brick.image.set_colorkey((0,0,0))
                        elif brick.brick_type == "watsonite":
                            self.model.purple_block += 1
                            self.model.score += 100
                            brick.image.fill((0,0,0))
                            brick.image.set_colorkey((0,0,0))

                        brick.color = "black"
                        brick.brick_type = "empty"
                        pygame.draw.rect(self.screen, pygame.Color(brick.color), r)

                    else:
                        pygame.draw.rect(self.screen, pygame.Color(brick.color), r)
                
                    
      
        r = pygame.Rect(self.model.vehicle.left,self.model.vehicle.top,self.model.vehicle.width,self.model.vehicle.height) #the mining vehicle
                     
        pygame.draw.rect(self.screen, pygame.Color('white'), r) 

        r = pygame.Rect(self.model.fuel_station.left,self.model.fuel_station.top,self.model.fuel_station.width,self.model.fuel_station.height) #defines fuel station

        pygame.draw.rect(self.screen, pygame.Color('deep pink'),r) 

        self.model.sprite_list.draw(self.screen)

        r = pygame.Rect(self.model.shop.left,self.model.shop.top,self.model.shop.width,self.model.shop.height) #defines the shop

        #Vehicle visiting fuel station
        if pygame.sprite.collide_rect(self.model.fuel_station, self.model.vehicle): #checks collision with fuel station
            self.model.fuel = self.model.max_fuel

        #Vehicle visiting shop
        if pygame.sprite.collide_rect(self.model.shop, self.model.vehicle):
            self.model.money += 100 * self.model.red_block
            self.model.money += 100 * self.model.green_block
            self.model.money += 100 * self.model.orange_block
            self.model.money += 100 * self.model.blue_block
            self.model.money += 100 * self.model.purple_block
            self.model.red_block = 0
            self.model.green_block = 0
            self.model.orange_block = 0
            self.model.blue_block = 0
            self.model.purple_block = 0
     
        #Vehicle visiting workshop
        if pygame.sprite.collide_rect(self.model.workshop, self.model.vehicle):
            if self.model.money >= 500:
                self.model.money -= 500
                self.model.max_fuel += 500

        #ends game if player runs out of fuels
        if self.model.fuel <= 0:
            msg = game_over_font.render("GAME OVER",1,(255,255,0))
            screen.blit(msg, (0, 240))
        else:
            timer = myFont.render(str(self.model.fuel), 1, (255,255,0))
            screen.blit(timer, (20,20))

        #increments minterals based on drilling
        red_counter = myFont.render("Red: " + str(self.model.red_block), 1, (255,255,0))
        screen.blit(red_counter,(540,20))
        
        green_counter = myFont.render("Green: " + str(self.model.green_block), 1, (255,255,0))
        screen.blit(green_counter,(540,40))

        orange_counter = myFont.render("Orange: " + str(self.model.orange_block), 1, (255,255,0))
        screen.blit(orange_counter,(540,60))
        
        blue_counter = myFont.render("Blue: " + str(self.model.blue_block), 1, (255,255,0))
        screen.blit(blue_counter,(540,80))
        
        purple_counter = myFont.render("Purplpe: " + str(self.model.purple_block), 1, (255,255,0))
        screen.blit(purple_counter,(540,100))

        money_counter = myFont.render("Money: " + str(self.model.money), 1, (255,255, 0))
        screen.blit(money_counter, (540,120))

        score_counter = myFont.render("Score: " + str(self.model.score), 1, (255,255, 0))
        screen.blit(score_counter, (540,140))

        pygame.display.update()



class KeyboardController(object):
    def __init__(self, model,view):
        self.model = model
        self.view = view

    def handle_event(self):
        """
        handles any keyboard input
        """

        pygame.init()

        while self.view.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.view.running = False

            if model.fuel < 0:
                self.view.running = False

            
              #checks if the world should enlarge
            if self.model.temp_world[-1][0].top >= self.model.FAR_BOTTOM and self.model.temp_world[-1][0].top < self.model.FAR_BOTTOM + 40: 
                mistake = self.model.FAR_BOTTOM - self.model.temp_world[-1][0].top
                self.model.world_enlarger("down")


            #checks for key press
            keys = pygame.key.get_pressed()


            if keys[pygame.K_UP] and self.model.vehicle.can_move_up:

                for top in range(len(self.model.temp_world)):
                    for left in range(len(self.model.temp_world[top])):
                            brick = self.model.temp_world[top][left]
                            brick.top -= self.model.vehicle.speed_y
                            brick.rect.y = brick.top

                self.model.fuel_station.top -= self.model.vehicle.speed_y
                self.model.fuel_station.rect.y = self.model.fuel_station.top
                self.model.shop.top -= self.model.vehicle.speed_y
                self.model.shop.rect.y = self.model.shop.top
                self.model.workshop.top -= self.model.vehicle.speed_y
                self.model.workshop.rect.y = self.model.workshop.top

                self.model.vehicle.speed_y = self.model.vehicle.speed_y + self.model.vehicle.thruster;   

                if self.model.vehicle.speed_y  > 1:
                    self.model.vehicle.speed_y  = 0
                elif self.model.vehicle.speed_y  > 10:
                    self.model.vehicle.speed_y  = 10
            elif keys[pygame.K_UP] and not model.vehicle.can_move_up:
                self.model.vehicle.speed_y  = 0



            if keys[pygame.K_LEFT] and not self.model.vehicle.can_drill_left and not self.model.vehicle.can_move_left:
                pass
            elif keys[pygame.K_LEFT] and self.model.vehicle.can_drill_left:
                speed_x = .7
                #loops through the game model and moves all the blocks appropriately based off of key press
                for top in range(len(self.model.temp_world)):
                    for left in range(len(self.model.temp_world[top])):
                        brick = self.model.temp_world[top][left]
                        brick.left += self.model.vehicle.speed_x
                        brick.rect.x = brick.left
                #moves all game objects appropriately bassed off of key presses
                self.model.fuel_station.left += self.model.vehicle.speed_x
                self.model.fuel_station.rect.x = self.model.fuel_station.left
                self.model.shop.left += self.model.vehicle.speed_x
                self.model.shop.rect.x = self.model.shop.left
                self.model.workshop.left += self.model.vehicle.speed_x
                self.model.workshop.rect.x = self.model.workshop.left

            elif keys[pygame.K_LEFT] and self.model.vehicle.can_move_left:
                speed_x = 2
                for top in range(len(self.model.temp_world)):
                    for left in range(len(self.model.temp_world[top])):
                        brick = self.model.temp_world[top][left]
                        brick.left += self.model.vehicle.speed_x
                        brick.rect.x = brick.left
                self.model.fuel_station.left += self.model.vehicle.speed_x
                self.model.fuel_station.rect.x = self.model.fuel_station.left
                self.model.shop.left += self.model.vehicle.speed_x
                self.model.shop.rect.x = self.model.shop.left
                self.model.workshop.left += self.model.vehicle.speed_x
                self.model.workshop.rect.x = self.model.workshop.left

                self.model.vehicle.speed_x = self.model.vehicle.speed_x + self.model.vehicle.thruster_x;   

                if self.model.vehicle.speed_x > 1:
                    self.model.vehicle.speed_x = 0
                elif self.model.vehicle.speed_x > 10:
                    self.model.vehicle.speed_x = 10

            if keys[pygame.K_RIGHT] and self.model.vehicle.can_drill_right:
                    
                speed_x = .7
                for top in range(len(self.model.temp_world)):
                    for left in range(len(self.model.temp_world[top])):
                        brick = self.model.temp_world[top][left]
                        brick.left -= self.model.vehicle.speed_x
                        brick.rect.x = brick.left
                self.model.fuel_station.left -= self.model.vehicle.speed_x
                self.model.fuel_station.rect.x = self.model.fuel_station.left
                self.model.shop.left -= self.model.vehicle.speed_x
                self.model.shop.rect.x = self.model.shop.left
                self.model.workshop.left -= self.model.vehicle.speed_x
                self.model.workshop.rect.x = self.model.workshop.left

            elif keys[pygame.K_RIGHT] and self.model.vehicle.can_move_right:
                speed_x = 2
                for top in range(len(self.model.temp_world)):
                    for left in range(len(self.model.temp_world[top])):
                        brick = self.model.temp_world[top][left]
                        brick.left -= self.model.vehicle.speed_x
                        brick.rect.x = brick.left

                self.model.fuel_station.left -= self.model.vehicle.speed_x
                self.model.fuel_station.rect.x = self.model.fuel_station.left
                self.model.shop.left -= self.model.vehicle.speed_x
                self.model.shop.rect.x = self.model.shop.left
                self.model.workshop.left -= self.model.vehicle.speed_x
                self.model.workshop.rect.x = self.model.workshop.left

                self.model.vehicle.speed_x = self.model.vehicle.speed_x + self.model.vehicle.thruster_x;   

                if self.model.vehicle.speed_x > 1:
                    self.model.vehicle.speed_x = 0
                elif self.model.vehicle.speed_x > 10:
                    self.model.vehicle.speed_x = 10


            if keys[pygame.K_DOWN] and not self.model.can_move_down and self.model.vehicle.can_drill_down:
            
                self.model.vehicle.speed_y = .7
                for top in range(len(self.model.temp_world)):
                    for left in range(len(self.model.temp_world[top])):
                        brick = self.model.temp_world[top][left]
                        brick.top -= self.model.vehicle.speed_y
                        brick.rect.y = brick.top
                self.model.fuel_station.top -= self.model.vehicle.speed_y
                self.model.fuel_station.rect.y = self.model.fuel_station.top
                self.model.shop.top -= self.model.vehicle.speed_y
                self.model.shop.rect.y = self.model.shop.top
                self.model.workshop.top -= self.model.vehicle.speed_y
                self.model.workshop.rect.y = self.model.workshop.top


            elif self.model.can_move_down and not keys[pygame.K_UP]:    
                for top in range(len(self.model.temp_world)):
                    for left in range(len(self.model.temp_world[top])):
                        brick = self.model.temp_world[top][left]
                        brick.top -= self.model.vehicle.speed_y
                        brick.rect.y = brick.top


                self.model.fuel_station.top -= self.model.vehicle.speed_y

                self.model.fuel_station.rect.y = self.model.fuel_station.top

                self.model.shop.top -= self.model.vehicle.speed_y
                self.model.shop.rect.y = self.model.shop.top

                self.model.workshop.top -= self.model.vehicle.speed_y
                self.model.workshop.rect.y = self.model.workshop.top

                self.model.vehicle.speed_y = self.model.vehicle.speed_y + self.model.vehicle.gravity
                if self.model.vehicle.speed_y > 12:
                    self.model.vehicle.speed_y -=.5


            if not self.model.can_move_down and event.type != KEYDOWN:
                self.model.vehicle.speed_y = 0
            if not self.model.vehicle.can_drill_left and not self.model.vehicle.can_drill_right and event.type != KEYDOWN:
                self.model.vehicle.speed_x = 0

            
          
            #self.view.draw()
            self.model.fuel -= 1 #decrease fuel value every frame
            self.view.draw()
        return
      
  

#clock = pygame.time.Clock()

if __name__ == '__main__':
    
  
   
    pygame.init()
    size = (640, 480)
    screen = pygame.display.set_mode(size)
    model = game_model.BrickModel()
    view = GameViewer(model, screen)
    controller = KeyboardController(model,view)
    
    controller.handle_event()   

    
      

        
            
                  