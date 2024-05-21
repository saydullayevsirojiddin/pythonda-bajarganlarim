# -*- coding: utf-8 -*-
"""
Created on Sat Jul 10 12:14:52 2021

@author: sirojiddin
"""
"""
olim = {
        'Abu Abdullox Muhammad ibn Ismoyil 810-yil Buxoroda tavallud topgan.':'60 yil umur ko\'rgan',
        'Abdulla Qodiriy 1894 yil Toshkentda tavallud topgan':'44 yil umur ko\'rgan',
        'Erkin Vohidov 1936 yil Farg\'onada tavallud topgan':'80 yil umur ko\'rgan',
        'Alisher Navoiy 1441-yilda Xirotda tavallud topgan':'60 yil umur ko\'rgan'
        }
for kalit, qiymat in olim.items():
    print(kalit,qiymat)

############  LUG'AT ICHIDA RO'YXAT ##############
olim = {
        'Abu Abdullox Muhammad ibn Ismoyil':['Al jome as-sahih','Al adab al-mufrad',['At-tarix al kabir','At-tarix as-sag\'ir']],
        'Abdulla Qodiriy':['O\'tgan kunlar','Mehropdan chayon','Obit ketmon'],
        'Erkin Vohidov ':['Tong nafasi','Qo\'shiqlarin sizga','O\'zbegim','Qiziquvchan Matsuma'],
        'Alisher Navoiy ':['Xamsa','Lison ut-Tayr','Mahbub Al-Qulub','Munojat']
        }
for kalit, qiymat in olim.items():
    print(f"\n{kalit}, mashxur asarlari. ")
    for asar in qiymat:
        print(asar)

•	Oila a'zolaringiz (do'stlaringiz) dan 3 ta sevimli kino-seriali haqida so'rang. 
    Do'stingiz ismi kalit, uning sevimli kinolarini esa ro'yxat ko'rinishida lug'artga 
    saqlang. Natijani konsolga chiqaring.

Kinolar = {
    "sardor" : ['Xeshnik','Rembo','Tetanik'],
    "sirojiddin" : ['Tag\'dir o\'yini','Forsaj','NFS'],
    "Hasan" : ['Abdullajon','Shaytanat','Bomba'],
    "husan" : ['Panoh','Baron','Halk']
    }
for kalit, qiymat in Kinolar.items():
    print(f"\n{kalit.title()}ning sevimli kenolari ")
    for kino in qiymat:
        print(kino.upper())
"""    
########## LUG'AT ICHIDA LUG'AT   ############
# •	Davlatlar degan lug'at yarating, lug'at ichida bir nechta davlatlar haqida 
# ma'lumotlarni lug'at ko'rinishida saqlang. Har bir davlat haqida ma'lumotni konsolga 
# chiqaring.
Davlatlar = {
    "O'zbekiston":{'poytaxti':'toshkent',
                   'hududi':'448978 kv.km',
                   'aholisi':'33000000',
                   'pul birligi':'so\'m'},
    "Rossiya":{'poytaxti':'moskva',
               'hududi':'17098246 kv.km',
               'aholisi':'144000000',
               'pul birligi':'rubl'},
    "AQSH":{'poytaxti':'vashinton',
            'hududi':'9631418 kv.km',
            'aholisi':'33000000',
            'pul birligi':'dollar'},
    "Malayziya":{'poytaxti':'kuala-lumpur',
                 'hududi':'329750 kv.km',
                 'aholisi':'25000000',
                 'pul birligi':'rinngit'}
    }
nom = input("DAvlat nomini kiriting: ")
for i in Davlatlar:
    if nom==i:
        #for kalit, qiymat in Davlatlar.items():
        print(f"\n{kalit} davlati poytxti {qiymat['poytaxti'].title()}"
              f"\nHududi {qiymat['hududi'].title()}"
              f"\nAholisi {qiymat['aholisi']} kishi"
              f"\nPul birligi '{qiymat['pul birligi'].upper()}'")
    else:
            print("Bizda bu davlatlar haqida ma'lumot movjut emas")
        

    
    
