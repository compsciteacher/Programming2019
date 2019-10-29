#Howard Davis
#Space Shuttle v.1

#global variables to make takeoff easier
SCORE=0
NAME=''
DESTINATION=''
LOCATION=''

#startup menu, code not in use yet
def menu():
    c=input("""
    1. New Game
    2. Enter Code
    3. Quit
    
    : """)
    if c=='1':
        new_game()
    elif c=='3':
        quit()
    else:
        print('Invalid Choice')
        menu()

#only takes place if person chooses new game
def new_game():
    global LOCATION, DESTINATION, NAME
    LOCATION='earth' #always start on Earth
    print("""
    Welcome to the Space Shuttle game! You will try and lift off from various planets using the correct escape velocity,
    and if you make it you get some points! Try for the high score, and maybe you'll even be remembered.
    """)
    NAME=input("Name: ")
    print("You start out on Earth, now we try to get to other planets! ")
    weight=float(input("What is the ship's weight? ")) #not used, who knows maybe someday it will be
    spd=float(input("Takeoff speed (km/s): "))
    DESTINATION=input("Where to: ").lower() #changes global destination to wherever we are going
    if destination_check(): #runs destination_check function, if True i returned it does planet check
        planet_check(spd)
    else:
        print("That's not a valid destination, try again") #
        planet_choice()

def destination_check(): #just checks all valid destinations, returns True if included, False if not
    global LOCATION, DESTINATION, NAME
    if DESTINATION=='mercury' or DESTINATION=='venus' or DESTINATION=='earth' or DESTINATION=='moon' or DESTINATION=='mars' or DESTINATION=='ceres' or DESTINATION=='jupiter' or DESTINATION=='io' or DESTINATION=='europa' or DESTINATION=='ganymede' or DESTINATION=='callisto' or DESTINATION=='saturn' or DESTINATION=='titan' or DESTINATION=='uranus' or DESTINATION=='neptune' or DESTINATION=='triton' or DESTINATION=='pluto':
        return True
    else:
        return False

def planet_check(spd): #sets the minimum speed based on location, then runs the speed check
    global LOCATION, DESTINATION, NAME
    print(f"{NAME.title()} you are trying to make your way to  {DESTINATION.title()} at {spd} km/s")
    if DESTINATION==LOCATION:
        print("You're already there! ")
        planet_choice()
    elif LOCATION=='earth':
        min=11.186
    elif LOCATION=='mercury':
        min=4.25
    elif LOCATION=='venus':
        min=10.36
    elif LOCATION=='moon':
        min=2.38
    elif LOCATION=='mars':
        min=5.03
    elif LOCATION=='ceres':
        min=.51
    elif LOCATION=='jupiter':
        min=60.2
    elif LOCATION=='io':
        min=2.558
    elif LOCATION=='europa':
        min=2.025
    elif LOCATION=='saturn':
        min=36.09
    elif LOCATION=='uranus':
        min=21.38
    elif LOCATION=='neptune':
        min=23.56
    elif LOCATION=='pluto':
        min=1.23
    else:
        print('oops')
        menu()
    speed_check(spd,min)

def speed_check(spd,min): #checks if takeoff is successful based on minimum needed, but a max of %110
    global LOCATION, DESTINATION, NAME
    #print(f'you are on {LOCATION} going to {DESTINATION}')
    if spd>=min and spd<=(min*1.1):
        print('SUCCESS! ')
        LOCATION=DESTINATION #if the player succeeds, their location changes to wherever they were going, and destination resets
        DESTINATION=''
        planet_choice()

def planet_choice(): #get speed and destination
    global LOCATION, DESTINATION, NAME
    print(f'{NAME.title()} you are on {LOCATION.title()}, time to take off! ')
    spd = float(input("Takeoff speed (km/s): "))
    DESTINATION = input("Where to: ").lower()
    planet_check(spd)





menu()