import pygame,sys
pygame.init()

kollane=[255,255,10]
punane=[255,0,0]
hall=[200,200,200]
roosa=[255,150,255]
roheline=[100,255,100]

X=640
Y=480
ekraan=pygame.display.set_mode([X,Y])
pygame.display.set_caption("Animatsioon")
ekraan.fill(roheline)
kell=pygame.time.Clock()
mesilane=pygame.image.load("bee.png")
posX=X-mesilane.get_rect().width
posY=Y-mesilane.get_rect().height
lõpp=False
sammX=2
sammY=2

code_choice = input("Vajutage kvadraadil liikumiseks numbrit 1 ja diagonaalselt liikumiseks numbrit 2: ")

while not lõpp:
    kell.tick(60)
    events=pygame.event.get()
    for i in pygame.event.get():
        if i.type==pygame.QUIT():
            sys.exit()
    if code_choice == '2':
        if posX == 0 or posX == X - mesilane.get_rect().width:
          sammX = -sammX
        if posY == 0 or posY == Y - mesilane.get_rect().height:
          sammY = -sammY
    
          posX += sammX
          posY += sammY
    elif code_choice == '2':
        keys = pygame.key.get_pressed()
        if posX == 0 and posY == 0:
           sammX = 1
           sammY = 0
    if posX == X - mesilane.get_rect().width and posY <= Y - mesilane.get_rect().height:
        sammX = 0
        sammY = 1
    if posX <= X - mesilane.get_rect().width and posY == Y - mesilane.get_rect().height:
        sammX = 1
        sammY = 0
        sammX = -sammX
    if posX == 0 and posY >= Y - mesilane.get_rect().height:
        sammX = 0
        sammY = 1
        sammY = -sammY
    posX += sammX
    posY += sammY

    
    ekraan.blit(mesilane,(posX,posY))
    pygame.display.flip()
    ekraan.fill(roheline)
    
pygame.quit()

