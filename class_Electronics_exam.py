class Electronics:
    def __init__(self,id,name,brand,category,price,quantity):
        self.id=id
        self.name=name
        self.brand=brand
        self.category=category
        self.price=price
        self.quantity=quantity
    def product_info(self):
        print(f"ID: {self.id}, BRAND: {self.brand}, "
              f"CATEGORY: {self.category},"
              f" PRICE: {self.price}, QUANTITY: {self.quantity}")
    def update_product(self):
        new_price=float(input("Enter new price: "))
        self.price=new_price
    def update_quantity(self):
        new_qty=int(input("Enter new quantity: "))
        self.quantity=new_qty
products_list=[]
for i in range(2):
    id=int(input("ID= "))
    name=str(input("NAME= "))
    brand=str(input("BRAND= "))
    category=str(input("CATEGORY= "))
    price=float(input("PRICE= "))
    quantity=int(input("QUANTITY= "))
    electronic=Electronics(id,name,brand,category,price,quantity)
    products_list.append(electronic)

def search_by_name(products_list,name):
    for i in products_list:
        if i.name==name:
            i.product_info()
            break
        else:
            print("Product not founded")
            break
search_by_name(products_list,"laptop")
def search_by_category(products_list,category):
    for i in products_list:
        if i.category==category:
            i.product_info()
            break
        else:
            print("Product not founded")
            break
search_by_category(products_list,"computer")
def sell_product_by_id(products_list,id,num):
    for i in products_list:
        if i.id==id and i.quantity>=num:
            print("Your order is ready!")
            i.quantity-=num
            break
        elif i.id==id and i.quantity<num:
            print("Not enough quantity!")
            break
        else:
            print("Product not founded!")
            break
sell_product_by_id(products_list,2,4)








