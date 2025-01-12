list_len=int(input("Enter list length between 15 and 35: "))
if list_len<15 or list_len>35:
    list_len=int(input("Enter valid length: "))
list=[]
for i in range(list_len):
    number=int(input("Enter number between 30 and 300: "))
    if number<30 or number>300:
        number=int("Enter valid number between 30 and 300: ")
    else:
        list.append(number)
counter=0
for i in range(len(list)):
    if (list[i]//10)%3==0:
        counter+=1
print("Count //10 %3 ==0: ",counter)
list.sort()
for i in range(len(list)):
    if list[i]%6==4:
        print("Index %6==4: ",i)
        break
list_2=[]
for i in range(len(list)):
    if (list[i]>=10) and (list[i]%2==0 or list[i]%3==0):
        list_2.append(list[i])
count=0
sum=0
for i in range(len(list_2)):
    if i%2!=0:
        sum+=list_2[i]
        count+=1
average=sum/count
print("Average= ",average)
min=0
for i in range(len(list_2)):
    min=list_2[0]
    if list_2[i]%2==0 and list_2[i]<min:
        min=list_2[i]
list_2.remove(min)
print(list_2)

