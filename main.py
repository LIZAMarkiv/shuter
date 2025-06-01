import pygame


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
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.hitbox.x -= self.speed
        if keys[pygame.K_d]:
            self.hitbox.x += self.speed




class Asteroid(OurClass):
    def update(self):
        pass

class Ufo(OurClass):
    def __init__(self, x1,x2,texture,speed,w,h):
        self

    def update(self):


class Ballet(OurClass):
    def update(self):
        pass



rocket = Rocket(300,380,5,"rocket (1).png",80,110)
asteroid = Asteroid(500,200,0,"asteroid (1).png",50,50)
ufo = Ufo(400,150,0, "ufo (1).png", 50,50)
ballet = Ballet(330,320,0,"bullet (1).png", 30,60)






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
    window.blit(background_img, [0, 0])
    rocket.update()
    rocket.draw(window)
    asteroid.draw(window)
    ufo.draw(window)
    ballet.draw(window)
    pygame.display.flip()
    clock.tick(60)