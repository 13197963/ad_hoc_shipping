import socket
import sys

contactList =[]

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

while True:
    print >>sys.stderr, '\nwaiting to receive message'
    data, address = sock.recvfrom(4096)
    if address not in contactList:
    	contactList.append(address)

    
    print >>sys.stderr, 'received %s bytes from %s' % (len(data), address)
    print >>sys.stderr, data
    
    if data:
    	for address in contactList:
        	sent = sock.sendto(data, address)
        	print >>sys.stderr, 'sent %s bytes back to %s' % (sent, address)