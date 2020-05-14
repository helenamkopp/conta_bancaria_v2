class Employee:

    def __init__(self, name, cpf, pay):
        self._name = name
        self._cpf = cpf
        self._pay = pay


class Manager(Employee):

    def __init__(self, name, cpf, pay, password, number_of_managed):
        super().__init__(name, cpf, pay)
        self._password = password
        self._number_of_managed = number_of_managed

    def authenticate(self, password):
        if self._password == password:
            print("access allowed")
            return True
        else:
            print("access denied")
            return False
