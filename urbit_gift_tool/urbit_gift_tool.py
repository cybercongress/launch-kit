import re
import pandas as pd
import requests
from io import StringIO
from web3 import Web3
from progressbar import ProgressBar

pbar = ProgressBar()


eth_rpc_url = "http://titan.cybernode.ai:38645"
web3 = Web3(Web3.HTTPProvider(eth_rpc_url))
url = 'https://azimuth.network/stats/events.txt'
abi = [{"constant":True,"inputs":[{"name":"","type":"uint32"},{"name":"","type":"uint32"}],"name":"escapeRequestsIndexes","outputs":[{"name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"name":"_whose","type":"address"}],"name":"getOwnedPoints","outputs":[{"name":"ownedPoints","type":"uint32[]"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"name":"","type":"address"},{"name":"","type":"uint256"}],"name":"votingFor","outputs":[{"name":"","type":"uint32"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"name":"","type":"uint32"}],"name":"rights","outputs":[{"name":"owner","type":"address"},{"name":"managementProxy","type":"address"},{"name":"spawnProxy","type":"address"},{"name":"votingProxy","type":"address"},{"name":"transferProxy","type":"address"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"name":"","type":"address"},{"name":"","type":"uint256"}],"name":"transferringFor","outputs":[{"name":"","type":"uint32"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"name":"_point","type":"uint32"},{"name":"_sponsor","type":"uint32"}],"name":"isSponsor","outputs":[{"name":"result","type":"bool"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"name":"_point","type":"uint32"}],"name":"getManagementProxy","outputs":[{"name":"manager","type":"address"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"name":"_point","type":"uint32"}],"name":"getContinuityNumber","outputs":[{"name":"continuityNumber","type":"uint32"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"name":"","type":"uint32"},{"name":"","type":"uint256"}],"name":"sponsoring","outputs":[{"name":"","type":"uint32"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"name":"_whose","type":"address"}],"name":"getOwnedPointCount","outputs":[{"name":"count","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"name":"_point","type":"uint32"}],"name":"doEscape","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[{"name":"_whose","type":"address"},{"name":"_index","type":"uint256"}],"name":"getOwnedPointAtIndex","outputs":[{"name":"point","type":"uint32"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"name":"_point","type":"uint32"}],"name":"getTransferProxy","outputs":[{"name":"transferProxy","type":"address"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"name":"_point","type":"uint32"},{"name":"_proxy","type":"address"}],"name":"isSpawnProxy","outputs":[{"name":"result","type":"bool"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"name":"","type":"address"},{"name":"","type":"uint256"}],"name":"pointsOwnedBy","outputs":[{"name":"","type":"uint32"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"name":"","type":"address"},{"name":"","type":"address"}],"name":"operators","outputs":[{"name":"","type":"bool"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"name":"_point","type":"uint32"}],"name":"getSpawnCount","outputs":[{"name":"spawnCount","type":"uint32"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"name":"_point","type":"uint32"},{"name":"_proxy","type":"address"}],"name":"setSpawnProxy","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"name":"_point","type":"uint32"},{"name":"_proxy","type":"address"}],"name":"setTransferProxy","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[{"name":"","type":"uint32"},{"name":"","type":"uint32"}],"name":"sponsoringIndexes","outputs":[{"name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"name":"_point","type":"uint32"},{"name":"_proxy","type":"address"}],"name":"isTransferProxy","outputs":[{"name":"result","type":"bool"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"name":"_point","type":"uint32"}],"name":"getVotingProxy","outputs":[{"name":"voter","type":"address"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"name":"_point","type":"uint32"},{"name":"_proxy","type":"address"}],"name":"isManagementProxy","outputs":[{"name":"result","type":"bool"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"name":"","type":"address"},{"name":"","type":"uint32"}],"name":"votingForIndexes","outputs":[{"name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"name":"_point","type":"uint32"}],"name":"isLive","outputs":[{"name":"result","type":"bool"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"name":"_sponsor","type":"uint32"}],"name":"getEscapeRequests","outputs":[{"name":"requests","type":"uint32[]"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"name":"_point","type":"uint32"}],"name":"getSponsor","outputs":[{"name":"sponsor","type":"uint32"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"name":"_sponsor","type":"uint32"}],"name":"getEscapeRequestsCount","outputs":[{"name":"count","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"name":"","type":"address"},{"name":"","type":"uint32"}],"name":"pointOwnerIndexes","outputs":[{"name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"name":"_proxy","type":"address"}],"name":"getManagerFor","outputs":[{"name":"mfor","type":"uint32[]"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"name":"","type":"address"},{"name":"","type":"uint32"}],"name":"managerForIndexes","outputs":[{"name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"name":"","type":"address"},{"name":"","type":"uint256"}],"name":"managerFor","outputs":[{"name":"","type":"uint32"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"name":"_point","type":"uint32"}],"name":"isActive","outputs":[{"name":"equals","type":"bool"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"name":"_point","type":"uint32"}],"name":"getOwner","outputs":[{"name":"owner","type":"address"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"name":"","type":"uint32"}],"name":"points","outputs":[{"name":"encryptionKey","type":"bytes32"},{"name":"authenticationKey","type":"bytes32"},{"name":"hasSponsor","type":"bool"},{"name":"active","type":"bool"},{"name":"escapeRequested","type":"bool"},{"name":"sponsor","type":"uint32"},{"name":"escapeRequestedTo","type":"uint32"},{"name":"cryptoSuiteVersion","type":"uint32"},{"name":"keyRevisionNumber","type":"uint32"},{"name":"continuityNumber","type":"uint32"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"name":"_proxy","type":"address"}],"name":"getSpawningForCount","outputs":[{"name":"count","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"name":"_point","type":"uint32"}],"name":"hasBeenLinked","outputs":[{"name":"result","type":"bool"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[],"name":"renounceOwnership","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[{"name":"_point","type":"uint32"},{"name":"_who","type":"address"}],"name":"canTransfer","outputs":[{"name":"result","type":"bool"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"name":"","type":"address"},{"name":"","type":"uint32"}],"name":"spawningForIndexes","outputs":[{"name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"name":"_point","type":"uint32"}],"name":"hasSponsor","outputs":[{"name":"has","type":"bool"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"name":"_point","type":"uint32"}],"name":"activatePoint","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[{"name":"_point","type":"uint32"}],"name":"getSpawned","outputs":[{"name":"spawned","type":"uint32[]"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"name":"_point","type":"uint32"},{"name":"_proxy","type":"address"}],"name":"setManagementProxy","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[{"name":"_point","type":"uint32"},{"name":"_who","type":"address"}],"name":"canSpawnAs","outputs":[{"name":"result","type":"bool"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"name":"_point","type":"uint32"}],"name":"getKeyRevisionNumber","outputs":[{"name":"revision","type":"uint32"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"owner","outputs":[{"name":"","type":"address"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"name":"_point","type":"uint32"},{"name":"_who","type":"address"}],"name":"canManage","outputs":[{"name":"result","type":"bool"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"name":"_proxy","type":"address"}],"name":"getTransferringFor","outputs":[{"name":"tfor","type":"uint32[]"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"name":"_point","type":"uint32"}],"name":"getPointSize","outputs":[{"name":"_size","type":"uint8"}],"payable":False,"stateMutability":"pure","type":"function"},{"constant":True,"inputs":[{"name":"_sponsor","type":"uint32"}],"name":"getSponsoringCount","outputs":[{"name":"count","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"name":"_proxy","type":"address"}],"name":"getSpawningFor","outputs":[{"name":"sfor","type":"uint32[]"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"name":"_point","type":"uint32"}],"name":"isEscaping","outputs":[{"name":"escaping","type":"bool"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"name":"","type":"uint32"},{"name":"","type":"uint256"}],"name":"escapeRequests","outputs":[{"name":"","type":"uint32"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"name":"_point","type":"uint32"},{"name":"_proxy","type":"address"}],"name":"setVotingProxy","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[{"name":"_sponsor","type":"uint32"}],"name":"getSponsoring","outputs":[{"name":"sponsees","type":"uint32[]"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"name":"_point","type":"uint32"},{"name":"_sponsor","type":"uint32"}],"name":"setEscapeRequest","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[{"name":"_owner","type":"address"},{"name":"_operator","type":"address"}],"name":"isOperator","outputs":[{"name":"result","type":"bool"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"name":"_point","type":"uint32"},{"name":"_who","type":"address"}],"name":"canVoteAs","outputs":[{"name":"result","type":"bool"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"name":"_primary","type":"string"},{"name":"_secondary","type":"string"},{"name":"_tertiary","type":"string"}],"name":"setDnsDomains","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"name":"_point","type":"uint32"}],"name":"loseSponsor","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"name":"_owner","type":"address"},{"name":"_operator","type":"address"},{"name":"_approved","type":"bool"}],"name":"setOperator","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"name":"_point","type":"uint32"}],"name":"registerSpawned","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[{"name":"_point","type":"uint32"}],"name":"getKeys","outputs":[{"name":"crypt","type":"bytes32"},{"name":"auth","type":"bytes32"},{"name":"suite","type":"uint32"},{"name":"revision","type":"uint32"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"name":"_point","type":"uint32"}],"name":"cancelEscape","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[{"name":"_point","type":"uint32"},{"name":"_address","type":"address"}],"name":"isOwner","outputs":[{"name":"result","type":"bool"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"name":"_proxy","type":"address"}],"name":"getManagerForCount","outputs":[{"name":"count","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"name":"","type":"address"},{"name":"","type":"uint32"}],"name":"transferringForIndexes","outputs":[{"name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"name":"_proxy","type":"address"}],"name":"getVotingFor","outputs":[{"name":"vfor","type":"uint32[]"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"name":"","type":"address"},{"name":"","type":"uint256"}],"name":"spawningFor","outputs":[{"name":"","type":"uint32"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"name":"_point","type":"uint32"},{"name":"_owner","type":"address"}],"name":"setOwner","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[{"name":"_proxy","type":"address"}],"name":"getTransferringForCount","outputs":[{"name":"count","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"name":"_point","type":"uint32"},{"name":"_proxy","type":"address"}],"name":"isVotingProxy","outputs":[{"name":"result","type":"bool"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"name":"_point","type":"uint32"}],"name":"getPrefix","outputs":[{"name":"prefix","type":"uint16"}],"payable":False,"stateMutability":"pure","type":"function"},{"constant":True,"inputs":[{"name":"","type":"uint256"}],"name":"dnsDomains","outputs":[{"name":"","type":"string"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"name":"_newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"name":"_point","type":"uint32"}],"name":"incrementContinuityNumber","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[{"name":"_point","type":"uint32"}],"name":"getSpawnProxy","outputs":[{"name":"spawnProxy","type":"address"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"name":"_point","type":"uint32"}],"name":"getEscapeRequest","outputs":[{"name":"escape","type":"uint32"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"name":"_point","type":"uint32"},{"name":"_encryptionKey","type":"bytes32"},{"name":"_authenticationKey","type":"bytes32"},{"name":"_cryptoSuiteVersion","type":"uint32"}],"name":"setKeys","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[{"name":"_proxy","type":"address"}],"name":"getVotingForCount","outputs":[{"name":"count","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"name":"_point","type":"uint32"},{"name":"_sponsor","type":"uint32"}],"name":"isRequestingEscapeTo","outputs":[{"name":"equals","type":"bool"}],"payable":False,"stateMutability":"view","type":"function"},{"inputs":[],"payable":False,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":False,"inputs":[{"indexed":True,"name":"point","type":"uint32"},{"indexed":True,"name":"owner","type":"address"}],"name":"OwnerChanged","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"name":"point","type":"uint32"}],"name":"Activated","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"name":"prefix","type":"uint32"},{"indexed":True,"name":"child","type":"uint32"}],"name":"Spawned","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"name":"point","type":"uint32"},{"indexed":True,"name":"sponsor","type":"uint32"}],"name":"EscapeRequested","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"name":"point","type":"uint32"},{"indexed":True,"name":"sponsor","type":"uint32"}],"name":"EscapeCanceled","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"name":"point","type":"uint32"},{"indexed":True,"name":"sponsor","type":"uint32"}],"name":"EscapeAccepted","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"name":"point","type":"uint32"},{"indexed":True,"name":"sponsor","type":"uint32"}],"name":"LostSponsor","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"name":"point","type":"uint32"},{"indexed":False,"name":"encryptionKey","type":"bytes32"},{"indexed":False,"name":"authenticationKey","type":"bytes32"},{"indexed":False,"name":"cryptoSuiteVersion","type":"uint32"},{"indexed":False,"name":"keyRevisionNumber","type":"uint32"}],"name":"ChangedKeys","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"name":"point","type":"uint32"},{"indexed":False,"name":"number","type":"uint32"}],"name":"BrokeContinuity","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"name":"point","type":"uint32"},{"indexed":True,"name":"spawnProxy","type":"address"}],"name":"ChangedSpawnProxy","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"name":"point","type":"uint32"},{"indexed":True,"name":"transferProxy","type":"address"}],"name":"ChangedTransferProxy","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"name":"point","type":"uint32"},{"indexed":True,"name":"managementProxy","type":"address"}],"name":"ChangedManagementProxy","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"name":"point","type":"uint32"},{"indexed":True,"name":"votingProxy","type":"address"}],"name":"ChangedVotingProxy","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"name":"primary","type":"string"},{"indexed":False,"name":"secondary","type":"string"},{"indexed":False,"name":"tertiary","type":"string"}],"name":"ChangedDns","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"name":"previousOwner","type":"address"}],"name":"OwnershipRenounced","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"name":"previousOwner","type":"address"},{"indexed":True,"name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"}]
address = "0x223c067F8CF28ae173EE5CafEa60cA44C335fecB"
contract = web3.eth.contract(address=address, abi=abi)

