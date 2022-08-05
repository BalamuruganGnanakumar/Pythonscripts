    
#funtions--> group of codes is my funtions or methods    

#start with def keyword 

def addition(a,b):#with parameter with return 
    c=a+b
    return c




def sub(a,b):#with parameter no return 
    c=a-b
    print("sub",c)
    
    
def mmul():#no parameter no return 
    a=1
    b=2
    c=a*b
    print("mul",c)   
    
def divsion():#no parameter with return 
    a=10
    b=2
    c=a/b
    return c   

#class --> grouping of function 

class maths():
    def add(self,a,b):
        print(self)
        return a+b
    def sub(self):
        print("sub")

if __name__ =="__main__":#start 
    #fucntion call
    result=addition(100,200)#a=100 b=200
    print(result)###output  300
    
    #function call
    sub(13,15)   ###output -2
    
    #function call for mul
    mul()#output mul 2
     
    
    #fuction call for div
    resu=div()
    print(resu) #div 5
    
    #class call
    ob=maths()#create object first
    result=ob.add(12,34)
    print("result",result)
    
    ob.sub()
	
	
	
	#create four different types of function 
	#call the fucntion inside class and create object for calling your class
	
