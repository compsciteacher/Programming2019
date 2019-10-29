
def main():

    menu()

def menu():
    name=input("Name: ") #what's the bad idea here?
    c=input("""
    1. Hello
    2. Math
    3. Quit
    : """)
    if c=='1':
        hello(name)
    elif c=='2':
        math()
    elif c=='3':
        quit()
    else:
        print('Not valid choice')
        menu()
def hello(name):
    print(f"Hi {name}")
    menu()
def math():
    type_math=input("""
    What type of math would you like to do:
    1. Addition
    2. Subtraction
    3. Back to menu
    : """)
    if type_math=='1':
        answer=addition()
        print(answer)
        math()
    elif type_math=='2':
        answer=subtraction()
        print(answer)
        math()
    elif type_math=='3':
        menu()
    # elif type_math=='4':
    #     answer=testit()
    #     print(answer)
    else:
        print('Invalid choice')
        math()
def addition():
    num1=float(input("First number: "))
    num2=float(input("Second number: "))
    total=num2+num1
    return total
def subtraction():
    num1 = float(input("First number: "))
    num2 = float(input("Second number: "))
    total = num1-num2
    return total

# def testit():
#     word = "Testing"
#     return word


main()