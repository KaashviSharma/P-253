# --------------253 Proj----------------
from web3 import Web3
import time
# Import time module here
 

ganache_url = 'http://127.0.0.1:7545'

web3_ganache_connection = Web3(Web3.HTTPProvider(ganache_url))

Alice_account = '0x564dBDBe40fD4ACEa4Ae9cf78A84A95Ea61bad8A'
James_account = '0x80ae2B6eF15A6174338414c9314DAd07B6619bbD'
Ryan_account  = '0x408c48b576c0e13115bE873D784758C4252DE9E0'


nonce1 = web3_ganache_connection.eth.get_transaction_count(Alice_account)

transaction_data1 = {
    'nonce': nonce1,
    'to': James_account,
    'value':web3_ganache_connection.to_wei(10, 'ether'),
    'gas':21000,
    'gasPrice':web3_ganache_connection.to_wei(50,'gwei')
}

private_key1 = '0x5ad643a54cc27610eb76800d2296b859c72d3bf86b0dc8a85a1c28b285312cb4'

singed_transaction1 = web3_ganache_connection.eth.account.sign_transaction(transaction_data1,private_key1)
transaction_hash1 = web3_ganache_connection.eth.send_raw_transaction(singed_transaction1.rawTransaction)

print(web3_ganache_connection.to_hex(transaction_hash1))


print("Wait for a few seconds transaction is in progress : ")
time.sleep(5)
# -----------------
"Define the print statement and" 
"sleep() function here"
# -----------------



nonce2 = web3_ganache_connection.eth.get_transaction_count(James_account)

transaction_data2 = {
    'nonce':nonce2,
    'to': Ryan_account,
    'value':web3_ganache_connection.to_wei(10, 'ether'),
    'gas':21000,
    'gasPrice':web3_ganache_connection.to_wei(40,'gwei')
}

private_key2 = '0xe971ddcb824565f69eefdda306db5a473b92a511af6ca0235e94fee3b10a324d'

singed_transaction2 = web3_ganache_connection.eth.account.sign_transaction(transaction_data2,private_key2)
transaction_hash2 = web3_ganache_connection.eth.send_raw_transaction(singed_transaction2.rawTransaction)

print(web3_ganache_connection.to_hex(transaction_hash2))



