from pygame import *
from random import *
font.init()
pisat_bukvi = font.SysFont('Arial', 20)
glavni_bbukvi = font.SysFont('Arial', 72)
wind = display.set_mode((700, 500))
display.set_caption('пинг пионг')
z_fon = transform.scale(image.load('pink.jpg'), (700, 500))
global sf 
global sik 
global goroh
global struchok
global f
sik = 4
sf = 4
goroh = 0
struchok = 0
class GameCola(sprite.Sprite):
    def __init__(self, imageee, xxx, yyy, ckorast, razmer_1, razmer_2):
        super().__init__()
        self.razme1 = razmer_1
        self.razme2 = razmer_2
        self.image = transform.scale(image.load(imageee), (razmer_1, razmer_2))
        self.speed = ckorast
        self.rect = self.image.get_rect()
        self.rect.y = yyy
        self.rect.x = xxx
    def chino_hills(self):
        wind.blit(self.image, (self.rect.x, self.rect.y))
    def hussky(self):
        kon_prigaet = key.get_pressed()
        if kon_prigaet[K_w] and self.rect.y < 435:
            self.rect.x += self.speed
        if kon_prigaet[K_s] and self.rect.y > 0:
            self.rect.x -= self.speed

class Lamelo(GameCola):
    def beskonechno(self):
        if self.rect.x > 635 or self.rect.x < 0:
            global sf
            sf *= -1
        if self.rect.y > 435 or self. rect.y < 0:
            global sik
            sik *= -1

class Lonzo(GameCola):
    def hussky(self):
        kon_prigaet = key.get_pressed()
        if kon_prigaet[K_s] and self.rect.y < 400:
            self.rect.y += 4
        if kon_prigaet[K_w] and self.rect.y > 0:
            self.rect.y -= 4
    def player_2(self):
        kon_prigaet = key.get_pressed()
        if kon_prigaet[K_DOWN] and self.rect.y < 400:
            self.rect.y += 4
        if kon_prigaet[K_UP] and self.rect.y > 0:
            self.rect.y -= 4

ball = Lamelo('lameloball.png', 300, 300, 1, 65, 65)
lonzob = Lonzo('raketka_tipa.png', 100, 250, 1, 20, 100)
liangelo = Lonzo('raketka_tipa.png', 600, 250, 1, 20, 100)



FPS = 60
clock = time.Clock()
dodepchik = False
vrun = True   
kon_prigaet2 = key.get_pressed()
while vrun:
    for e in event.get():
        if e.type == QUIT:
            vrun = False
    if not dodepchik:
        wind.blit(z_fon, (0,0))
        ball.rect.x += sf
        ball.rect.y += sik
        ball.beskonechno()
        ball.chino_hills()
        lonzob.chino_hills()
        lonzob.hussky()
        liangelo.chino_hills()
        liangelo.player_2()
        if sprite.collide_rect(ball, lonzob):
            f = True
            if f == True:
                sf *= -1
                sf *= 1.1
                f = False
        if sprite.collide_rect(ball, liangelo):
            f = True
            if f == True:
                sf *= -1
                sf *= 1.1
                f = False
        if sf >= 10:
            dodepchik = True
            sf = 2
            wind.blit(z_fon, (0,0))
            ball.rect.x += sf
            ball.rect.y += sik
            ball.beskonechno()
            ball.chino_hills()
            lonzob.chino_hills()
            lonzob.hussky()
            liangelo.chino_hills()
            liangelo.player_2()
            goroh_tekst = pisat_bukvi.render('Счёт:' + str(goroh), 1, (0,0,0))
            struchok_tekst = pisat_bukvi.render('Счёт:' + str(struchok), 1, (0,0,0))
            wind.blit(struchok_tekst, (10, 20))
            wind.blit(goroh_tekst, (640, 20))
            dodepchik = False
        if ball.rect.x < 0:   
            goroh += 1
            dodepchik = True
            sf = 2
            wind.blit(z_fon, (0,0))
            ball.rect.x += sf
            ball.rect.y += sik
            ball.beskonechno()
            ball.chino_hills()
            lonzob.chino_hills()
            lonzob.hussky()
            liangelo.chino_hills()
            liangelo.player_2()
            goroh_tekst = pisat_bukvi.render('Счёт:' + str(goroh), 1, (0,0,0))
            struchok_tekst = pisat_bukvi.render('Счёт:' + str(struchok), 1, (0,0,0))
            wind.blit(struchok_tekst, (10, 20))
            wind.blit(goroh_tekst, (640, 20))
            ball.rect.x = 300
            ball.rect.y = 300
            dodepchik = False
            if goroh == 5:
                wind.blit(winner_winner_chicken_dinner2, (150, 300))
                dodepchik = True
        if ball.rect.x > 635:
            struchok += 1
            dodepchik = True
            sf = 1
            wind.blit(z_fon, (0,0))
            ball.rect.x += sf
            ball.rect.y += sik
            ball.beskonechno()
            ball.chino_hills()
            lonzob.chino_hills()
            lonzob.hussky()
            liangelo.chino_hills()
            liangelo.player_2()
            goroh_tekst = pisat_bukvi.render('Счёт:' + str(goroh), 1, (0,0,0))
            struchok_tekst = pisat_bukvi.render('Счёт:' + str(struchok), 1, (0,0,0))
            wind.blit(struchok_tekst, (10, 20))
            wind.blit(goroh_tekst, (640, 20))
            ball.rect.x = 300
            ball.rect.y = 300
            dodepchik = False
        if struchok == 5:
            wind.blit(winner_winner_chicken_dinner, (150, 300))
            dodepchik = True
        goroh_tekst = pisat_bukvi.render('Счёт:' + str(goroh), 1, (0,0,0))
        winner_winner_chicken_dinner = pisat_bukvi.render('player1 выиграл со счётом:' + str(struchok) + '/' + str(goroh),1, (0,0,0))
        winner_winner_chicken_dinner2 = pisat_bukvi.render('player2 выиграл со счётом:' + str(struchok) + '/' + str(goroh),1, (0,0,0))
        struchok_tekst = pisat_bukvi.render('Счёт:' + str(struchok), 1, (0,0,0))
        wind.blit(struchok_tekst, (10, 20))
        wind.blit(goroh_tekst, (640, 20))
    clock.tick(FPS)
    display.update()