urlData = requests.get(url, verify=False).content.decode('utf-8')
urbit = StringIO(urlData)
urbit_df = pd.read_csv(urbit, sep=",")
urbit_dict = urbit_df.to_dict('index')

urbit_list = []

for i in urbit_dict:
    x = re.search("^0x", str(urbit_dict[i]["field 1"]))
    if (x):
    # if urbit_dict[i]["event"] == "owner":
      urbit_list.append(urbit_dict[i]["field 1"])


urbit_addresses_set = set(urbit_list)
urbit_addresses = list(urbit_addresses_set)

galaxies = {}
stars = {}
planets = {}

for address in pbar(urbit_addresses):

    address = address.lower()
    address = Web3.toChecksumAddress(address)

    galaxies_counter = 0
    stars_counter = 0
    planets_counter = 0

    if contract.functions.getOwnedPoints(address).call():
        for point in contract.functions.getOwnedPoints(address).call():
            if point < 2**8:
                galaxies_counter += 1
            elif point < 2**16 and point >= 2**8:
                stars_counter += 1
            else:
                planets_counter += 1
    if galaxies_counter != 0:
        galaxies.update({address:galaxies_counter})
    elif stars_counter != 0:
        stars.update({address:stars_counter})
    elif planets_counter != 0:
        planets.update({address:planets_counter})

print("galaxies: ", len(galaxies))
print("stars: ", len(stars))
print("planets: ", len(planets))







