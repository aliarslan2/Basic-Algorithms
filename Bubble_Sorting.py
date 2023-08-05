"""
Created on Sat Aug  5 18:08:03 2023

"""
def BubbleSort(array):
    lastindex=len(array)
    print("Our array is ",array)
    
    
    for i in range(lastindex-1):       # We repeat the process len(array) times
        index1=0
        index2=1
        
    
        while index2<lastindex:        # We want to compare each of the two elements of the set till the very end.
            
        
            if(array[index1]>array[index2]):            # We check the two values and switch them if they are not in order
                
                switch1=array[index1]
                switch2=array[index2]
                
                array[index1]=switch2
                array[index2]=switch1
                
            index1+=1
            index2+=1
            
    return array

array=[0,0,0,0,0,0,0,0]

for i in range(0,8):
    
    n= int(input("Enter a value of an array containing 8 integer values: "))
    array[i]+=n
    
print("Our sorted array is ",BubbleSort(array))
