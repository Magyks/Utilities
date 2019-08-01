import pygame,time,random


w,h = 1000,800
pygame.init()
screen = pygame.display.set_mode((w, h))

class snake:
    body = []
    head=[0,0]
    direc="right"
    size = 0
    lasthead=[0,0]


    def __init__(self,startpos,w,h,screen):
        self.head = startpos
        self.w = w
        self.h = h
        self.screen = screen
        self.generateapple()

    def drawsnake(self):
        drawlist = list(self.body)
        drawlist.insert(0,self.head)

        for i in range(len(drawlist)):
            pygame.draw.rect(screen,(255,255,255),[drawlist[i][0],drawlist[i][1],20,20])

        pygame.draw.rect(screen,(255,15,15),[self.appleloc[0],self.appleloc[1],20,20])

    def move(self):
        self.changedir()

        self.lasthead =list(self.head)

        if self.direc == "right":
            self.head[0] += 20
        elif self.direc =="left":
            self.head[0] += -20
        elif self.direc =="up":
            self.head[1] += -20
        else :
            self.head[1] += 20

        if self.head[0]>(self.w/2):
            divew = -1
        else:
            divew = 1

        if self.head[1]>(self.h/2):
            diveh = 1
        else:
            diveh = -1

        if self.head[1] > self.h + 20:
            self.head[1] -= 20
            self.head[0] += 20*divew
        if self.head[0] < 0:
            self.head[0] += 20
            self.head[1] -= 20*diveh
        if self.head[1] < 0:
            self.head[1] += 20
            self.head[0] += 20*divew
        if self.head[0] > self.w-20:
            self.head[0] -= 20
            self.head[1] -= 20*diveh

        self.timemarker = time.perf_counter()
        self.bodyregulate()
        self.eatapple()
        
        return self.checkbodycollision()
        
    def changedir(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_a] or pressed[pygame.K_LEFT]:
            self.direc = "left"
            #print("left")
        if pressed[pygame.K_w] or pressed[pygame.K_UP]:
            self.direc = "up"
            #print("up")
        if pressed[pygame.K_s]or pressed[pygame.K_DOWN]:
            self.direc = "down"
            #print("down")
        if pressed[pygame.K_d]or pressed[pygame.K_RIGHT]:
            self.direc = "right"
            #print("right")

    def checkbodycollision(self):
        if self.head in self.body:
            print("collsion")
            return False
        else:
            return True

    def bodyregulate(self):
        self.body.insert(0,self.lasthead)
        if len(self.body)>self.size:
            self.body.pop(len(self.body)-1)


    def eatapple(self):
        if self.head == self.appleloc:
            self.size +=1
            self.generateapple()

    def generateapple(self):
        self.appleloc = [int(random.randint(0,int(self.w/20))*20),int(random.randint(0,int(self.h/20))*20)]
        pygame.draw.rect(screen,(255,15,15),[self.appleloc[0],self.appleloc[1],20,20])


pixelarrayB=[[0 for i in range(int(h/20))]for i in range(int(w/20))]
pixelarray = list(pixelarrayB)
snakeobject = snake([60,60],w,h,screen)
timemarker=time.perf_counter()
running = True
while running:
    screen.fill((0, 0, 0))

    if (time.perf_counter() - timemarker) > 0.5:
        running = snakeobject.move()
        timemarker = time.perf_counter()
        pixelarray=list(pixelarrayB)
        pixelarray[int(snakeobject.head[0]/20)][int(snakeobject.head[1]/20)] = 1
        for i in range(len(snakeobject.body)-1):
            pixelarray[int(snakeobject.body[i][0]/20)][int(snakeobject.body[i][1]/20)] = 1

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            print("Quit")

    snakeobject.drawsnake()

    pygame.display.flip()

pygame.quit()