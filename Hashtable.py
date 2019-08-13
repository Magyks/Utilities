##hashtable

class htable:
    def __init__(self,size):
        self.size=size
        self.array = [" " for i in range(size)] 

    def add(self,data):
        "returns 00 when data added sucessfully, returns 01 when the hash table is full"
        index= hash(data)%self.size
        print(index,hash(data))
        z=self.array[index]
        if z ==" ":
            self.array[index] = data
            return "00"
        elif z != " ":
            spacefound = False
            i=0
            while spacefound == False and i != self.size -1:
                i+=1
                if self.array[(index+i)%self.size] == " ":
                    self.array[(index+i)%self.size] = data
                    spacefound = True
                    return "00"

            if i==self.size -1:
                return "01"


    def find (self,data):
        index= hash(data)
        print(index%self.size)
        z=self.array[index%self.size]
        results=[]
        if z ==" ":
            return results
        elif z != " ":
            spacefound = False
            i=0
            while spacefound == False and i != self.size -1:
                if self.array[(index+i)%self.size] == " ":
                    spacefound = True
                else:
                    results.append([self.array[(index+i)%self.size],(index+i)%self.size])
                    i+=1
                    

            return results

    def delete(self,index=-1,data="-1"):
        if index == -1 and data == "-1":   ##neitherindex or data are defined
            return "02"
        elif index == -1 and data != "-1":  ##only data defined
            index = hash(data) % self.size
            results = self.find(data)
            if len(results) == 0:
                return "03"
            elif len(results) == 1:
                indexc = results[0][1]
                self.array[indexc] = " "
                return "00"
            else :
                message=""
                for i in range(len(results)):
                    message+=results[i][0]+" "
                print(message)
                deci = int(input("Enter index of record deletion  :"))
                self.array[results[deci][1]] = " "
                return "00"
        elif index != -1 and data == "-1":  ##only index defined
            self.array[index] = " "
        else:
            if self.array[index]  == data:
                self.array[index] = " "
            else:
                return "04"

    def errors(self,check):
        if check == "00":
            print("No error")
        elif check == "01":
            print("Hash table is full")
        elif check =="02":
            print("At least 1 paramater has to be non-default")
        elif check == "03":
            print("Could not find a data entry for the given index or data")
        elif check == "04":
            print("At the index provided, the data provided does not match the data stored")


table = htable(4)

