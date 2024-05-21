# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 16:56:00 2021

@author: sirojiddin
"""
'''
def toliq_ism_yasa(ism, familiya):
    """Toliq isma qaytaruvchi funksiya"""
    toliq_ism = f"{ism} {familiya}"
    return toliq_ism 
talaba1 = toliq_ism_yasa('Hasan', 'G\'ulomov')
talaba2 = toliq_ism_yasa('Chori', 'Norchayev')
print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")
'''
'''
def toliq_ism_yasa(ism, familiya, otasining_ismi = ''):
    """To'liq ism qaytaruvchi fo'nksiy"""
    if otasining_ismi:
        toliq_isma = f"{ism} {familiya} {otasining_ismi}"
    else:
        toliq_isma = f"{ism} {familiya}"
    return toliq_isma.title()
talaba1 = toliq_ism_yasa('sirojiddin', 'saydullayev')
talaba2 = toliq_ism_yasa('sirojiddin', 'saydullayev', 'muxiddinovich')
print(f"{talaba1}\n{talaba2}")
'''
'''
def afto_komplar(kompaniya, model, rangi, karobka, yili, narhi=None):
    avto={'kompaniya':kompaniya,
          'model':model,
          'rang':rangi,
          'karobka':karobka,
          'yil':yili,
          'narh':narhi}
    return avto

avto1 = afto_komplar('GM', 'malibu', 'oq', 'maexanika', 2016,)
avto2 = afto_komplar('GM', 'gentira', 'qora', 'maexanika', 2018,13000)
avto3 = afto_komplar('GM', 'spark', 'oq', 'maexanika', 2016,)
avto4 = afto_komplar('GM', 'nexa', 'qora', 'maexanika', 2018,13000)
aftolar = [avto1,avto2,avto3,avto4]

print("Online bozorda movjud avtomabillar.")
for avto in aftolar:
    if avto['narh']:
        narh = avto['narh']
    else:
        narh = 'Nomalum'
    print(f"{avto['rang'].title()} {avto['model']}. Narhi: {narh}")
'''
"""
def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
    avto = {'kompaniya':kompaniya,
            'model':model,
            'rang':rangi,
            'korobka':korobka,
            'yil':yili,
            'narh':narhi}
    return avto

avto1 = avto_info('GM','Malibu','Qora','Avtomat',2018)
avto2 = avto_info('GM','Gentra','Oq','Mexanika',2016,15000)
avtolar = [avto1, avto2]
print('Onlayn bozordagi mavjud avtomashinalar:')
for avto in avtolar:
    if avto['narh']:
        narh = avto['narh']
    else:
        narh = "Noma'lum"
    print(f"{avto['rang']} {avto['model']}. Narhi: {narh}")
"""
'''
def oraliq(min,max):
    sonlar = []
    while min<max:
        sonlar.append(min)
        min += 1
    return sonlar
print(oraliq(0, 10))
print(oraliq(11,23))

#range() funksiyasi. 
def oraliq(min,max,qadam):
    sonlar = []
    while min<max:
        sonlar.append(min)
        min += qadam
    return sonlar
print(oraliq(0, 10,2))
print(oraliq(0,50,5))
'''
'''
def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
    avto = {'kompaniya':kompaniya,
            'model':model,
            'rang':rangi,
            'korobka':korobka,
            'yil':yili,
            'narh':narhi}
    return avto
print("Saytimizdagi avtolar ro'yxatini shakllantiramiz.")
avtolar=[] # salondagi avtolar uchun bo'sh ro'yxat
while True:
    print("\nQuyidagi ma'lumotlarni kiriting",end='')
    kompaniya=input("Ishlab chiqaruvchi: ")
    model=input("Modeli: ")
    rangi=input("Rangi: ")
    korobka=input("Korobka: ")
    yili=input("Ishlab chiqarilgan yili: ")
    narhi=input("Narhi: ")
    
    #Foydalanuvchi kiritdan ma'lumotlardan avto_info yordamida 
    #lug'at shakllantirib, har bir lug'atni ro'yxatga qo'shamiz:
    avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narhi))
    
    # Yana avto qo'shish-qo'shmaslikni so'raymiz
    javob = input("Yana avto qo'shasizmi? (yes/no): ")
    if javob=='no':
        break
'''
'''1.	Foydanaluvchidan ismi, familiyasi, tug'ilgan yili, tug'ilgan joyi,
email manzili va telefon raqamini qabul qilib, lug'at ko'rinishida 
qaytaruvchi funksiya yozing. Lug'atda foydalanuvchu yoshi ham bo'lsin.
Ba'zi argumentlarni kiritishni ixtiyoriy qiling (masalan, tel.raqam, 
el.manzil)
    2.	Yuqoridagi funksiyani while yordamida bir necha bor chaqiring va
mijozlar degan ro'yxatni shakllantiring. Ro'yxatdagi mijozlar haqidagi 
ma'lumotni konsolga chiqaring.    '''
def shaxsiy_malumot(ismi, familiyasi, tug_yili, tug_joyi, email, telefon):
    malumot = {"ismi":ismi,
               "familiyasi":familiyasi,
               "tug_yili":tug_yili,
               "tug_joyi":tug_joyi,
               "email":email,
               "telefon":telefon}
    return malumot

mijozlar = []
while True:
    ismi=input("Isimni kiriting: ")
    familiyasi=input("Familiyani kiriting: ")
    tug_yili=input("Tug_yil kiriting: ")
    tug_joyi=input("tug_joy kiriting: ")
    email=input("Email kiriting: ")
    telefon=input("Tel_nomerni kiriting: ")
    mijozlar.append(shaxsiy_malumot(ismi, familiyasi, tug_yili, tug_joyi, email, telefon))
    a=input("yes/no:  ")
    if 'no' == a:
        break
print(mijozlar)
print("dastur tugadi!")








