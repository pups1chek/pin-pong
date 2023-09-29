from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x , player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(65,65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect = player_x
        self.rect = player_y


window = display.set_mode((700,500))
display.set_caption('piiiing-pooooong')
background = transform.scale(image.load('background.jpg'), (700,500))
























game = True
finish = False


while game:
    for e in event.get():
        if e.tipe == QUIT:
            game = False

    if finish != True:
        window.blit(background,(0,0))

display.update()
