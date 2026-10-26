import pygame

pygame.init()

display1=pygame.display.set_mode((400,300))

done=False

while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True



    pygame.draw.rect(display1,(0,125,225),pygame.Rect(50,50,100,100))

    pygame.display.flip()

    