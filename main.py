import pygame
import os
from variables import *

#!SEE variables.py FOR GLOBAL VARIABLE DEFINITIONS
pygame.display.set_caption("Tetris")

class tetronimo_stack:
    def __init__(self):
        self.__items = []
    
    def get_items(self):
        return self.__items
    
    def add_top(self, item):
        self.__items = [item] + self.__items
    def add_bottom(self, item):
        self.__items = self.__items + [item]

    #Remove and return bottom/top item from stack.
    def remove_top(self):
        top_item = self.__items[0]
        self.__items = self.__items[1:]
        top_item -= game_border.width
        return top_item
    def remove_bottom(self):
        bottom_item = self.__items[-1]
        self.__items = self.__items[:-1]
        bottom_item -= game_border.width   #Moves piece back into play to enable movement
        return bottom_item
    
    #Remove without returning bottom/top item from stack. 
    def peek_top(self):
        return self.__items[0]
    def peek_bottom(self):
        return self.__items[-1]

    def size(self):
        return len(self.__items)
    
    def populate(self, size, hitbox_list):
        hitbox_list = hitbox_list*(size//len(hitbox_list) + 1) #avoids IndexError by lengthening hitbox_list
        while size > 0:
            self.add_bottom(tetronimo(hitbox_list.pop(0)))
            size -= 1

class tetronimo():
    def __init__(self, hitbox):
        self.__bricks = hitbox
        self.__location = 0

        self.x = min([brick.x for brick in self.__bricks])
        self.width = max([brick.x for brick in self.__bricks]) - min([brick.x for brick in self.__bricks]) + brick_width
    
    #Overriding the "for __ in __:" iterator to move individual bricks
    def __iter__(self):
        return self
    def __next__(self):
        if self.__location == len(self.__bricks):
            self.__location = 0
            raise StopIteration
        value = self.__bricks[self.__location]
        self.__location += 1
        return value

    def __isub__(self, number):
        for brick in self.__bricks:
            brick.x -= number
        self.x = min([brick.x for brick in self.__bricks])
        return self
    def __iadd__(self, number):
        for brick in self.__bricks:
            brick.x += number
        self.x = min([brick.x for brick in self.__bricks])
        return self
    
    def display(self):
        for brick in self.__bricks:
            pygame.draw.rect(window, (0, 255, 0), brick)

def movement_handler(keys_pressed, current_tetronimo, movement_timer):
    if movement_timer > movement_cooldown:
        if keys_pressed[pygame.K_LEFT] or keys_pressed[pygame.K_RIGHT]: #Check if we need to reset the movement_timer (movement_timer resets if the object moves to limit the speed of each object)
            if keys_pressed[pygame.K_LEFT] and current_tetronimo.x > game_border.x:
                current_tetronimo -= brick_width
                movement_timer = 0

            if keys_pressed[pygame.K_RIGHT] and current_tetronimo.x + current_tetronimo.width < game_border.x + game_border.width:
                current_tetronimo += brick_width
                movement_timer = 0

    if keys_pressed[pygame.K_DOWN]:
        print() #Downward script in development
    
    return movement_timer + 1

def draw_window(current_tetronimo):
    window.fill(white)
    pygame.draw.rect(window, black, game_border)
    current_tetronimo.display()
    pygame.display.update()

def main():
    tetronimos = tetronimo_stack()
    tetronimos.populate(20, hitbox_list)

    clock = pygame.time.Clock()
    run = True
    movement_timer = 0
    current_tetronimo = tetronimos.remove_top()
    while run:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        keys_pressed = pygame.key.get_pressed()
        movement_timer = movement_handler(keys_pressed, current_tetronimo, movement_timer)
        
        draw_window(current_tetronimo)
    pygame.quit()

main()