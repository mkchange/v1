# -*- coding:utf-8 -*-
import pygame
import time
import random

#自己控制的飞机
class playone(object):
    def __init__(self,screen_main):
        self.x = 220
        self.y = 700
        self.screen = screen_main
        self.image = pygame.image.load("D:\BaiduNetdiskDownload/feiji/hero1.png")
        self.bullet_list = []
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
        for bullet_tem in self.bullet_list:
            bullet_tem.display()
            bullet_tem.move()
            if bullet_tem.judge():
                self.bullet_list.remove(bullet_tem)
    def move_left(self):
        self.x-=5
    def move_right(self):
        self.x+=5
    def fire(self):
        self.bullet_list.append(bullet(self.screen,self.x,self.y))

#敌机
class enemy(object):
    def __init__(self, screen_main):
        self.x = 0
        self.y = 2
        self.screen = screen_main
        self.image = pygame.image.load("D:\BaiduNetdiskDownload/feiji/enemy0.png")
        self.bullet_list = []
        self.direction = 'right'
    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
        for bullet_tem in self.bullet_list:
            bullet_tem.display()
            bullet_tem.move()
            if bullet_tem.judge():
                self.bullet_list.remove(bullet_tem)

    def fire(self):
        random_num = random.randint(1,100)
        if random_num==1 or random_num==60:
            self.bullet_list.append(Enemy_bullet(self.screen, self.x, self.y))

    def aot_move(self):
        if self.direction == 'right':
            self.x+=2
            if self.x>440:
                self.direction = 'left'
        elif self.direction == 'left':
            self.x-=2
            if self.x<0:
                self.direction = 'right'

#自己飞机发射子弹
class bullet(object):
    def __init__(self,screen_main,x,y):
        self.x = x+40
        self.y = y-20
        self.screen = screen_main
        self.image = pygame.image.load("D:\BaiduNetdiskDownload/feiji/bullet.png")
    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
    def move(self):
        self.y-=5
    def judge(self):
        if self.y<1:
            return True
        else:
            return False

#敌机发射子弹
class Enemy_bullet(bullet):
    def __init__(self, screen_main, x, y):
        self.x = x +20
        self.y = y + 40
        self.screen = screen_main
        self.image = pygame.image.load("D:\BaiduNetdiskDownload/feiji/bullet1.png")
    def move(self):
        self.y+=5
    def judge(self):
        if self.y>852:
            return True
        else:
            return False

#飞机控制
def play_control(hero1):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a or event == pygame.K_LEFT:
                print('left')
                hero1.move_left()
            if event.key == pygame.K_d or event == pygame.K_RIGHT:
                print('right')
                hero1.move_right()
            if event.key == pygame.K_SPACE:
                print('space')
                hero1.fire()

#碰撞检测
def Impact_check():
    pass


def main():
    screen = pygame.display.set_mode((480,852),0,32)
    background = pygame.image.load("D:\BaiduNetdiskDownload/feiji/background.png")
    hero1 = playone(screen)
    enemy1 = enemy(screen)
    i=0
    while True:
        time.sleep(0.001)
        screen.blit(background,(0,0))
        hero1.display()
        enemy1.display()
        enemy1.aot_move()
        enemy1.fire()
        pygame.display.update()
        play_control(hero1)


if __name__=='__main__':
    main()
