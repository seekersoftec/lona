import json
from web3 import Web3, HTTPProvider
from api.conf.config import BLOCKCHAIN_WEB_ADDRESS, CONTRACT_ADDRESS

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
        add_LOA = self.contract_reference.functions.addLOA(int(loa_amount),eth_address).transact()
        # waits for the specified transaction (tx_hash) to be confirmed
        # (included in a mined block)
        tx_receipt = web3.eth.waitForTransactionReceipt(add_LOA)
        # 
        return tx_receipt
    
    # 
    def addMARK(self,eth_address,mark_amount):
        """
            adds specified amount of MARK tokens to the user's current balance
        """
        add_MARK = self.contract_reference.functions.addMARK(int(mark_amount),eth_address).transact()
        # waits for the specified transaction (tx_hash) to be confirmed
        # (included in a mined block)
        tx_receipt = web3.eth.waitForTransactionReceipt(add_MARK)
        return tx_receipt
        
    
    # 
    def destroyLOA(self,eth_address):
        """
            destroys all of user's LOA tokens
        """
        destroy_LOA = self.contract_reference.functions.destroyLOA(eth_address).transact()
        # waits for the specified transaction (tx_hash) to be confirmed
        # (included in a mined block)
        tx_receipt = web3.eth.waitForTransactionReceipt(destroy_LOA)
        return tx_receipt
        
    # 
    def reduceMARK(self,eth_address,mark_amount):
        """
            removes specified amount of MARK tokens from the user's current balance
        """
        reduce_MARK = self.contract_reference.functions.reduceMARK(mark_amount,eth_address).transact()
        # waits for the specified transaction (tx_hash) to be confirmed
        # (included in a mined block)
        tx_receipt = web3.eth.waitForTransactionReceipt(reduce_MARK)
        return tx_receipt
    
    # 
    def LOAAmount(self,eth_address):
        """
            Fetches the user's current LOA balance
        """
        amount = self.contract_reference.functions.getUserLoa(eth_address).call()
        return amount
    
    # 
    def MarkAmount(self,eth_address):
        """
            Fetches the user's current MARK balance
        """
        amount = self.contract_reference.functions.getUserMark(eth_address).call()
        return amount
        
# 
# def initializer():
    
    
#     # fetch contract's abi - necessary to call its functions
    # contract = LONAContract('build/contracts/lona.json')

#     # Set the default account (so we don't need to set the "from" for every transaction call)
#     web3.eth.defaultAccount = web3.eth.accounts[0] #from address
#     # from_eth_account_address = ''
    
#     # eth_account_address = Web3.toChecksumAddress("<Your Account Address>") #Modify
#     eth_account_address = Web3.toChecksumAddress('0x74adfaf57d7a60327a2bfee8424459fac283ff5b')
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
    
    
    



   