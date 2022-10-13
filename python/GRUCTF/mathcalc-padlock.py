import socket
ip = '0.0.0.0'
port = 12345
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip,port))
for x in range(300):
    data = s.recv(1024)
    data = data.decode()
    linelist = data.split('\n')
    endstring = ''
    for line in linelist:
        print(line)
        if '+' in line or '-' in line:
            for char in line:
                if char.isalpha():
                    continue
                if char == '?':
                    break
                if char == '*':
                    endstring += '*'
                    continue
                endstring += char
        else:
            continue
        result = eval(endstring)
        result = str(result)
        s.send(str.encode(result))
