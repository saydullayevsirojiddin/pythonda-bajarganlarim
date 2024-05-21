telifonlar = {
	'ali':'samsung S9',
	'jaxon':'iphone X',
	'olim':'mi 10 pro',
	'toxir':'nokio 3310',
	'anvar':'samsung A3'
	}

phone = telifonlar['jaxon']
print(f"Jaxonning telifoni {telifonlar['jaxon']}")
phone = telifonlar.get('jaxon','bunday isim yo\'q')
print(phone)
phone = telifonlar.get('hasan','Bunday isim yo\'q')
print(phone)
