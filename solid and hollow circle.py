import pygame

pygame.init()

dis=pygame.display.set_mode((500,500))

green=(0,255,0)

green=(0,255,0)

pygame.draw.circle(dis,green,(300,300),50)

pygame.draw.circle(dis,green,(100,100),50,3)


d=False

while not d:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True



    pygame.display.flip()