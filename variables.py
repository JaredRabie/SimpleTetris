import pygame

brick_width = 50
white = (255,255,255)
black = (0,0,0)
fps = 60
movement_cooldown = 15     #Number of frames before movement is allowed again (Prevents player moving too quickly since keypresses are polled with 60fps)

window = pygame.display.set_mode((1920, 1080))
game_border = pygame.Rect(brick_width, brick_width, brick_width*10, brick_width*20)
tetronimo_bench_x, tetronimo_bench_y = game_border.x + game_border.width, game_border.y #coordinates that tetronimos are stored before being put into play

green_hitbox = [pygame.Rect(tetronimo_bench_x, tetronimo_bench_y, brick_width, brick_width),\
                pygame.Rect(tetronimo_bench_x, tetronimo_bench_y + brick_width, brick_width, brick_width),\
                pygame.Rect(tetronimo_bench_x + brick_width, tetronimo_bench_y + brick_width, brick_width, brick_width),\
                pygame.Rect(tetronimo_bench_x + brick_width, tetronimo_bench_y + 2*brick_width, brick_width, brick_width)]
hitbox_list = [green_hitbox]