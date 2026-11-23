import sys
import pygame

pygame.init()
tela = pygame.display.set_mode((800, 600))
pygame.time.Clock()
clock = pygame.time.Clock()

# 1. Cria uma superfície para o objeto (substitua por pygame.image.load('sua_imagem.png'))
#imagem_original = pygame.Surface((100, 100), pygame.SRCALPHA)
#imagem_original.fill((255, 99, 71))  # Cor vermelha/tomate

imagem_original = pygame.image.load('./spinnerfundotransparente.png')
imagem_original = pygame.transform.scale_by(imagem_original, 0.3)

# Define a posição fixa onde o centro do objeto estará
posicao_centro = (400, 300)

angulo = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Incrementa o ângulo a cada frame
    angulo = (angulo + 2) % 360

    # 2. Gira a imagem original
    imagem_rotacionada = pygame.transform.rotate(imagem_original, angulo)

    # 3. Ajusta o novo retângulo mantendo o centro anterior
    rect_rotacionado = imagem_rotacionada.get_rect(center=posicao_centro)

    # Renderização
    tela.fill((30, 30, 30))
    tela.blit(imagem_rotacionada, rect_rotacionado)
    pygame.display.flip()

    clock.tick(60)