from __future__ import division
checkNum = 10
primeList_num = []
divList = []
listLength=0

def isPrime(number):
    divList=[]
    for x in range(1, number+1):

        if number / x == 1 or number % x == 0 or number % x == number:

            divList.append(x)

           
    
            listLength=len(divList)

    #print divList

    if listLength<3:

        return True

    else:

        return False


for c in range(1,checkNum):
        
        if checkNum% c ==0:
            if isPrime(c):
                primeList_num.append(c)


print primeList_num

        



