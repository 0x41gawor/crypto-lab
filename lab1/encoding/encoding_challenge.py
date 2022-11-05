from pwn import *  
import json
import codecs

r = remote('socket.cryptohack.org', 13377, level = 'debug')

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)


while True:
    received = json_recv()

    print("Received type: ")
    print(received["type"])
    print("Received encoded value: ")
    print(received["encoded"])

    type = received["type"]
    encoded = received["encoded"]

    if type == "base64":
        print("--------------- base64")
        decoded = base64.b64decode(encoded).decode('utf-8')
        print(decoded)
    elif type == "hex":
        decoded = bytes.fromhex(encoded).decode('utf-8')
        #print(decoded)
    elif type == "rot13": #dziala
        decoded = codecs.decode(encoded, 'rot_13')
        #print(decoded)
    elif type == "bigint":
        langi = int(encoded,16)
        decoded = langi.to_bytes(64, 'big')
        decoded = decoded.decode('utf-8')
        decoded = decoded.lstrip('\x00')
        #print(decoded)
    elif type == "utf-8": #dziala
        decoded = [chr(b) for b in encoded]
        decoded = "".join(i for i in decoded) 
        #print(decoded)

    print(f"ZDEKODOWALEM: {decoded}")
    to_send = {
        "decoded": decoded
    }
    json_send(to_send)

json_recv()