# 0x8145bC99355198AE4324E0e0Ac7480Fc7cC7faE8
# 
# 0x25364cfa0778dfcb5c735538626365319460e4c4
# 
# Blockchain 
BLOCKCHAIN_WEB_ADDRESS = 'https://ropsten.infura.io/v3/40462918cb0b45aab9abfb422aaa0f3c'
COMPILED_CONTRACT_ABI = "lona.json"
CONTRACT_ADDRESS = '0x8145bC99355198AE4324E0e0Ac7480Fc7cC7faE8'
FROM_ADDRESS = '0x2a2Af8bdcACD5136ab504E33268f9aFE72C12007'
FROM_ADDRESS_KEY = '7249937e83295c27b5db549ed22f61cc503c78324023862c441fd5330995891a'

import json
from web3 import Web3, HTTPProvider
# from api.conf.config import BLOCKCHAIN_WEB_ADDRESS, CONTRACT_ADDRESS, FROM_ADDRESS, FROM_ADDRESS_KEY

# Client instance to interact with the blockchain
web3 = Web3(HTTPProvider(BLOCKCHAIN_WEB_ADDRESS))

# 
class LONAContract:
    """
        LONA Tokens
        - Initializes ABI from compiled contract path
    """
    def __init__(self,compiled_contract_path):
        # open Path to the compiled contract JSON file
        try:
            with open(compiled_contract_path) as file:
                contract_json = json.load(file)  # load contract info as JSON

            # Fetch deployed contract reference
            self.contract_reference = web3.eth.contract(address=Web3.toChecksumAddress(CONTRACT_ADDRESS), abi=contract_json['abi'])
        except IOError as error:
            print('Unable to open compiled contract file: ', error)
            raise IOError

    # 
    def isReady(self):
        return "{} Network Connected: {} ".format(BLOCKCHAIN_WEB_ADDRESS,web3.isConnected())
        
    # 
    def addLOA(self,eth_address,loa_amount):
        """
            adds specified amount of LOA tokens to the user's current balance
        """
        # tx_hash = self.contract_reference.functions.addLOA(loa_amount,Web3.toChecksumAddress(eth_address.lower())).transact({'from':FROM_ADDRESS})
        # waits for the specified transaction (tx_hash) to be confirmed
        # (included in a mined block)
        add_LOA_tx = self.contract_reference.functions.addLOA(loa_amount,Web3.toChecksumAddress(eth_address.lower())).buildTransaction(
            {
                'nonce': web3.eth.getTransactionCount(FROM_ADDRESS),
                'gas':70000, 
                'chainId': 3
             })
        signed_tx = web3.eth.account.signTransaction(add_LOA_tx, private_key=FROM_ADDRESS_KEY)
        tx_hash= web3.eth.sendRawTransaction(signed_tx.rawTransaction)
        tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
        # 
        return tx_receipt
    
    # 
    def addMARK(self,eth_address,mark_amount):
        """
            adds specified amount of MARK tokens to the user's current balance
        """
        # tx_hash = self.contract_reference.functions.addMARK(mark_amount,Web3.toChecksumAddress(eth_address.lower())).transact({'from':FROM_ADDRESS})
        # waits for the specified transaction (tx_hash) to be confirmed
        # (included in a mined block)
        add_MARK_tx = self.contract_reference.functions.addMARK(mark_amount,Web3.toChecksumAddress(eth_address.lower())).buildTransaction(
            {
                'nonce': web3.eth.getTransactionCount(FROM_ADDRESS),
                'gas':70000, 
                'chainId': 3
            })
        signed_tx = web3.eth.account.signTransaction(add_MARK_tx, FROM_ADDRESS_KEY)
        tx_hash= web3.eth.sendRawTransaction(signed_tx.rawTransaction)
        tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
        # 
        return tx_receipt
        
    
    # 
    def destroyLOA(self,eth_address):
        """
            destroys all of user's LOA tokens
        """
        # destroy_LOA = self.contract_reference.functions.destroyLOA(Web3.toChecksumAddress(eth_address.lower())).transact({'from':FROM_ADDRESS})
        # waits for the specified transaction (tx_hash) to be confirmed
        # (included in a mined block)
        destroy_LOA_tx = self.contract_reference.functions.destroyLOA(Web3.toChecksumAddress(eth_address.lower())).buildTransaction(
            {
                'nonce': web3.eth.getTransactionCount(FROM_ADDRESS),
                'gas':70000, 
                'chainId': 3
            })
        signed_tx = web3.eth.account.signTransaction(destroy_LOA_tx, FROM_ADDRESS_KEY)
        tx_hash= web3.eth.sendRawTransaction(signed_tx.rawTransaction)
        tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
        # 
        return tx_receipt
        
    # 
    def reduceMARK(self,eth_address,mark_amount):
        """
            removes specified amount of MARK tokens from the user's current balance
        """
        # reduce_MARK = self.contract_reference.functions.reduceMARK(mark_amount,Web3.toChecksumAddress(eth_address.lower())).transact({'from':FROM_ADDRESS})
        # waits for the specified transaction (tx_hash) to be confirmed
        # (included in a mined block)
        reduce_MARK_tx = self.contract_reference.functions.reduceMARK(mark_amount,Web3.toChecksumAddress(eth_address.lower())).buildTransaction(
            {
                'nonce': web3.eth.getTransactionCount(FROM_ADDRESS),
                'gas':70000, 
                'chainId': 3
            })
        signed_tx = web3.eth.account.signTransaction(reduce_MARK_tx, FROM_ADDRESS_KEY)
        tx_hash= web3.eth.sendRawTransaction(signed_tx.rawTransaction)
        tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
        # 
        return tx_receipt
    
    # 
    def LOAAmount(self,eth_address):
        """
            Fetches the user's current LOA balance
        """
        amount = self.contract_reference.functions.getUserLoa(Web3.toChecksumAddress(eth_address.lower())).call()
        return amount
    
    # 
    def MarkAmount(self,eth_address):
        """
            Fetches the user's current MARK balance
        """
        amount = self.contract_reference.functions.getUserMark(Web3.toChecksumAddress(eth_address.lower())).call()
        return amount
        
        
        



lc = LONAContract(COMPILED_CONTRACT_ABI)
eth_address = '0x25364cfa0778dfcb5c735538626365319460e4c4'
# print(lc.destroyLOA(eth_address))
print(lc.reduceMARK(eth_address,616))

# 
# def initializer():
    
    
    # fetch contract's abi - necessary to call its functions
    # contract = LONAContract('build/contracts/lona.json')

#     # Set the default account (so we don't need to set the "from" for every transaction call)
    # web3.eth.defaultAccount = web3.eth.accounts[0] #from address
#     # from_eth_account_address = ''
    
#     # eth_account_address = Web3.toChecksumAddress("<Your Account Address>") #Modify
    # eth_account_address = Web3.toChecksumAddress('0x74adfaf57d7a60327a2bfee8424459fac283ff5b')
#     # 

#     # user
#     # add_LOA_tx_hash = contract.addLOA(10)

#     #    
#     # print('{0} LOA: {1}'.format(eth_account_address,user.LOAAmount()))
#     # print('{0} MARK: {1}'.format(eth_account_address,user.MarkAmount()))
#     # Tx Hash
#     # print('LOA tx_hash: {}'.format(add_LOA_tx_hash['transactionHash'].hex()))
#     # 

# if __name__ == "__main__":
#     initializer()
    
    
    



   