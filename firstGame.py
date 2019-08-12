import pygame 

pygame.init()

win = pygame.display.set_mode((500, 500))
pygame.display.set_caption('First Game')


screenWidth = 500
isJump = False
jumpCount = 10
'''
Variables to represent our chapter
'''
x = 50
y = 50
width = 40
heigth = 70
vel = 10
run = True

'''
Main-loop or Game-loop
'''
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel 
    if keys[pygame.K_RIGHT] and x < screenWidth - width - vel:
        x += vel
    if not(isJump):
        if keys[pygame.K_UP] and y > vel:
            y -= vel
        if keys[pygame.K_DOWN] and y < screenWidth - heigth - vel:
            y += vel
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10


    

    win.fill((0,0,0))
    pygame.draw.rect(win, (255,0,0), (x,y,width,heigth))
    pygame.display.update()

pygame.quit()