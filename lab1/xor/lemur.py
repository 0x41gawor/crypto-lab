# based on https://crypto.stackexchange.com/questions/88430/how-to-decrypt-two-images-encrypted-using-xor-with-the-same-key, https://pastebin.com/CWkGcRjw
from PIL import Image # Python Imaging Library, https://python-pillow.org
# Po co ta libka?
# plik PNG nie dosc ze jest skompresowany, to jeszcze posiada naglowek oraz sume kontrolna
# domyslam sie, ze operacje xor trzeba bedzie wykonac na raw data obrazka, dlatego potrzebna jest libka, ktora umie to wyciągnąć

# obiekty png, PLI umie je wczytac z pliku
lemur_image = Image.open('lemur.png')
flag_image = Image.open('flag.png')

# tak jak wspomnialem trzeba sie dogrzebać do raw data (czyli zakodowane pixele)
# metoda Image.load() zwraca obiekt klasy PixelAccess - która provides read/write access to PIL.Image data at PIXEL LEVEL
# czyli te obiekty pozwolą nam operować na pixelach 
lemur_pixels = lemur_image.load()
flag_pixels = flag_image.load()
 
# obranie width i height obrazkow (oba maja te same - sprawdzone empirycznie)
w, h = lemur_image.size

# tworzymy nowy image o rozmiarze takim samym jak lemur i flag i wszystkie pixele (r,g,b) ustawiamy na (0,0,0)
new_image = Image.new("RGB", (w, h), "black")
# klasa access do pixeli nowego image
new_pixels = new_image.load()

# teraz pixel po pixelu wypełnimy nowy obrazek xor'em pixeli z obrazków lemur i flag

for i in range(w):    
    for j in range(h): 
        # tu wchodzimy w pojedyczy pixel

        r1, g1, b1 = lemur_pixels[i, j] # rgb pixel'a z lemura
        r2, g2, b2 = flag_pixels[i, j]  # rgb pixel'a z flagi
        
        # rgb pixel'a nowego obrazka
        rn = r1^r2
        gn = g1^g2
        bn = b1^b2
 
        new_pixels[i,j] =  (rn, gn, bn) # napisujemy (0,0,0) poprzez (rn,gn,bn)
        
# nie trzeba teraz jakos przypisywac new_pixels do new_image, te obiekty są coupled
new_image.save("new.png")
