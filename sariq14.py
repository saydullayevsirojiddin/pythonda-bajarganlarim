"""
14-dars
Sirojiddin
Saydullayev
Muxiddin o'g'li
03.06.2021
@ssmmoviy
"""
#car_0 = {'model':'Ferrare', 'rang':'Qizil'}
#print(car_0['model'])
#print(car_0['rang'])

#en_uz = {'apple':"Olma", "banana":"banan", "apricot":"o'rik"}
#print(en_uz)
#print(en_uz['apple'])
#print(en_uz['banana'])
#print(en_uz['apricot'])

#mevalar = {'olma':12000,'gilos':7000,'olcha':5000,'anor':8000,'shaftoli':7000,'nok':9000}
#print(mevalar)
#print(f"Olmaning narhi {mevalar['olma']} so'm turadi")
#print(f"Gilos narhi {mevalar['gilos']} so'm turadi")
#print(f"Olchaning narhi {mevalar['olcha']} so'm turadi")
#print(f"Anorning narhi {mevalar['anor']} so'm turadi")
#print(f"Shaftolining narhi {mevalar['shaftoli']} so'm turadi")
#print(f"Nokning narhi {mevalar['nok']} so'm turadi")

#talaba_1={'ism':'saydullayev sirojiddin','yosh':'27','t_yil':'1995'}
#print(f"{talaba_1['ism'].title()},\
#	{talaba_1['t_yil']}-yilda tug'ulgan, \
#	{talaba_1['yosh']} yoshda")

########## kalit so'z va qiymat kiritish
#talaba_1['kurs'] = 4
#talaba_1['fakultet'] = 'informatika'
#talaba_1['oliygoh'] = 'TATU'
#talaba_1['ism'] = 'sirojiddin'
#print(talaba_1)

########## Bo'sh lug'at
talaba_2 = {}
talaba_2['kurs'] = 4
talaba_2['fakultet'] = 'informatika'
talaba_2['oliygoh'] = 'TATU'
talaba_2['ism'] = 'sirojiddin'
print(talaba_2)
print(f"{talaba_2['ism'].title()} \
	{talaba_2['oliygoh']} \
	{talaba_2['fakultet'].title()} \
	{talaba_2['kurs']}")

telifonlar = {
	'ali':'samsung S9',
	'jaxon':'iphone X',
	'olim':'mi 10 pro',
	'toxir':'nokio 3310',
	'anvar':'samsung A3'
	}
#       .get() metodi
phone = telifonlar['jaxon']
print(f"Jaxonning telifoni {telifonlar['jaxon']}")
phone = telifonlar.get('jaxon','bunday isim yo\'q')
print(phone)
phone = telifonlar.get('hasan','Bunday isim yo\'q')
print(phone)