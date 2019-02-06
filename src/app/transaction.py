class Transaction:
    def __init__(self, *, sender, recipient, subject, amount):
        self.sender = sender
        self.recipient = recipient
        self.subject = subject
        self.amount = amount

        assert type(self.sender) == int, 'Sender needs to be an integer'
        assert type(self.recipient) == int, 'Recipient needs to be an integer'
        assert type(self.amount) == float, 'Amount needs to be a float'
        assert amount > 0, 'Amount needs to be greater than 0'

    def info(self):
        return f'From {self.sender} to {self.recipient}: Test transaction - {self.amount} €'
