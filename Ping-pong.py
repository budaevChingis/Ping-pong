from pygame import*
font.init()
window = display.set_mode((1000, 700))
display.set_caption('Пинг Понг')

font1 = font.SysFont('Courier New', 60)
win1 = font1.render('LEFT PLAYER WIN', True, (0, 255, 0))
win2 = font1.render('RIGHT PLAYER WIN', True, (0, 255, 0))


background = transform.scale(image.load('Group1.png'), (1000, 700))

class GameSprite(sprite.Sprite):
    def __init__(self, p_image, x, y, speed, w, h):
        super().__init__()
        self.image = transform.scale(image.load(p_image), (w, h))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.w = w
        self.h = h
    def resat(self):
        window.blit(self.image, (self.rect.x , self.rect.y))

class Player(GameSprite):
    def update1(self):
        kays = key.get_pressed()
        if kays[K_w] and self.rect.y > 25:
            self.rect.y -= self.speed
        if kays[K_s] and self.rect.y < 555:
            self.rect.y += self.speed 

    def update2(self):
        kays = key.get_pressed()
        if kays[K_UP] and self.rect.y > 25:
            self.rect.y -= self.speed
        if kays[K_DOWN] and self.rect.y < 555:
            self.rect.y += self.speed 


class Ball(GameSprite):
    def __init__(self, p_image, x, y, speed, w, h, speed_y):
        super().__init__(p_image, x, y, speed, w, h)
        self.speed_y = speed_y
    def updateB(self):
        self.rect.x += self.speed 
        self.rect.y += self.speed_y 
        if self.rect.y < 25 or self.rect.y > 645:
            self.speed_y *= -1  
          
        
    
    

Racket1 = Player('racketL.png', 20, 500, 20, 30, 120)
Racket2 = Player('racketR.png', 950, 500, 20, 30, 120)
Ball = Ball('ball.png', 50, 50, 5, 40, 40, -5)

#sprite.collide_rect(a, b)

finish = False
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.blit(background, (0, 0))
        Racket1.update1()
        Racket1.resat()
        Racket2.update2()
        Racket2.resat()
        Ball.updateB()
        Ball.resat()
        if sprite.collide_rect(Racket1, Ball) or sprite.collide_rect(Racket2, Ball):
            Ball.speed *= -1
        
        if Ball.rect.x < 0:
            window.blit(win2, (260, 200))
            finish = True
        if Ball.rect.x > 990:
            window.blit(win1, (260, 200))
            finish = True
    

    time.delay(10)
    display.update()
    

    

        
