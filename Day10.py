class Staff:
    def __init__(self, name, age, address, salary, total_time):
        self.name = name
        self.age = age
        self.address = address
        self.salary = salary
        self.total_time = total_time
    
    def show_info(self):
        print(f'Name: {self.name} - Age: {self.age} - Address: {self.address}')
    
    def calculate_bonus(self):
        if self.total_time >= 200:
            return self.salary * 20
        elif self.total_time >= 100:
            return self.salary * 10
        elif self.total_time < 100:
            return self.salary 

if __name__ == '__main__':
    name = 'Jek'
    age = 21
    address = 'Ha Noi'
    salary = 10000000
    total_time = 300
    
    nhanVien = Staff(name, age, address, salary, total_time)
    print("Thong tin cua nhan vien:")
    nhanVien.show_info()
    
    bonus = nhanVien.calculate_bonus()
    print(f'Bonus: {bonus}')
