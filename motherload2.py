import pygame, os, sys
from pygame.locals import *
import time
from random import choice
import random
import game_model
import pygame, os, sys
import math 


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
                if not (left == 0 or top == 0 or top == len(self.model.temp_world) -1 or left == len(self.model.temp_world[0])-1) and pygame.sprite.collide_rect(brick,self.model.vehicle):

                    brick_left = self.model.temp_world[top][left-1]
                    brick_top_left =  self.model.temp_world[top-1][left-1]
                    brick_top_right = self.model.temp_world[top-1][left+1]
                    brick_bottom_left = self.model.temp_world[top+1][left-1]
                    brick_bottom_right = self.model.temp_world[top+1][left+1]
                    brick_right = self.model.temp_world[top][left+1]
                    brick_bottom = self.model.temp_world[top+1][left]
                    brick_top = self.model.temp_world[top-1][left]
                      
                    t = True
                    tl = True
                    tr = True

                    l = True
                    r = True

                    bl = True
                    b = True
                    br = True

                    if pygame.sprite.collide_rect(brick,self.model.vehicle):

                        if pygame.sprite.collide_rect(self.model.vehicle,brick_left):  #checks collision with left
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

                        #if brick.color == "black" and brick_bottom.color == "black":
                            #print "gravity is TRUE"

                        #Collision detection using sprite collision
                        if t and not tl and not tr:
                        #print "tl",tl,"t: ",t, "tr", tr
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

                        #Checks for drilling availability
                        if l and b and not self.model.can_move_down:
                            if brick_left.color != "black" and brick_bottom.color != "black":
                                #print "CAN DRILL!!"
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
             
           

                if not (top == 0 or top ==1):
                    if math.fabs(brick.left - self.model.vehicle.left) < 20 and math.fabs(self.model.vehicle.top - brick.top)<20: #checks if the vehicle overlaps a block, if so change block to black
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

        r = pygame.Rect(self.model.fuel_station.left,self.model.fuel_station.top,self.model.fuel_station.width,self.model.fuel_station.height)
        pygame.draw.rect(self.screen, pygame.Color('deep pink'),r) 

        self.model.sprite_list.draw(self.screen)

        r = pygame.Rect(self.model.shop.left,self.model.shop.top,self.model.shop.width,self.model.shop.height)

        #Vehicle visiting fuel station
        if pygame.sprite.collide_rect(self.model.fuel_station, self.model.vehicle):
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

        if self.model.fuel <= 0:
            msg = game_over_font.render("GAME OVER",1,(255,255,0))
            screen.blit(msg, (0, 240))
        else:
            timer = myFont.render(str(self.model.fuel), 1, (255,255,0))
            screen.blit(timer, (20,20))

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




class PyGameKeyboardController(object):
    def __init__(self, model):
        self.model = model

    def handle_event(self, event):
        """ Look for left and right keypresses to
            modify the x position of the paddle """
        if event.type != KEYDOWN:
            return





clock = pygame.time.Clock()

