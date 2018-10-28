# Ethereum Analysis


## Question

Consider an Ethereum blockchain. Pick any testnet that you see fit. Write a simplest program that checks which of the smart contracts deployed on the network (a testnet of your choice) has the largest Ether balance (A) and which one has the largest amount of transactions that has been executed on its behalf (B). Which one is easier to answer? A or B? Why?

## Answer

In Ethereum network, smart contracts are treated very similar to wallets; each transaction with them has an address to their wallet. Also, as opposed to the UTXO approach of bitcoin, in Ethereum, the universal state trie is always kept up to date. The state trie containts the key value pairs of the wallets and their current state including balance and nonce. Nonce is the number that prevents the double spending attack; it is incremented for each transaction. This makes sense for regular transactions but for contracts, nonce counts the number of subcontracts that are created starting from 1 (EIP 161). Therefore nonce does not count the number of transactions created by a contract. This makes finding the balance easier (choice A)

## Implementation

I used web3 in python with Infura as provider on ropsten network.
Python is my language of choice since it is easy for data manipulation and I have experience in it (Machine learning and web development). JS is also a good choice.
I used Infura because it is much faster to work with (compared to local node implementation; about 100x !). Also ropsten is the de facto option for testnet (although other networks exist).


## Limitations

It is worth noting that internal transactions are not recorded on the blockchain (and only available in EVM during execution) therefore 'from' match is not found.

