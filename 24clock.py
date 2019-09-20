#HCD
#24 hour clock v.1
#9/10/2019

current=int(input("What time is it on a 24 hour clock? "))
wait=int(input("How long before you want the alarm to go off (in hours)? "))

alarm_time=(current+wait)%24 #add the clock time and wait time, then divide by 24 and the remainder will be the alarm time
print(f"The alarm time is {alarm_time}")

