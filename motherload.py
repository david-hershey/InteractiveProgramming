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

                r = pygame.Rect(brick.left, brick.top, brick.width, brick.height)
               
                if pygame.sprite.collide_rect(brick, self.model.vehicle) and  brick.rect.y > self.model.vehicle.rect.y and math.fabs(brick.rect.x - self.model.vehicle.rect.x) < 2:
              

                # if brick.left == self.model.vehicle.left and brick.top <= self.model.vehicle.top + brick.height and brick.top + brick.height > self.model.vehicle.top + brick.height:

              #checks if the vehicle overlaps a block, if so change block to black
                    if brick.color != "black":
                        self.model.can_move_down = False

                        #print "can move down", model.can_move_down

                    else:
                        self.model.can_move_down = True
                # elif not pygame.sprite.collide_rect(brick, self.model.vehicle):
                #     self.model.can_move_down = False

                        #print "can move down", self.model.can_move_down
               

                if self.model.vehicle.left + float(brick.width)/2 < brick.left and brick.left + float(brick.width)/2 > self.model.vehicle.left and not (brick.left > self.model.vehicle.left + float(brick.width)*3/2) \
                     and brick.top > self.model.vehicle.top - brick.width/2 and brick.top + brick.height < self.model.vehicle.top + float(brick.width)*3/2: #checks if the vehicle has a block to the right
                    if brick.color != "black" and not model.can_move_down:
                        self.model.can_drill_right = True
                        #print "can move right", self.model.can_drill_right
                    else:
                        self.model.can_drill_right = False
                       # print "can move right", self.model.can_drill_right
                        # print "can move?", model.can_move_down
                        # print "vehicle left", self.model.vehicle.left
                        # print "brick left ", brick.left
                        # print "brick top", brick.top
                        # print "veh top", self.model.vehicle.top
                        # print "can drill right,", model.can_drill_right
              #  print self.model.can_drill_right

                if brick.left == self.model.vehicle.left and self.model.vehicle.top > brick.top and self.model.vehicle.top + brick.height < brick.top + brick.height*2: #checks if the vehicle overlaps a block, if so change block to black
                    if brick.color != "black" and brick.color != "brown":
                        print "I am eating ...", brick.color
                    if brick.color == "red":
                        self.model.red_block += 1
                        brick.image.fill((0,0,0))
                        brick.image.set_colorkey((0,0,0))
                    elif brick.color == "green":
                        self.model.green_block += 1
                    elif brick.color == "orange":
                        self.model.orange_block += 1
                    elif brick.color == "blue":
                        self.model.blue_block += 1
                    elif brick.color == "purple":
                        self.model.purple_block += 1
                    brick.color = "black"
                    pygame.draw.rect(self.screen, pygame.Color(brick.color), r)

                else:
                    pygame.draw.rect(self.screen, pygame.Color(brick.color), r)
                
                    
        
        r = pygame.Rect(self.model.vehicle.left,self.model.vehicle.top,self.model.vehicle.width,self.model.vehicle.height) #the mining vehicle
                     
        pygame.draw.rect(self.screen, pygame.Color('white'), r)

        r = pygame.Rect(self.model.fuel_station.left,self.model.fuel_station.top,self.model.fuel_station.width,self.model.fuel_station.height)
        pygame.draw.rect(self.screen, pygame.Color('deep pink'),r) 

        self.model.sprite_list.draw(self.screen)

        r = pygame.Rect(self.model.shop.left,self.model.shop.top,self.model.shop.width,self.model.shop.height)
        #subpygame.draw.rect(self.screen, pygame.Color('yellow'), r)

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
     
        if self.model.fuel <= 0:
            msg = game_over_font.render("GAME OVER",1,(255,255,0))
            screen.blit(msg, (0, 240))
        else:
            timer = myFont.render(str(self.model.fuel), 1, (255,255,0))
            screen.blit(timer, (20,20))

        red_counter = myFont.render("Red: " + str(self.model.red_block), 1, (255,255,0))
        screen.blit(red_counter,(550,20))
        
        green_counter = myFont.render("Green: " + str(self.model.green_block), 1, (255,255,0))
        screen.blit(green_counter,(550,40))

        orange_counter = myFont.render("Orange: " + str(self.model.orange_block), 1, (255,255,0))
        screen.blit(orange_counter,(550,60))
        
        blue_counter = myFont.render("Blue: " + str(self.model.blue_block), 1, (255,255,0))
        screen.blit(blue_counter,(550,80))
        
        purple_counter = myFont.render("Purplpe: " + str(self.model.purple_block), 1, (255,255,0))
        screen.blit(purple_counter,(550,100))

        money_counter = myFont.render("Money: " + str(self.model.money), 1, (255,255, 0))
        screen.blit(money_counter, (550,120))

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
        #   print self.model.temp_world[-1][0].top
        #   if self.model.temp_world[-1][0].top != self.model.FAR_BOTTOM: 
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
                        brick.rect.x += brick.width #sprites stuff
                self.model.fuel_station.left += self.model.BRICK_HEIGHT
                self.model.fuel_station.rect.x += self.model.BRICK_HEIGHT
                self.model.shop.left += self.model.BRICK_HEIGHT
                self.model.shop.rect.x += self.model.BRICK_HEIGHT
                # print self.model.fuel_station.left
                # print self.model.fuel_station.rect.x
           
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
                        brick.rect.x -= brick.width
                self.model.fuel_station.left -= self.model.BRICK_HEIGHT
                self.model.fuel_station.rect.x -= self.model.BRICK_HEIGHT
                self.model.shop.left -= self.model.BRICK_HEIGHT                
                self.model.shop.rect.x -= self.model.BRICK_HEIGHT
                # print self.model.fuel_station.left
                # print self.model.fuel_station.rect.x
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
    gravity = 0.5;
    thruster = -0.05
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
        model.can_drill_right = False


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
                        brick.rect.y = brick.top
            model.fuel_station.top -= speed
            model.fuel_station.rect.y = model.fuel_station.top
            model.shop.top -= speed
            model.shop.rect.y = model.shop.top

            speed = speed + thruster;   

            if speed > 1:
                speed = 0
            elif speed > 10:
                speed = 10

        elif keys[pygame.K_DOWN] and not model.can_move_down:
        #   print "juss drilling"
            speed = .7
            for top in range(len(model.temp_world)):
                for left in range(len(model.temp_world[top])):
                    brick = model.temp_world[top][left]
                    brick.top -= speed
                    brick.rect.y = brick.top
            model.fuel_station.top -= speed
            model.fuel_station.rect.y = model.fuel_station.top
            model.shop.top -= speed
            model.shop.rect.y = model.shop.top

        elif model.can_move_down and not keys[pygame.K_UP]:    
            for top in range(len(model.temp_world)):
                for left in range(len(model.temp_world[top])):
                    brick = model.temp_world[top][left]
                    brick.top -= speed
                    brick.rect.y = brick.top
