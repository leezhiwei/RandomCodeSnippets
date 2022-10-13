import socket
ip = '0.0.0.0'
port = 12345
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip,port))
for x in range(200):
    data = s.recv(1024)
    data = data.decode()
    linelist = data.split('\n')
    count = 0
    pival = 3.14
    for line in linelist:
        print(line)
        if 'area' in line:
            radius = ''
            length = ''
            if 'sphere' in line:
                for char in line:
                    if char.isnumeric():
                        radius += char
                radius = int(radius)
                result = 4 * pival * (radius ** 2)
                print(f'Result is {result}')
                s.send(f'{result:.2f}'.encode())
            elif 'cube' in line:
                for char in line:
                    if char.isnumeric():
                        length += char
                length = int(length)
                result = 6 * (length ** 2)
                print(f'Result is {result}')
                s.send(f'{result:.2f}'.encode())
        elif 'volume' in line:
            radius = ''
            length = ''
            if 'sphere' in line:
                for char in line:
                    if char.isnumeric():
                        radius += char
                radius = int(radius)
                result = (4/3) * pival * (radius ** 3)
                print(f'Result is {result}')
                s.send(f'{result:.2f}'.encode())
            elif 'cube' in line:
                for char in line:
                    if char.isnumeric():
                        length += char
                length = int(length)
                result = (length ** 3)
                print(f'Result is {result}')
                s.send(f'{result:.2f}'.encode())
