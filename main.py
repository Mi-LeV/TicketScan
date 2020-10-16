from PIL import Image

import pytesseract as tess

tess.pytesseract.tesseract_cmd = r'/bin/tesseract'

img = Image.open('test4.jpg')

#new_size = tuple(2*x for x in img.size)
#img = img.resize(new_size, Image.ANTIALIAS)
#img = img.convert('L')
#img.rotate(90).show()

text = tess.image_to_string(img).lower()

lignes = text.split('\n')
somme = 0
for ligne in lignes:
    if '€' in ligne:
        if 'total' in ligne:
            somme += float(str(ligne.split('total')[-1].replace(' ','').replace('€','').replace(',','.')))

print(somme)
