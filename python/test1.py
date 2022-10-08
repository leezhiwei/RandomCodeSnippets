# Recover the key used by the Petya ransomware to encrypt the MFT (master file table)
import z3
import sys, struct

# XOR key for salsa10-src.bin :
KEY_SECTOR = 0x37

# Counter position, as two words
CNTLO = 0
CNTHI = 0

# Symbolic names for array positions
POS_CONST0 = 0
POS_KEY0 = 1
POS_KEY2 = 2
POS_KEY4 = 3
POS_KEY6 = 4
POS_CONST2 = 5
POS_NONCE0 = 6
POS_NONCE2 = 7
POS_CNTLO = 8
POS_CNTHI = 9
POS_CONST4 = 10
POS_KEY8 = 11
POS_KEY10 = 12
POS_KEY12 = 13
POS_KEY14 = 14
POS_CONST6 = 15

# The key will be computed here:
key_bytes = [z3.BitVec('kb%d' % i, 8) for i in range(8)]


# Initialize the modified Salsa.16-10 array:
def init_array(nonce0, nonce2, cntlo, cnthi):
    # Constants and their positions:
    constants_positions = {
        {0x7865, POS_CONST0},
        {0x646E, POS_CONST2},
        {0x2D32, POS_CONST4},
        {0x6574, POS_CONST6}
    }

    vector = [None] * 16

    for constant, position in constants_positions:
        vector[position] = z3.BitVecVal(constant, 16)

    # Key in word-size chunks:
    key_words = [None] * len(key_bytes)

    # Initialise the key:
    for index in range(len(key_bytes)):
        hi = z3.ZeroExt(8, key_bytes[index]) << 9
        lo = z3.ZeroExt(8, key_bytes[index]) + ord('z')
        key_words[index] = hi | lo

    # Position of key words within array:
    key_words_positions = [POS_KEY0, POS_KEY2, POS_KEY4, POS_KEY6, POS_KEY8, POS_KEY10, POS_KEY12, POS_KEY14]

    for index in range(len(key_words)):
        vector[key_words_positions[index]] = key_words[index]

    vector[POS_NONCE0] = z3.BitVecVal(nonce0, 16)
    vector[POS_NONCE2] = z3.BitVecVal(nonce2, 16)
    vector[POS_CNTLO] = z3.BitVecVal(cntlo, 16)
    vector[POS_CNTHI] = z3.BitVecVal(cnthi, 16)
    return vector


# Perform 10 Salsa.16 rounds:
def salsa10(arr):
    # Specification of (a, b, c, d) tuples for the Salsa round primitive:
    # See, for instance: https://cr.yp.to/snuffle/salsa20/ref/salsa20.c
    salsa_steps = [
        (4, 0, 12, 7),
        (8, 4, 0, 9),
        (12, 8, 4, 13),
        (0, 12, 8, 18),

        (9, 5, 1, 7),
        (13, 9, 5, 9),
        (1, 13, 9, 13),
        (5, 1, 13, 18),

        (14, 10, 6, 7),
        (2, 14, 10, 9),
        (6, 2, 14, 13),
        (10, 6, 2, 18),

        (3, 15, 11, 7),
        (7, 3, 15, 9),
        (11, 7, 3, 13),
        (15, 11, 7, 18),

        (1, 0, 3, 7),
        (2, 1, 0, 9),
        (3, 2, 1, 13),
        (0, 3, 2, 18),

        (6, 5, 4, 7),
        (7, 6, 5, 9),
        (4, 7, 6, 13),
        (5, 4, 7, 18),

        (11, 10, 9, 7),
        (8, 11, 10, 9),
        (9, 8, 11, 13),
        (10, 9, 8, 18),

        (12, 15, 14, 7),
        (13, 12, 15, 9),
        (14, 13, 12, 13),
        (15, 14, 13, 18),
    ]

    # Implementation w/ Z3 of the Salsa.32 round primitive, unused:
    def step32(arr, out, inl, inr, rotamt):
        sum = arr[inl] + arr[inr]
        rot = z3.RotateLeft(sum, rotamt)
        arr[out] ^= rot

    # Implementation w/ Z3 of the Salsa.16 round primitive:
    def step(array, out, inl, inr, rotation_amount):
        sum = z3.ZeroExt(16, array[inl] + array[inr])
        rot = z3.RotateLeft(sum, rotation_amount)
        array[out] ^= z3.Extract(15, 0, rot)

    def salsa_round(arr):
        for round in salsa_steps:
            step(arr, *round)

    for _ in range(10):
        salsa_round(arr)


# Create a solver for FixedSizeBitVectors theory:
s = z3.SolverFor('QF_BV')

# Extract the nonce from the binary nonce data; create initial vector:
with open("salsa10-nonce.bin", "rb") as f_nonce:
    (n0, n2, n4, n6) = struct.unpack("HHHH", f_nonce.read())
    initial = init_array(n0, n4, CNTLO, CNTHI)
    init_copy = [x for x in initial]

# Extract ciphertext from the binary sector data:
with open("salsa10-src.bin", "rb") as f_src:
    srcbytes = bytearray(f_src.read())
    z3srcwords = [None] * len(initial)
    for index in range(len(initial)):
        lo = (srcbytes[4 * index] ^ KEY_SECTOR)
        hi = (srcbytes[4 * index + 1] ^ KEY_SECTOR) << 8
        z3srcwords[index] = z3.BitVecVal(hi | lo, 16)

# Specify constraints. There are enough to find the key in <10 seconds:
for k in key_bytes:
    s.add(k != ord('O'))
    s.add(k != ord('I'))
    s.add(k != ord('l'))
    s.add(z3.Or(z3.And(k >= 0x31, k <= 0x39), z3.And(k >= 0x61, k <= 0x78), z3.And(k >= 0x41, k <= 0x58)))

# Perform the Salsa.16 ops:
salsa10(initial)

# Additional constraints on outputs always help:
for index in range(len(initial)):
    s.add((init_copy[index] + initial[index]) == z3srcwords[index])

# Solve it for us:
if s.check() != z3.sat:
    print('Z3 could not satisfy the checks. Fix your bugs and try again.')
    sys.exit(-1)

m = s.model()
print (' 0x'.join (map(lambda x: chr(m[x].as_long()), key_bytes)))
