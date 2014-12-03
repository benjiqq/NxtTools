import socket;
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
peer = '85.214.222.82'
result = sock.connect_ex((peer,80))
if result == 0:
   print "Port is open"
else:
   print "Port is not open"
