import sys
import pygame


pygame.init()

tela = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Space Invaders")

#Colors
ROXO = (128,0,128)
PRETO = (0,0,0)

#Square size
x = 100
y = 100
tamanho = 50
velocidade = 10




rodando = True
while rodando:
  pygame.time.delay(50)
  
  for evento in pygame.event.get():
    if evento.type == pygame.QUIT:
      rodando = False
  teclas = pygame.key.get_pressed()
  if teclas[pygame.K_UP] or teclas[pygame.K_w]:
    y -= velocidade

  if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
    x -= velocidade

  if teclas[pygame.K_DOWN] or teclas[pygame.K_s]:
    y += velocidade

  if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
    x += velocidade
  tela.fill((PRETO))
  pygame.draw.rect(tela, ROXO, (x ,y , tamanho, tamanho))
  pygame.display.update()

pygame.quit()
