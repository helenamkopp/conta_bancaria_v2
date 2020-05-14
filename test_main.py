import unittest
from main import Employee, Manager, Bonus_Control, Client

class TestMain(unittest.TestCase):

    def setUp(self):
        self.emp_1 = Employee("José", "111.111.111-11", "2000.00")
        self.emp_2 = Employee("Mario", "444.444.444-44", "1800.00")
        self.emp_3 = Employee("César", "555.555.555-55", "2200.00")
        self.man_1 = Manager("Maria", "222.222.222-22", "5000.00", "3542", "3")
        self.man_2 = Manager("Paula", "666.666.666-66", "6000.00", "8546", "4")
        self.man_3 = Manager("Carolina", "777.777.777-77", "7000.00", "9852", "6")
        self.cli_1 = Client("Luiza", "333.333.333-33", "3854")


    def tearDown(self):
        pass

    def test_name(self):
        self.assertEqual(self.emp_1._name, "José")
        self.assertEqual(self.man_1._name, "Maria")
        self.assertEqual(self.cli_1._name, "Luiza")

    def test_get_bonus(self):
        self.assertEqual(self.emp_1.get_bonus(), 200)
        self.assertEqual(self.emp_2.get_bonus(), 180)
        self.assertEqual(self.emp_3.get_bonus(), 220)
        self.assertEqual(self.man_1.get_bonus(), 1500)
        self.assertEqual(self.man_2.get_bonus(), 1600)
        self.assertEqual(self.man_3.get_bonus(), 1700)



if __name__ == "__main__":
    unittest.main()










