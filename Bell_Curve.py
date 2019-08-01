import math,pygame,time

pygame.init()

def difstat(seed):
    ##different spread of values using method "dif"
    global change
    val = int(seed[change]) +3
    seed = list(seed)
    seed[change] = val
    seed[change] %=10
    newseed = ""
    for i in range(len(seed)):
        newseed += str(seed [i])
    seed = newseed
    change += 5
    change %= 12
    return str(seed)

def multstat(seed):
    ##not good at all , the multiples leave big gaps in decimals
    x = int(seed)
    x = (x*5) %999999999999     
    return str(x)

def addstat(seed):
    ##using method "add"
    x = int(seed) + 543212345678
    ##currently this is the better stratergy
    #however there is still a large spike around 0.6
    return str(x)

def altstat(seed):
    ##this works really well , there are some gaps here 
    ##and there but thoes change with the seed
    newseed = ""
    for i in range(len(seed)):
        d = int(seed[(i+1)%12]) + int(seed[(i+2)%12])
        newseed += str(d)
    return str(newseed)

def deci(seed):
    seed = str(seed)
    total = 0
    for i in range(len(seed)):
        total += int(seed[i])
    decision = float(total/108) % 1

    #x = addstat(seed)
    #x = multstat(seed)
    x = altstat(seed)
    #x = difstat(seed)
    return x,decision


width, height = 640, 480
screen = pygame.display.set_mode((width, height))

seed  = 123456789876
##basic seed
array = [0 for i in range(1000)]

##set some markers with 0.1 intervals to essentially graph the curve
for i in range(10):
    x = 100 + (500 *i / 10)
    y= height - 50
    pygame.draw.rect(screen,(255,255,255), [x,y ,3,3])

change = 0

notdone = True
while notdone:
    #screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            notdone =False

    ##Here is essentially a hash table but the hash is deci(seed)
    ##Grab the new seed and the total
    seed,dec  = deci(seed)
    ##add one to the culmalative frequency
    array[int(dec * 1000)%1000] +=1
    ##x is based on the actual value of the total(dec)
    x = 100 + (500 *dec)
    ##y is based on the number of occuraces hence the array
    y=array[int(dec * 1000)%1000]
    ##stops when the max spike reaaches the top of the window
    if y == height - 100:  
        notdone = False
    pygame.draw.rect(screen,(255,255,255), [x,height-y-100 ,1,1])
    pygame.display.flip()

##give some time to look at the graph
time.sleep(2)
pygame.quit()
