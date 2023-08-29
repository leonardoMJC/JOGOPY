import pygame

# Inicializa o Pygame
pygame.init()

# Cria uma janela
tela = pygame.display.set_mode((640, 480))

# Cria uma bolinha
bola = pygame.Rect((0, 0), (20, 20))

# Define a velocidade da bolinha como uma lista
velocidade = [10, 10]

# Loop principal do jogo
while True:

    # Limpa a tela
    tela.fill((0, 0, 0))

    # Move a bolinha
    bola.move_ip(velocidade)

    # Verifica se a bolinha colidiu com alguma borda da tela
    if bola.top < 0 or bola.bottom > 480:
        velocidade[1] *= -1

    if bola.left < 0 or bola.right > 640:
        velocidade[0] *= -1

    # Desenha a bolinha
    pygame.draw.rect(tela, (255, 255, 255), bola)

    # Atualiza a tela
    pygame.display.update()

    # Verifica se o usuário fechou a janela
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
