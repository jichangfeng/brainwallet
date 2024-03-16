Brain Wallet
===============

Print out the bitcoin private key, wif, address, balance, etc. based on the provided pass phrase.

Installation
------------

To install the Python library and the command line utility, run:

```shell
git clone https://github.com/jichangfeng/brainwallet.git
cd brainwallet
poetry shell
poetry install
```

Usage
------------

legacy address

```shell
python ./brainwallet/legacy_address.py <passphrase>
```

multi address

```shell
python ./brainwallet/multi_address.py <passphrase>
```

Example
------------

legacy address

```shell
python ./brainwallet/legacy_address.py "it was the best of times it was the worst of times"
+-----------------+------------------------------------------------------------------+
| item            | value                                                            |
+=================+==================================================================+
| pass phrase     | it was the best of times it was the worst of times               |
+-----------------+------------------------------------------------------------------+
| private key     | af8da705bfd95621983e5cf4232ac1ca0c79b47122e3defd8a98fa9a4387d985 |
+-----------------+------------------------------------------------------------------+
| bitcoin wif     | 5K9braqLdamgpg4aGT3sgyEBbGMp7MhPDUKPzgZpnX9cSc19eUE              |
+-----------------+------------------------------------------------------------------+
| bitcoin address | 17WenQJaYvqCNumebQU54TsixWtQ1GQ4ND                               |
+-----------------+------------------------------------------------------------------+
| bitcoin balance | 0.00000000 BTC                                                   |
+-----------------+------------------------------------------------------------------+
| total received  | 1.00000000 BTC                                                   |
+-----------------+------------------------------------------------------------------+
| total sent      | 1.00000000 BTC                                                   |
+-----------------+------------------------------------------------------------------+
| transactions    | 2                                                                |
+-----------------+------------------------------------------------------------------+
```

multi address

```shell
python ./brainwallet/multi_address.py "it was the best of times it was the worst of times"
+------------------------------------------------------+------------------------------------+----------------+-----------------+----------------+----------------+
| wif                                                  | address                            | balance        | total receive   | total sent     |   transactions |
+======================================================+====================================+================+=================+================+================+
| 5K9braqLdamgpg4aGT3sgyEBbGMp7MhPDUKPzgZpnX9cSc19eUE  | 17WenQJaYvqCNumebQU54TsixWtQ1GQ4ND | 0.00000000 BTC | 1.00000000 BTC  | 1.00000000 BTC |              2 |
+------------------------------------------------------+------------------------------------+----------------+-----------------+----------------+----------------+
| L36xqrLMeU4EmRQmqBygjRBBkEnrw4MF43aCVbdsuv51RnvcrPnT | 1CRPVRevYicYKapNEhUTqWxyvhyzopNB4B | 0.00000000 BTC | 0.00005000 BTC  | 0.00005000 BTC |              2 |
+------------------------------------------------------+------------------------------------+----------------+-----------------+----------------+----------------+
| L36xqrLMeU4EmRQmqBygjRBBkEnrw4MF43aCVbdsuv51RnvcrPnT | 3AUCaHXFtaWW3AP9YDfiuwzWZStgskUdYn | 0.00000000 BTC | 0.00000000 BTC  | 0.00000000 BTC |              0 |
+------------------------------------------------------+------------------------------------+----------------+-----------------+----------------+----------------+
```
