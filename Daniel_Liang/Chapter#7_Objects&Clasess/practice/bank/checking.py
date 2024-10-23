from super import Super

class Checking(Super):
    def __init__(self, name, family_name, account_type, amount):
        super().__init__(name, family_name, account_type)
        self.amount = amount