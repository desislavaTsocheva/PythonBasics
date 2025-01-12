n=int(input("Enter count: "))
if n<20 or n>40:
    n=int(input("Enter new len: "))
list=[]
for i in range(n):
    number=int(input("Enter number 2-200: "))
    if number<2 or number>200:
        number=int(input("Enter valid number: "))
    else:
        list.append(number)
min=min(list)
list.remove(min)
sum=0
for i in range(len(list)):
    if i%2==0:
        sum+=list[i]
print("Sum:",sum)
counter=0
for i in range(len(list)):
    if list[i]%10==0:
        counter+=1
print("%10=0: ",counter)
list_2=[]
for i in range(len(list)):
    if list[i]%3==0 or list[i]%4==0:
        list_2.append(list[i])
        if list[i]%3==0 and list[i]%4==0:
            list_2.remove(list[i])
sum_2=0
count_2=0
print(list_2)
for i in range(len(list_2)):
    if list_2[i]%2!=0:
        sum+=list_2[i]
        count_2+=1
average=sum_2/count_2
print("AVR= ",average)
max_num=max(list_2)
for i in range(len(list_2)):
    if list_2[i]==max_num:
        print(i)
        break