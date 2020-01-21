import pygame
import random

pygame.init()
sizeW_x = 1366; sizeW_y = 768
window = pygame.display.set_mode((sizeW_x, sizeW_y), pygame.FULLSCREEN)
pygame.display.set_caption("Aim")
background_image = pygame.image.load('back.jpg')

#var#var#var#var#var#var#var#var#var#var#var#var#var#var#var#var#var#var#var#var#var#var#var#var#var#var#var#var
run = True
clock = pygame.time.Clock()
aim = []
score = 0
alltime = 0
click = 0

#class#class#class#class#class#class#class#class#class#class#class#class#class#class#class#class#class#class#class
class circles():
    def __init__(self):
        self.r = 10
        self.x = random.randint(200 + self.r, sizeW_x - self.r - 200)
        self.y = random.randint(100 + self.r, sizeW_y - self.r - 100)
        self.time = 0
        self.anim = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21,
        22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
        self.end = False
        self.color = 0


    def draw(self):
        global score
        pygame.draw.circle(window, (255,0, self.color // 2), (self.x, self.y), self.r)
        self.color += 5
        #pygame.display.update()

        if not(self.end):
            self.time += 1
            self.r = self.anim[self.time]
            #pygame.time.wait(10)
            if self.time == 25:
                self.end = True

        if self.end:
            self.time -= 1
            self.r = self.anim[self.time]
            #pygame.time.wait(10)
            if self.time == 0:
                aim.pop(aim.index(self))
                i.draw()
                score -= 10


    def click(self):
        global score, click
        if (pos_Mouse[0] >= (self.x - (self.r)) and pos_Mouse[0] <= (self.x + self.r) and
            pos_Mouse[1] >= (self.y - (self.r)) and pos_Mouse[1] <= (self.y + self.r)):
            aim.pop(aim.index(self))
            #i.draw()
            score += 10
            click += 1
        else:
            click = 0



#run#run#run#run#run#run#run#run#run#run#run#run#run#run#run#run#run#run#run#run#run#run#run#run#run#run#run#
while run:
    clock.tick(30)
    window.blit(background_image, (0, 0))
    font = pygame.font.Font(None, 25)
    text = font.render("Score: "+str(score),True, (0,0,255))
    window.blit(text, [1200, 50])
    keys = pygame.key.get_pressed()
    #global alltime


    if len(aim) < 5:
        for i in range(100):
            alltime += i
            if alltime >= 50000:
                x = circles()
                aim.append(x)
                alltime = 0

    for i in aim:
        i.draw()

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos_Mouse = pygame.mouse.get_pos()
            for obj in aim:
                obj.click()
            if click == 0:
                score -= 5
                click = 0


        if event.type == pygame.QUIT:
            run = False

    #exit from while

    if keys[pygame.K_SPACE]:
        run = False

    pygame.display.update()

#exit#exit#exit#exit#exit#exit#exit#exit#exit#exit#exit#exit#exit#exit#exit#exit#exit#exit#exit#exit#exit#exit#
pygame.quit()
