from secrets import token_bytes
from coincurve import PublicKey
from sha3 import keccak_256

#how many wallets to generate
wallets = 20

def getPrivateKey():
	return keccak_256(token_bytes(32)).digest()
	
def getPublicKey(priKey):
	return PublicKey.from_valid_secret(priKey).format(compressed=False)[1:]
	
def getEthAddress(pubKey):
	return keccak_256(pubKey).digest()[-20:]

def getXEthKeyPairs(x):
	for i in range(1, x+1):
		privateKey = getPrivateKey()
		publicKey = getPublicKey(privateKey)
		ethAddress = getEthAddress(publicKey)
		print(privateKey.hex() , "0x"+ethAddress.hex())


#column headings
print("Private Key",", ETH Address")

#prints the wallets to the console
getXEthKeyPairs(wallets)
