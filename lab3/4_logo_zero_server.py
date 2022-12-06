#!/usr/bin/env python3

from Crypto.Cipher import AES
from Crypto.Util.number import bytes_to_long
from os import urandom
from utils import listener

FLAG = "crypto{???????????????????????????????}"


class CFB8:
    def __init__(self, key):
        self.key = key

    def encrypt(self, plaintext):
        IV = urandom(16)
        cipher = AES.new(self.key, AES.MODE_ECB) # ECB czyli najizi niezależny
        ct = b''
        state = IV
        for i in range(len(plaintext)):
            b = cipher.encrypt(state)[0] # b to pierwszy bajtu stateu
            c = b ^ plaintext[i] # c to b XOR bajt plaintextu
            ct += bytes([c]) # do ciphertext dodawane jest c 
            state = state[1:] + bytes([c]) # state do po prostu jego znaki 1:16 + c
            # czyli state tak się przesuwa nono stop w sensie robiony jest shift w lewo a ostatni baj to pierwszy bajt XOR plaintext
        return IV + ct # zwracany jest IV i ct 

    def decrypt(self, ciphertext):
        IV = ciphertext[:16]
        ct = ciphertext[16:]
        cipher = AES.new(self.key, AES.MODE_ECB)
        pt = b''
        state = IV
        for i in range(len(ct)):
            b = cipher.encrypt(state)[0]
            c = b ^ ct[i]
            pt += bytes([c])
            state = state[1:] + bytes([ct[i]])
            # na odwrót to co w encrypt
        return pt


class Challenge():
    def __init__(self):
        self.before_input = "Please authenticate to this Domain Controller to proceed\n"
        self.password = urandom(20) #haslo to wylosowane 20uintów
        self.password_length = len(self.password)
        self.cipher = CFB8(urandom(16)) #klucz to wylosowane 16 uintów

    def challenge(self, your_input):
        if your_input['option'] == 'authenticate': # mozna się zautentykować hasłem, albo zrestować connection albo resetowac haslo
            if 'password' not in your_input:
                return {'msg': 'No password provided.'}
            your_password = your_input['password']
            if your_password.encode() == self.password: # jeśli zgadniemy hasło to dostaniemy flage
                self.exit = True
                return {'msg': 'Welcome admin, flag: ' + FLAG}
            else:
                return {'msg': 'Wrong password.'}

        if your_input['option'] == 'reset_connection': # reset connection po prostu stworzy nowy klucz i nowe hasło
            self.cipher = CFB8(urandom(16))
            return {'msg': 'Connection has been reset.'}

        if your_input['option'] == 'reset_password': # zeby zresetować hasło to trzeba podać token 
            if 'token' not in your_input:
                return {'msg': 'No token provided.'}
            token_ct = bytes.fromhex(your_input['token'])
            if len(token_ct) < 28:
                return {'msg': 'New password should be at least 8-characters long.'}

            token = self.cipher.decrypt(token_ct) #token podajemy w ciphertext a tutaj zostaje on odszyfrowany 
            new_password = token[:-4] # haslo to token bez ostatnich 4 bajtów
            self.password_length = bytes_to_long(token[-4:]) 
            self.password = new_password[:self.password_length]
            return {'msg': 'Password has been correctly reset.'}

# jednak nie ogarniam poddaje sie

listener.start_server(port=13399)
