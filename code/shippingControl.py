###############################################################################
#Shipping Control V2.0
#Daniel Osmond
#18/01/19
###############################################################################



###############################################################################
#HEADERS & DEFINITIONS
###############################################################################


from bitstring import *
from addressControl import *
from datetime import datetime

SYNC_HEADER = ""#"0b00000000000000000000000000000000"
PACKET_DELIM = ""#"0b10101010"
MY_ADDRESS = "CSQ305438"
BROADCAST_ADDRESS = "000000000"

deviceList = []


class shortHeader():
	def __init__(self, bit_beacon, bit_radio, bit_extHeader, bit_dest, bit_crc, u8_nearbyDevices, bm8_commTypes):
		self.bit_beacon = bit_beacon
		self.bit_radio = bit_radio
		self.bit_extHeader = bit_extHeader
		self.bit_dest = bit_dest
		self.bit_crc = bit_crc
		self.u8_nearbyDevices = u8_nearbyDevices
		self.bm8_commTypes = bm8_commTypes


class longHeader():
	def __init__(self, bit_beacon, bit_radio, bit_extHeader, bit_dest, bit_crc, u8_nearbyDevices, bm8_commTypes, bm8_prefCommType, u4_security, u8_payloadSize, u8_sequence, u8_routing):
		self.bit_beacon = bit_beacon
		self.bit_radio = bit_radio
		self.bit_extHeader = bit_extHeader
		self.bit_dest = bit_dest
		self.bit_crc = bit_crc
		self.u8_nearbyDevices = u8_nearbyDevices
		self.bm8_commTypes = bm8_commTypes
		self.bm8_prefCommType = bm8_prefCommType
		self.u4_security = u4_security
		self.u8_payloadSize = u8_payloadSize
		self.u8_sequence = u8_sequence
		self.u8_routing = u8_routing

###############################################################################



###############################################################################
#FUNCTION DEFINITIONS
###############################################################################


def lowFreqMessage(bit_beacon, bit_radio, bit_extHeader, bit_dest, bit_crc, u8_nearbyDevices, bm8_commTypes, bm8_prefCommType, u4_security, u8_payloadSize, u8_sequence, u8_routing, str_destAddr, str_sourceAddr):
	#message = BitArray(SYNC_HEADER)
	
	#message.append(PACKET_DELIM)

	message = BitArray()

	message.append("0b"+str(bit_beacon))
	
	message.append("0b"+str(bit_radio))

	message.append("0b"+str(bit_extHeader))

	message.append("0b"+str(bit_dest))

	message.append("0b"+str(bit_crc))

	message.append(BitArray(format(u8_nearbyDevices, '#010b')))

	message.append(bm8_commTypes)

	if bit_extHeader == 1:

		message.append(bm8_prefCommType)

		message.append(BitArray(format(u4_security, '#010b')))

		message.append(BitArray(format(u8_payloadSize, '#010b')))

		message.append(BitArray(format(u8_sequence, '#010b')))

		message.append(BitArray(format(u8_routing, '#010b')))

		message.append("0b0000000")	

		

	
	if bit_dest == 1:
		message.append(addEncoder(str_destAddr))

	message.append(addEncoder(str_sourceAddr))

	message.append("0b00000000")
	if bit_extHeader == 0:
		message.append("0b0000")

	return(message)


def parseMessage(message, deviceList, my_address):
	message = "0b" + message
	message = BitArray(message)
	#message = message[40:]
	header, offset = headerParse(message[:64])
	message = message[offset:]
	
	if header.bit_dest == 1:
		str_destAddr = addDecoder(message[:39])
		message = message[39:]
	print(message[:39])
	str_sourceAddr = addDecoder(message[:39])
	if str_sourceAddr == my_address:
		print("This is my own message, ignoring")
		return
	if header.bit_beacon == 0:
		#perform payload ops here
		print("Not yet implemented")

	if header.bit_beacon == 1:
		device = nearbyDevice(str_sourceAddr, header.u8_nearbyDevices, header.bm8_commTypes[0], header.bm8_commTypes[1], datetime.now())
		device.printer()
		if addressLookup(deviceList, str_sourceAddr) == False:
			print("Device {} not previously seen".format(str_sourceAddr))
			
			addressAppend(deviceList, device)
		else:
			print("Device {} seen previously, updating records".format(str_sourceAddr))
			addressUpdate(deviceList, device)
		addressPrint(deviceList)




	# #checksum = bit_message[-16:]
	# padding = message[-8:]
	# bin_sourceAddr = message[-47:-8]
	# print((bin_sourceAddr).bin)
	# bin_destAddr = message[-86:-47]
	# print((bin_destAddr).bin)
	# bit_extHeader = message[-86]
	# bit_beacon	= message[-87]
	# str_sourceAddr = addDecoder(bin_sourceAddr)
	# print(str_sourceAddr)
	# str_destAddr = addDecoder(bin_destAddr)
	# print(str_destAddr)
	# return(lowFreqMessageHolder(bit_beacon, bit_extHeader, str_destAddr, str_sourceAddr))


def headerParse(bit_message):
	bit_beacon = bit_message[0]
	bit_radio = bit_message[1]
	bit_extHeader = bit_message[2]
	bit_dest = bit_message[3]
	bit_crc = bit_message[4]
	u8_nearbyDevices = bit_message[5:13]
	bm8_commTypes = bit_message[13:21]
	if bit_extHeader == 0:
		return(shortHeader(bit_beacon, bit_radio, bit_extHeader, bit_dest, bit_crc, u8_nearbyDevices, bm8_commTypes), 21)
	else:
		bm8_prefCommType = bit_message[21:29]
		u4_security = bit_message[29:33]
		u8_payloadSize = bit_message[33:41]
		u8_sequence = bit_message[41:49]
		u8_routing = bit_message[49:57]
		return(longHeader(bit_beacon, bit_radio, bit_extHeader, bit_dest, bit_crc, u8_nearbyDevices, bm8_commTypes, bm8_prefCommType, u4_security, u8_payloadSize, u8_sequence, u8_routing), 64)







###############################################################################



###############################################################################
#MAIN
###############################################################################

def main():
	
	print("Main Running")
	userInput = raw_input("Enter a command: ")
	while(userInput != "0"):
		if userInput == "1":
			print((lowFreqMessage(1,0,0,0,0,4, BitArray("0b10000000"), BitArray("0b10000000"), 0, 0, 0, 0, BROADCAST_ADDRESS, MY_ADDRESS).bin))
		elif userInput == "2":
			userInput = raw_input("Enter bitstream to decode> ")
			parseMessage(userInput)
			

		userInput = raw_input("Enter a command: ")
	









###############################################################################


if __name__ == '__main__':
	main()

###############################################################################
#END OF FILE

