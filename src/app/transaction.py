
import datetime
import time


class Transaction:
    def __init__(self, *, sender, recipient, subject, amount, date=None, senderaccount, recaccount):
        assert type(sender) == int, 'Sender needs to be an integer'
        assert type(recipient) == int, 'Recipient needs to be an integer'
        assert type(amount) == float, 'Amount needs to be a float'
        assert amount > 0, 'Amount needs to be greater than 0'

        if date is None:
            self.datetime = datetime.datetime.now()
            self.timestamp = self.datetime.timestamp()
            self.date = self.datetime.strftime('%Y-%m-%d %H:%M:%S')
        else:
            self.date = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
            self.timestamp = time.mktime(time.strptime(date, '%Y-%m-%d %H:%M:%S'))
            self.datetime = datetime.datetime.fromtimestamp(self.timestamp)

        self.sender = sender
        self.recipient = recipient
        self.subject = subject
        self.amount = amount
        self.senderaccount = senderaccount
        self.recaccount = recaccount

    def info(self):
        return f' {self.date} : From {self.senderaccount.firstname} {self.senderaccount.lastname} ' \
            f'to {self.recaccount.firstname} {self.recaccount.lastname}, Subject {self.subject}: Transaction '
