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

    def __init__(self,width,height,seed,compression = 20,startpoint = 0):
        self.compression = compression
        self.width  = width
        self.height = height
        self.seed = str(seed)
        self.curvedseed = str(seed)
        self.map = [[0 for i in range(int(height/self.compression))]for i in range(int(width/self.compression))]

        if startpoint == 0:
            x = (int(self.seed) % (width/self.compression) ) *self.compression
            y = ((int(self.seed) / 3)  % (height / self.compression)) *self.compression
            if x<40 : 
                x=40
            elif x> width - 60 :
                x = width - 60 
                
            if y<40 : 
                y=40
            elif y> height - 60 :
                y = height - 60
            self.startpoint = [int(x),int(y)]
        else:
            self.startpoint = startpoint
        
        self.map[int(self.startpoint[0]/self.compression)][int(self.startpoint[1]/self.compression)]
        runcode = self.generateroom(self.startpoint)
        try:
            val = self.generatedec()
        finally:
            val = self.generatedec()
            if val != 0:
                print("There was an error with an error code of "+val+".")
        print(runcode)

    def draw(self,screen):
        for i in range(int(self.width/self.compression)):
            for j in range(int(self.height/self.compression)):
                if self.map[i][j] == 1:
                    pygame.draw.rect(screen,(255,255,255),[i*self.compression,j*self.compression,self.compression,self.compression])
                else:
                    pygame.draw.rect(screen,(0,0,0),[i,j,self.compression,self.compression])
        
        

    def generatedec(self):
        
        ####################
        ## This ensures that a seed can exactly
        ## replicate the same level generaton
        ####################
        total = 0
        for i in range(len(self.curvedseed)):
            total += int(self.curvedseed[i])
        decision = float(total/108) % 1

        rooms = int(5+decision*7)
        for i in range(rooms):
            self.curveseed()
            self.generateroom([int(self.curvedseed[8]*(self.width/20))*20,int(curvedseed[9]*(self.height/20))*20])

        return 0 

    def curveseed(self):
        ##this works really well , there are some gaps here 
        ##and there but thoes change with the seed
        newseed = ""
        for i in range(12):
            ##if i add the next value after the consecutive, 
            ##there is less of an even spread
            try:
                d =(int (self.curvedseed[i])+ int(self.curvedseed[(i+1)%12]))
            except IndexError:
                d = "0"
            except:
                d = (int (self.curvedseed[i])+ int(self.curvedseed[(i+1)%12]))
            newseed += str(d)
        
        self.curvedseed =  str(int(newseed)%999999999999) 

    def generateroom(self,centre):
        w=int((int(self.curvedseed[5])+int(self.curvedseed[7]))/1.6)
        if w%2 == 0:
            w+=1
        if w>11:
            w=11
        elif w<5:
            w=5
        
        h = int((int(self.curvedseed[2])+int(self.curvedseed[9]))/1.6)
        if h%2==0:
            h+=1
        if h>11:
            h=11
        elif h<5:
            h=5
        

        insidebounds=False
        while insidebounds == False:
            test1 = centre[0]/self.compression+(w-1)/2 > self.width/self.compression
            test2 = centre[0]/self.compression-(w-1)/2 < 0
            test3 = centre[1]/self.compression+(h-1)/2 > self.height/self.compression 
            test4 = centre[1]/self.compression+(h-1)/2 < 0
            if test1 or test2 or test3 or test4:
                w-=1
                h-=1
            else:
                insidebounds = True
        
        self.rectanglecheck(w,h,centre)

    def generatepath(self):
        pass

    def rectangleflip(self,w,h,centre):
        ##removes a rectangle
        for i in range(h):
            for j in range(2):
                x=centre[0]/self.compression + (w-1)/2 - (w-1)*j
                y=centre[1]/self.compression - (h-1)/2 + i 
                self.map[int(x)][int(y)] = 0
                

        for i in range(w-2):
            for j in range(2):
                x = centre[0]/self.compression - (w-3)/2 + i
                y = centre[1]/self.compression + (h-1)/2 -(h-1)*j
                self.map[int(x)][int(y)]=0

    def rectanglecheck(self,w,h,centre):
        ##checks for collision in the creation of a rectangle
        non = True
        for i in range(h):
            for j in range(2):
                x=centre[0]/self.compression + (w-1)/2 - (w-1)*j
                y=centre[1]/self.compression - (h-1)/2 + i 
                if self.map[int(x)][int(y)] == 1:
                    non =False
                else:
                    self.map[int(x)][int(y)] =1

        for i in range(w-2):
            for j in range(2):
                x = centre[0]/self.compression - (w-3)/2 + i
                y= centre[1]/self.compression + (h-1)/2 -(h-1)*j
                if self.map[int(x)][int(y)] == 1:
                    non =False
                else:
                    self.map[int(x)][int(y)] =1
                
        if non == False:
            self.rectangleflip(w,h,centre)
            return 1
        else:
            return 0

seed = 123456789111 ##12 digit seed

creator = dungeon(width,height,seed,10)

Done=False
while Done == False:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Done =True

    creator.draw(screen)
    pygame.display.flip()

pygame.quit()
