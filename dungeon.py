import pygame,random
 
pygame.init()
 
fps = 60
fpsClock = pygame.time.Clock()
 
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
 
# Game loop.
print("pygame should be running")


class dungeon:

    change=0
    previous = "start"
    flatseed = ""
    curveseed = ""

    def __init__(self,width,height,seed,startpoint = 0):
        self.width  = width
        self.height = height
        self.flatseed = str(seed)
        self.curveseed = str(seed)

        maparray = [[ 0 for i in range(int(height/20)) ]for j in range (int(width/20))]

        if startpoint == 0:
            x = (int(self.seed) % (width/20) ) *20
            y = ((int(self.seed) / 3)  % (height / 20)) *20
            if x<40 : 
                x=40
            elif x> width - 60 :
                x = width - 60 
                
            if y<40 : 
                y=40
            elif y> height - 60 :
                y = height - 60
            self.startpoint = [int(x),int(y)]
            print(x,y)

    def draw(self,screen):
        pygame.draw.rect(screen,(255,255,255),[self.startpoint[0],self.startpoint[1],20,20])
        try:
            val = self.generatedec()
        finally:
            val = self.generatedec()
            if val != 0:
                print("There was an error with an error code of "+val+".")
        

    def generatedec(self):
        
        ####################
        ## This ensures that a seed can exactly
        ## replicate the same level generaton
        ####################
        total = 0
        for i in range(len(self.seed)):
            total += int(self.seed[i])
        decision = float(total/108) % 1
        self.updateseeds()
        ####################

        if  self.previous == "start":
            if decision > 0.5 :
                ##generate a path
                pass
            else:
                ##generate a room
                pass
        elif self.previous == "path":
            if decision > 0.4 :
                ##generate more path
                pass
            else:
                ##generate a room
                pass
        else:
            ##the previous must have been a room
            if 0.2 < decision < 0.3  :
                ##generate another room that is connected 
                pass
            elif decision < 0.2 :
                ##generate a conjoined room:
                pass
        
        return 0 

    def generateroom(self):
        pass
    
    def generatepath(self):
        pass

    def updateseeds(self):
        self.flatfreq()
        self.curvefreq()

    def flatfreq(self):
        newseed = ""
        for i in range(len(self.flatseed)):
            ##if i add the next value after the consecutive, 
            ##there is less of an even spread
            d =int (self.flatseed[i])+ int(self.flatseed[(i+1)%12])
            newseed += str(d)
        self.flatseed = str(newseed)

    def curvefreq(self):
        val = int(self.curveseed[self.change]) +3
        self.curveseed = list(self.seed)
        self.curveseed[self.change] = val
        self.curveseed[self.change] %=10
        newseed = ""
        for i in range(len(self.curveseed)):
            newseed += str(self.curveseed [i])
        self.curveseed = newseed
        self.change += 5
        self.change %= 12 

seed = 123456789111 ##12 digit seed

creator = dungeon(width,height,seed)

Done=False
while Done == False:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Done =True

    creator.draw(screen)
    pygame.display.flip()

pygame.quit()
