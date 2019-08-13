import vigenere
generator =vigenere.cipher("E","ghost","helpmeimallalone")
MyFile = open("C:\\Users\\44\\Documents\\A Level Work\\Database.txt","rt")
SMile = []
for lines in MyFile:
    if lines.find("\n") == -1:
        SMile.append(lines)
    else:
        SMile.append(lines[:len(lines)-1])

full = False
while full == False:
    imput = str(input("Enter the person's sername  :"))
    index = hash(imput)%1000
    found = False
    while found ==False:
        results=[]
        if SMile[index] = "0\n":
            print("Sorry, that person does not exist.")
        else:
            hvalue = hash(imput)
            spacenotfound = True
            i=0
            while spacenotfound :
                x= SMile[index+i].split(" ")
                if x[0] != hvalue and str(x[0]) != "0\n"  :
                    i+=1
                elif x[0] == hvalue:
                    index +=i
                    spacenotfound =False
                else:
                    spacenotfound = False

            if i == 1000
            rvalue = False
            i=0
            while rvalue == False and i!=1000 :
                x= SMile[index+i].split(" ")
                if int(x[0]) == hvalue:
                    results.append(SMile[index+i])
                    i+=1
                else:
                    rvalue == True

            if len(results) != 0:
                
                
