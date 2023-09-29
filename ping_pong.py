from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x , player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(65,65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect = player_x
        self.rect = player_y
class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP]:
            self.rect.x += self.speed
        if keys[K_DOWN]:
            self.rect.y -= self.speed
    def update_l(self):
         keys = key.get_pressed()
        if keys[K_w]:
            self.rect.x += self.speed
        if keys[K_s]:
            self.rect.y -= self.speed


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
