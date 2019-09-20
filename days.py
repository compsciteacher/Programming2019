#HCD
#7 days v.1
#9/10/2019

start_day=int(input("What day are you leaving on (starting with 0 as Sunday and 6 as Saturday)? "))
away_time=int(input("How many days will you be gone? "))
total=start_day+away_time
return_day=total%7 #same as 24 hour clock you just divide by days in the week, remainder is day you will return on
print(f"You will return on {return_day}")
