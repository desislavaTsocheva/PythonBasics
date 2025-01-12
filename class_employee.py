class Employee:
    def __init__(self,i_num,fname,lname,work_experience,education_level,salary,age):
        self.i_num=i_num
        self.fname=fname
        self.lname=lname
        self.work_experience=work_experience
        self.education_level=education_level
        self.salary=salary
        self.age=age
    def display_info(self):
        print(f"ID: {self.i_num}, NAME: {self.fname} {self.lname}"
              f"EXP: {self.work_experience}, EDUCATION: {self.education_level}"
              f"SALARY: {self.salary}, AGE= {self.age}")
    def bonus(self):
        if self.education_level=="Висше образование":
           self.salary=self.salary+(5/100)+self.work_experience*(1.2/100)
        elif self.education_level=="Средно образование":
            self.salary=self.salary+(2/100)+self.work_experience*(1.2/100)
employees_count=int(input("Enter employees count: "))
employees=[]
for i in range(employees_count):
    i_num=int(input("Enter employee id: "))
    f_name=str(input("Enter employee first name: "))
    l_name=str(input("Enter employee last name: "))
    work_experience=int(input("Enter employee years experience: "))
    education_level=str(input("Enter employee education level: "))
    salary=float(input("Enter employee salary: "))
    age=int(input("Enter employee age: "))
    emp=Employee(i_num,f_name,l_name,work_experience,education_level,salary,age)
    employees.append(emp)

def sort_by_age(employees):
    employees.sort(key=lambda emp:emp.age)
def search_by_name(employee_list,name,lname):
    name=str(input("NAME: "))
    lname=str(input("LAST NAME: "))
    for i in range(len(employee_list)):
        if employee_list.fname==name and employee_list.lname==lname:
            employee_list.display_info()
            break
        else:
            print("Not found!!!")
            break
def print_by_education_experience(employee_list,education=" ",experience=0):
    education=str(input("Education: "))
    experience=int(input("Experience: "))
    for i in range(len(employee_list)):
        if employee_list.education_level==education and employee_list.work_experience==experience:
            employee_list.display_info()
            break
        else:
            print("Not found!!!")
            break
def remove_employee(employee_list,i_num):
    i_num=int(input("Enter id: "))
    for i in range(len(employee_list)):
        if employee_list[i].i_num==i_num:
            employee_list.remove(i)
            print("Information deleted!!!")
            break
        else:
            print("Wrong id!!!")
            break