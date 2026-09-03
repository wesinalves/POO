# Example file showing a basic pygame "game loop"
import pygame
from spin import Spin

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
angulo = 0

posicao_centro = (screen.get_rect().centerx, screen.get_rect().centery)

spinner = Spin(screen)
origin_rect = spinner.image.get_rect()

# fill the screen with a color to wipe away anything from last frame
screen.fill("white")
spinner.blitme()
speed = 1

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    keys = pygame.key.get_pressed()
    if keys[pygame.K_b]:
        speed = (speed * 2)
        # Incrementa o ângulo a cada frame
        angulo = (angulo + speed) % 360
        imagem_rotacionada = pygame.transform.rotate(spinner.image, angulo)
        rect_rotacionado = imagem_rotacionada.get_rect(center=posicao_centro)
        # flip() the display to put your work on screen
        screen.fill("white")
        screen.blit(imagem_rotacionada, rect_rotacionado)
        pygame.display.flip()

    # if speed > 5:
    #     speed = speed - 1
    #     # Incrementa o ângulo a cada frame
    #     angulo = (angulo + speed) % 360
    #     imagem_rotacionada = pygame.transform.rotate(spinner.image, angulo)
    #     rect_rotacionado = imagem_rotacionada.get_rect(center=posicao_centro)
    #     # flip() the display to put your work on screen
    #     screen.fill("white")
    #     screen.blit(imagem_rotacionada, rect_rotacionado)
    #     pygame.display.flip()
    
   

    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()