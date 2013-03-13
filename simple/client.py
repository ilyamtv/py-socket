import socket, sys
from optparse import OptionParser

port = 50010
host = '127.0.0.1'
message = [b'Hello server']

parser = OptionParser()
parser.add_option('--host', dest='host')
parser.add_option('-m', '--message', dest='message')
(options, args) = parser.parse_args()

if None != options.host:
    host = options.host

if None != options.message:
    message = [options.message.encode()]

sockobj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sockobj.connect((host, port))

for line in message:
    sockobj.send(line)
    data = sockobj.recv(1024)
    print('Server received: %s' % data)

sockobj.close()