import pygame
import random as rand
import sys
import high_score

pygame.init()
player_fire = False
size = weight,height = 640,400
window_caption = pygame.display.set_caption("Steve's Railway")
display_surf = pygame.display.set_mode(size, pygame.HWSURFACE)
transparent_surf = pygame.Surface(size,pygame.SRCALPHA)

titleBG_surf = pygame.image.load("./Assets/StevesRailwayTitleScreen.png").convert()
endBG_surf = pygame.image.load("./Assets/StevesRailwayGOScreen.png").convert()
background_surf = pygame.image.load("./Assets/pixle_landscape.png").convert()
finalBackground_surf = pygame.transform.scale_by(background_surf, 1.25)

high_score_value = high_score.load_high_score()


def title_screen():
    title_running = True
    title_font = pygame.font.SysFont('Times New Roman', 60, bold=True)
    
    while(title_running):
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                title_running = False
            display_surf.blit(titleBG_surf, (0, 0))
            text = title_font.render("Press any to start", True, ('#0a1a58'))
            display_surf.blit(text, (100, 250))
        pygame.display.update()

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
        
                self.ammo_total[ammo].ammo_x += movement
                self.fire_rect.topleft = (self.ammo_total[ammo].ammo_x  , self.ammo_total[ammo].ammo_y)
            else:
                fireball.ammo_x = self.ammo_x
                fireball.ammo_y = self.ammo_y

class Scoreboard():
    def __init__(self):
        self.score_total = 0
        self.score_font = pygame.font.SysFont('Times New Roman', 20, bold=True)
        self.score_text = None

        self.enemy_alive = False
        self.boss_dead = False
        self.enemy_health_text = None
        self.enemy_health_bar_rect = None
        self.enemy_health = 100

        self.player_health_text = None
        self.player_health_bar_rect = None
        self.player_health = 100
        self.leftWindowScore_onPass_rect = None

    def render(self):
        self.score_text = self.score_font.render("Total Score: " + str(self.score_total), True, (243,140,5))
        display_surf.blit(self.score_text, (10,10))

        if self.enemy_alive:
            self.enemy_health_text = self.score_font.render("Enemy Health:", True, (243,140,5))
            display_surf.blit(self.enemy_health_text, (400, 10))
            self.enemy_health_bar_rect = pygame.draw.rect(display_surf, (200,0,0),(535,15,self.enemy_health,15))

        self.player_health_text = self.score_font.render("Health:", True, (243,140,5))
        display_surf.blit(self.player_health_text, (10, 30))
        self.player_health_bar_rect = pygame.draw.rect(display_surf, (0,200,0),(80,35,self.player_health,15))

        #Displayed on transparent surface to hide rect from player
        self.leftWindowScore_onPass_rect = pygame.draw.rect(transparent_surf,(0,0,0,0),(-5,0,10,400),2)

    def add_score(self):
        self.score_total += 1
        
    def player_lose_health(self, life_loss):
        if self.player_health > 0:
            self.player_health -= life_loss
            self.player_health_bar_rect = pygame.draw.rect(display_surf,(0,200,0),(80,35,self.player_health,15))
        else:
            global gameover 
            gameover = True

    def enemy_lose_health(self, life_loss):
        if self.enemy_health > 0:
            self.enemy_health -= life_loss
            self.enemy_health_bar_rect = pygame.draw.rect(display_surf,(200,0,0),(535,15,self.enemy_health,15))
        else:
            self.enemy_alive = False
            self.boss_dead = True
            self.score_total += 500


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
        self.health = 100
        
        self.count = 0

        self.movingDown = True

        self.boss_alien_surf = pygame.image.load('./Assets/greenUFO.png')
        self.boss_alien = pygame.transform.scale_by(self.boss_alien_surf, .3)

        self.boss_alien_rect = self.boss_alien.get_rect(topleft = (self.BossA_x,self.BossA_y))


    def draw(self):
        #Draw Ship
        display_surf.blit(self.boss_alien, (self.BossA_x, self.BossA_y))
        #pygame.draw.rect(display_surf, (255,0,0), self.boss_alien_rect, 2)

    
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

            #pygame.draw.rect(display_surf, (255,0,0), self.alien_fireball_rect, 2)

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
        self.power_x = rand.randint(5000, 10000)
        self.power_y = rand.randint(10, 380)
        self.power_vel = 50
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
 
def end_screen():
    gameOver_running = True
    gameOver_font = pygame.font.SysFont('Times New Roman', 30, bold=True)
    
    while(gameOver_running):
        display_surf.blit(titleBG_surf, (0, 0))
        text = gameOver_font.render("Press r to play again or q to quit", True, ('#0a1a58'))
        best_score_text = gameOver_font.render(f"High Score: {high_score_value}", True, ('#0a1a58'))
        display_surf.blit(best_score_text, (200, 300))
        display_surf.blit(text, (125, 250))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    pygame.event.clear()
                    title_screen()
                    start_game()
                    return
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
    
        pygame.display.update()

def start_game():
    
    global boss_alien,player,boss_fireball,fireball,score,power_up,power_up_timer,cows,coins,bFireBall,cow_timer,coin_timer,bossFireBall_timer

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
    pygame.time.set_timer(cow_timer, 1000)

    bossFireBall_timer = pygame.event.custom_type()
    pygame.time.set_timer(bossFireBall_timer, 3000)


    cows = []
    coins = []
    bFireBall = []

title_screen()
start_game() 

running = True
while (running):
    
    gameover = False
    boss_total = 1000
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

    if not score.enemy_alive:
        for i in range(len(coins) - 1, -1, -1):
            coins[i].draw()
            coins[i].coin_motion(delta_time)
            if player.player_rect.colliderect(coins[i].coin_rect):
                score.score_total += 1
                coins.pop(i)

        for i in range(len(cows) - 1, -1, -1):
            cows[i].draw()
            cows[i].cow_motion(delta_time)
            if fireball.fire_rect.colliderect(cows[i].baby_cow_rect):

                score.score_total += 5
                cows.pop(i)
                continue

            if score.leftWindowScore_onPass_rect.colliderect(cows[i].baby_cow_rect):

                score.player_lose_health(10)
                cows.pop(i)

        if score.score_total >= boss_total and not score.boss_dead:
            score.enemy_alive = True

    if score.enemy_alive:
        boss_alien.draw()
        boss_alien.moveShip(delta_time)

        for i in range(len(bFireBall) - 1, -1, -1):
            bFireBall[i].draw()
            bFireBall[i].shootFireball(delta_time)
            if player.player_rect.colliderect(bFireBall[i].alien_fireball_rect):
                score.player_lose_health(25)
                bFireBall.pop(i)
        
        for i in range(len(fireball.ammo_total) - 1, -1, -1):
            if fireball.fire_rect.colliderect(boss_alien.boss_alien_rect):
                fireball.ammo_total.pop(i)
                score.enemy_lose_health(2)
    
    #Checks if current user score is all time high score
    if score.score_total > high_score_value:
        high_score_value = score.score_total
        high_score.save_high_scores(high_score_value)
    
    if(gameover):
        display_surf.blit(endBG_surf,(0,0))
       
        end_screen()

    pygame.display.flip()

pygame.quit()