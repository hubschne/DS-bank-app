import app
# import datetime


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
        assert sender.number in self.accounts, 'Sender has no account yet!'
        assert recipient.number in self.accounts, 'Recipient has no account yet!'
        transaction = app.Transaction(sender=sender.number,
                                      recipient=recipient.number,
                                      subject=subject,
                                      amount=amount,
                                      senderaccount=sender,
                                      recaccount=recipient)
        if not sender.has_funds_for(amount):
            raise AssertionError('Account has not enough funds')
        else:
            sender.balance -= amount
            recipient.balance += amount
            self.transactions.append(transaction)
            return transaction

    def find_name(self, value):
        acc = self.accounts[value]
        print(f'{acc.firstname} {acc.lastname}')

    def transactions_of_account(self, account):
        for item in self.transactions:
            if item.sender == account.number:
                print(item.info() + f'+ {item.amount} €')
        for item2 in self.transactions:
            if item2.recipient == account.number:
                print(item2.info() + f'- {item2.amount} €')
        print(' current balance                                       ' + f' {account.balance} €')

    def bank_statement_year(self, account, year):
        print(self.name + f'   Statement of the year {year}')

        sorted_date_transactions = sorted(self.transactions, key=lambda transaction: transaction.timestamp)
        for item in sorted_date_transactions:
            if item.datetime.year == year:
                if item.sender == account.number or item.recipient == account.number:
                        print(item.info() + f'+ {item.amount} €')
        print(' current balance                                       ' + f' {account.balance} €')

    def bank_statement_month(self, account, month, year):
        print(self.name + f'   Statement of the month {month} {year}')

        sorted_date_transactions = sorted(self.transactions, key=lambda transaction: transaction.timestamp)
        for item in sorted_date_transactions:
            if item.datetime.year == year:
                if item.datetime.month == month:
                    if item.sender == account.number or item.recipient == account.number:
                        print(item.info() + f'+ {item.amount} €')
        print(' current balance                                       ' + f' {account.balance} €')

    def filter_transactions(self, account, value):
        print(f'Suspicious Transactions over amount of {value} €')
        for transaction in self.transactions:
            if transaction.sender == account.number and transaction.amount >= value:
                    print(transaction.info() + f'+ {transaction.amount} €')
        for transaction2 in self.transactions:
            if transaction2.recipient == account.number and transaction2.amount >= value:
                    print(transaction2.info() + f'- {transaction2.amount} €')

    @classmethod
    def print_transaction(cls, tra):
        print(tra.info() + f'+ {tra.amount} €')

    def print_transaction2(self, account, tra):
        for x in tra:
            if account == x.sender:
                print(tra.info() + f'- {tra.amount} €')
            else:
                print(tra.info() + f'+ {tra.amount} €')

    @classmethod
    def sort_list_date(cls, l):
        return sorted(l, key=lambda x: x.timestamp)

    @classmethod
    def sort_list_subject(cls, l):
        return sorted(l, key=lambda x: x.subject)

    def time_statement(self, *, account, year=None, month=None,):
        account_transactions = []
        for tr in self.transactions:
            if tr.sender == account.number or tr.recipient == account.number:
                account_transactions.append(tr)
        sorted_account_transactions = self.sort_list_date(account_transactions)

        account_transactions_year = []

        if year and month is None:
            for tra in sorted_account_transactions:
                if tra.datetime.year == year:
                    account_transactions_year.append(tra)
            return account_transactions_year

        elif year and month:
            for tran in sorted_account_transactions:
                if tran.datetime.year == year and tran.datetime.month == month:
                    self.print_transaction(tran)

    def filter_subject_statement(self, *, account, year=None, month=None):
        account_transactions_year = self.time_statement(account=account, year=year, month=month)
        new_list = self.sort_list_subject(account_transactions_year)
        for x in new_list:
            self.print_transaction2(account, x)

        # for tra in account_transaction_year:
            #     print(tra.info() + f'- {tra.amount} €')
