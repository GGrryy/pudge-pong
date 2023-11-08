import pygame as pg

#Cоздаем переменные
WIDTH = 1920
HEIGHT = 1080
FPS = 60

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#Создаем группу со всеми спрайтами(объектами)
All_sprites = pg.sprite.Group()


#Создаем класс игрового объекта
class Pudge(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.imagelist = [
            pg.image.load('images\PudgeRight.png'),
            pg.image.load('images\PudgeLeft.png')
        ]
        self.image = self.imagelist[0]
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.xspeed = 5
        self.yspeed = 2.5

    def update(self):
        self.rect.y += self.yspeed
        self.rect.x += self.xspeed
        if self.rect.right >= enemy.rect.left:
            self.xspeed = -(self.xspeed)
            self.image = self.imagelist[1]
        if self.rect.left <= player.rect.right and ( self.rect.y < player.rect.y ):
            self.xspeed = -(self.xspeed)
            self.image = self.imagelist[0]
        if self.rect.bottom >= HEIGHT:
            self.yspeed = -(self.yspeed)
            self.rect.bottom = HEIGHT
        if self.rect.top <= 0:
            self.yspeed = -(self.yspeed)
            self.rect.top = 0


pudge = Pudge()
All_sprites.add(pudge)


#Cоздаем класс врага
class Enemy(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((20, 200))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.right = WIDTH - 30
        self.rect.y = pudge.rect.y - 28

    def update(self):
        self.rect.y = pudge.rect.y - 28

    def testgit(self):
        pass


enemy = Enemy()
All_sprites.add(enemy)


class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((20, 200))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = 30
        self.rect.y = HEIGHT / 2


player = Player()
All_sprites.add(player)


#Инициализируем окно
pg.init()
screen = pg.display.set_mode( (WIDTH, HEIGHT) )
fpsClock = pg.time.Clock()

running = True

while running:
    # Держим цикл на правильной скорости
    fpsClock.tick(FPS)
    # Ввод процесса (события)
    for event in pg.event.get():
        # check for closing window
        if event.type == pg.QUIT:
            running = False

    # Обновление
    All_sprites.update()

    # Рендеринг
    screen.fill(BLACK)
    All_sprites.draw(screen)
    # После отрисовки всего, переворачиваем экран
    pg.display.flip()

pg.quit()

