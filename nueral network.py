
import math,random,numpy
e=math.e
class nn:
    net =[]
    neurons=[]

    def __init__ (self,input_size,learning_rate=0.005):
        self.net.append(input_size)
        self.neurons.append([])
        self.learning_rate = learning_rate
        

    def add(self,neurons):
        self.net.append(neurons)
        self.neurons.append([])
    
        for i in range(neurons):
            self.neurons[len(self.neurons)-1].append(neuron(self.net[len(self.net)-2]))


    def input(self,input,output):
        self.truevalue = output
        self.neurons[0] = input
        self.forwardpass(input)
        self.backprop()

    def output(self):
        values = list(self.neurons[len(self.neurons)-1])
        for i in range(len(self.neurons[len(self.neurons)-1])):
            values[i] = self.sigmoid(self.neurons[len(self.neurons)-1][i].currentvalue)
        return values

    def forwardpass(self,input):
        i=0
        j=0
        for i in range(1,len(self.net)):
            if i == 1:
                for j in range(self.net[i]):
                    x= numpy.dot(input,self.neurons[i][j].weightvector) ##dot product of neuron value against weight
                    x += self.neurons[i][j].bias
                    self.neurons[i][j].currentvalue = 1/(1 - math.e **-x)
            else:  
                values=[]
                for k in range(len(self.neurons[i-1])):
                    values.append(self.neurons[i-1][k].currentvalue)

                for j in range(0,self.net[i]):
                    x= numpy.dot(values,self.neurons[i][j].weightvector) ##dot product of neuron value against weight
                    x += self.neurons[i][j].bias
                    self.neurons[i][j].currentvalue = self.sigmoid(x)

                


    def backprop(self):
        print("backprop")

        for i in range(len(self.neurons)-1,0,-1):     
            for j in range(len(self.neurons[i])):
                gradient = []
                if i == (len(self.neurons)-1):
                    #The derivative of the error / the corosponding weight is (a-t) * sigmoidprime(a) * a(of the connecting node weight[k])
                    self.neurons[i][j].error = 0.5*(self.neurons[i][j].currentvalue - self.truevalue[j])**2
                    for k in range(len(self.neurons[i][j].weightvector)):
                        gradient.append((self.neurons[i][j].currentvalue - self.truevalue[j]) * self.sigmoidprime(self.neurons[i][j].currentvalue) * self.neurons[i-1][k].currentvalue)
                        

                elif (i == 1):
                    error = 0
                    for l in range(len(self.neurons[i+1])-1):  ##the neurons in the previous layer
                        error += self.neurons[i+1][l].error / self.sigmoidprime(self.neurons[i+1][l].currentvalue) * self.neurons[i+1][l].weightvector[j]

                    self.neurons[i][j].error =error

                    ##if not, add up the weights of the
                    for k in range(len(self.neurons[i][j].weightvector)):
                        gradient.append( error * self.sigmoidprime(self.neurons[i][j].currentvalue) * self.neurons[i-1][k] )
                    

                else :
                    error = 0
                    for l in range(len(self.neurons[i+1])-1):  ##the neurons in the previous layer
                        error += self.neurons[i+1][l].error / self.sigmoidprime(self.neurons[i+1][l].currentvalue) * self.neurons[i+1][l].weightvector[j]

                    self.neurons[i][j].error =error

                    ##if not, add up the weights of the
                    for k in range(len(self.neurons[i][j].weightvector)):
                        gradient.append( error * self.sigmoidprime(self.neurons[i][j].currentvalue) * self.neurons[i-1][k].currentvalue )

                x=self.neurons[i][j].wgradient
                print(gradient)
                print(x ,  " x")
                print(i, j ," i, j")
                x.append(gradient)
                print(len(self.neurons[i][j].wgradient))
                print("")

    def sigmoid(self,x):
        if (x==0):
            print("Divide by zero error")
            return 1
        else:
            y =1 / (1-math.e**-x) 
        return y

    def sigmoidprime(self,x):
        y= x * (1-x)
        return y

    def batch(self,array):
        print("batch")
        self.iterations = len(array)-1
        for i in range(len(array)-1):
            self.input(array[i][0],array[i][1])   ##[[data],output]
        self.applybackprop()

    def averagegradients(self):
        print("averagegradients")
        for i in range(1,len(self.neurons)+1):
            for j in range(len(self.neurons[i])):
                print(len(self.neurons[i][j].wgradient))
                average = []
                #print(self.neurons[i][j].wgradient)
                for k in range (self.iterations+1):
                     value = 0
                     for l in range(len(self.neurons[i][j].weightvector)):
                        value += self.neurons[i][j].wgradient[l][k]

                     average.append(value/(l+1))

                self.neurons[i][j].wgradient = list(average)
        pass

    def applybackprop(self):
        print("applybackprop")
        self.averagegradients()
        myFile = open("CurrentWeights","wt")
        for i in range(1,len(self.neurons)-1):
            for j in range(len(self.neurons[i])-1):
                for k in range(len(self.neurons[i][j].weightvector)-1):
                    myFile.write(str(self.neurons[i][j].weightvector[k]))
                    self.neurons[i][j].weightvector[k] -= self.neurons[i][j].wgradient[k] * self.learning_rate
        myFile.close()

class neuron:
    currentvalue=0
    error=0
    wgradient = []
    biasgradient = []
    def __init__ (self,connections):
        self.weightvector = [random.uniform(0.2,0.7) for i in range(connections)]
        self.bias = random.uniform(0.2,0.7)
        self.weightchange = []
    

print("start")  
net = nn(3)
net.add(5)
net.add(7)
net.add(6)
net.batch([[[1,2,3],[0,0,0,0,0,1]],[[1,0,1],[0,1,0,0,0,0]],[[3,1,2],[0,0,0,0,0,1]],[[0,2,3],[0,0,0,0,1,0]],[[2,2,0],[0,0,0,1,0,0]],[[2,-1,5],[0,0,0,0,0,1]],[[2,0,1],[0,0,1,0,0,0]]])  ##seven tests