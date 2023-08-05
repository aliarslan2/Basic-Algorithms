# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 17:44:29 2023

@author: arsla
"""

def QuickSorting(array):
    
    print("Our array is ",array)
    
    for pivot in range (len(array)):
        left=0
        right= len(array)-1
     
        while   right>left:
    
            
            if(array[left]>array[right]):
                
                switch1=array[right]
                switch2=array[left]
                
                array[left]=switch1
                array[right]=switch2
    
            left+=1
            if (left==pivot):
                left=0
                right-=1
        
    return array
                
array=[0,0,0,0,0,0,0,0]

for i in range(0,8):
    
    n= int(input("Enter a value of an array containing 8 integer values: "))
    array[i]+=n
    
print("Our sorted array is ",QuickSorting(array))