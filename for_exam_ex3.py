lst_15=[]
counter=0
for i in range(15):
    number=int(input("enter negative number: "))
    if number>0:
        number = int(input("enter NEGATIVE number: "))
    else:
        lst_15.append(number)

for i in range(len(lst_15)):
    if lst_15[i]%2==0:
        counter+=1
print("Четни числа: ",counter)
lst_15.sort()

lst_15_min=min(lst_15)
print("Min: ",lst_15_min)
lst_15_max=max(lst_15)
print("Max: ",lst_15_max)
sub=lst_15_max-lst_15_min
print("Substraction of min and max num: ",sub)
lst_7=[]
for i in range(len(lst_15)):
    if lst_15[i]%2!=0:
        lst_7.append(lst_15[i])
lst_7.sort()
lst_7=lst_7[:7]
print("List 7: ",lst_7)
for i in lst_7:
    if i%3==0:
        lst_7.remove(i)
print("List 7 without %3==0: ",lst_7)
#list_7_odd=[]
""""for i in range(len(lst_7)):
    if lst_7[i]%3==0:
        list_7_odd.append(lst_7[i])
print("List 7 without 3-kratni: ",list_7_odd)"""""

