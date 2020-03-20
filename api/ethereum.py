from web3 import Web3
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
#import {Admin} from 'web3-eth-admin';
#from web3.geth.admin import admin
class ethereum:
   # eth_url = "http://3.92.83.194:8545/"

    def __init__(self):
        self.eth_url = "http://3.92.83.194:8545/"
        self.web3 = Web3(Web3.HTTPProvider(self.eth_url))
        #self.web3.geth.admin.start_rpc()
        
        #print(self.web3.isConnected())
        #print(web3.eth.getBlock('latest'))
    def print_art(self):
        #a=self.web3.eth.defaultAccount()
        # self.web3.clientVersion.startswith('Geth')
        #print(self.web3.isConnected())
        print(self.web3.geth.personal.newAccount('the-passphrase'))
    def getAccount(self, lable):
        try:
            return self.web3.geth.personal.newAccount(lable)
           
        except JSONRPCException as e:
            raise (e.error)

    def get(self):
        try:
            return self.web3.isConnected()
           
        except JSONRPCException as e:
            raise (e.error)

    def getAccountList(self):
        try:
            return self.web3.geth.personal.listAccounts()
           
        except JSONRPCException as e:
            raise (e.error)

    def getblockcount(self):
        """
        Returns the number of blocks in the longest block chain.
        """
        try:
            return self.web3.geth.personal.listAccounts()
        except JSONRPCException as e:
            raise (e.error)
    def lockAccount(self,account):
        """
        Returns the number of blocks in the longest block chain.
        """
        try:
            return self.web3.geth.personal.lockAccount(account)
        except JSONRPCException as e:
            raise (e.error)
    def unlockAccount(self,account,passwordohrase):
        """
        Returns the number of blocks in the longest block chain.
        """
        try:
            return self.web3.geth.personal.unlockAccount(account,passwordohrase)
        except JSONRPCException as e:
            raise (e.error)
    def dumpKey(self,key,passwordohrase):
        """
        Returns the number of blocks in the longest block chain.
        """
        try:
            return self.web3.geth.personal.importRawKey(key,passwordohrase)
        except JSONRPCException as e:
            raise (e.error)
    def getBalance(self,account):
        """
        Returns the number of blocks in the longest block chain.
        """
        print(self.web3.eth.coinbase)
        try:
            return self.web3.eth.getBalance(account)
        except JSONRPCException as e:
            raise (e.error)
    def sendfrom(self,sender,reciverAddress,amount):
        """
        Returns the number of blocks in the longest block chain.
        """
        try:
            return self.web3.eth.sendTransaction({'to':reciverAddress,'from':sender,'value':amount})
        except JSONRPCException as e:
            raise (e.error)
    def send(self,reciverAddress,amount):
        """
        Returns the number of blocks in the longest block chain.
        """
        try:
            return self.web3.eth.sendTransaction({'to':reciverAddress,'from':self.web3.eth.coinbase,'value':amount})
        except JSONRPCException as e:
            raise (e.error)