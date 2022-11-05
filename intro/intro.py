#!/usr/bin/env python3
import base64

words = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]

hexstr = '72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf'

a = bytes.fromhex(hexstr)
print(base64.b64encode(a))