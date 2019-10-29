import math

def menu():

    c=input("""
    1. Sum It
    2. Circle Area
    3. Difference Nums
    4. Sum Of
    5. Names and Times
    : """)
    if c=='1':
        n=int(input("Number: "))
        total=sumit(n)
        print(total)
        menu()
    elif c=='2':
        r=float(input("Radius of circle: "))
        print(circlearea(r))
        menu()
    elif c=='3':
        num=differencenums()
        print(num)
    elif c == '4':
        sumof()
    elif c=='5':
        namestimes()
    else:
        print('Not valid choice')
        menu()

#------------------
def sumit(n):
    sum=0
    for x in range(n+1):
        sum+=x
    return sum
    #This also works
    #sum=(n*(n+1))/2
#------------------
def circlearea(r):
    area=math.pi*r*r
    return area
#------------------
def differencenums():
    x=int(input("Number: "))
    if x>17:
        diff=(x-17)*2
    else:
        diff=x-17
    return diff
#--------------------
def sumof():
    x = int(input("Number: "))
    y = int(input("Number: "))
    z=x+y
    print(f'The sum is {z}')
    menu()
#--------------------
def namestimes():
    name=input("Name: ")
    repeat=int(input('Number of repetitions: '))
    print(name*repeat)
    print((name+' ')*repeat)
    menu()
menu()