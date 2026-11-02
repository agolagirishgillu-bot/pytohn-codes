import pygame
import random

pygame.init()

screen_height=500
screen_widht=400
mvt_spd=4

text=pygame.font.SysFont('Times New Roman',72)

background_image=pygame.transform.scale(
    pygame.image.load(''),screen_height,screen_widht)

class Sprite(pygame.sprite.Sprite):

    def __init__(self,color,height,width):

        super().__init__()

        self.image=pygame.surface([screen_widht,screen_height])
        self.image.fill(pygame.Color('lightblue'))

        pygame.draw.rect(self.image,color,self.Rect(0,0,width,height))

        self.rect=self.image.get_rect()


    def move(self,x_chng,y_chng):
         self.rect.x=max((min,self.rect.x+x_chng,screen_height-self.rect.width),0)
         self.rect.y=max((min,self.rect.y+y_chng,screen_height-self.rect.height),0)

screen=pygame.display.set_mode((screen_height,screen_widht))

pygame.display.set_caption('Colliding Sprites')

all_sprite=pygame.sprite.Group()

sprite1=Sprite(pygame.Color('black'),20,30)
sprite1.rect.x,sprite1.rect.y=random.randint(0,screen_widht-sprite1.rect.widht),random.randint(0,screen_height-sprite1.rect.height)

sprite2=Sprite(pygame.Color('red'),20,30)
sprite2.rect.x,sprite1.rect.y=random.randint(0,screen_widht-sprite2.rect.widht),random.randint(0,screen_height-sprite2.rect.height)

all_sprite.add(sprite2)

a=False
collide=False

while not a