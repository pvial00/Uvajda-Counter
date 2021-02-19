''' For testing purposes with the Dark family derivative ciphers '''

test_array = [0, 1, 1, 0, 0, 0, 1, 1, 0]

def number_of_ones(bitstream):
    n = 0
    for bit in bitstream:
        if bit == 1:
            n += 1
    return n

def number_of_zeros(bitstream):
    n = 0
    for bit in bitstream:
        if bit == 1:
            n += 1
    return n

def succession_topB(bitstream, threshold=4):
    return None

def succession_topA(bitstream, threshold=4):
    c = 0
    s = 0
    for bit in bitstream:
        if bit == 1:
            c += 1
        else:
            c = 0
        if c >= threshold:
            s = c
    if c > 0 and s == 0:
        return c
    else:
        return s

def successiion_bottomB(bitstream, threshold=4):
    c = 0
    for bit in bitstream:
        if bit == 0:
            c += 1
        else:
            c = 0
    if c > 0 and s == 0:
        return c
    else:
        return s

def successiion_bottomA(bitstream, threshold=4):
    return None

def row_sort(bitstream, width=9, heighth=30):
    return None

def vlad_counterB(bit_stream, bit_stream_length, level=1):
    r = [0, 1]
    c = 0
    q = 0
    n = 0
    p = 0
    for x in range(bit_stream_length-level):
        q ^= bit_stream[x]
        if bit_stream[x] == 1:
            n += 1
        if bit_stream[x] == 0:
            p += 1
        r[c] ^= q
        c = (c + 1) & 0x01
    avg = n / q
    num_1s = number_of_ones(bitstream)

    print(avg)
    if r[0] == 1:
        return 1
    else:
        return 0

def vlad_counterBA(bit_stream, bit_stream_length, level=1):
    r = [0, 1]
    c = 0
    q = 1
    for x in range(bit_stream_length-level):
        q ^= bit_stream[x]
        r[c] ^= q
        c = (c + 1) & 0x01
    if r[0] == 1:
        return 1
    else:
        return 0

def venus_counterB(bit_stream, bit_stream_length, level=1):
    r = [0, 1]
    c = 1
    q = 0
    for x in range(bit_stream_length-level):
        q ^= bit_stream[x]
        r[c] ^= q
        c = (c + 1) & 0x01
    if r[0] == 1:
        return 1
    else:
        return 0

def venus_counterBA(bit_stream, bit_stream_length, level=1):
    r = [0, 1]
    c = 1
    q = 1
    for x in range(bit_stream_length-level):
        q ^= bit_stream[x]
        r[c] ^= q
        c = (c + 1) & 0x01
    if r[0] == 1:
        return 1
    else:
        return 0
