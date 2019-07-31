PlainText=str(input("Enter the plain Text  :"))
KeyWord=str(input("Enter the keyword :"))
KeySquare=[]
numbs=[]
for i in range(6):
    CarryOn=False
    while CarryOn==False:
        Row=str(input( f"Enter the #{i+1} row contents  :"))
        if len(Row)!=6:
            print("Each row must be comprised of six values, please try again.")
            continue

        LocalCarryOn=False
        j=0
        while LocalCarryOn==False and j <=5:
            if Row[j] in numbs:
                print(f"{Row[j]} has already been used, each value can only be used once.")
                LocalCarryOn=True
            elif Row[j] not in "abcdefghijklmnopqrstuvwxyz0123456789":
                print(f"{Row[j]} is not in the English alphabet nor between 0-9.")
                LocalCarryOn=True
            else:
                j+=1
            
        if LocalCarryOn==False:
            CarryOn=True
            #for j in range(6):
                #numbs.append(Row[j])
        else:
            CarryOn=False
    KeySquare.append(Row)

Value="adfgvx"
FirstCipher=[]

for k in range(len(PlainText)):
    CarryOn=False
    i,j=0,0
    while i <6  and CarryOn ==False:
        while j < 6 and CarryOn==False:
            if PlainText[k] == KeySquare[i][j]:
                FirstCipher.append(Value[i]+Value[j])
                CarryOn=True
                continue
            else:
                j+=1
        i+=1
        j=0
    
FirstCipher="".join(FirstCipher)
CipherText=""
for i in range(len(KeyWord)):
    for j in range(6):
        x=123
        if x > ord(KeyWord[i]):
            x=ord(KeyWord[i])

    
    for z in range(int(len(FirstCipher)/len(KeyWord))+1):
            try:
                CipherText+=FirstCipher[z*len(KeyWord) + KeyWord.index(chr(x))]
            except IndexError:
                continue
            else:
                continue

print(CipherText.upper())
