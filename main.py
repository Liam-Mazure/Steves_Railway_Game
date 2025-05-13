import pygame
import random as rand


pygame.init()
running = True
player_fire = False
size = weight,height = 640,400
display_surf = pygame.display.set_mode(size, pygame.HWSURFACE)
clock = pygame.time.Clock()


background_surf = pygame.image.load("./Assets/pixle_landscape.png").convert()
finalBackground_surf = pygame.transform.scale_by(background_surf, 1.25)


class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.coin_x = x
        self.coin_y = y
        self.coin_vel = .5
        self.total_coin = 100
        self.coin_list = []
        self.count = 0
        self._coin_surf = [pygame.image.load("./Assets/SilverCoin_Img1.png"), pygame.image.load("./Assets/SilverCoin_Img2.png"), pygame.image.load("./Assets/SilverCoin_Img3.png"), pygame.image.load("./Assets/SilverCoin_Img4.png"), pygame.image.load("./Assets/SilverCoin_Img5.png")]
        self.coin_rect = self._coin_surf[0].get_rect(topleft = (x,y))


    def draw(self):

        if self.count + 1 >= 30:
            self.count = 0
        
        display_surf.blit(self._coin_surf[self.count//6], (self.coin_x, self.coin_y))
        self.count += 1

        #pygame.draw.rect(display_surf, (255,0,0), self.coin_rect, 2)

    def coin_motion(self):
        time = pygame.time.get_ticks()
        
        if time % 2 == 0:
            self.coin_x -= self.coin_vel
            self.coin_rect.topleft = (self.coin_x, self.coin_y)
            

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.player_x = 220
        self.player_y = 200
        self.player_vel = 5
        
        self.count = 0

        self._trainEng_surf = pygame.image.load("./Assets/train_v18.gif").convert()
        self._trainCar_surf = pygame.image.load("./Assets/carriage_v18_car5.gif").convert()
        self._smokeStack = [pygame.image.load("./Assets/SM000_nyknck_img1.png"), pygame.image.load("./Assets/SM000_nyknck_img2.png"), pygame.image.load("./Assets/SM000_nyknck_img3.png"), pygame.image.load("./Assets/SM000_nyknck_img4.png")]
        
        self.player_rect = self._trainEng_surf.get_rect(topleft = (self.player_x, self.player_y))
        

    def on_movement(self):

        if keys[pygame.K_UP] and self.player_y >= -25:
            self.player_y -= self.player_vel
            self.player_rect.topleft = (self.player_x, self.player_y)
        if keys[pygame.K_DOWN] and self.player_y <= 350:
            self.player_y += self.player_vel
            self.player_rect.topleft = (self.player_x, self.player_y)
        if keys[pygame.K_LEFT] and self.player_x >= -150:
            self.player_x -= self.player_vel
            self.player_rect.topleft = (self.player_x, self.player_y)
        if keys[pygame.K_RIGHT] and self.player_x <= 700:
            self.player_x += self.player_vel
            self.player_rect.topleft = (self.player_x, self.player_y)

    def draw(self):
        display_surf.blit(self._trainEng_surf, (self.player_x, self.player_y))
        display_surf.blit(self._trainCar_surf, (self.player_x - 250, self.player_y))


        if self.count + 1 >= 24:
            self.count = 0
        
        display_surf.blit(self._smokeStack[self.count//6], (self.player_x + 200, self.player_y - 75))

        self.count += 1

        # pygame.draw.rect(display_surf, (255,0,0), self.player_rect, 2)

class Fireball():
    def __init__(self):
        self.ammo_total = []
        self.ammo_x = player.player_rect.x + 200
        self.ammo_y = player.player_rect.y + 10
        self.ammo_vel = 10
        self.count = 0
        self.cooldown = 500
        self.lastFired = 0

        self._fireBall = [pygame.image.load("./Assets/FB001.png"), pygame.image.load("./Assets/FB002.png"), pygame.image.load("./Assets/FB003.png"), pygame.image.load("./Assets/FB004.png"), pygame.image.load("./Assets/FB005.png")]
        self.fire_rect = self._fireBall[0].get_rect(topleft = (self.ammo_x,self.ammo_y) )
    
    def draw(self):
        if self.count + 1 >= 24:
            self.count = 0
        
        display_surf.blit(self._fireBall[self.count//6], (self.ammo_x, self.ammo_y))

        self.count += 1

        #pygame.draw.rect(display_surf, (255,0,0), self.fire_rect, 2)
         
    def on_shoot(self):
        time = pygame.time.get_ticks()
        #Second half adds a delay to prevent too many fireballs being added at once. 
        if keys[pygame.K_SPACE] and (time - self.lastFired >= self.cooldown):
            self.ammo_total.append(Fireball())
            self.lastFired = time
        for ammo in range(len(self.ammo_total)):
            if fireball.ammo_x < 700:
                self.ammo_total[ammo].draw()
        
                if time % 2 == 0:
                    self.ammo_total[ammo].ammo_x += self.ammo_total[ammo].ammo_vel
                    self.fire_rect.topleft = (self.ammo_total[ammo].ammo_x  , self.ammo_total[ammo].ammo_y)
            else:
                fireball.ammo_x = self.ammo_x
                fireball.ammo_y = self.ammo_y

class Scoreboard():
    def __init__(self):
        self.total = 0
        self.score_font = pygame.font.Font(None, 36)
        self.score_text = None
    def render(self):
        self.score_text = self.score_font.render("Total Score: " + str(self.total), True, (0,0,0))
        display_surf.blit(self.score_text, (10,10))
    def add_score(self):
        self.total += 1

class BabyCow():
    def __init__(self, x, y):
        self.BC_x = x
        self.BC_y = y
        self.BC_vel = 1
        self.count = 0

        self.baby_cow_surf = [pygame.image.load('./Assets/CowSpriteLeft1.png'),pygame.image.load('./Assets/CowSpriteLeft2.png'), pygame.image.load('./Assets/CowSpriteLeft3.png')]
        self.baby_cow_dead_surf = pygame.image.load('./Assets/CowSpriteLeftDead.png')

        self.baby_cow_rect = self.baby_cow_surf[0].get_rect(topleft = (self.BC_x,self.BC_y))

    def draw(self):
        if self.count + 1 >= 18:
            self.count = 0
        display_surf.blit(self.baby_cow_surf[self.count // 6], (self.BC_x, self.BC_y))
        self.count += 1

        #pygame.draw.rect(display_surf, (255,0,0), self.baby_cow_rect, 2)
    
    def cow_motion(self):
        time = pygame.time.get_ticks()

        if time % 2 == 0:
            self.BC_x -= self.BC_vel
            self.baby_cow_rect.topleft = (self.BC_x, self.BC_y)

    def bcow_hit(self):
        pass

#Change to another image(alien ship?)
class BossCow():
    def __init__(self):
        self.BossC_x = 300
        self.BossC_y = 50
        self.BossC_vel = 1
        self.count = 0

        self.boss_cow_surf = pygame.image.load('./Assets/CowSpriteLeft1.png')
        self.boss_cow = pygame.transform.scale_by(self.boss_cow_surf, 20)
        self.boss_cow_dead_surf = pygame.image.load('./Assets/CowSpriteLeftDead.png')

        self.boss_cow_rect = self.boss_cow.get_rect(topleft = (self.BossC_x,self.BossC_y))

    def draw(self):
        display_surf.blit(self.boss_cow, (self.BossC_x, self.BossC_y))

class PowerUp():
    def __init__(self):
        self.power_x = rand.randint(2000, 5000)
        self.power_y = rand.randint(10, 380)
        self.power_vel = 2
        self.gas_can_surf = pygame.image.load('./Assets/medium_fuel_red.png')
        self.gas_can = pygame.transform.scale_by(self.gas_can_surf, .1)
        self.gas_rect = self.gas_can.get_rect(topleft = (self.power_x, self.power_y))
        self.active = False

    def draw(self):
        display_surf.blit(self.gas_can, (self.power_x, self.power_y))

        # pygame.draw.rect(display_surf, (255,0,0), self.gas_rect, 2)

    def move(self):
        time = pygame.time.get_ticks()

        if time % 2 == 0:
            self.power_x -= self.power_vel
            self.gas_rect.topleft = (self.power_x, self.power_y)

    def player_collide(self):
        if player.player_rect.colliderect(self.gas_rect):
            fireball.cooldown = 0
            self.active = True
            power_up_timer.activate()
            self.gas_can.fill((0,0,0,0))


class Timer():
    def __init__(self, duration):
        self.duration = duration
        self.start_time = 0
        self.active = False

    def activate(self):
        self.active = True
        self.start_time = pygame.time.get_ticks()

    def deactivate(self):
        self.active = False
        self.start_time = 0

    def update(self):
      if self.active:
          current_time = pygame.time.get_ticks()
          if current_time - self.start_time >= self.duration:
              self.deactivate()


player = Player()
boss_cow = BossCow()
fireball = Fireball()
score = Scoreboard()
power_up = PowerUp()
power_up_timer = Timer(10000)


coin_timer = pygame.event.custom_type()
pygame.time.set_timer(coin_timer, 300)

cow_timer = pygame.event.custom_type()
pygame.time.set_timer(cow_timer, 500)


cows = []
coins = []

    

while (running):
    display_surf.blit(finalBackground_surf, (0,0))
    score.render()
    keys = pygame.key.get_pressed()
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == coin_timer:
            x = rand.randint(630, 3000)
            y = rand.randint(0, 390)
            coins.append(Coin(x,y))
        
        if event.type == cow_timer:
            x = rand.randint(630, 3000)
            y = rand.randint(10, 380)
            cows.append(BabyCow(x,y))
    
    player.draw()
    player.on_movement()

    power_up.draw()
    power_up.move()
    
    power_up.player_collide()

    if power_up.active:
        power_up_timer.update()

        if not power_up_timer.active:
            fireball.cooldown = 500
            power_up.active = False
    

    fireball.on_shoot()

    for i in range(len(coins) - 1, -1, -1):
        coins[i].draw()
        coins[i].coin_motion()
        if player.player_rect.colliderect(coins[i].coin_rect):
            score.total += 1
            coins.pop(i)
    
    for i in range(len(cows) - 1, -1, -1):
        cows[i].draw()
        cows[i].cow_motion()
        if fireball.fire_rect.colliderect(cows[i].baby_cow_rect):

            score.total += 5
            cows.pop(i)

    if score.total >= 1000:
        boss_cow.draw()

    pygame.display.flip()
    clock.tick(60)
pygame.quit()