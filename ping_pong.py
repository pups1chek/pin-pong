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

rocket1 = Player('rocket.jpg', 30,200, 5 )
rocket2 = Player('rocket.jpg', 500,200,5)
ball = GameSprite('ball.png', 200,200, 5)

game = True
finish = False
ball_speed_x = 5
ball_speed_y = 5

font.init()
font = font.Font('Arial', 60)

lose1 = font.render('lose player 1', True, (255, 0, 0))
lose2 = font.render('lose player 2', True, (255,0,0))

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.blit(background,(0,0))
        rocket1.update_r()
        rocket2.update_l()    
        ball.rect.x += ball_speed_x
        ball.rect.y += ball_speed_y
    
        if sprite.collide_rect(rocket1,ball) or sprite.collide_rect(rocket2,ball):
            ball_speed_x *= -1
            ball_speed_y *= -1

        if ball.rect.y > 450 or ball.rect.y < 0:
            ball_speed_y *= -1

        if ball.rect.x > 650:
            finish = True
            window.blit(lose2, (200,200))
        if ball.rect.x < 0 :
            finish = True
            window.blit(lose1, (200,200))




        
display.update()
