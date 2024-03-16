class BitcoinAccount:
    def __init__(self, wif, address, balance, total_receive, total_sent, transactions):
        self.wif = wif
        self.address = address
        self.balance = balance
        self.total_receive = total_receive
        self.total_sent = total_sent
        self.transactions = transactions

    def __iter__(self):
        return iter([self.wif, self.address, f"{self.balance:.8f} BTC", f"{self.total_receive:.8f} BTC", f"{self.total_sent:.8f} BTC", self.transactions])
