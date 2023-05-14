from pygame import*

window = display.set_mode((1000, 700))
display.set_caption('Пинг Понг')


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
    def updateB(self):
        
        
        self.rect.x += self.speed 
        self.rect.y += self.speed 
        '''if self.rect.y < 25 or self.rect.y > 645:
            self.diry *= -1 '''       
        
    
    

Racket1 = Player('racketL.png', 20, 500, 20, 30, 120)
Racket2 = Player('racketR.png', 950, 500, 20, 30, 120)
Ball = Ball('ball.png', 50, 50, 20, 40, 40)



game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    window.blit(background, (0, 0))
    Racket1.update1()
    Racket1.resat()
    Racket2.update2()
    Racket2.resat()
    Ball.updateB()
    Ball.resat()

    time.delay(50)
    display.update()
    

    

        
