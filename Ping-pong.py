from pygame import*

window = display.set_mode((1000, 1000))
display.set_caption('Пинг Понг')


background = transform.scale(image.load('фон1.jpg'), (1000, 1000))

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
        if kays[K_w] and self.rect.x <990:
            self.rect.x += self.speed
        if kays[K_s] and self.rect.x > 10:
            self.rect.x -= self.speed 

    def update2(self):
        kays = key.get_pressed()
        if kays[K_UP] and self.rect.x <990:
            self.rect.x += self.speed
        if kays[K_DOWN] and self.rect.x > 10:
            self.rect.x -= self.speed 
        
    

#Racket1 = Playr()
#racket2 = 
#ball = 



game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    window.blit(background, (0, 0))

    time.delay(50)
    display.update()
    

    

        
