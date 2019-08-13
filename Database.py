import vigenere,Hashtable
size = 1000

table  = Hashtable.htable(size)

full = False
while full == False:
    MyFile = open("C:\\Users\\44\\Documents\\A Level Work\\Database.txt","wt")
    deci = str(input("Add, delete, find a data entry or quit?  :"))
    if deci == "A":
        imput = str(input("Input the person's surname  :"))
        data = str(input("input the person's details to be encrypted.  :"))
        data = vigenere.cipher("E",imput,data)
        index = hash(imput)%size
        table.add(str(hash(imput))+" "+data.output,index)
    elif deci == "D":
        imput = str(input("Enter the person's surname  :"))
        ereturn = table.find(imput)
        if len(ereturn) == 0:
            print(f"No entry matches {imput}.")
        elif len(ereturn)==1:
            x=ereturn[0][0].find(" ")+1
            if hash(imput) == ereturn[0][0][:x]:
                table.delete(ereturn[0][1])
            print(f"Entry for {imput} deleted.")
        else:
            print(f"There are multiple matches that match {imput}:")
            checklist=[]
            for i in range(len(ereturn)):
                x=ereturn[i][0].find(" ")+1
                if hash(imput)== ereturn[i][0][:x]:
                    checklist.append([vigenere.cipher("D",imput,ereturn[i][0][x:]).output,ereturn[i][1]])
            if len(checklist)>1 :
                print(checklist)
                num = int(input("Which data entry is to be deleted?  :"))
                index = checklist[num][1]
                table.delete(index)
                print(f"Entry for {imput}, occurance number {index} deleted.")
            elif len(checklist)==1:
                index = checklist[0][1]
                table.delete(index)
                print(f"Entry for {imput} deleted.")
            else:
                print(f"No entry matches {imput}.")

    elif deci =="F":
        imput = str(input("Enter the person's surname  :"))
        ereturn = table.find(hash(imput)%size)
        if len(ereturn) == 0:

            print("There are no people who meet you're search term. Remeber the searchterm\nonly looks for Surnames.")
        elif len(ereturn)==1:
            x=ereturn[0][0].find(" ")
            print(imput + " "+ vigenere.cipher("D",imput,ereturn[0][0][x:]).output)
        else:
            print(f"There are multiple matches that match {imput}:")
            for i in range(len(ereturn)):
                x=ereturn[i][0].find(" ")
                print(vigenere.cipher("D",imput,ereturn[i][0][x+1:]).output)
    elif deci == "Q":
        full = True
    else:
        print("Please input A for add, D for delete and F for find.")

    for i in range(size):
        MyFile.write(table.array[i]+"\n")
    MyFile.close()