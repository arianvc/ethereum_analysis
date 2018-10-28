#!/usr/bin/env python
# coding: utf-8

# Question:
# 
# Consider an Ethereum blockchain. Pick any testnet that you see fit. Write a simplest program that checks which of the smart contracts deployed on the network (a testnet of your choice) has the largest Ether balance (A) and which one has the largest amount of transactions that has been executed on its behalf (B). Which one is easier to answer? A or B? Why? 
# 
# Answer:
# 
# In Ethereum network, smart contracts are treated very similar to wallets; each transaction with them has an address to their wallet. Also, as opposed to the UTXO approach of bitcoin, in Ethereum, the universal state trie is always kept up to date. The state trie containts the key value pairs of the wallets and their current state including balance and nonce. Nonce is the number that prevents the double spending attack; it is incremented for each transaction.
# This makes sense for regular transactions but for contracts, nonce counts the number of subcontracts that are created starting from 1 (EIP 161). Therefore nonce does not count the number of transactions created by a contract.
# This makes finding the balance easier (choice A)
# 
# Implementation: 
# 
# I used web3 with Infura as provider on ropsten network

# In[38]:


import sys
from web3 import Web3 
INFURA_KEY = ''
if not INFURA_KEY:
    print('please insert the INFURA_KEY above before attempting to run the script.')
    sys.exit()
web3 = Web3(Web3.HTTPProvider("https://ropsten.infura.io/v3/%s"%INFURA_KEY))


# In[39]:


latest = web3.eth.getBlock('latest')['number']
address = input('Enter an address: ').lower()
start_block = input('Enter first block for search (default=0): ')
end_block = input('Enter the last block for search (default(latest)=%d: '%latest)

start_block = 0 if start_block == '' else int(start_block)
end_block = latest if end_block == '' else int(end_block)


# In[40]:


# check to see if it's contract not regular wallet
laddress = web3.toChecksumAddress(address)
assert len(web3.eth.getCode(laddress)) > 2

print('Searching for ', address)
balance = web3.eth.getBalance(laddress)
print('The balance is: ', balance)

print('Searching for the count of transactions from %d to '%start_block, end_block)
transactions_found, last_print_percent = 0, 0

for b in range(start_block, end_block+1):
    
    block = web3.eth.getBlock(b, full_transactions=True)
    
    for tx in block.transactions:
        if tx['to']:
                if tx['to'].lower() == address:
                    transactions_found += 1
    
    percent = int((b-start_block)/(end_block-start_block) * 10)
    if percent > last_print_percent:
        print('%d0 percent done: %d of %d'%(percent, b, end_block))
        last_print_percent += 1

print('Done! Transactions found: ', transactions_found)


# It is worth noting that internal transactions are not recorded on the blockchain (and only available in EVM) therefore 'from' transactions are always empty
