import sys
import blockcypher
from pycoin.symbols.btc import network
from tabulate import tabulate
from brainwallet.BrainWallet import BrainWallet

if len(sys.argv) <= 1:
    print("No passphrase provided")
    print("Usage: " + sys.argv[0] + " <passphrase>")
    sys.exit()
passphrase = sys.argv[1]
wallet = BrainWallet()
private_key, address = wallet.generate_address_from_passphrase(passphrase)
key = network.keys.private(secret_exponent=int(private_key, 16))
wif_uncompressed = key.wif(is_compressed=False)
address_overview = blockcypher.get_address_overview(address, coin_symbol='btc')
satoshi = address_overview['final_balance']
balance = blockcypher.from_base_unit(satoshi, 'btc')
total_received = blockcypher.from_base_unit(address_overview['total_received'], 'btc')
total_sent = blockcypher.from_base_unit(address_overview['total_sent'], 'btc')
transactions = address_overview['final_n_tx']

data = [
    ['pass phrase', passphrase],
    ['private key', private_key],
    ['bitcoin wif', wif_uncompressed],
    ['bitcoin address', address],
    ['bitcoin balance', f'{balance:.8f} BTC'],
    ['total received', f'{total_received:.8f} BTC'],
    ['total sent', f'{total_sent:.8f} BTC'],
    ['transactions', transactions]
]

print(tabulate(data, headers=['item', 'value'], tablefmt='grid'))
