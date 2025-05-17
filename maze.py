from pygame import *
from random import randint
sharik = "white_ball.png"
raketka = "short_handle_ping_pong_racket.png"
pole = "pole.jpg"
font.init()
font1 = font.Font(None, 70)
font2 = font.Font(None, 40)
win_height = 400
win_width = 560
st = randint(1,2)
ug = randint(1,2)
x = 270
shetok1 = 0
shetok2 = 0
y = 192
class GameSprite(sprite.Sprite):
 #конструктор класса
   def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
       #Вызываем конструктор класса (Sprite):
       sprite.Sprite.__init__(self)


       #каждый спрайт должен хранить свойство image - изображение
       self.image = transform.scale(image.load(player_image), (size_x, size_y))
       self.speed = player_speed


       #каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
 #метод, отрисовывающий героя на окне
   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))



class Player(GameSprite):
   #метод для управления спрайтом стрелками клавиатуры
   def update_l(self):
       keys = key.get_pressed()
       if keys[K_w] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_s] and self.rect.y < win_height - 40:
           self.rect.y += self.speed
   def update_r(self):
       keys = key.get_pressed()
       if keys[K_UP] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_DOWN] and self.rect.y < win_height - 40:
           self.rect.y += self.speed
   def restart(self):
       self.rect.y = 88
class Ball(GameSprite):
    def update(self):
        global st
        global ug
        global x
        global y 
        y = self.rect.y
        x = self.rect.x           
        if ug == 1 and st == 1:
            self.rect.y -= self.speed
            self.rect.x -= self.speed # на лево вверх
        elif ug == 1 and st == 2:
            self.rect.y -= self.speed
            self.rect.x += self.speed # на право вверх
        elif ug == 2 and st == 1:
            self.rect.y += self.speed
            self.rect.x -= self.speed # на лево в низ
        elif ug == 2 and st == 2:
            self.rect.y += self.speed
            self.rect.x += self.speed # на право вниз
        else:
            pass
    def restart(self):
        st = randint(1,2)
        ug = randint(1,2)
        self.rect.x = 270
        self.rect.y = 192

        
        
win1 = font1.render('PLAYER1 WIN', True, (255, 15, 1))
win2 = font1.render('PLAYER2 WIN', True, (255, 15, 1))
shet1 = font2.render(str(shetok1), True, (0, 255, 255))
shet2 = font2.render(str(shetok2), True, (0, 0, 255))
display.set_caption("Ping Pong")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(pole), (win_width, win_height))
raket1 = Player(raketka, 20, 88, 55, 55, 20)
raket2 = Player(raketka, win_width - 80, 88, 55, 55, 20)
sharik = Ball(sharik, 270, 192, 45, 45, 7) #середина для шарика 675, 480,
finish = False
#Основной цикл игры:
run = True #флаг сбрасывается кнопкой закрытия окна
while run:
   #событие нажатия на кнопку “Закрыть”
   for e in event.get():
       if e.type == QUIT:
           run = False
   if not finish:
       window.blit(background,(0,0))
       
       if y >= win_height - 26:
            ug = 1
       elif y <= 16:
            ug = 2
       else:auto-py-to-exe
           pass
       if x >= 20 and x <= win_width - 40:
            if sprite.collide_rect(sharik, raket1):
                st = 2
            elif sprite.collide_rect(sharik, raket2):
                st = 1
            else:
                    pass
       else:
           pass

        
       if shetok1 >= 6:
           window.blit(win1, (100, 100))
           finish = True
       elif shetok2 >= 6:
           window.blit(win2, (100, 100))
           finish = True
       else:
           pass
       if x < 32:
           shetok1 += 1
           sharik.restart()
           raket1.restart()
           raket2.restart()
           
           
           
       elif x >= win_width - 30:
           shetok2 += 1
           sharik.restart()
           raket1.restart()
           raket2.restart()
           
           
       else:
           pass
       window.blit(shet2, (win_width - 50, 50))
       window.blit(shet1, (50, 50))
       raket1.update_l()
       raket2.update_r()
       sharik.update()
       raket1.reset()
       raket2.reset()
       sharik.reset()
       display.update()
   
   time.delay(60)