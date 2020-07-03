from __future__ import division
checkNum = 600851475143 
primeList_num = []
divList = []
listLength = 0
max_prime = 0
x = 2


def isPrime(number):  # check if number is prime
    divList = []

    for x in range(1, number + 1):

        if number / x == 1 or number % x == 0 or number % x == number:

            divList.append(x)

            listLength = len(divList)
   # print divList
    return listLength < 3

while checkNum != 1:  # loop for checking if checkNum is divisible by x

    while (checkNum % x == 0):
        checkNum = checkNum / x
        print x
    x = x + 1

print checkNum
