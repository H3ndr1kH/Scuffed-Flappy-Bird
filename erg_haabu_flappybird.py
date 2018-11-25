import pygame

pygame.init()

ekraan = pygame.display.set_mode([1280, 720])
lind = pygame.image.load("lind.png")

mäng_töötab = True
linnu_x = 400
linnu_y = 360
loendaja = 0

hüpe = False
kukkumine = False

while mäng_töötab:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            mäng_töötab = False
        elif e.type == pygame.MOUSEBUTTONDOWN:
            hüpe = True
                
    if hüpe:
        linnu_y -= 20
        loendaja += 1
        if loendaja >= 10:
            loendaja = 0
            hüpe = False
            kukkumine = True   
    if kukkumine:    #gravitatsioon
        linnu_y += 7
    if linnu_y >= 640: #et lind ei saaks alumisest ekraani servast allapoole kukkuda
        linnu_y = 640
    if linnu_y <= -5: #et lind ei saaks üle ülemise ääre minna
        linnu_y = -5
             
    ekraan.fill([255, 255, 255])
    ekraan.blit(lind, [linnu_x, linnu_y])
    pygame.display.flip()
    pygame.time.delay(17)
pygame.quit()
