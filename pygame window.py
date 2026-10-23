import  pygame 

pygame.init()

screen=pygame.display.set_mode((400,500))


done=False

while not done:

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit

text=pygame.font.Font(None,36).render('Hello',True,pygame.Color('white'))

text_rect=text.get_rect(center=(200,300))


pygame.display.flip