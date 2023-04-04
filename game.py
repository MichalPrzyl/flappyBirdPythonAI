import pygame
from globals import MAX_HEIGHT, MAX_WIDTH, PLAYER_WIDTH, PLAYER_HEIGHT,\
    NEW_PIPE_INTERVAL
from player import Player
from pipe import PipeManager


pygame.init()
screen = pygame.display.set_mode((MAX_WIDTH, MAX_HEIGHT))
clock = pygame.time.Clock()
running = True

player = Player()
start_ticks=pygame.time.get_ticks()
while running:
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.key.key_code("Space"):
                player.jump()

    screen.fill("gray")

    # RENDER YOUR GAME HERE
    position = pygame.Rect(player.pos_x, player.pos_y, PLAYER_WIDTH, PLAYER_HEIGHT)
    pygame.draw.rect(screen, "blue", position)
    player.apply_gravity()
    if player.check_collisions():
        font = pygame.font.SysFont(None, 72)
        img = font.render('GAME OVER', True, "red")
        screen.blit(img, (MAX_WIDTH/2, MAX_HEIGHT/2))

    seconds=(pygame.time.get_ticks()-start_ticks)/1000 #calculate how many seconds
    if seconds > NEW_PIPE_INTERVAL:
        pipe = PipeManager.create_pipe()
        start_ticks=pygame.time.get_ticks()

    for pipe_instance in PipeManager.pipes:
        pipe_instance.draw(screen)        
        pipe_instance.update()
    PipeManager.cleanup()

    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()