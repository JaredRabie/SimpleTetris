
import pygame
import os

brick_width = 50
white = (255,255,255)
black = (0,0,0)
fps = 60
movement_cooldown = 15     #Number of frames before movement is allowed again (Prevents player moving too quickly since keypresses are polled with 60fps)
window = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("Tetris")


game_border = pygame.Rect(brick_width, brick_width, brick_width*10, brick_width*20)

#green_image = pygame.image.load(os.path.join('Assets', 'Green.png'))
#green_tetronimo = pygame.transform.scale(green_image, (2*brick_width, 3*brick_width))

tetronimo_bench_x, tetronimo_bench_y = game_border.x + game_border.width, game_border.y #coordinates that tetronimos are stored before being put into play
        

placed_tiles = []

green_hitbox = [pygame.Rect(tetronimo_bench_x, tetronimo_bench_y, brick_width, brick_width),\
                pygame.Rect(tetronimo_bench_x, tetronimo_bench_y + brick_width, brick_width, brick_width),\
                pygame.Rect(tetronimo_bench_x + brick_width, tetronimo_bench_y + brick_width, brick_width, brick_width),\
                pygame.Rect(tetronimo_bench_x + brick_width, tetronimo_bench_y + 2*brick_width, brick_width, brick_width)]
hitbox_list = [green_hitbox]


def x(bricks_list):
    return min([brick.x for brick in bricks_list])
def width(bricks_list):
    return max([brick.x for brick in bricks_list]) - min([brick.x for brick in bricks_list]) + brick_width



#The following function handles the movement for each tetronimo. Every time the display is refreshed (at 60fps) a counter called movement_timer increases, after movement_timer > movement_cooldown the 
#player can move the tetronimo left or right which resets movement_timer. Since the tetronimos move in bricks this slows down the movement of each tetronimo to a manageable rate. Tetronimos can always be
#moved downwards.
def movement_handler(keys_pressed, tetronimo_list, movement_timer):
    if movement_timer > movement_cooldown:
        if keys_pressed[pygame.K_LEFT] or keys_pressed[pygame.K_RIGHT]: #Check if we need to reset the movement_timer (movement_timer resets if the object moves to limit the speed of each object)
            if keys_pressed[pygame.K_LEFT] and x(tetronimo_list) > game_border.x:
                for brick in tetronimo_list:
                    brick.x -= brick_width 
                movement_timer = 0
            if keys_pressed[pygame.K_RIGHT] and x(tetronimo_list) + width(tetronimo_list) < game_border.x + game_border.width:
                for brick in tetronimo_list:
                    brick.x += brick_width
                movement_timer = 0

    if keys_pressed[pygame.K_DOWN]:
        print() #Downward script in development
    
    return movement_timer + 1





def draw_window(tetronimo_list):
    window.fill(white)
    pygame.draw.rect(window, black, game_border)
    for brick in tetronimo_list:
        pygame.draw.rect(window, (0, 255, 0), brick)
    pygame.display.update()


def initialise_tetronimo(hitbox_list, count):
    tetronimo = hitbox_list[count]
    for brick in tetronimo:
        brick.x -= game_border.width #moves tetronimo back into playing field
    return tetronimo



#main() initialises the game and starts the while loop that refreshes the display at 60fps until the game ends. Time-based events are located in this while loop.
def main():
    clock = pygame.time.Clock()
    run = True
    movement_timer = 0
    tetronimo_number = 0
    current_tetronimo = initialise_tetronimo(hitbox_list, tetronimo_number)
    while run:
        clock.tick(fps)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        keys_pressed = pygame.key.get_pressed()
        movement_timer = movement_handler(keys_pressed, current_tetronimo, movement_timer)
        
        draw_window(current_tetronimo)
    pygame.quit()





#Ensuring that game runs if the file is run directly, not in instances like when main.py is imported as a module.
if __name__ == "__main__":
    main()