from __future__ import division
checkNum = 13195
primeList_num = []
divList = []
listLength = 0
max_prime = 0


def isPrime(number):  #check if number is prime
    divList = []

    for x in range(1, number + 1):

        if number / x == 1 or number % x == 0 or number % x == number:

            divList.append(x)

            listLength = len(divList)

   # print divList
    if listLength < 3:

        return True

    else:

        return False

for x in xrange(1,checkNum):   #loop for checking if checkNum is divisible by x

    if checkNum % x== 0:       
        isPrime(x)
        if isPrime(x)==True:
            divList.append(x)

        
print divList
