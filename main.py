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
        self.coin_vel = 50
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

    def coin_motion(self, delta_time):
        movement = self.coin_vel * delta_time
        
        self.coin_x -= movement
        self.coin_rect.topleft = (self.coin_x, self.coin_y)
            

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.player_x = 40
        self.player_y = 200
        self.player_vel = 300
        
        self.count = 0

        self._trainEng_surf = pygame.image.load("./Assets/train_v18.gif").convert()
        self._trainCar_surf = pygame.image.load("./Assets/carriage_v18_car5.gif").convert()
        self._smokeStack = [pygame.image.load("./Assets/SM000_nyknck_img1.png"), pygame.image.load("./Assets/SM000_nyknck_img2.png"), pygame.image.load("./Assets/SM000_nyknck_img3.png"), pygame.image.load("./Assets/SM000_nyknck_img4.png")]
        
        self.player_rect = self._trainEng_surf.get_rect(topleft = (self.player_x, self.player_y))
        

    def on_movement(self, delta_time):
        movement = self.player_vel * delta_time

        if keys[pygame.K_UP] and self.player_y >= -25:
            self.player_y -= movement
            self.player_rect.topleft = (self.player_x, self.player_y)
        if keys[pygame.K_DOWN] and self.player_y <= 350:
            self.player_y += movement
            self.player_rect.topleft = (self.player_x, self.player_y)
        if keys[pygame.K_LEFT] and self.player_x >= -150:
            self.player_x -= movement
            self.player_rect.topleft = (self.player_x, self.player_y)
        if keys[pygame.K_RIGHT] and self.player_x <= 700:
            self.player_x += movement
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
        self.ammo_vel = 250
        self.count = 0
        self.cooldown = 500
        self.lastFired = 0

        self._fireBall = [pygame.image.load("./Assets/FB001.png"), pygame.image.load("./Assets/FB002.png"), pygame.image.load("./Assets/FB003.png"), pygame.image.load("./Assets/FB004.png"), pygame.image.load("./Assets/FB005.png")]
        self.fire_rect = self._fireBall[0].get_rect(topleft = (self.ammo_x,self.ammo_y) )
    
    def draw(self):
        if self.count + 1 >= 30:
            self.count = 0
        
        display_surf.blit(self._fireBall[self.count//6], (self.ammo_x, self.ammo_y))

        self.count += 1

        #pygame.draw.rect(display_surf, (255,0,0), self.fire_rect, 2)
         
    def on_shoot(self, delta_time):
        time = pygame.time.get_ticks()
        movement = self.ammo_vel * delta_time
        #Second half adds a delay to prevent too many fireballs being added at once. 
        if keys[pygame.K_SPACE] and (time - self.lastFired >= self.cooldown):
            self.ammo_total.append(Fireball())
            self.lastFired = time
        for ammo in range(len(self.ammo_total)):
            if fireball.ammo_x < 700:
                self.ammo_total[ammo].draw()
        
                # if time % 2 == 0:
                self.ammo_total[ammo].ammo_x += movement
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
        self.BC_vel = 75
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
    
    def cow_motion(self, delta_time):
        movement = self.BC_vel * delta_time


        self.BC_x -= movement
        self.baby_cow_rect.topleft = (self.BC_x, self.BC_y)


class BossAlien():
    def __init__(self):
        self.BossA_x = 470
        self.BossA_y = 70
        self.BossA_vel = 100
        
        self.count = 0

        self.movingDown = True

        self.boss_alien_surf = pygame.image.load('./Assets/greenUFO.png')
        self.boss_alien = pygame.transform.scale_by(self.boss_alien_surf, .3)

        self.boss_alien_rect = self.boss_alien.get_rect(topleft = (self.BossA_x,self.BossA_y))


    def draw(self):
        #Draw Ship
        display_surf.blit(self.boss_alien, (self.BossA_x, self.BossA_y))
        pygame.draw.rect(display_surf, (255,0,0), self.boss_alien_rect, 2)

    
    def moveShip(self, delta_time):
        movement = self.BossA_vel * delta_time

        if(self.movingDown):
            self.BossA_y += movement
            if(self.BossA_y >= 350):
                self.movingDown = False
        else:
            self.BossA_y -= movement
            if(self.BossA_y <=-50):
                self.movingDown = True
        self.boss_alien_rect.topleft = (self.BossA_x, self.BossA_y)
            

class BossFireBall():
    def __init__(self):
        self.shootX = boss_alien.BossA_x - 50
        self.shootY = boss_alien.BossA_y
        self.shoot_vel = 150
        self.shoot = False
        self.count = 0

        self.alien_fireball_surf = [pygame.image.load('./Assets/FireBeam_01.png'),pygame.image.load('./Assets/FireBeam_02.png'),pygame.image.load('./Assets/FireBeam_03.png')]
        self.alien_fireball_rect = self.alien_fireball_surf[0].get_rect(topleft = (self.shootX, self.shootY))

    def draw(self):
        #Draw ships fireballs
        if(self.shoot):
            if self.count + 1 >= 18:
                self.count = 0
        
            display_surf.blit(self.alien_fireball_surf[self.count//6], (self.shootX, self.shootY))

            self.count += 1

            pygame.draw.rect(display_surf, (255,0,0), self.alien_fireball_rect, 2)

    def shootFireball(self, detla_time):
        self.shoot = True

        movement = self.shoot_vel * delta_time

        self.shootX -= movement
        self.alien_fireball_rect.topleft = (self.shootX, self.shootY)

    def player_collied(self):
        pass

#Need to shoot laser on timer after boss is beyond half health
class BossLaser():
    def __init__(self):
        self.laserX = boss_alien.BossA_x
        self.laserY = boss_alien.BossA_y
        self.alien_laser_surf = [pygame.image.load('./Assets/LaserShot_01.png'),pygame.image.load('./Assets/LaserShot_02.png'),pygame.image.load('./Assets/LaserShot_03.png'),pygame.image.load('./Assets/LaserShot_04.png'),pygame.image.load('./Assets/LaserShot_05.png'),pygame.image.load('./Assets/LaserShot_06.png'),pygame.image.load('./Assets/LaserShot_07.png')]
        self.alien_laser_rect = self.alien_laser_surf[0].get_rect(topleft = (self.laserX, self.laserY))
        self.count = 0

    def draw(self):
        if self.count + 1 >= 49:
            self.count = 0
            
        display_surf.blit(self.alien_laser_surf[self.count % 6], (self.laserX,self.laserY))
        count += 1

        pygame.draw.rect(display_surf, (255,0,0), self.alien_laser_rect, 2)

    def shoot_laser(self):
        pass

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

    def move(self, delta_time):
        movement = self.power_vel * delta_time

        self.power_x -= movement
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
boss_alien = BossAlien()
boss_fireball = BossFireBall()
fireball = Fireball()
score = Scoreboard()
power_up = PowerUp()
power_up_timer = Timer(10000)


coin_timer = pygame.event.custom_type()
pygame.time.set_timer(coin_timer, 300)

cow_timer = pygame.event.custom_type()
pygame.time.set_timer(cow_timer, 500)

bossFireBall_timer = pygame.event.custom_type()
pygame.time.set_timer(bossFireBall_timer, 3000)


cows = []
coins = []
bFireBall = []

    

while (running):
    boss_total = 5
    clock = pygame.time.Clock()
    delta_time = clock.tick(60) / 1000.0
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

        if event.type == bossFireBall_timer:
            bFireBall.append(BossFireBall())
    
    player.draw()
    player.on_movement(delta_time)

    power_up.draw()
    power_up.move(delta_time)
    
    power_up.player_collide()

    if power_up.active:
        power_up_timer.update()

        if not power_up_timer.active:
            fireball.cooldown = 500
            power_up.active = False
    

    fireball.on_shoot(delta_time)

    if score.total < boss_total:
        for i in range(len(coins) - 1, -1, -1):
            coins[i].draw()
            coins[i].coin_motion(delta_time)
            if player.player_rect.colliderect(coins[i].coin_rect):
                score.total += 1
                coins.pop(i)

        for i in range(len(cows) - 1, -1, -1):
            cows[i].draw()
            cows[i].cow_motion(delta_time)
            if fireball.fire_rect.colliderect(cows[i].baby_cow_rect):

                score.total += 5
                cows.pop(i)

    if score.total >= boss_total:
        boss_alien.draw()
        boss_alien.moveShip(delta_time)

        for i in range(len(bFireBall) - 1, -1, -1):
            bFireBall[i].draw()
            bFireBall[i].shootFireball(delta_time)
            if player.player_rect.colliderect(bFireBall[i].alien_fireball_rect):
                #Change to player life rather than coins. Boss with disapear if you loose too many points.
                score.total -= 1
                bFireBall.pop(i)

    pygame.display.flip()
pygame.quit()