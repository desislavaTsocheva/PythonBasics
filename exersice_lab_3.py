import math
from idlelib.autocomplete_w import HIDE_FOCUS_OUT_SEQUENCE

#Ex1: Find average
numbers_count=int(input("Enter numbers count= "))
sum=0
for i in range(numbers_count):
    num=(int(input(f"Enter number {i+1}: ")))
    sum+=num
average=sum/numbers_count
print(average)

#Ex2: Print strings
name=str(input("Enter name: "))
last_name=str(input("Enter lastname: "))
print(name+" "+last_name)

#Ex3: C --> F
cel=float(input("C= "))
far=round(cel*1.8+32.2)
print("Farenheit= ",far)

#EX4: Minutes to days, hours and mins
minutes=int(input("Enter minutes: "))
days=minutes/1400
hours=minutes/60
mins=minutes%60
print(f"DAYS: {days}, HOURS: {hours}, MINS: {mins}")

