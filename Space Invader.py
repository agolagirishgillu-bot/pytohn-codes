import pygame
import math
import random

player_position_x=370
player_position_y=380
screen_width=500
screen_height=500
enmy_start_min_y=50
enmy_start_max_y=150
enmy_spd_x=4
enmy_spd_y=50
bullet_spd_y=40
collide_distance=27

pygame.init()

screen=pygame.display.set_mode((screen_height,screen_width))

background_img=pygame.image.load('')

pygame.display.set_caption('Space Invader')

icon=pygame.image.load('')
pygame.display.set_icon(icon)

player_img=pygame.image.load('')

player_x=player_position_x
player_y=player_position_y

playerx_chng=0

enmy_img=[]
enmy_x=[]
enmy_y=[]
enmyx_chng=[]
enmy_y_chng=[]
num_enmy=6

for i in range(num_enmy):
    enmy_img.append(pygame.image.load(''))
    enmy_x.append(random.randint(0,screen_width-64))
    enmy_y.append(random.randint(enmy_start_min_y,enmy_start_max_y))
    enmy_x.append(enmy_spd_x)
    enmy_y.append(enmy_spd_y)


bllt_img=pygame.image.load('')

bllt_x=0
bllt_start_y=player_position_y

bllt_x_chng=0
bllt_y_chng=bullet_spd_y
bllt_state='ready'

scr=0

fnt=pygame.font.Font('freesansbold.ttf',64)

txt_x=10
txt_y=10

def show_score(x,y):
    scr=fnt.render('Score :', +str(scr),True,255,255,255)