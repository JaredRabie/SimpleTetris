import pygame

brick_width = 50
white = (255,255,255)
black = (0,0,0)
fps = 60
vert_movement_cooldown = 60
movement_cooldown = 15     #Number of frames before movement is allowed again (Prevents player moving too quickly since keypresses are polled with 60fps)

window = pygame.display.set_mode((1920, 1080))
game_border = pygame.Rect(brick_width, brick_width, brick_width*10, brick_width*20)
tetronimo_bench_x, tetronimo_bench_y = game_border.x + game_border.width, game_border.y #coordinates that tetronimos are stored before being put into play

green = (0, 255, 0)
yellow = (255,255,0)
turquoise = (64,224,208)

green_hitbox_generator = [(0,0),(0,1),(1,1),(1,2), "Green"]
yellow_hitbox_generator = [(0,0), (0,1),(1,0),(1,1), "Yellow"]
turquoise_hitbox_generator = [(0,0),(0,1),(0,2),(0,3),"Turquoise"]

hitbox_generators = [green_hitbox_generator, yellow_hitbox_generator, turquoise_hitbox_generator]


grid = [[None, None, None, None, None, None, None, None, None, None],\
                       [None, None, None, None, None, None, None, None, None, None],\
                       [None, None, None, None, None, None, None, None, None, None],\
                       [None, None, None, None, None, None, None, None, None, None],\
                       [None, None, None, None, None, None, None, None, None, None],\
                       [None, None, None, None, None, None, None, None, None, None],\
                       [None, None, None, None, None, None, None, None, None, None],\
                       [None, None, None, None, None, None, None, None, None, None],\
                       [None, None, None, None, None, None, None, None, None, None],\
                       [None, None, None, None, None, None, None, None, None, None],\
                       [None, None, None, None, None, None, None, None, None, None],\
                       [None, None, None, None, None, None, None, None, None, None],\
                       [None, None, None, None, None, None, None, None, None, None],\
                       [None, None, None, None, None, None, None, None, None, None],\
                       [None, None, None, None, None, None, None, None, None, None],\
                       [None, None, None, None, None, None, None, None, None, None],\
                       [None, None, None, None, None, None, None, None, None, None],\
                       [None, None, None, None, None, None, None, None, None, None],\
                       [None, None, None, None, None, None, None, None, None, None]]