import math
budget=float(input("enter your budget= "))
days=int(input("Days= "))
price_per_night=float(input("Price per night= "))
percent=int(input("Percent= "))

hotel_budget=budget-(percent*budget)/100
price=price_per_night*days
if days>7:
    price=price-((5/price_per_night)*100)*days
if(price<hotel_budget):
    print(f"Ivanovi will be left with {round(hotel_budget-price,2)} leva")
else:
    print(f"{price-hotel_budget} leva needed")