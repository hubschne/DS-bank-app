class Account:
    def __init__(self, *, firstname, lastname, number, balance=None):
        self.firstname = firstname
        self.lastname = lastname
        self.number = number
        self.balance = balance

        assert type(number) == int, 'Number needs to be an integer'
        if balance is not None:
            assert type(self.balance) == float, 'Balance needs to be a float'
        else:
            self.balance = 0

    def info(self):
        return f'Number {self.number}: {self.firstname} {self.lastname} - {self.balance} €'

    def add_to_balance(self, value):
        assert value != 0, 'Amount needs to be greater than 0'
        assert value > 0, 'Amount needs to be greater than 0'
        self.balance = self.balance + value

    def has_funds_for(self, value):
        if value <= self.balance:
            return True
        else:
            return False

    def subtract_from_balance(self, value):
        if value <= self.balance:
            self.balance = self.balance - value
        else:
            assert value <= self.balance, 'Account has not enough funds'
