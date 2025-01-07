class Library:
    def __init__(self,id,title,author,genre,price,quantity):
        self.id=id
        self.title=title
        self.author=author
        self.genre=genre
        self.price=price
        self.quantity=quantity
    def book_info(self):
        print(f"ID:{self.id} BOOK: {self.title} AUTHOR:{self.author} GENRE:{self.genre} PRICE:{self.price} QUANTITY:{self.quantity}")
    def change_price(self):
        new_price=float(input("Enter new price: "))
        self.price=new_price
    def change_qty(self):
        new_qty=int(input("Enter new quantity: "))
        self.quantity=new_qty
book_1=Library(1,"Червената шапчица","Братя Грим","Приказка",20,5)
book_2=Library(2,"Пътникът без име","Никола Бьогле","Трилър",10,50)
book_3=Library(3,"Под игото","Иван Вазов","Роман",50,10)
books_list=[]
books_list.extend([book_1,book_2,book_3])

book_1.book_info()
book_1.change_price()
book_1.change_qty()

def search_by_title(books_list,title):
    for titles in books_list:
        if titles.title.lower()==title.lower():
            titles.book_info()
def search_by_genre(books_list,genre):
    for genres in books_list:
        if genres.genre==genre:
            genres.book_info()
def sell_book_by_id(books_list,id,num):
    for ident in books_list:
        if ident.id==id and ident.quantity>=num:
            ident.quantity-=num
            total_price=ident.quantity*ident.price
            print(f"Успешна продажба. Дължите: {total_price:.2f}")
            return
        elif ident.id==id and ident.quantity<num:
            print("Недостатъчно количество")
            return
    print("Не е намерена книгата ")

search_by_title(books_list,"Под Игото")
search_by_genre(books_list,"Роман")
sell_book_by_id(books_list,2,4)