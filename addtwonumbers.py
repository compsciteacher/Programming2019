#Easiest for most of you
numone=input('First number: ')
numtwo=input('Second number: ')
int_numone=int(numone)
int_numtwo=int(numtwo)
total=int_numone+int_numtwo
print(total)

#A little shorter
numone=int(input('First Number: '))
numtwo=int(input('Second Number: '))
total = numone+numtwo
print(total)

#Shorter with proper formatting

numone=int(input('First Number: '))
numtwo=int(input('Second Number: '))
print("%i plus %i equals %i"%(numone,numtwo,(numone+numtwo)))

#Shortest
print(int(input('first number '))+int(input('second number ')))
