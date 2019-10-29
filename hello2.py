




#HCD 10/15/2019
#Welcome (continuous)


import random

def hello():
    name=input("Name? ")
    print(f"Hello {name}")
    answer=input("Want to run again? ")
    answer=answer.lower()
    if answer=='yes' or answer=='y':
        hello()
    else:
        print('Bye')

menu()


