from api.ethereum import ethereum
from web3 import Web3
"""
eth_url = "http://3.92.83.194:8545/"
web3 = Web3(Web3.HTTPProvider(eth_url))
print(web3.isConnected())
print(web3.eth.getBlock('latest'))
"""
test_obj=ethereum()
#test_obj.print_art()
ab=test_obj.getAccount('it is me')
print(ab)
#print(test_obj.lockAccount('0xd957b8CADc89e3E3bbBBF6A6c2d3f20C61999e34'))
#print(test_obj.sendfrom('0xA33281e32Fcf19Ff284E0381Bcfb426F5E7c0F58','0x189025a578c0cbaC1d325269f9E1D6c6520411a1',20))
#print(test_obj.unlockAccount('0x189025a578c0cbaC1d325269f9E1D6c6520411a1','this is truth'))
#getblockcount