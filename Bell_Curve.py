import math,pygame,time

pygame.init()

def stat(seed):
    seed = str(seed)
    total = 0
    for i in range(len(seed)):
        total += int(seed[i])
    decision = float(total/108) % 1

    x = int(seed) + 123456789976
    return x,decision

width, height = 640, 480
screen = pygame.display.set_mode((width, height))

seed  = 123456789876
array = [0 for i in range(1000)]

for i in range(10):
    x = 100 + (500 *i / 10)
    print(x)
    y= height - 50
    pygame.draw.rect(screen,(255,255,255), [x,y ,3,3])

notdone = True
while notdone:
    #screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            notdone =False

    seed,dec  = stat(seed)
    array[int(dec * 1000)%1000] +=1
    x = 100 + (500 *dec)
    y=array[int(dec * 1000)%1000]
    if y == height - 100:
        notdone = False
    pygame.draw.rect(screen,(255,255,255), [x,height-y-100 ,1,1])
    pygame.display.flip()

time.sleep(5)
pygame.quit()
