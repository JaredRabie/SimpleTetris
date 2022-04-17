import pygame
import os
from variables import *

#!SEE variables.py FOR GLOBAL VARIABLE DEFINITIONS

class placed_tetronimo_grid:
    def __init__(self):
        self.__grid = grid

    def place(self, current_tetronimo):
        for brick in current_tetronimo:
            brick_col = (brick.x//brick_width) - 1 
            brick_row = 19 - ((brick.y//brick_width) - 1)
            self.__grid[brick_row][brick_col] = current_tetronimo.get_colour()        
    
    def display(self):
        for row in range(0, 19):
            for col in range(0, 10):
                if self.__grid[row][col] != None:
                    x_coord = (col + 1)*brick_width
                    y_coord = (20 - row)*brick_width
                    brick = pygame.Rect(x_coord, y_coord, brick_width, brick_width)
                    colour = self.__grid[row][col]
                    pygame.draw.rect(window, colour, brick)
                

class tetronimo_stack_class:
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
    
    def populate(self, size, hitbox_generators):
        while size > 0:
            colour = hitbox_generators[size % len(hitbox_generators)][-1] #taking colour from final element
            lst = hitbox_generators[size % len(hitbox_generators)][:len(hitbox_generators)+1] #taking all tuples (everything but colour)
            hitbox = []
            for item in lst:
                print(item)
                hitbox.insert(0, pygame.Rect(tetronimo_bench_x + item[0]*brick_width, tetronimo_bench_y + item[1]*brick_width, brick_width, brick_width))
            hitbox.append(colour)
            self.add_bottom(tetronimo_class(hitbox))
            size -= 1

class tetronimo_class():
    def __init__(self, hitbox):
        self.__bricks = hitbox[:4]
        self.__colour = hitbox[4]
        self.__location = 0

        self.x = min([brick.x for brick in self.__bricks])
        self.y = min([brick.y for brick in self.__bricks])
        self.width = max([brick.x for brick in self.__bricks]) - min([brick.x for brick in self.__bricks]) + brick_width
        self.height = max([brick.y for brick in self.__bricks]) - min([brick.y for brick in self.__bricks]) + brick_width
    
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
    
    def move_down(self):
        for brick in self.__bricks:
            brick.y += brick_width
            self.y = min([brick.y for brick in self.__bricks])

    def get_colour(self):
        if self.__colour == "Green":
            colour = green
        if self.__colour == "Yellow":
            colour = yellow
        if self.__colour == "Turquoise":
            colour = turquoise
        return colour

    def display(self):
        colour = self.get_colour()
        for brick in self.__bricks:
            pygame.draw.rect(window, colour, brick)

def movement_handler(keys_pressed, current_tetronimo, lateral_timer, vertical_timer):
    if lateral_timer > movement_cooldown:
        if keys_pressed[pygame.K_LEFT] or keys_pressed[pygame.K_RIGHT]: #Check if we need to reset the lateral_timer (lateral_timer resets if the object moves to limit the speed of each object)
            if keys_pressed[pygame.K_LEFT] and current_tetronimo.x > game_border.x:
                current_tetronimo -= brick_width
                lateral_timer = 0

            if keys_pressed[pygame.K_RIGHT] and current_tetronimo.x + current_tetronimo.width < game_border.x + game_border.width:
                current_tetronimo += brick_width
                lateral_timer = 0

    if keys_pressed[pygame.K_DOWN]:
        pass
    
    if vertical_timer > vert_movement_cooldown:
        current_tetronimo.move_down()
        vertical_timer = 0

    return lateral_timer + 1, vertical_timer + 1

def draw_window(current_tetronimo, tetronimos_placed):
    window.fill(white)
    pygame.draw.rect(window, black, game_border)
    current_tetronimo.display()
    tetronimos_placed.display()
    pygame.display.update()

def main():
    tetronimo_stack = tetronimo_stack_class()
    tetronimo_stack.populate(20, hitbox_generators)
    current_tetronimo = tetronimo_stack.remove_top()
    current_tetronimo -= game_border.width

    tetronimos_placed = placed_tetronimo_grid()

    pygame.display.set_caption("Tetris")
    clock = pygame.time.Clock()
    run = True
    lateral_timer = 0
    vertical_timer = 0
    while run:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        keys_pressed = pygame.key.get_pressed()
        lateral_timer, vertical_timer = movement_handler(keys_pressed, current_tetronimo, lateral_timer, vertical_timer)
        if current_tetronimo.y + current_tetronimo.height > 20*brick_width:
            tetronimos_placed.place(current_tetronimo)
            current_tetronimo = tetronimo_stack.remove_top()
            current_tetronimo -= game_border.width


        
        draw_window(current_tetronimo, tetronimos_placed)
    pygame.quit()

main()