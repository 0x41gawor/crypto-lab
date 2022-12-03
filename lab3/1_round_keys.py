state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]


def add_round_key(s, k):
    res = [
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]
    ]
    for x in range(4):
        for y in range(4):
            res[x][y] = state[x][y] ^ round_key[x][y]
            
    return res

def matrix2bytes(matrix):
    """ Converts a 4x4 matrix into a 16-byte array.  """
    res = ""
    for x in range(4):
        for y in range(4):
            res += chr(matrix[x][y])
    return res

print(matrix2bytes(add_round_key(state, round_key)))

