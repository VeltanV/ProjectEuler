from __future__ import division
checkNum = 600851475143
primeList_num = []
divList = []
listLength = 0
max_prime = 0


def isPrime(number):
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

for x in xrange(1,11000):

    if isPrime(x):
            primeList_num.append(x)
        
print len(primeList_num)
print primeList_num[10001]

