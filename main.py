class Employee:

    def __init__(self, name, cpf, pay):
        self._name = str(name)
        self._cpf = str(cpf)
        self._pay = float(pay)

    def get_bonus(self):
        return self._pay * 0.10


class Manager(Employee):

    def __init__(self, name, cpf, pay, password, number_of_managed):
        super().__init__(name, cpf, pay)
        self._password = int(password)
        self._number_of_managed = int(number_of_managed)

    def get_bonus(self):
        return self._pay * 0.15

    def authenticate(self, password):
        if self._password == password:
            print("access allowed")
            return True
        else:
            print("access denied")
            return False
