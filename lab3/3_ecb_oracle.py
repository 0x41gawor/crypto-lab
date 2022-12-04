import requests
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad




# @chal.route('/ecb_oracle/encrypt/<plaintext>/')
# def encrypt(plaintext):
#     ten kod bierze nasz plain text
#     plaintext = bytes.fromhex(plaintext)
      # i dodaje do flagę, a następnie robi padding czyli dopełnia aby długość całości to była wielokrotność 16bajtów (ECB format)
      # https://github.com/onealmond/hacking-lab/blob/master/cryptohack/ecb-oracle/writeup.md
#     padded = pad(plaintext + FLAG.encode(), 16)
#     cipher = AES.new(KEY, AES.MODE_ECB)
#     try:
#         encrypted = cipher.encrypt(padded)
#     except ValueError as e:
#         return {"error": str(e)}

#     return {"ciphertext": encrypted.hex()}

# Analizując to jak kod wyżej działa, jeżeli to nasz plaintext to jeżeli mamy wypełnione plaintextem n znaków to dostajemy jakiś szyfr
# Jeżeli wypełnimy znak plaintextu numer `n+1` i szyfr który otrzymamy jest taki sam (do danego miejsca - nie cały), to znaczy, że krok temu ten znak na tym miejscu 
# też taki był, czyli to co daliśmy teraz jako nasz plaintext zgadza się z tym co było tam wcześniej jako flag

# Jak uzyć tej wiedzy?
# Wiemy, że flaga zaczyna się od `crypto{` czyli np pierwsze 7 znaków już mamy, wysyłamy to jako plaintext (oczywiście w formie hex)
# Teraz szukamy 8-go znaku, próbujemy tylok te z Ascii, które mogą znaleźć się w fladze (czyli od 33[! - pierwszy nie spacja itd.] do 126[~])
# Jeśli dokleimy jakiś znak do naszego plaintext i otrzymamy odpowiedź od endpointa taką jak w poprzedniej iteracji, to znaczy że ten znak jest taki sam
# jak był w padded strin w poprzedniej iteracji, a w poprzedniej iteracji znalazł się w padded z racji bycią częścią flagi EZ
# No i idziemy tak znak po znaku

def response(byte_string):
	url = "http://aes.cryptohack.org/ecb_oracle/encrypt/"
	url += byte_string.hex()
	url += "/"
	r = requests.get(url)
	js = r.json()
	return bytes.fromhex(js["ciphertext"])

flag = b"crypto{"

for i in range(7, 26): # pętla od 7 znaku flagi do 26 # czemu 26 to nie wiem xddd
	byte_string = b""
	byte_string += b"\x00" * (31 - i)
	
	res = response(byte_string)[:32]

	byte_string += flag 
	for j in range(33, 126): #iterujemy po znakach Ascii kwalifikujących się do bycia we fladze
		byte_string = byte_string[:31]
		byte_string += j.to_bytes(1, byteorder = "big")
		print("Flaga: " +  str(flag) + "  |Rozwazam znak: " + str(j) + ": " + chr(j)) # Ten znak Ascii teraz rozpatrujemy

		res2 = response(byte_string)[:32]
		if res == res2:
			flag += j.to_bytes(1, byteorder = "big")
			
			break