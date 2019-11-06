import base64

ALPHABET = 'qpzry9x8gf2tvdw0s3jn54khce6mua7l'

ALPHABET_MAP = {}
for z in range(len(ALPHABET_MAP)):
    x = ALPHABET[z]
    if (x in ALPHABET_MAP): 
        raise TypeError(x + ' is ambiguous')
    ALPHABET_MAP[x] = z

def polymodStep (pre):
    b = pre >> 25
    return ((pre & 0x1FFFFFF) << 5) ^ (-((b >> 0) & 1) & 0x3b6a57b2) ^ (-((b >> 1) & 1) & 0x26508e6d) ^ (-((b >> 2) & 1) & 0x1ea119fa) ^ (-((b >> 3) & 1) & 0x3d4233dd) ^ (-((b >> 4) & 1) & 0x2a1462b3)

def prefixChk (prefix):
    chk = 1
    for i in range(len(prefix)):
        c = ord(prefix[i])
        if (c < 33 or c > 126): 
            raise Error('Invalid prefix (' + prefix + ')')

        chk = polymodStep(chk) ^ (c >> 5)
        
    chk = polymodStep(chk)

    for i in range(len(prefix)):
        v = ord(prefix[i])
        chk = polymodStep(chk) ^ (v & 0x1f)
    
    return chk

def encode (prefix, words, LIMIT=0):
    LIMIT = LIMIT or 90
    if ((len(prefix) + 7 + len(words)) > LIMIT):
        raise TypeError('Exceeds length limit')

    prefix = prefix.lower()

    chk = prefixChk(prefix)
    result = prefix + '1'
    for i in range(len(words)):
        x = words[i]
        if ((x >> 5) != 0): 
            raise Error('Non 5-bit word')

        chk = polymodStep(chk) ^ x
        result += ALPHABET[x]

    for i in range(0, 6):
        chk = polymodStep(chk)
        
    chk ^= 1

    for i in range(0, 6):
        v = (chk >> ((5 - i) * 5)) & 0x1f
        result += ALPHABET[v]

    return result

def decode (str, LIMIT):
    LIMIT = LIMIT or 90
    if (len(str) < 8):
        raise TypeError(str + ' too short')
    if (len(str) > LIMIT): 
        raise TypeError('Exceeds length limit')

    lowered = str.lower()
    uppered = str.upper()
    
    if ((str != lowered) and (str != uppered)): 
        raise Error('Mixed-case string ' + str)

    str = lowered

    split = str.rfind('1')
    if (split == -1):
        raise Error('No separator character for ' + str)
    if (split == 0):
        raise Error('Missing prefix for ' + str)

    prefix = str[0:split]
    wordChars = str[split + 1:]
    if (wordChars.length < 6): 
        raise Error('Data too short')

    chk = prefixChk(prefix)
    words = []
    for i in range(len(wordChars)):
        c = wordChars[i]
        v = ALPHABET_MAP.get(c)
        if v is None: 
            raise Error('Unknown character ' + c)
        chk = polymodStep(chk) ^ v

        if (i + 6 >= len(wordChars)): 
            continue
        words.append(v)

    if (chk != 1): 
        raise Error('Invalid checksum for ' + str)
    return { 
      "prefix": prefix, 
      "words": words 
    }

def convert (data, inBits, outBits, pad):
    value = 0
    bits = 0
    maxV = (1 << outBits) - 1

    result = []
    for i in range(len(data)):
        value = (value << inBits) | data[i]
        bits += inBits

        while (bits >= outBits):
            bits -= outBits
            result.append((value >> bits) & maxV)

    if (pad):
        if (bits > 0):
            result.append((value << (outBits - bits)) & maxV)
    else:
        if (bits >= inBits): 
            raise Error('Excess padding')
        if ((value << (outBits - bits)) & maxV):
            raise Error('Non-zero padding')

    return result

def toWords (bytes):
    return convert(bytes, 8, 5, True)

def fromWords (words):
    return convert(words, 5, 8, False)

def pubkeyToBech32(pubkey, prefix):
    part1 = bytes.fromhex('1624DE6420')
    part2 = base64.b64decode(pubkey)
    return encode(prefix, toWords(part1 + part2))

def base64_to_bech32(pk="7GglL8LOiwNrYIiyGzsrEAaIvYn5iVqYLKG05TG5RXk="):
    validator = pubkeyToBech32(pk,'cybervalconspub');
    return validator