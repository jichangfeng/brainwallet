import sys
import hashlib
import blockcypher
from pycoin.symbols.btc import network
from pycoin.encoding.hexbytes import h2b, b2h
from tabulate import tabulate

from brainwallet.BitcoinAccount import BitcoinAccount

if len(sys.argv) <= 1:
    print("No passphrase provided")
    print("Usage: " + sys.argv[0] + " <passphrase>")
    sys.exit()
passphrase = sys.argv[1]
private_key = str(hashlib.sha256(passphrase.encode('utf-8')).hexdigest())
secret_exponent_hex = private_key
secret_exponent = int(secret_exponent_hex, 16)
key = network.keys.private(secret_exponent=secret_exponent)

accounts = []

address = key.address(is_compressed=False)
address_overview = blockcypher.get_address_overview(address, coin_symbol='btc')
account = BitcoinAccount(
    key.wif(is_compressed=False),
    address,
    blockcypher.from_base_unit(address_overview['final_balance'], 'btc'),
    blockcypher.from_base_unit(address_overview['total_received'], 'btc'),
    blockcypher.from_base_unit(address_overview['total_sent'], 'btc'),
    address_overview['final_n_tx']
)
accounts.append(account)

address = key.address(is_compressed=True)
address_overview = blockcypher.get_address_overview(address, coin_symbol='btc')
account = BitcoinAccount(
    key.wif(is_compressed=True),
    address,
    blockcypher.from_base_unit(address_overview['final_balance'], 'btc'),
    blockcypher.from_base_unit(address_overview['total_received'], 'btc'),
    blockcypher.from_base_unit(address_overview['total_sent'], 'btc'),
    address_overview['final_n_tx']
)
accounts.append(account)

hash160 = b2h(key.hash160(is_compressed=True))
p2sh_script = key._network.contract.for_p2pkh_wit(h2b(hash160))
address = key._network.address.for_p2s(p2sh_script)
address_overview = blockcypher.get_address_overview(address, coin_symbol='btc')
account = BitcoinAccount(
    key.wif(is_compressed=True),
    address,
    blockcypher.from_base_unit(address_overview['final_balance'], 'btc'),
    blockcypher.from_base_unit(address_overview['total_received'], 'btc'),
    blockcypher.from_base_unit(address_overview['total_sent'], 'btc'),
    address_overview['final_n_tx']
)
accounts.append(account)

print(tabulate(accounts, headers=['wif', 'address', 'balance', 'total receive', 'total sent', 'transactions'], tablefmt='grid'))
