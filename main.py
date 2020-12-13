import pygame
import sys
import random
import secrets
pygame.init()
window = pygame.display.set_mode((500,500))
pygame.display.set_caption("TBD")

x=100
y=150
width=300
height=60
buttonlight=(250,250,250)
buttondark=(0,0,0)
textdark=(0,0,0)
textlight=(250,250,250)
def button1(buttonlight,textdark):
    col=buttonlight
    color=textdark
    pygame.draw.rect(window, (col), (x,100, width, height))
    thefont=pygame.font.SysFont('Arial',50)
    word1=thefont.render('  Events', True, color)
    window.blit(word1, (x,100))
def button2(buttonlight,textdark):
    col=buttonlight
    color=textdark
    pygame.draw.rect(window, (col), (x,180, width, height))
    thefont=pygame.font.SysFont('   Arial',50)
    word2=thefont.render('  Equipments', True, color)
    window.blit(word2, (x,180))
def button3(buttonlight,textdark):
    col=buttonlight
    color=textdark
    pygame.draw.rect(window, (col), (x,260, width, height))
    thefont=pygame.font.SysFont('Arial',50)
    word3=thefont.render('  Funding', True, color)
    window.blit(word3, (x,260))
def button4(buttonlight,textdark):
    col=buttonlight
    color=textdark
    pygame.draw.rect(window, (col), (x,340, width, height))
    thefont=pygame.font.SysFont('Arial',50)
    word4=thefont.render('  News', True, color)
    window.blit(word4, (x,340))
make=True
yes=True
welpic1='images/OIP.pKTq4InLWg7UMmb4asHmFAHaEK.jpg'
welpic2='images/OIP.VekmEveSq678y9UgY9ZvFQHaE8.jpg'
welpic3='images/OIP.GmbLXVdVtacAH7dkdFnTsQHaFj.jpg'
welpic4='images/OIP.Rl_cfo4-UDievXD8ztwnUQHaGI.jpg'
welpic5='images/index.jpg'
welpic6='images/rainbow.jpg'
welpiclist=[welpic1,welpic2,welpic3,welpic4,welpic5,welpic6]
wel=secrets.choice(welpiclist)
bg1='images/forest.jpg'
bg2='images/OIP.eqqnIaxaDi5VypDVyMaUHwHaE7.jpg'
bg3='images/OIP.rffkSJBXVy_x2kmW4qSeQQHaFj.jpg'
bg4='images/OIP.M2SujemyQcZBiLUPZylJRwHaEo.jpg'
bg5='images/OIP.LpLjxeL2sUdmliYHLENEGQHaEo.jpg'
bg6='images/OIP.OLirq33El4BYzSCjDPcqeQHaEo.jpg'
bg7='images/OIP.yl-cHCzPvaCcNIb-oE3HEgHaEo.jpg'
bglist=[bg1,bg2,bg3,bg4,bg5,bg6,bg7]
bg=secrets.choice(bglist)
def Welcome(wel):
    Wel=wel
    text=pygame.image.load(Wel)
    window.blit(text, (0,0))
    pygame.display.update()
def Welcomedelete(wel):
    Wel=wel
    text=pygame.image.load(Wel)
    del text
    pygame.display.update()
def Window(bg):
    Bg=bg
    background = pygame.image.load(Bg)
    window.blit(background, (0,0))
    pygame.display.update()
while yes:
    Welcome(wel)
    pygame.time.delay(3000)
    Welcomedelete(wel)
    yes=False
Window(bg)
button1(buttonlight,textdark)
button2(buttonlight,textdark)
button3(buttonlight,textdark)
button4(buttonlight,textdark)
pygame.display.update()
while make:#main loop#
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            make=False
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if x <= mouse[0] <=400 and 100 <= mouse[1] <= 160:
                print("Hi")
            if x <= mouse[0] <=400 and 180 <= mouse[1] <= 240:
                print("Hi")
            if x <= mouse[0] <=400 and 260 <= mouse[1] <= 320:
                print("Hi")
            if x <= mouse[0] <=400 and 350 <= mouse[1] <= 410:
                print("Hi")
    mouse=pygame.mouse.get_pos()
    if x <= mouse[0] <= 400 and 100 <= mouse[1] <= 160:
        button1(buttondark,textlight)
    else:
        button1(buttonlight,textdark)
    if x <= mouse[0] <= 400 and 180 <= mouse[1] <= 240:
        button2(buttondark,textlight)
    else:
        button2(buttonlight,buttondark)
    if x <= mouse[0] <= 400 and 260 <= mouse[1] <= 320:
        button3(buttondark,textlight)
    else:
        button3(buttonlight,textdark)
    if x <= mouse[0] <= 400 and 350 <= mouse[1] <= 410:
        button4(buttondark,textlight)
    else:
        button4(buttonlight,textdark)
    pygame.display.update()