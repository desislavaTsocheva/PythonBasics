#ПЪРВА ИЗПИТНА ЗАДАЧА
#Да се въведе лист с 10 елементи, цели, положителни числа
lst_10=[]
for i in range(10):
    number=int(input("Enter number= "))
    if(number>0&number%1==0):
        lst_10.append(number)
    else:
        print("Enter right number!!!")
        number = int(input("Enter number= "))
#Да се изведе броят на нечетните числа в списъка
counter=0
sum=0
for i in range(len(lst_10)):
    sum+=lst_10[i]
    if lst_10[i]%2!=0:
        counter+=1
print("Odd= ", counter)
#Средноаритемтично на числата в списъка
average=sum/len(lst_10)
print("Average= ",average)
#2-ри списък, съхраняващ 5-те най-големи числа от списъка
lst_5=[]
lst_10.sort()
lst_10.reverse()
"""" Взема първите 5 елемента! *Кратни на 2 """
for i in range(len(lst_10)):
    if lst_10[i]%2==0:
        lst_5.append(lst_10[i])
    elif len(lst_10)==5:
        break
print(lst_5)
#Да се сортира 2-рия списък в възходящ ред
lst_5.reverse()
print(lst_5)
#Да се изтрият всички елементи от 2-рия списък с четен индекс
for i in lst_5:
    if i%2==0:
        lst_5.remove(i)
print(lst_5)