if __name__ == '__main__':
    
  
  
    speed_y = 0;
    speed_x=0;
    gravity = 0.25;
    thruster = -0.05
    thruster_x = .025
    pygame.init()
    size = (640, 480)
    screen = pygame.display.set_mode(size)
    model = game_model.BrickBreakerModel()
    view = PygameBrickBreakerView(model, screen)
    controller = PyGameKeyboardController(model)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            controller.handle_event(event)
        model.can_drill_right = False

        if model.fuel < 0:
            running = False

        if model.temp_world[-1][0].top >= model.FAR_BOTTOM and model.temp_world[-1][0].top < model.FAR_BOTTOM + 40: 
            mistake = model.FAR_BOTTOM - model.temp_world[-1][0].top
            model.world_enlarger("down")


        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and model.vehicle.can_move_up:

            for top in range(len(model.temp_world)):
                for left in range(len(model.temp_world[top])):
                        brick = model.temp_world[top][left]
                        brick.top -= speed_y
                        brick.rect.y = brick.top
            model.fuel_station.top -= speed_y
            model.fuel_station.rect.y = model.fuel_station.top
            model.shop.top -= speed_y
            model.shop.rect.y = model.shop.top
            model.workshop.top -= speed_y
            model.workshop.rect.y = model.workshop.top

            speed_y = speed_y + thruster;   

            if speed_y > 1:
                speed_y = 0
            elif speed_y > 10:
                speed_y = 10
        elif keys[pygame.K_UP] and not model.vehicle.can_move_up:
            speed_y = 0

        if keys[pygame.K_LEFT] and not model.vehicle.can_drill_left and not model.vehicle.can_move_left:
            pass
        elif keys[pygame.K_LEFT] and model.vehicle.can_drill_left:
            speed_x = .7
            for top in range(len(model.temp_world)):
                for left in range(len(model.temp_world[top])):
                    brick = model.temp_world[top][left]
                    brick.left += speed_x
                    brick.rect.x = brick.left
            model.fuel_station.left += speed_x
            model.fuel_station.rect.x = model.fuel_station.left
            model.shop.left += speed_x
            model.shop.rect.x = model.shop.left
            model.workshop.left += speed_x
            model.workshop.rect.x = model.workshop.left

        elif keys[pygame.K_LEFT] and model.vehicle.can_move_left:
            speed_x = 2
            for top in range(len(model.temp_world)):
                for left in range(len(model.temp_world[top])):
                    brick = model.temp_world[top][left]
                    brick.left += speed_x
                    brick.rect.x = brick.left
            model.fuel_station.left += speed_x
            model.fuel_station.rect.x = model.fuel_station.left
            model.shop.left += speed_x
            model.shop.rect.x = model.shop.left
            model.workshop.left += speed_x
            model.workshop.rect.x = model.workshop.left

            speed_x = speed_x + thruster_x;   

            if speed_x > 1:
                speed_x = 0
            elif speed_x > 10:
                speed_x = 10

        if keys[pygame.K_RIGHT] and model.vehicle.can_drill_right:
                
            speed_x = .7
            for top in range(len(model.temp_world)):
                for left in range(len(model.temp_world[top])):
                    brick = model.temp_world[top][left]
                    brick.left -= speed_x
                    brick.rect.x = brick.left
            model.fuel_station.left -= speed_x
            model.fuel_station.rect.x = model.fuel_station.left
            model.shop.left -= speed_x
            model.shop.rect.x = model.shop.left
            model.workshop.left -= speed_x
            model.workshop.rect.x = model.workshop.left

        elif keys[pygame.K_RIGHT] and model.vehicle.can_move_right:
            speed_x = 2
            for top in range(len(model.temp_world)):
                for left in range(len(model.temp_world[top])):
                    brick = model.temp_world[top][left]
                    brick.left -= speed_x
                    brick.rect.x = brick.left

            model.fuel_station.left -= speed_x
            model.fuel_station.rect.x = model.fuel_station.left
            model.shop.left -= speed_x
            model.shop.rect.x = model.shop.left
            model.workshop.left -= speed_x
            model.workshop.rect.x = model.workshop.left

            speed_x = speed_x + thruster_x;   

            if speed_x > 1:
                speed_x = 0
            elif speed_x > 10:
                speed_x = 10


        elif keys[pygame.K_DOWN] and not model.can_move_down and model.vehicle.can_drill_down:
            speed_y = .7
            for top in range(len(model.temp_world)):
                for left in range(len(model.temp_world[top])):
                    brick = model.temp_world[top][left]
                    brick.top -= speed_y
                    brick.rect.y = brick.top
            model.fuel_station.top -= speed_y
            model.fuel_station.rect.y = model.fuel_station.top
            model.shop.top -= speed_y
            model.shop.rect.y = model.shop.top
            model.workshop.top -= speed_y
            model.workshop.rect.y = model.workshop.top

        elif model.can_move_down and not keys[pygame.K_UP]:    
            for top in range(len(model.temp_world)):
                for left in range(len(model.temp_world[top])):
                    brick = model.temp_world[top][left]
                    brick.top -= speed_y
                    brick.rect.y = brick.top


            model.fuel_station.top -= speed_y

            model.fuel_station.rect.y = model.fuel_station.top

            model.shop.top -= speed_y
            model.shop.rect.y = model.shop.top

            model.workshop.top -= speed_y
            model.workshop.rect.y = model.workshop.top

            speed_y = speed_y + gravity
            if speed_y > 12:
                speed_y -=.5



        if not model.can_move_down and event.type != KEYDOWN:
            speed_y = 0
        if not model.vehicle.can_drill_left and not model.vehicle.can_drill_right and event.type != KEYDOWN:
            speed_x = 0

        
        model.fuel -= 1 #decrease fuel value every frame
        view.draw()
              
