
"""
Created on Sun Dec 27 19:44:40 2020
"""

# PROBLEM1

sumOfNumbers = 0
for i in range(1000):
    if (i%3==0 or i%5==0) :
        sumOfNumbers += i         
print(sumOfNumbers)


# PROBLEM2

number1 = 1
number2 = 2
number3 = 3
sumOfNumbers=2
while ( number3 <= 4000000 ):
    number3 = number1+ number2
    number1 = number2
    number2= number3
    if ( number3 % 2 ==0):
        sumOfNumbers += number3
print( sumOfNumbers )


# PROBLEM3

i = 600851475143
j=2
while ( i>=2):
    j+=1
    while( i%j == 0):
        maxnumber= j
        i = i/j 
print(maxnumber)
    

# PROBLEM4

result = 0
for i in range (1000):
    for j in range(1000):
        checkNumber = i*j
        if( str(checkNumber) == str(checkNumber)[::-1]):
            ourNumber = checkNumber
            if(ourNumber>result):
                result = ourNumber
                k=i
                l=j
          
print(result," i: ",k," j:",l)

#PROBLEM5

number = 1
for i in range (1,21):
    if (number%i != 0): 
        for j in range (1,21):
            if (number * j) % i == 0:
                number *= j
                break
print (number)
            

#PROBLEM6

number=0
for i in range(101):
    number2 = i*i
    number+=number2
    
numbersquare=0
for i in range(101):
    numbersquare+=i
    
myNumber = numbersquare*numbersquare - number
print(myNumber)

#PROBLEM7

myList= []
myList.append(2)
i=3
while( len(myList)<10001):
    isPrime= True
    
    for j in range(2,i):        
        if(i%j == 0):
            isPrime = False
            break
            
    if(isPrime):        
        myList.append(i)
    
    i+=1

print(myList[10000])


#PROBLEM8

number = str(7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450)
i=0
myNumber = 1
while ( i< len(number)):
    checkNumber=1
    k=i
    if(k<len(number)-13):
        for j in range(13):      
            checkNumber*= int(number[k])
            k+=1
            if(checkNumber>myNumber):
                myNumber = checkNumber
    i+=1
        
print(myNumber)


#PROBLEM9

for i in range(1000):
    for j in range(1000):
        if( i<j):
            k = i*i + j*j
            if (j< (k**(1/2))):
                ourNumber = i+j+k**(1/2)
                if ( ourNumber == 1000):
                    myNumber = i*j*k**(1/2)
                    print(myNumber)
                    break

#PROBLEM10
myList=[]
myNumber=2
for i in range(2,2000000):
    
    if(i%2 != 0):
        isPrime = True
        for j in range(2,int(i**0.5)+1):
            if( i%j == 0):
                isPrime = False
               
        if(isPrime):
            myNumber +=i    
print(myNumber)

#PROBLEM11


myGrid ="08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08 49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00 81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65 52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91 22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80 24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50 32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70 67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21 24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72 21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95 78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92 16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57 86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58 19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40 04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66 88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69 04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36 20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16 20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54 01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48"
myList= []
myCounter=0
# 0-2, 3-5, 6-8
for i in range(20):
    myList.append([])
    for j in range(20):
        myList[i].append(myGrid[myCounter:myCounter+2])
        myCounter+=3

greatestNumber=0

for i in range(20):
    for j in range(20):    
      
        if(i<=16):
            myNumber = int(myList[i][j])*int(myList[i+1][j])*int(myList[i+2][j])*int(myList[i+3][j])
            if (myNumber>greatestNumber):
                greatestNumber = myNumber
                
        if(j<=16):
            myNumber = int(myList[i][j])*int(myList[i][j+1])*int(myList[i][j+2])*int(myList[i][j+3])
            if (myNumber>greatestNumber):
                greatestNumber = myNumber
            
        if(i<=16 and j<=16):
            myNumber = int(myList[i][j])*int(myList[i+1][j+1])*int(myList[i+2][j+2])*int(myList[i+3][j+3])
            if (myNumber>greatestNumber):
                greatestNumber = myNumber
                
        if(i<=16 and j>2):
            myNumber= int(myList[i][j])*int(myList[i+1][j-1])*int(myList[i+2][j-2])*int(myList[i+3][j-3])
            if(myNumber>greatestNumber):
                greatestNumber = myNumber
   
print(greatestNumber)
        
        

#PROBLEM12

sumNumbers=0
i=0
count=0
myList=[]
while(len(myList)<500):
    i+=1 
    sumNumbers+=i
    count=0
    myList=[]
    for j in range(1,int(sumNumbers**0.5)+1): 
        if sumNumbers%j ==0:       
            if j not in myList:
                myList.append(j)
            if sumNumbers/j not in myList:
                myList.append(sumNumbers/j)
            
print(sumNumbers)
       
    
#PROBLEM13

myList=[]
with open("problem12.txt") as file:
    lines = file.read().splitlines()    
sumOfNumbers=0
for i in lines:
    sumOfNumbers+= int(i)
 
sumOfNumbers = str(sumOfNumbers)

print(sumOfNumbers[:10])
    

#PROBLEM14

counter=0
myNumber=0
for i in range(1000000):
    lastPoint=i
    myCounter=0
    while(lastPoint>1):
        
        if lastPoint%2==0:
            lastPoint/=2
            
        elif lastPoint%2==1:
            lastPoint=3*(lastPoint)+1
        myCounter+=1
        
    if(myCounter>counter):
        myNumber=i
        counter=myCounter
        
print(myNumber)
        
            
#PROBLEM15

def factorial(a):
    myFac=1
    for i in range(1,a+1):
        myFac *= i
    return myFac
        
grid=20

firstRule = grid+grid
routes= factorial(firstRule)/(factorial(grid)*factorial(grid))

print(int(routes))

#PROBLEM16

myNumber=1
for i in range(1,1001):
    myNumber*=2
myNumber=str(myNumber)
sumOfNumbers=0
for i in range(len(myNumber)):
    theNumber =int( myNumber[i])
    sumOfNumbers += theNumber
   
print(sumOfNumbers)


    
    


    
    
    
                
                
                
        
    

        


    
    
