import pygame
from random import uniform as func
from time import sleep

pygame.init()
WIDTH, HEIGHT = 400, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("My Game")

clock = pygame.time.Clock()

bound = 5
c2s = 30
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)

x, y = WIDTH // 2, HEIGHT // 2
radius = 10
velocity = 8
vx = velocity * func(-1, 1)
vy = velocity * func(-1, 1)

border_u = bound + radius
border_d = HEIGHT - bound - radius
border_r = WIDTH - bound - radius
border_l = bound + radius

height = 10
width = 80
xp = (WIDTH - width) // 2
yp = HEIGHT - height
vp = 10

score = 0


def drawScore():
    win.fill(black)
    pygame.font.init()
    path = pygame.font.match_font("arial")
    Font = pygame.font.Font(path, 30)
    text = f"Your score: {score}"
    a = Font.render(text, 1, white)
    win.blit(a, (WIDTH // 2 - 90, HEIGHT // 3))
    pygame.display.update()


def drawWindow():
    win.fill(black)
    pygame.draw.rect(win, white, (0, 0, WIDTH, bound))  
    pygame.draw.rect(win, white, (0, 0, bound, HEIGHT))  
    pygame.draw.rect(win, white, (WIDTH - bound, 0, bound, HEIGHT))  
    pygame.draw.circle(win, green, (int(x), int(y)), radius)  
    pygame.draw.rect(win, white, (xp, yp, width, height)) 
    pygame.display.update()


run = True

while run:
    clock.tick(c2s)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and xp > bound:
        xp -= vp
    if keys[pygame.K_RIGHT] and xp < WIDTH - bound - width:
        xp += vp

    if x + vx < border_l or x + vx > border_r:
        vx = -vx

    if y + vy < border_u:
        vy = -vy

    if y + vy > border_d:
        if xp <= x + vx <= xp + width:
            vy = -vy
            vx *= 1.5
            vy *= 1.5
            score += 10  
        else:
            drawScore()
            sleep(10)
            run = False

    x += vx
    y += vy

    drawWindow()

pygame.quit()
