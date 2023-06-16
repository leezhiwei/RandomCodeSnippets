import base64
import secrets
import string
import gzip
f = open('output.txt','rb')
gz = f.read()
b64strandj = gzip.decompress(gz).decode('ascii')
for _ in range(30):
    b64strandj = b64strandj.rstrip(b64strandj[-1])
b64str = b64strandj.encode('ascii')
print(b64str)
string = base64.b64decode(b64str)
print(string)
