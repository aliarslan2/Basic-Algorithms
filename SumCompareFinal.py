
"""
Created on Sun Aug  7 16:27:19 2023

"""

from itertools import combinations

def function(x):
    
    biggestValue=0
    print("Our array is ",x)
    
    for i in x:
        if (i>biggestValue):
            
            biggestValue=i    
    
    print("Biggest value: ",biggestValue)
    
    
    setofadditions = []
    
    for i in range(2, len(x) + 1):
        
        for combination in combinations(x, i):
            
            summ = sum(combination)
            
            setofadditions.append(summ)
            
            
    
    DistincSetofAdditions=[]
    
    for i in setofadditions:
        if i not in DistincSetofAdditions:
            
            
            DistincSetofAdditions.append(i)
            
    return [DistincSetofAdditions,biggestValue]

x=[1,4]

array=function(x)
Setofadditions=array[0]
biggestValue=array[1]


print("Set of additions: ",Setofadditions)
print("length of set of additions is ", len(Setofadditions))

k=0
for i in Setofadditions:
    
   
    if (biggestValue==i):
        
        k=1
        
if (k==1):
    
    print("The biggest number can be obtained by an addition of elements in the array")
    
if (k==0):
    print("The biggest number cannot be obtained by any addition of elements in the array!!!")


"""
a=int(input("Enter a number in the list: "))
x=[]

while a!=999:
    
    x.append(a)
    a=int(input("Enter a number in the list: "))
    
    """