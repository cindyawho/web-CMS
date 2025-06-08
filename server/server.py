import socket

# ~~~ Setting up SERVER Side ~~~ #
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server.bind(('localhost', 12345)) 
server.listen(5)
print('\nListening on localhost : port 12345!')

# Allow website to run through localhost

server.close()