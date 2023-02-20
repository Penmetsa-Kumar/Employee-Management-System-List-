Emp = []
class Employee:
    
    def __init__(self,id,name,age,salary,grade,dep):
        self.__id = id
        self.__name = name
        self.__age = age
        self.__salary = salary
        self.__grade = grade
        self.__dep = dep
    
    def set_id(self, id):
        self.__id = id

    def set_name(self, name):
        self.__ = name

    def set_age(self, age):
        self.__age = age

    def set_salary(self, salary):
        self.__salary = salary

    def set_grade(self, grade):
        self.__grade = grade

    def set_dep(self, dep):
        self.__dep = dep

    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_salary(self):
        return self.__salary

    def get_grade(self):
        return self.__grade

    def get_dep(self):
        return self.__dep

    def __str__(self):
        return "ID:" + str(self.__id) + \
        ",Name:" + self.__name + \
        ",Age:" + str(self.__age)
    
    def New_Emp():
        try:
            n_emp = int(input("Enter the number of records: "))        
            for i in range(n_emp):
                id = int(input("Enter the Employee Id: "))
                name = input("Emter the Employee Name: ")
                age = int(input("Enter the age: "))
                salary = int(input("Enter the salary: "))
                grade = input("Enter the grade: ")
                dep = input("Enter the Department: ")
                emp = Employee(id,name,age,salary,grade,dep)
                Emp.append(emp)
                print('Record add')
        except:
            print("\nInvalid input")
    
    def Show_Emp():
        if len(Emp) == 0:
            print('No records found')
        else:
            print('Employee detailes:\n')
            for emp in Emp:
                print('ID: ', emp.get_id())
                print('Name: ', emp.get_name())
                print('Age: ', emp.get_age())
                print('Salary: ', emp.get_salary())
                print('Grade: ', emp.get_grade())
                print('Department: ', emp.get_dep())
        
    def Search_Emp():
        try:
            id = int(input('Employee ID to search:'))
            for emp in Emp:
                if emp.get_id() == id:
                    print(emp)
                break
            else:
                print('record not found.')
        except:
            print("\nInvalid Input")

    def Update_Emp():
        try:
            id = int(input('Employee ID to update:'))
            for emp in Emp:
                if emp.get_id() == id:
                    new_name = input('Enter the name: ')
                    new_salary = int(input('Enter the new salary: '))
                    emp.set_name(new_name)
                    emp.set_salary(new_salary)
                    print('Employee updated')
                    break
            else:
                print('record not found.')
        except:
            print("\nInvalid Input")

    def Delete_Emp():
        try:
            id = int(input('Employee ID to delete:'))
            for emp in Emp:
                if emp.get_id() == id:
                    Emp.remove(emp)
                    print('Employee Deleted')
                    print(emp)
                    break
            else:
                print('record not found.')
        except:
            print("\nInvalid Input")

print('Welcom to Employee ')
while True:
    user_input = input('\n 1.add new Employee\n 2.search employee\n 3.update employee\n 4.delete employee\n 5.show employee detailes\n-->')
    if user_input == '1':
        Employee.New_Emp()
    elif user_input == '2':
        Employee.Search_Emp()
    elif user_input == '3':
        Employee.Update_Emp()
    elif user_input == '4':
        Employee.Delete_Emp()
    elif user_input == '5':
        Employee.Show_Emp()
    else:
        break