<<<<<<< HEAD

=======
>>>>>>> e1e45cb10efd529c6d82dcc495d1c2808c6f68ae
            model.fuel_station.top -= speed
            model.fuel_station.rect.y = model.fuel_station.top
            model.shop.top -= speed
            model.shop.rect.y = model.shop.top

            speed = speed + gravity
            if speed > 12:
                speed -=.5

        # elif keys[pygame.K_RIGHT]:
        #     if not model.can_move_down:
        #         speed = .7
        #         for top in range(len(model.temp_world)):
        #             for left in range(len(model.temp_world[top])):
        #                     brick = model.temp_world[top][left]
        #                     brick.left -= speed
        #         model.fuel_station.left -= speed

        #     else: 
        #         for top in range(len(model.temp_world)):
        #             for left in range(len(model.temp_world[top])):
        #                     brick = model.temp_world[top][left]
        #                     brick.left -= speed
        #         model.fuel_station.left -= speed


      #   elif not model.can_move_down and keys[pygame.K_RIGHT]:
            # speed = .7
            # for top in range(len(model.temp_world)):
         #        for left in range(len(model.temp_world[top])):
         #                brick = model.temp_world[top][left]
         #                brick.left -= speed
         #    model.fuel_station.left -= speed

      #   elif not model.can_move_down and keys[pygame.K_LEFT]:
            # speed = .7
            # for top in range(len(model.temp_world)):
         #        for left in range(len(model.temp_world[top])):
         #                brick = model.temp_world[top][left]
         #                brick.left += speed
         #    model.fuel_station.left += speed

        if not model.can_move_down and event.type != KEYDOWN:
            speed = 0

        
        model.fuel -= 1 #decrease fuel value every frame
        view.draw()
        #print "can move right??", model.can_drill_right
     #   clock.tick(500000000)
