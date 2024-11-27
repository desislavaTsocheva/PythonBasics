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

    def search_by_id(self, list):
        search_id=int(input("Enter search id: "))
        for i in list:
            if i.id==search_id:
                i.clothe_info()
                return
        print("No id's found.")

    def search_by_brand(self,list):
        search_brand = str(input("Enter search brand: "))
        list_brand=[]
        for i in list:
            if i.brand == search_brand:
                i.clothe_info()
                return
        print("No items for brand found.")

    def sell_clothe_by_id(self,clothe_list):
        id=int(input("Enter id: "))
        num=int(input("Enter quantity: "))
        for i in clothe_list:
            if i.id==id and self.quantity>=num:
                print("Your order was made!")
                self.quantity=self.quantity-num
            elif self.quantity<num:
                print("Not enought quantity! ")
                return
    print("No products were found")

list_clothes=[]
for i in range(3):
    id=i+1
    type=str(input("Enter type: "))
    brand=str(input("Enter brand: "))
    price=float(input("Enter price: "))
    quantity=int(input("Enter quantity: "))
    clothe_shop1=ClotheShop(id,type,brand,price,quantity)
    list_clothes.append(clothe_shop1)
    clothe_shop1.clothe_info()
clothe_shop1.search_by_id(list_clothes)
clothe_shop1.search_by_brand(list_clothes)
clothe_shop1.sell_clothe_by_id(list_clothes)




