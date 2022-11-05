#!/usr/bin/env python3
import base64


def byte_xor(ba1, ba2):
    return bytes([_a ^ _b for _a, _b in zip(ba1, ba2)])

key1 = bytes.fromhex('a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313')
key2 = byte_xor(key1,bytes.fromhex('37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e'))


key3 = byte_xor(key2,bytes.fromhex('c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1') )

key1key2 = byte_xor(key1,key2)
key1key2key3 = byte_xor(key1key2, key3)

flag = byte_xor(key1key2key3, bytes.fromhex('04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf'))

print(flag)

