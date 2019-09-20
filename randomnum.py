

import random

minimum=int(input("What's your lowest number? "))

maximum=input("What's your maximum number? ")
maximum=int(maximum)



for i in range(10):
    print(random.random()*10)
    print(random.randint(minimum,maximum))

