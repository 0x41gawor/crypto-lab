N = 171731371218065444125482536302245915415603318380280392385291836472299752747934607246477508507827284075763910264995326010251268493630501989810855418416643352631102434317900028697993224868629935657273062472544675693365930943308086634291936846505861203914449338007760990051788980485462592823446469606824421932591                                                                  
e = 65537
ciphertext = 161367550346730604451454756189028938964941280347662098798775466019463375610700074840105776873791605070092554650190486030367121011578171525759600774739890458414593857709994072516290998135846956596662071379067305011746842247628316996977338024343628757374524136260758515864509435302781735938531030576289086798942  

# chciałem rozbić na p i q
# ale factordb pokazuje mi
# ze p=q=N w sensie tylko N mi wyskakuje
# moze to jest ten błąd o którym mówili chłopaki z KRYS?

# dobra to trzeba przekminić: przypomnij sobie definicje totient (readme).
# zauważ ze jak liczba jest pierwsza to z każdą liczbą od 1 do niej samej po kolej gdc(i,j) = 1 no bo jest pierwsza
# tak więc counter totientowy naliczy je wszystkie
# czyli totien z liczby pierwszej i, to i-1

# kod kopiuje z poprzedniego zadania a podmieniam tylko linijke na totient
 
totient = N-1

d = pow(e, -1, totient) # klucz prywatny mam :D

plaintext = pow(ciphertext, d, N) # plaintext odszyfrowany ale to long

from Crypto.Util.number import long_to_bytes
byted_from_longed_xd_plaintext = long_to_bytes(plaintext)
print(byted_from_longed_xd_plaintext)