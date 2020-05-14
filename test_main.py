from main import Employee, Manager

manager = Manager("Helena", "555.457.854-95", "5000.00", "9854", "4")
print(manager.get_bonus())
print()
print()
employee = Employee("Isabel", "452.753.930-00", "2000.00")
print(vars(employee))
print()
print(vars(manager))