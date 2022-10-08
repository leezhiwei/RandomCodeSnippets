def uf(val):
    T3 = val
    I = ''
    X = ''
    U = []
    for m in range(len(val)):
        if m%2 == 0:
            I += T3[m]
        else:
            X = T3[m] + X
    T3 = I + X
    for letters in T3:
        U.append(letters)
    for m in range(len(U)):
        if U[m].isnumeric == True:
            R = m + 1
            while R < len(U):
                if U[R].isnumeric == True:
                    S = U[m]^U[R]
                    if S < 10:
                        U[m] = S
                    m = R
                    R = len(U)
                R += 1
    T3 = ''
    for letters in U:
        T3 += letters
    import base64
    T3 = T3.encode()
    print(T3)
    T3 = base64.b64decode(T3)
    return T3
print(uf('Hello'))
