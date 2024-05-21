# -*- coding: utf-8 -*-
"""

Created on Sat Jun 26 05:49:34 2021
LUG'ATlar bilan ishlash
@author: sirojiddin
"""

"""items() metoti yordamida kalit va qiymatni saralab chiqaqrdik.
har bir element uchun
"""
talaba0 = {
    'isim' : 'sirojiddin',
    'familiya' : 'saydullayev',
    'yosh' : '26',
    'fakultet' : 'marematika',
    'kurs' : '4'
    }
"""print(talaba0.items())
for kalit, qiymat in talaba0.items():  # items() da saralash. har bir element uchun
    print(f"kalit: {kalit}")
    print("qiymat: {qiymat} \n")

telefonlar = {
    "ali" : "iphon X",
    "vali" : "iphon 10",
    "olim" : "mi 10 pro",
    "orif" : "nokiyo 3310"
    }

for k, q in telefonlar.items():
    print(f"{k.title()} ni telifoni {q}")

####################keys()
mahsulotlar = {
    'olma' : '12 000',
    'anor' : '11 000',
    'shaftoli' : '9 000',
    'nok' : '13 000',
    'shftoli' : '14 000'
    }
#print(mahsulotlar.keys())
print("Do'kondagi mahsulotlar")
for mahsulotl in mahsulotlar.keys():
    print(mahsulotl.title())
"""
"""Do'kondagi mahsulotlar ichidan, ro'yhatdagi mahsulotlarni qidirish. 
ro'yhatdagi mahsulotlar yo'q bo'lsa buyurtma berisin    
mahsulotlar = {
    'olma' : '12 000',
    'anor' : '11 000',
    'shaftoli' : '9 000',
    'nok' : '13 000',
    'shftoli' : '14 000',
    'uzum' : '8 000'
    }

bozorlik = ['anor', 'uzum', 'non', 'baliq', 'olma']

print("Ro'yharda bor mahsulotlar")
for mahsulot in mahsulotlar:
    if mahsulot in bozorlik:
        print(f"{mahsulot.title()} {mahsulotlar[mahsulot]}, so'm")
print("\nRo'thatdan chiqmagan mahsulotlar ")
for buyum in bozorlik:
    if buyum in mahsulotlar:
        print(f"Iltimos do'koningizga {buyum.title()} ham olib keling")

mahsulotlar = {
    'olma' : '12 000',
    'anor' : '11 000',
    'shaftoli' : '9 000',
    'nok' : '13 000',
    'anjir' : '14 000',
    'uzum' : '8 000',
    'gilos' : '6 000'
    }
print("Bozorda bor mahsulotlar")
for mahsulot in sorted(mahsulotlar): #sorted() Alfobet bo'yicha taxlash
    print(mahsulot.title())
"""
#################### .values() FAQAT QIYMATNI CHIQARADI ###########
#print(mahsulotlar.values())
telefonlar = {
    "ali" : "iphon X",
    "vali" : "iphon 10",
    "olim" : "mi 10 pro",
    "orif" : "nokiyo 3310",
    "nurik" : "iphon X",
    "shoxruz" : "iphon 10",
    "salim" : "mi 10 pro",    
    "shox" : "iphon X",
    "azam" : "iphon 10",
    "akmal" : "mi 10 pro"
    }


## set()--foydalanuvchilar ishlatgan telifonlarni yani malumot 
##turlarini saralaydi. yani takrorlanuvchi elementni 1 tasini oliq qoladi 
print("Foydalanuvchilar quyidagi telifonlarni ishlatadi")
for tel in set(telefonlar.values()):
    print(tel)

toys = {'car', 'ball', 'lamp', 'car', 'lamp', 'bear'}
print(type(toys))    
print(toys)
