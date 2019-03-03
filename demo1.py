import  socket
import  re
img_url = 'http://pic.hsw.cn/0/13/09/09/13090929_929741.jpg'
client = socket.socket()
client.connect(('pic.hsw.cn',80))
requst = b'GET /0/13/09/09/13090929_929741.jpg HTTP/1.0\r\nHost: pic.hsw.cn\r\n\r\n'
client.send(requst)
res = b''
temp = client.recv(1024)
while temp:
    res += temp
    temp = client.recv(1024)
with open('picture.jpg','wb') as f:
    f.write(re.findall(b'\r\n\r\n(.*)',res,re.S)[0])