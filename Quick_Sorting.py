"""
Created on Sat Aug  5 17:44:29 2023
"""

def QuickSorting(array):
    
    print("Our array is ",array)    #Original Array
    
    for pivot in range (len(array)):            # We repeat the process by taking all of the elements as a pivot one by one
        left=0                #Left index of the array
        right= len(array)-1     #Right index of the array
     
        while   right>left:
    
            
            if(array[left]>array[right]):
                
                switch1=array[right]
                switch2=array[left]
                
                array[left]=switch1
                array[right]=switch2        #Switching the array elements in case there is a misorder
    
            left+=1                        # We check if any of the elements on the left is greater than that on the right  
            if (left==pivot):                #When we reach the pivot, we push back the left index and move one step back our right index
                                            # and repeat the process until the left and the right side of the pivot is sorted
                left=0
                right-=1
        
    return array
                
array=[0,0,0,0,0,0,0,0]

for i in range(0,8):                        # Our array consists of 8 elements and we take the elements from the user
    
    n= int(input("Enter a value of an array containing 8 integer values: "))
    array[i]+=n
    
print("Our sorted array is ",QuickSorting(array))
