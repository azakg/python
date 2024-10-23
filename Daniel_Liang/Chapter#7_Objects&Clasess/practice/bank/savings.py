from super import Super

class Savings(Super):
    def __init__(self, name, famuly_name, account_type, amount):
        super().__init__(name, famuly_name, account_type)
        self.amount = amount