import pygame
import random

class OurClass():
    def __init__(self,x,y,speed,texture,w,h):
        self.texture = pygame.image.load(texture)
        self.texture = pygame.transform.scale(self.texture, [w,h])
        self.hitbox = self.texture.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y
        self.speed = speed



    def draw (self,window):
        window.blit(self.texture, self.hitbox)



class Rocket(OurClass):

    def __init__(self, x, y, speed, texture, w, h):
        self.texture = pygame.image.load(texture)
        self.texture = pygame.transform.scale(self.texture, [w, h])
        self.hitbox = self.texture.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y
        self.speed = speed
        self.ballets = []


    def draw (self,window):
        window.blit(self.texture, self.hitbox)

        for ballet in self.ballets:
            ballet.update()
            ballet.draw(window)
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.hitbox.x -= self.speed
        if keys[pygame.K_d]:
            self.hitbox.x += self.speed
        if keys[pygame.K_SPACE]:
            self.ballets.append(Ballet(self.hitbox.x+10, self.hitbox.y, 5 , "bullet (1).png",20,30))







class Asteroid(OurClass):
    def update(self):
        pass

class Ufo():
    def __init__(self,x,y, texture, speed, w, h):
        self.direction = "forward"
        self.texture = pygame.image.load(texture)
        self.texture = pygame.transform.scale(self.texture, [w, h])
        self.hitbox = self.texture.get_rect()
        self.x = x
        self.y = y
        self.speed = speed


    def draw (self,window):
        window.blit(self.texture, self.hitbox)

    def update(self):
        self.hitbox.y += self.speed
        if self.hitbox.y > 500:
            self.hitbox.y = -100
            self.hitbox.x = random.randint(1,600)






class Ballet(OurClass):
    def update(self):
        self.hitbox.y -= self.speed



rocket = Rocket(300,380,5,"rocket (1).png",80,110)
asteroid = Asteroid(500,200,0,"asteroid (1).png",50,50)
ufos = []
for i in range(20):
   ufos.append(Ufo(random.randint(10,600),random.randint(-100,200),"ufo (1).png",5,50,50))





# pygame.mixer.init()
# pygame.mixer.music.load("rocket (1).ogg")
# pygame.mixer.music.play(-1)
# pygame.mixer.music.set_volume(0.5)
#


background_img = pygame.image.load("galaxy (1).jpg")
background_img = pygame.transform.scale(background_img, [700,500])
window = pygame.display.set_mode([700,500])
clock = pygame.time.Clock()
game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    # if ufo.hitbox.colliderect(ballet.hitbox):
    #     ufo.hitbox.x.random.randint = (10,500)
    #     ufo.hitbox.y.random.randint = (10, 500)

    for ballet in rocket.ballets[:]:
        for ufo in ufos[:]:
            if ballet.hitbox.colliderect(ufo.hitbox):
                rocket.ballets.remove(ballet)
                ufo.hitbox.y = -100
                ufo.hitbox.x = random.randint(0,600)
                break


    window.blit(background_img, [0, 0])
    rocket.update()
    rocket.draw(window)
    asteroid.draw(window)
    for u in ufos:
        u.update()
        u.draw(window)

    pygame.display.flip()
    clock.tick(60)