#!/usr/bin/env python3
# wezmy ze niby ten hexstring wejsciowy to '7362' -> wiemy ze to hex czyli są dwa znaki hex `73 62`
# jako bity to jest `01110011 01100010` -> jak zamienimy to na DEC to mamy `115 98` -> jak zamienimy na ASCII to mamy `s b`
input_bytes_as_hex = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
input_bytes_as_ascii_nums = [byte for byte in bytes.fromhex(input_bytes_as_hex)] # zrobienie z ciagu bitow listy znakow ascii

for asciNum in range(256): #iterujemy po numerach ascii
    print(f"Checking byte represeted with ascii num as: {asciNum}")
    possible_flag_as_ascii_nums = [asciNum ^ byte_as_ascii for byte_as_ascii in input_bytes_as_ascii_nums] #xor kazdego bajtu wejsciowego z bajtem asciNum
    print(possible_flag_as_ascii_nums)
    possible_flag_as_ascii_chars = "".join(chr(i) for i in possible_flag_as_ascii_nums) #zamiana byte'ów ascii num na ascii char
    print(possible_flag_as_ascii_chars)
    print("------------------------------------------")
    if possible_flag_as_ascii_chars.startswith("crypto"):
        break

