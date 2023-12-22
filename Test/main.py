import socket

HOST = (socket.gethostname(), 12626)   

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(HOST)
s.listen
print('im listenning!')

while True:
    conn, addr = s.accept()
    print('connected - ', addr)
    res = b'hello my friend! you are connected!' # encode(fmt)
    conn.send(res)