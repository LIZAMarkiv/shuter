import pygame
import random
import time
from helper import*
from shop import*

destroyed_enemy = 0
missed_enemy = 0

def start_game():
    global missed_enemy,destroyed_enemy
    data = read_file()
    save_file(data)

    pygame.init()
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
        global missed_enemy

        def __init__(self, x, y, texture, speed, w, h):
            self.direction = "forward"
            self.texture = pygame.image.load(texture)
            self.texture = pygame.transform.scale(self.texture, [w, h])
            self.hitbox = self.texture.get_rect()
            self.x = x
            self.y = y
            self.speed = speed

        def draw(self, window):
            window.blit(self.texture, self.hitbox)

        def update(self):
            global missed_enemy
            self.hitbox.y += self.speed
            if self.hitbox.y > 500:
                self.hitbox.y = -100
                self.hitbox.x = random.randint(1, 600)
                missed_enemy += 1


    class Ufo():
        global missed_enemy
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
            global missed_enemy
            self.hitbox.y += self.speed
            if self.hitbox.y > 500:
                self.hitbox.y = -100
                self.hitbox.x = random.randint(1,600)
                missed_enemy +=1



    class Moneta():
        def __init__(self, x, y, texture, speed, w, h):
            self.texture = pygame.image.load(texture)
            self.texture = pygame.transform.scale(self.texture, [w, h])
            self.hitbox = self.texture.get_rect()
            self.x = x
            self.y = y
            self.speed = speed

        def draw(self, window):
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

    ufos = []
    for i in range(10):
       ufos.append(Ufo(random.randint(10,600),random.randint(-100,200),"ufo (1).png",5,50,50))

    asteroids = []
    for a in range(5):
        asteroids.append(Asteroid(random.randint(10,600),random.randint(-100,200),"asteroid (1).png",5,50,50))

    monetas = []
    for m in range(3):
        monetas.append(Moneta(random.randint(10,600),-100,"image-removebg-preview (1).png",5,40,40))


    pygame.mixer.init()
    pygame.mixer.music.load("space (1).ogg")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(2)

    fire = pygame.mixer.Sound("fire (1).ogg")

    background_img = pygame.image.load("galaxy (1).jpg")
    background_img = pygame.transform.scale(background_img, [700,500])
    window = pygame.display.set_mode([700,500])
    clock = pygame.time.Clock()
    game = True
    start_time = 0
    speed_efect = False
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        fire.play()


        for ballet in rocket.ballets[:]:
            for ufo in ufos[:]:
                if ballet.hitbox.colliderect(ufo.hitbox):
                    rocket.ballets.remove(ballet)
                    ufo.hitbox.y = -100
                    ufo.hitbox.x = random.randint(0,600)
                    destroyed_enemy+=1

                    data = read_file()
                    data["money"] += 1
                    save_file(data)
                    break

        for ballet in rocket.ballets[:]:
            for asteroid in asteroids[:]:
                if ballet.hitbox.colliderect(asteroid.hitbox):
                    rocket.ballets.remove(ballet)
                    asteroid.hitbox.y = -100
                    asteroid.hitbox.x = random.randint(0, 600)
                    destroyed_enemy += 1
                    data = read_file()
                    data["money"] += 1
                    save_file(data)

                    break
        for monet in monetas[:]:
            if monet.hitbox.colliderect(rocket.hitbox):
                for asteroid in asteroids:
                    asteroid.speed = 3
                for ufo in ufos:
                    ufo.speed = 3
                    speed_efect = True
                    start_time = time.time()

                monetas.remove(monet)

        if speed_efect == True:
            if time.time() - start_time > 15:
                speed_efect = False
                for asteroid in asteroids:
                    asteroid.speed = 5
                for ufo in ufos:
                    ufo.speed =5




        destroyed_text = pygame.font.Font(None, 20).render("Знищено:" + str(destroyed_enemy), True, [0, 255, 255])
        missed_text = pygame.font.Font(None, 20).render("Пропущено:" + str(missed_enemy), True, [0, 255, 255])
        window.blit(background_img, [0, 0])
        rocket.update()
        rocket.draw(window)
        for i in monetas:
            i.update()
            i.draw(window)

        window.blit(destroyed_text,[0,0])
        window.blit(missed_text, [0, 20])
        for u in ufos:
            u.update()
            u.draw(window)
        for t in asteroids:
            t.update()
            t.draw(window)
        pygame.display.flip()
        clock.tick(60)