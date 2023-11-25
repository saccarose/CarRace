import pygame
import sys
import random

#global variables
global car1_rect, car2_rect

pygame.init()
pygame.display.set_caption("Car Race by Saccarose")

clock = pygame.time.Clock()

#create screen
screen = pygame.display.set_mode((300, 400))

#import images
road = pygame.image.load("images/road.jpg").convert_alpha()
car1 = pygame.image.load("images/car1.png").convert_alpha()
car2 = pygame.image.load("images/car2.png").convert_alpha()
startBtn1 = pygame.image.load("images/start_btn.png").convert_alpha()
exitBtn1 = pygame.image.load("images/exit_btn.png").convert_alpha()
startBtn2 = pygame.image.load("images/start_btn_touched.png").convert_alpha()
exitBtn2 = pygame.image.load("images/exit_btn_touched.png").convert_alpha()

class Background():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.speed = 3
        self.img = road
        self.width = self.img.get_width()
        self.height = self.img.get_height()

    def update(self):
        self.y += self.speed
        if self.y > self.width:
            self.y -= self.width

    def draw(self):
        screen.blit(self.img, (int(self.x), int(self.y)))
        screen.blit(self.img, (int(self.x), int(self.y - self.height)))

class CarSpawn():
    def __init__(self):
        self.car1_x = random.randrange(31, 231, 100)
        self.car1_y = -90
        self.car2_x = random.randrange(31, 231, 100)
        self.car2_y = -90
        self.car_speed = 4

    def spawn1(self):
        global car2_
        car2_ = screen.blit(car2, (self.car1_x, self.car1_y))
        if self.car1_y == 390:
            self.car1_y = -90
            self.car1_x = random.randrange(31, 231, 100)

    def spawn2(self):
        global car3_
        car3_ = screen.blit(car2, (self.car2_x, self.car2_y))
        if self.car2_y == 390:
            self.car2_y = -210
            self.car2_x = random.randrange(31, 231, 100)

    def update(self):
        self.car1_y += self.car_speed
        self.car2_y += self.car_speed

    def crash(self):
        global running
        if pygame.Rect.colliderect(car1_, car2_) or pygame.Rect.colliderect(car1_, car3_):
            running = False


cs = CarSpawn()
bg = Background()

def start():
    global touchedbtn1, touchedbtn2
    touchedbtn1 = False
    touchedbtn2 = False
    while True:
        touchedbtn1 = False
        touchedbtn2 = False
        bg.draw()
        bg.update()
        btn1 = screen.blit(startBtn1, (78, 131))
        btn2 = screen.blit(exitBtn1, (89, 223))

        mouse = pygame.mouse.get_pos()
        if 78 <= mouse[0] <= 219 and 131 <= mouse[1] <= 195:
            touchedbtn1 = True
        if 89 <= mouse[0] <= 210 and 223 <= mouse[1] <= 286:
            touchedbtn2 = True

        if touchedbtn1:
            btn1 = screen.blit(startBtn2, (78, 131))
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    game()
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()
        else:
            touchedbtn1 = False

        if touchedbtn2:
            btn2 = screen.blit(exitBtn2, (89, 223))
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:      
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()
        else:
            touchedbtn2 = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        clock.tick(60)
        


def game():
    global car1_, running

    running = True
    cs.__init__()
    car_x = 130
    car_y = 280
  
    while running:
        bg.draw()
        bg.update()
        car1_ = screen.blit(car1, (car_x, car_y))

        cs.spawn1()
        cs.spawn2()
        cs.update()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and car_x >= 12:
            car_x = car_x - 3
        if keys[pygame.K_RIGHT] and car_x <= 237:
            car_x = car_x + 3
        if keys[pygame.K_UP] and car_y >= 0:
            car_y = car_y - 3
        if keys[pygame.K_DOWN] and car_y <= 310:
            car_y = car_y + 3

        cs.crash()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        clock.tick(60)
        pygame.display.update()

    while not running:
        start()


while True:
    start()