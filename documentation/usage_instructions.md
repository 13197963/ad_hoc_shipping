# HOW TO USE THE SYSTEM


## Usage

The *shippingSender* block automatically sends out beacon messages at a preset rate. This is controlled by the **Message** and **Period** attributes.
**Message** must follow the form of 3 Letters, followed by 6 Numbers (i.e. ABC123456).
**Period** is the number of seconds the system should wait before sending the next beacon.

While not explicitly necessary, it is advisable to add a CRC generate as the next block in the stream (future updates will hopefully allow for dynamic inclusion of CRC). If CRC is added, there should be a CRC check when the message is recieved.

The final block is the *shippingReciever*. This block takes the beacon messages and uses them to generate a database of nearby devices. There is a sole input of **ContainerID**, which is used to check to see if a seen message is just an echo of a message sent by the same machine.
**ContainerID** must follow the form of 3 Letters, followed by 6 Numbers (i.e. ABC123456).

## Important Notes

It is recommended that you use a QT GUI Entry with the shippingSender block at this time, as it relies on a msg callback.
The system can only be stopped by using `Control+C`, or the "Kill The Flowgraph" option in GnuRadio Companion.
Having the same value for the senders **Message** and the recievers **ContainerID** will cause the system to ignore your message, as it thinks that its a message from itself.


## Tester Usage


Run the udpServer.py code first

Run the shippingTester code, ensuring that the udp client port and ip address match that of the udp server