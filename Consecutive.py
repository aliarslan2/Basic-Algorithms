
"""
Created on Thu Aug 10 17:19:21 2023
"""
# Returns the remaining number of numbers in order for the array to be in increasing order
#For instance input: [4,8] otuput: 3  That is because we want tne remaining number of terms
#which will help us sort the array in an increasing fashion (etc.[4,5,6,7,8]). We have extra 
#three numbers to achieve it.

def Consecutive(arr):

    ourarray=arr

    biggestNumber=ourarray[0]
    for i in ourarray:
        if (i > biggestNumber):
            biggestNumber=i

    smallestNumber=biggestNumber

    for i in ourarray:
        if (i<smallestNumber):
            smallestNumber=i

    sth=biggestNumber-smallestNumber-1
    
    for i in range (len(ourarray)-1):
        for k in range (i+1,len(ourarray)):
            if ourarray[k]==ourarray[i]:
                ourarray.remove(ourarray[k])
    b=len(ourarray)-2
    sth=sth-b
                
    return sth


# keep this function call here 
  
arr=[-2,15,5,5]
print (Consecutive(arr))
