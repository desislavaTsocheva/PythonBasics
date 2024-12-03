lst_15=[]
counter=0
for i in range(15):
    number=int(input("enter number: "))
    if(number>0):
        number=int(input("enter valid number: "))
    else:
        lst_15.append(number)
for i in range(len(lst_15)):
    if lst_15[i]%2==0:
        counter+=1
print(f"Odd count: {counter}")
lst_15.sort()
max=lst_15[14]
min=lst_15[0]
print(f"MAX= {max}")
print(f"MIN= {min}")
minus=max-min
print("MAX-MIN= ",minus)

lst_7=[]
for i in range(len(lst_15)):
    if lst_15[i]%2!=0:
        lst_7.append(lst_15[i])
lst_7.sort()
print(lst_7[:7])
for i in range(len(lst_7)):
    if lst_7[i]%3==0:
        lst_7.pop(lst_7[i])
        i-=1
    i+=1
print(lst_7)

