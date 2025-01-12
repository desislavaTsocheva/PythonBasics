lst_20=[]
for i in range(20):
    number=int(input(f"Enter integer positive number: "))
    if number<1:
        print(f"Enter valid positive number: ")
    else:
        lst_20.append(number)
counter_odd=0
for i in range(len(lst_20)):
    if lst_20[i]%2!=0:
        counter_odd+=lst_20[i]
print("Sum odd: ",counter_odd)
sum_numbers=0
average=0
for i in range(len(lst_20)):
    sum_numbers+=lst_20[i]
average=sum_numbers/20
print("Average:",average)
lst_10=[]
lst_20.sort()
lst_20.reverse()
for i in range(len(lst_20)):
    if lst_20[i]%2==0:
        lst_10.append(lst_20[i])
lst_10=lst_10[:10]
lst_10.sort()
lst_10.reverse()
print(lst_10)
for i in lst_10:
    if i%5==0:
        lst_10.remove(i)
print(lst_10)

