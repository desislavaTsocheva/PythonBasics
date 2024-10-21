import sys
countAdminLogins=int(0)
rigthAdminPass=str('Abc123')
passwordAdmin=""

def role_func(role):
    global passwordAdmin
    if role=="admin":
        passwordAdmin=(str(input("Enter your password: ")))
    elif role == "user" and countAdminLogins == 1:
        print("Welcome, dear user!")
    else:
        print("Welcome, dear user! ")
        print("No books added")

role=(str(input("Enter your role (admin or user)")))
role_func(role)
bibliothek={}
if (role=="admin")&(passwordAdmin==rigthAdminPass):
    countAdminLogins=int(1)
    countBooks=(int(input("Enter book count: ")))
    for i in range(countBooks):
        title=(str(input("Enter title: ")))
        status=(str(input("Enter status: ")))
        bibliothek[title]=status
    print("Thank you! Have a nice day!") 
        
role = str(input("Enter your role (admin or user): "))    
if role == "user":
    print("Welcome, dear user!")
    print("BOOKS")
    print("--------------------------------------------")
    for title, status in bibliothek.items():
        print(f"Book: {title} is {status}")
    sys.exit()
elif role == "admin" and passwordAdmin != rigthAdminPass:
    print("Incorrect password!")
    sys.exit()

