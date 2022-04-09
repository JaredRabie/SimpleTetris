import pygame
import os

#test

block_width = 50
white = (255,255,255)
fps = 60
width, height = (900,600)
window = pygame.display.set_mode((width,height))
pygame.display.set_caption("Tetris")

green_image = pygame.image.load(os.path.join('Assets', 'Green.png'))
green_tetronimo = pygame.transform.scale(green_image, (2*block_width, 3*block_width))

def movement_handler(keys_pressed, tetronimo):
    if keys_pressed[pygame.K_LEFT]:
        tetronimo.x -= block_width
    if keys_pressed[pygame.K_RIGHT]:
        tetronimo.x += block_width
    

def draw_window(green):
    window.fill(white)
    window.blit(green_tetronimo, (green.x,green.y))
    pygame.display.update()


def main():
    green = pygame.Rect(10,10,2*block_width, 3*block_width)
    clock = pygame.time.Clock()
    run = True
    
    while run:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        
        keys_pressed = pygame.key.get_pressed()
        movement_handler(keys_pressed, green)
        
        draw_window(green)

    pygame.quit()


#Ensuring that game runs if the file is run directly, not in instances like when main.py is imported as a module.
if __name__ == "__main__":
    main()