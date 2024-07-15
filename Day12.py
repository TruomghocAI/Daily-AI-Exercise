class Person:
    def __init__(self,name,phone):
        self._name = name
        self._phone = phone

class Employee(Person):
    def __init__(self,name,phone,annual_salary,year_of_starting_work):
        super().__init__(name,phone)
        self._annual_salary = annual_salary
        self._year_of_starting_work = year_of_starting_work

class StackEmployee():
    def  __init__(self,capacity):
        self._capacity = capacity
        self._data = []
    
    def is_empty(self):
        if len(self._data) == 0:
            return True
        return False
    
    def is_full(self):
        if len(self._data) == self._capacity:
            return True
        return False

    def pop(self):
        if self.is_empty():
            print("Empty data")
            return None
        
        return self._data.pop()
    
    def push(self,object):
        if self.is_full():
            print("Full data")
            
        else:
            self._data.append(object)
            
    def peek(self):
        return self._data[-1]
    
    def __call__(self):
            if self.is_empty():
                print("Stack is empty")
            else:
                for i, emp in enumerate(self._data, 1):
                    print(f"{i}. Name: {emp._name}, Phone: {emp._phone}  Salary: ${emp._annual_salary}, Started: {emp._year_of_starting_work}")

if __name__ == "__main__":
    emp1 = Employee("John Doe", "123-456-7890", 50000, 2020)
    emp2 = Employee("Jane Smith", "234-567-8901", 55000, 2019)
    emp3 = Employee("Mike Johnson", "345-678-9012", 52000, 2021)
    emp4 = Employee("Emily Brown", "456-789-0123", 58000, 2018)
    emp5 = Employee("David Lee", "567-890-1234", 51000, 2022)
    emp6 = Employee("Sarah Wilson", "678-901-2345", 54000, 2020)
    emp7 = Employee("Tom Anderson", "789-012-3456", 53000, 2021)
    
    stack = StackEmployee(5)
    for emp in [emp1, emp2, emp3, emp4, emp5]:
        stack.push(emp)
    stack()