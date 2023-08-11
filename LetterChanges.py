
"""
Created on Thu Aug 10 17:19:20 2023

"""

#take a string input and return the string that can be obtained shifting every letter 
#by one in the alphabet and obtain a new string. If this string obtains vowel characters
#make them upper case. For example, input:"School of%+& Londonn" will return:"tdIppm pg%+& mpOEpOO"


def LetterChanges(strParam):
  vowel=['a','e','i','o','u']
  strParam=strParam.lower()

  alphabet1="abcdefghijklmnopqrstuvwxyz"
  alphabet=[]
  for i in range (len(alphabet1)):
    alphabet.append(alphabet1[i])

  myparam=[]
  for i in range (len(strParam)):
    myparam.append(strParam[i])

  

  for i in range (len(myparam)):
    if myparam[i]=="z":
      myparam[i]=="a"


    for k in range (len(alphabet)-1):
      if (myparam[i]==alphabet[k]):

        myparam[i]=alphabet[k+1]
        break


  for i in range(len(myparam)):

    for k in range (len(vowel)):

      if myparam[i]==vowel[k]:
        myparam[i]=vowel[k].upper()
  
  newstring=""
  for i in myparam:
    newstring+=i



  return newstring

  # code goes here

# keep this function call here 

strParam="School of%+& Londonn"
print (LetterChanges(strParam))