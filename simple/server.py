import socket

host = ''
port = 50010

sockobj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sockobj.bind((host, port))
sockobj.listen(5)

while True:
    conn, address = sockobj.accept()

    #print('Server connected by %s' % ", ".join(address))
    print(address)

    while True:
        data = conn.recv(1024)
        if not data: break

        conn.send(b'Echo => %s' % data)
    conn.close()