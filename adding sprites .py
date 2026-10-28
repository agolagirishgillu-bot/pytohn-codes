import pygame
import random

pygame.init()

Sprite_color_change=pygame.USEREVENT +1
BACKGROUND_COLOR=pygame.USEREVENT +2

blue=pygame.Color('blue')
red=pygame.Color('red')
green=pygame.Color('green')

yellow=pygame.Color('yellow')
orange=pygame.Color('orange')
lightblue=pygame.Color('lightblue')
WHITE=pygame.Color('white')

class sprite(pygame.sprite.Sprite):

    def __init__(self,color,height,widht):
        super().__init__()

        self.image=pygame.surface[(height,widht)]
        self.image.fill(color)

        self.rect=self.image.get_rect()

        self.velocity=[random.choice([-1,1]),random.choice([-1,1])]

    def upd(self):

        self.rect.move_ip(self.velocity)

        b_h=False

        if self.rect.left <=0 or self.rect.right >=500:
            self.velocity[0]=-self.velocity[0]

            b_h=True

        if self.rect.top<=0 or self.rect.bottom >=0:
            self.velocity[1]=-self.velocity[1]

            b_h=True


        if b_h:
            pygame.event.post(pygame.event.Event[Sprite_color_change])
            pygame.event.post(pygame.event.Event[BACKGROUND_COLOR])


    def change_color(self):
        self.image.fill(random.choice[yellow,orange,lightblue])


    def b_c_c(self):
        global b_g_color

        b_g_color=random.choice([red,blue,green])


all_sprite_list=pygame.sprite.Group()

sp1=sprite(WHITE,20,30)

