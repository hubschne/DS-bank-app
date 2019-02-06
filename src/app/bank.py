class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = []
        self.transactions = []

    def open_account(self, account):
        accountnumber = account['number']
        for acc in self.accounts:
            if acc['number'] == accountnumber:
                raise (AssertionError(f'Account number {accountnumber} already taken!'))
        self.accounts.append(account)
        return account

    def add_transaction(self, *, sender, recipient, subject, amount):
        transaction = {'sender': sender, 'recipient': recipient, 'subject': subject, 'amount': amount}
        sender_exist = False
        recipient_exist = False
        for account_id in self.accounts:
            if account_id['firstname'] == sender['firstname'] and account_id['lastname'] == sender['lastname']:
                sender_exist = True
                break
        assert sender_exist, 'Sender has no account yet!'
        for recipient_id in self.accounts:
            if recipient_id['firstname'] == recipient['firstname'] \
                    and recipient_id['lastname'] == recipient['lastname']:
                recipient_exist = True
                break
        assert recipient_exist, 'Recipient has no account yet!'

        assert amount > 0, 'Amount has to be greater than 0'

        self.transactions.append(transaction)
        return transaction
