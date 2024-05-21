# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 10:11:42 2021

@author: sirojiddin
Python izohli lug'atini yarating va lug'atga kamida 10 ta so'z
qo'shing. Lug'atdagi har bir kalit va qiymatni for tsikli yordamida,
alifbo ketma-ketligida chiroyli qilib konsolga chiqaring.
"""
Mashina_turi = {
    "lacetti" : "2010",
    "spark" : "2015",
    "nexa" : "2009",
    "matiz" : "2015",
    "damas" : "2013",
    "orlando" : "2014",
    "cobalt" : "2019",
    "nexia" : "2010",
    "nexia 3" : "2018",
    "captiva" : "2020",
    "malibu" : "2015",
    "malibu 2" : "2019"
    }
#print("Salonda Mashinalar turlari")
#for turi, yili in sorted(Mashina_turi.items()):
#    print(f"{turi.title()} ishlab chiqilgan {yili} yil")
    
#for turi in sorted(Mashina_turi):
#    print(f"{turi.title()}")

Davlatlar = {
    "aqsh" : "washington D.C",
    "o'zbekiston" : "tashkent",
    "rossiya" : "moskva",
    "italiya" : "singapur",
    "qozoqiston" : "dushanbe",
    "qirg'iziston" : "beshkek",
    "tojikiston" : "nursulton",
    "malayziya" : "kuala-lumpur",
    "singapur" : "rim"
    }
"""
d_nomi = input("Qaysi davlat poytaxtini bilishni istaysiz: ")
for davlat, poytaxt in Davlatlar.items():
    if davlat == d_nomi:
        print(f"{davlat.title()} davlatning poytaxti {poytaxt.title()}")
        break
    else:
    asd    print("kechirasiz bunday davlat yo'q")
"""
taomlar_menu = {
    "osh" : "12000",
    "norin" : "10000",
    "o'za sho'rva" : "12000",
    "lavash" : "11000",
    "tandir" : "19000",
    "manti" : "13000",
    "mastava" : "9000",
    "do'lma" : "10000",
    "shashlik" : "16000",
    "somsa" : "11000",
    "lag'mon" : "10000"
    }
print("3 ta taom buyurtma bering.")
buyurtmalar = []
for n in range(3):
    buyurtmalar.append(input(f"{n+1}-taom:").lower())
print("Siz buyutma qilgan taomlar:",buyurtmalar)

for buyurtma in buyurtmalar:
    if buyurtma in taomlar_menu:
        print(f"{buyurtma.title()} {taomlar_menu[buyurtma]} so'm")
    else:
        print(f"Kechirasiz, bizda {buyurtma} yo'q ")





















