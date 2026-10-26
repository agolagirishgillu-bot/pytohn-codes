import pygame

def main():
    pygame.init()

    s_w=500
    s_h=500

    dis=pygame.display.set_mode((s_w,s_h))
    pygame.display.set_caption('Changing color sprite')

    colors={
        'red':pygame.Color('red'),
        'blue':pygame.Color('blue'),
        'yellow':pygame.Color('yellow'),
        'green':pygame.Color('green'),
        'white':pygame.Color('white'),
    }
    current_color=colors['white']

    x,y=30,30
    sprite_height,sprite_lenght=60,60


    clock=pygame.time.Clock()
    d=False

    while not d:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                d=True


        p=pygame.key.get_pressed()
        if p[pygame.K_LEFT]:x-=3
        if p[pygame.K_RIGHT]:x+=3
        if p[pygame.K_UP]:y-=3
        if p[pygame.K_DOWN]:y+=3

        x=min(max(0,x),s_w-sprite_lenght)
        y=min(max(0,y),s_h-sprite_height)

    

        if x == 0:current_color=colors['green']
        elif x == s_w-sprite_lenght:current_color=colors['red']
        elif y == s_w-sprite_lenght:current_color=colors['blue']       
        elif y == 0:current_color=colors['yellow']
        else:
            current_color=colors['white']

        dis.fill((0,0,0))
        pygame.draw.rect(dis,current_color,(x,y,sprite_lenght,sprite_height))

        pygame.display.flip()

        clock.tick(90)

    pygame.quit()


if __name__=='__main__':
    main()