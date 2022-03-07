from socket import socket
import sys

s = socket.socket()

host = ''
port = 50007

try:
   s.bind((host, port))
except (s.error , msg):
   print ('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
   sys.exit()

print ('Socket bind complete')
s.listen(1)

while True:
   client, addr = s.accept()

   # print a success message for connection
   print ('Got connection from', addr)

   # create our message to send to server
   msg = 'Server: You are connected'

   # we use our client socket object and use the "send" command.
   # before sending our message it is encoded to be sent to the client
   client.send(msg.encode())

   # we overwrite the msg variable with a message received from the client.
   # the message from the client is decoded and printed on the server
   msg = client.recv(1024).decode()
   print('Client: ', msg)
   
  # we then close the connection and exit our loop, terminating the program
   client.close()
   break;
