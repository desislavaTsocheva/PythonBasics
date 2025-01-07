class ClotheShop:
    def __init__(self, id,type,brand,price,quantity):
        self.id=id
        self.type=type
        self.brand=brand
        self.price=price
        self.quantity=quantity

    def clothe_info(self):
        print(f"ID: {self.id} -- TYPE: {self.type} -- BRAND: {self.brand} -- PRICE: {self.brand} -- PRICE: {self.price} -- QUANTITY: {self.quantity}")

    def change_price(self):
        new_price=float(input("Enter new price: "))
        self.price=new_price

    def change_qty(self):
        new_quantity=int(input("Enter quantity: "))
        self.quantity=new_quantity

clothe_1=ClotheShop(1,"shirt","LV",34.5,5)
clothe_2=ClotheShop(2,"pants","LV",874.5,1)
clothe_3=ClotheShop(3,"socks","NL",24.5,50)
clothes_list=[]
clothes_list.append(clothe_1)
clothes_list.append(clothe_2)
clothes_list.append(clothe_3)
def search_by_id(clothes_list,id):
    for identification in clothes_list:
        if identification.id==id:
            identification.clothe_info()

def search_by_brand(clothes_list,brand):
    for brands in clothes_list:
        if brands.brand==brand:
            brands.clothe_info()
def sell_clothe_by_id(clothes_list,id,num):
    for ident in clothes_list:
        if ident.id==id:
            if ident.quantity>=num:
                print("Your order is ready")
                break
            else:
                print("Not enough quantity")
                break
search_by_id(clothes_list,1)
search_by_brand(clothes_list,"LV")
sell_clothe_by_id(clothes_list,2,1)

