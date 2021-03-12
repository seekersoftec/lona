import json
from web3 import Web3, HTTPProvider
<<<<<<< HEAD
from api.conf.config import BLOCKCHAIN_WEB_ADDRESS, CONTRACT_ADDRESS, FROM_ADDRESS, FROM_ADDRESS_KEY
=======
from api.conf.config import BLOCKCHAIN_WEB_ADDRESS, CONTRACT_ADDRESS
>>>>>>> 44372833b2e689f10e4261cca465dce4e4d8c249

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
<<<<<<< HEAD
        
=======
    
>>>>>>> 44372833b2e689f10e4261cca465dce4e4d8c249
    # 
    def addLOA(self,eth_address,loa_amount):
        """
            adds specified amount of LOA tokens to the user's current balance
        """
<<<<<<< HEAD
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
=======
        add_LOA = self.contract_reference.functions.addLOA(int(loa_amount),eth_address).transact()
        # waits for the specified transaction (tx_hash) to be confirmed
        # (included in a mined block)
        tx_receipt = web3.eth.waitForTransactionReceipt(add_LOA)
>>>>>>> 44372833b2e689f10e4261cca465dce4e4d8c249
        # 
        return tx_receipt
    
    # 
    def addMARK(self,eth_address,mark_amount):
        """
            adds specified amount of MARK tokens to the user's current balance
        """
<<<<<<< HEAD
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
=======
        add_MARK = self.contract_reference.functions.addMARK(int(mark_amount),eth_address).transact()
        # waits for the specified transaction (tx_hash) to be confirmed
        # (included in a mined block)
        tx_receipt = web3.eth.waitForTransactionReceipt(add_MARK)
>>>>>>> 44372833b2e689f10e4261cca465dce4e4d8c249
        return tx_receipt
        
    
    # 
    def destroyLOA(self,eth_address):
        """
            destroys all of user's LOA tokens
        """
<<<<<<< HEAD
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
=======
        destroy_LOA = self.contract_reference.functions.destroyLOA(eth_address).transact()
        # waits for the specified transaction (tx_hash) to be confirmed
        # (included in a mined block)
        tx_receipt = web3.eth.waitForTransactionReceipt(destroy_LOA)
>>>>>>> 44372833b2e689f10e4261cca465dce4e4d8c249
        return tx_receipt
        
    # 
    def reduceMARK(self,eth_address,mark_amount):
        """
            removes specified amount of MARK tokens from the user's current balance
        """
<<<<<<< HEAD
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
=======
        reduce_MARK = self.contract_reference.functions.reduceMARK(mark_amount,eth_address).transact()
        # waits for the specified transaction (tx_hash) to be confirmed
        # (included in a mined block)
        tx_receipt = web3.eth.waitForTransactionReceipt(reduce_MARK)
>>>>>>> 44372833b2e689f10e4261cca465dce4e4d8c249
        return tx_receipt
    
    # 
    def LOAAmount(self,eth_address):
        """
            Fetches the user's current LOA balance
        """
<<<<<<< HEAD
        amount = self.contract_reference.functions.getUserLoa(Web3.toChecksumAddress(eth_address.lower())).call()
=======
        amount = self.contract_reference.functions.getUserLoa(eth_address).call()
>>>>>>> 44372833b2e689f10e4261cca465dce4e4d8c249
        return amount
    
    # 
    def MarkAmount(self,eth_address):
        """
            Fetches the user's current MARK balance
        """
<<<<<<< HEAD
        amount = self.contract_reference.functions.getUserMark(Web3.toChecksumAddress(eth_address.lower())).call()
        return amount
        
        
        



=======
        amount = self.contract_reference.functions.getUserMark(eth_address).call()
        return amount
        
>>>>>>> 44372833b2e689f10e4261cca465dce4e4d8c249
# 
# def initializer():
    
    
<<<<<<< HEAD
    # fetch contract's abi - necessary to call its functions
    # contract = LONAContract('build/contracts/lona.json')

#     # Set the default account (so we don't need to set the "from" for every transaction call)
    # web3.eth.defaultAccount = web3.eth.accounts[0] #from address
#     # from_eth_account_address = ''
    
#     # eth_account_address = Web3.toChecksumAddress("<Your Account Address>") #Modify
    # eth_account_address = Web3.toChecksumAddress('0x74adfaf57d7a60327a2bfee8424459fac283ff5b')
=======
#     # fetch contract's abi - necessary to call its functions
    # contract = LONAContract('build/contracts/lona.json')

#     # Set the default account (so we don't need to set the "from" for every transaction call)
#     web3.eth.defaultAccount = web3.eth.accounts[0] #from address
#     # from_eth_account_address = ''
    
#     # eth_account_address = Web3.toChecksumAddress("<Your Account Address>") #Modify
#     eth_account_address = Web3.toChecksumAddress('0x74adfaf57d7a60327a2bfee8424459fac283ff5b')
>>>>>>> 44372833b2e689f10e4261cca465dce4e4d8c249
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
    
    
    



   