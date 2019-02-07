import app


class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = {}
        self.transactions = []

    def open_account(self, account):
        if type(account) is app.Account:
            assert account.number not in self.accounts, f'Account number {account.number} already taken!'
            self.accounts.update({account.number: account})
            return account
        else:
            raise AssertionError('Account should be an app.Account')

    def add_transaction(self, *, sender, recipient, subject, amount):
        transaction = app.Transaction(sender=sender.number,
                                      recipient=recipient.number,
                                      subject=subject,
                                      amount=amount)
        assert sender.number in self.accounts, 'Sender has no account yet!'
        assert recipient.number in self.accounts, 'Recipient has no account yet!'
        if not sender.has_funds_for(amount):
            raise AssertionError('Account has not enough funds')
        else:
            sender.balance -= amount
            recipient.balance += amount
            self.transactions.append(transaction)
            return transaction
