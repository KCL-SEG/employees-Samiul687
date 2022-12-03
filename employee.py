"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""


class Employee:
    def __init__(self, name, commissions, commission_pay, bonus_commission, salary, hours=0):
        self.name = name
        self.commissions = commissions
        self.commission_pay = commission_pay
        self.bonus_commission = bonus_commission
        self.salary = salary
        self.hours = hours

    def get_pay(self):
        total = 0

        if self.hours == 0:
            total += self.salary
        else:
            total += (self.salary * self.hours)

        if self.commissions:
            total += (self.commissions * self.commission_pay)

        elif self.bonus_commission:
            total += self.bonus_commission

        return total

    def __str__(self):
        out = self.name + " works on a "
        if self.hours:
            out += "contract of " + str(self.hours) + " hours at " + str(self.salary) + "/hour"

        else:
            out += "monthly salary of " + str(self.salary)

        if self.commissions > 0:
            out += " and receives a commission for " + str(self.commissions) + " contract(s) at " + str(
                self.commission_pay) + "/contract. Their total pay is " + str(self.get_pay()) + "."

        elif self.bonus_commission:
            out += " and receives a bonus commission of " + str(
                self.bonus_commission) + ". Their total pay is " + str(self.get_pay()) + "."

        else:
            out += ". Their total pay is " + str(self.get_pay()) + "."

        return out


billie = Employee("Billie", 0, 0, 0, 4000)
charlie = Employee("Charlie", 0, 0, 0, 25, 100)
renee = Employee("Renee", 4, 200, 0, 3000)
jan = Employee("Jan", 3, 220, 0, 25, 150)
robbie = Employee("Robbie", 0, 0, 1500, 2000)
ariel = Employee("Ariel", 0, 0, 600, 30, 120)
