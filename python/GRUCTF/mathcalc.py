import socket
ip = '0.0.0.0'
port = 12345
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip,port))
for x in range(200):
    data = s.recv(1024)
    data = data.decode()
    linelist = data.split('\n')
    endstring = ''
    for line in linelist:
        print(line)
        if '+' in line or '-' in line:
            if '=' in line:
                for char in line:
                    if char == '=':
                        break
                    endstring += char
            print(endstring)
            result = eval(endstring)
            print(result)
            result = str(result)
            result = str.encode(result)
            s.sendall(result)
        elif 'x' in line:
            if '=' in line:
                for char in line:
                    if char == '=':
                        break
                    if char == 'x':
                        endstring += '*'
                        continue
                    endstring += char
            print(endstring)
            result = eval(endstring)
            print(result)
            result = str(result)
            result = str.encode(result)
            s.sendall(result)
        else:
            continue
