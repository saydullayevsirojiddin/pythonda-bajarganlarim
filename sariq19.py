# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 08:11:31 2021

@author: sirojiddin
"""

#def salom_ber():
#    """Salom beruvchi funksiya"""
#    print("Assalomu alaykum")
#salom_ber()

#def salom_ber(ism):
#    """Foydalanuvchi ismini qabul qilib, 
#    unga salom beruvchi funksiya"""
#    print(f"Assalomu alaykum, hurmatli {ism.title()}")
#salom_ber('sirojiddin')
#salom_ber('vali')

#def yoshni_hisobla(ism='hasan',tug_yil=1999):
#    """Foydalanuvchi ismini va tug'ulgsn yilini qabul qilib, 
#    yoshini chiqarib beruvchi funksiya"""
#    print(f"{ism.title()} siz {2021-tug_yil} yoshdasiz")
#yoshni_hisobla()

#def fam_ism(fam='saydullayev',ism='sirojiddin'):
#    """Foydalanuvchi ismini va familiyasini qabul qilib, 
#    konsolga chiqarib beruvchi funksiya"""
#    print(f"Ismingiz: {ism.title()}",
#          f"\nfamiliyangiz: {fam.title()}")
#fam_ism()
'''
## 1.	Foydalanuvchi ismi va yoshini so'rab, uning tug'ilgan 
## yilini hisoblaydigan funksiya yozing.
def tug_yil(ism,yosh):
    """Foydalanuvchi tug'ulgan yilini aniqlash"""
    print(f"Salom {ism.title()}, siz {2021-yosh} yilda tug'ilgansiz")
ism = input("Ismingiz nima: ")
yosh = int(input("yoshingiz nechchida: "))
tug_yil(ism, yosh)
'''
'''
## 2.	Foydalanuvchidan son olib, uning kvadrati va kubini konsolga chiqaruvchi
## funksiya yozing.
def son_kv_kub(son):
    """Sonning kivadrati va ko'bini hisoblaydi"""
    print(f"Kivadrati: {son**2}",
          f"\nKo'bi: {son**3}")
son=int(input("son = "))
son_kv_kub(son)
'''
'''
## 3.	Foydalanuvchidan son olib, son juft yoki toqligini konsolga
## chiqaruvchi funksiya yozing.
def juf_toq(son):
    """Sonning juft toqligini aniqlash"""
    if son%2!=0:
        print(son, "toq son")
    else:
        print(son, "juft son")
son=int(input("son = "))
juf_toq(son)
'''
''' 
## 4.	Foydalanuvchidan ikkita son olib, ulardan kattasini konsolga chiqaruvchi
## funksiya yozing. Agar sonlar teng bo'lsa "Sonlar teng" degan xabarni chiqaring.
def katta_son(son1,son2):
    """ikkita son olib, ulardan kattasini aniqlaydi"""
    if son1>son2:
        print('son1 katta')
    elif son1==son2:
        print("sonlar teng")
    else:
        print('son2 katta')
son1=int(input("son1 = "))
son2=int(input("son2 = "))
katta_son(son1, son2)
'''
'''
## 5.	Foydalanuvchidan x va y sonlarini olib, x^yxyni konsolga chiqaruvchi funksiya
## yozing.
def xning_ydarajasi(x,y):
    """x va y sonlarini olib, 
    x^y ni konsolga chiqaruvchi"""
    print('natija', x**y)
x=int(input(' x = '))
y=int(input(' y = '))
xning_ydarajasi(x,y)    
'''
'''
## 6.	Yuqoridagi funksiyada y uchun 2 standart qiymatini bering.
def xning_ydarajasi(x):
    """x va y sonlarini olib, 
    x^y ni konsolga chiqaruvchi"""
    print('natija', x**2)
x=int(input(' x = '))
xning_ydarajasi(x)

'''
## 7.	Foydalanuvchidan son qabul qilib, sonni 2 dan 10 gacha bo'lgan
## sonlarga qoldiqsiz bo'linishini tekshiruvchi funksiya yozing. Natijalarni
## konsolga chiqaring.
def bolinish_alomati(son):
    """son qabul qilib, sonni 2 dan 10 gacha
    bo'lgan sonlarga qoldiqsiz bo'linishini
    tekshiruvchi funksiya"""
    for i in range(2,11):
        if son%i==0:
            print(f"{son} {i} qoldiqsiz bo'linadi")
#son=int(input('son = '))
bolinish_alomati(70)    


