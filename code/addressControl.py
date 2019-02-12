###############################################################################
#Address Control V2.0
#Daniel Osmond
#18/01/19
###############################################################################



###############################################################################
#HEADERS & DEFINITIONS
###############################################################################

from bitstring import *

alphaDict = {
	'0' : '00000',
	'A' : '00001',
	'B' : '00010',
	'C' : '00011',
	'D' : '00100',
	'E' : '00101',
	'F' : '00110',
	'G' : '00111',
	'H' : '01000',
	'I' : '01001',
	'J' : '01010',
	'K' : '01011',
	'L' : '01100',
	'M' : '01101',
	'N' : '01110',
	'O' : '01111',
	'P' : '10000',
	'Q' : '10001',
	'R' : '10010',
	'S' : '10011',
	'T' : '10100',
	'U' : '10101',
	'V' : '10110',
	'W' : '10111',
	'X' : '11000',
	'Y' : '11001',
	'Z' : '11010'
}

invAlphaDict = {
	'00000' : '0',
	'00001' : 'A',
	'00010' : 'B',
	'00011' : 'C',
	'00100' : 'D',
	'00101' : 'E',
	'00110' : 'F',
	'00111' : 'G',
	'01000' : 'H',
	'01001' : 'I',
	'01010' : 'J',
	'01011' : 'K',
	'01100' : 'L',
	'01101' : 'M',
	'01110' : 'N',
	'01111' : 'O',
	'10000' : 'P',
	'10001' : 'Q',
	'10010' : 'R',
	'10011' : 'S',
	'10100' : 'T',
	'10101' : 'U',
	'10110' : 'V',
	'10111' : 'W',
	'11000' : 'X',
	'11001' : 'Y',
	'11010' : 'Z'
}

numericDict = {
	'0' : '0000',
	'1' : '0001',
	'2' : '0010',
	'3' : '0011',
	'4' : '0100',
	'5' : '0101',
	'6' : '0110',
	'7' : '0111',
	'8' : '1000',
	'9' : '1001'
}

invNumericDict = {
	'0000' : '0',
	'0001' : '1',
	'0010' : '2',
	'0011' : '3',
	'0100' : '4',
	'0101' : '5',
	'0110' : '6',
	'0111' : '7',
	'1000' : '8',
	'1001' : '9'
}


class nearbyDevice():
	def __init__(self, address, numNeighbours, bit_Sound, bit_Metal, lastSeen):
		self.address = address
		self.numNeighbours = numNeighbours
		self.bit_Sound = bit_Sound
		self.bit_Metal = bit_Metal
		self.lastSeen = lastSeen
		
	def printer(self):
		print(self.address)
		print(self.numNeighbours)
		print(bool(self.bit_Sound))
		print(bool(self.bit_Metal))
		print(self.lastSeen)

###############################################################################




###############################################################################
#FUNCTION DEFINITIONS
###############################################################################

def addressLookup(deviceList, str_conCode):
#checks to see if container exists in current db, if id found, returns true
#otherwise returns false
	found = False
	for device in deviceList:
		if device.address == str_conCode:
			found = True
			break
	if found:
		return True
	else:
		return False

def addressRemove(deviceList, str_conCode):
#removes a container from the list
	for i, o in enumerate(deviceList):
		if o.address == str_conCode:
			del deviceList[i]
			break

def addressAppend(deviceList, device):
	deviceList.append(device)


def addressUpdate(deviceList, device):
#updates existing container information
	if (addressLookup(deviceList, device.address) == False):
		print("Error, container device {} not in list of containers, cannot update".format(device.str_conCode))
	else:
		addressRemove(deviceList, device.address)
		addressAppend(deviceList, device)

def addressPrint(deviceList):
	for device in deviceList:
		device.printer()


def addEncoder(address):
	retAddr = alphaDict[address[0]]
	for i in range(1, 3):
		retAddr = retAddr + ((alphaDict[address[i]]))
		
	for i in range(3, 9):
		retAddr = retAddr + (numericDict[address[i]])
	retAddr = BitArray(bin = retAddr)
	return(retAddr)



def addDecoder(address):
	address = address.bin
	print address
	retAddr = invAlphaDict[address[0:5]]
	for i in range(1,3):
		retAddr = retAddr + invAlphaDict[address[5*i:(i+1)*5]]
		
	for i in range(0,6):
		retAddr = retAddr + invNumericDict[address[15+(i*4):15+((i+1)*4)]]
		
	
	return(retAddr)







###############################################################################




###############################################################################
#MAIN
###############################################################################
def main():

	input = raw_input("Enter value to encode: ")
	encInput = addEncoder(input)
	print(encInput.bin)	
	
	print("decoded value " + addDecoder(encInput))










###############################################################################


if __name__ == '__main__':
	main()


###############################################################################
#END OF FILE	 