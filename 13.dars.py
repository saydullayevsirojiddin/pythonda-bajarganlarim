# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 09:20:37 2021

@author: sirojiddin
"""

mevalar_menu = {
    "olma" : "12000",
    "anor" : "10000",
    "tarvuz" : "12000",
    "qovun" : "11000",
    "pamedor" : "19000",
    "uzum" : "13000",
    "nok" : "9000",
    "bexi" : "10000",
    "shaftoli" : "16000",
    "gilos" : "11000"
    }
print("N ta meva buyurtma bering.")
N=int(input("N="))
buyurtmalar = []

for n in range(N):
    buyurtmalar.append(input(f"{n+1}-meva:").lower())
print("Siz buyutma qilgan mevalar:",buyurtmalar)

for buyurtma in buyurtmalar:
    if buyurtma in mevalar_menu:
        print(f"{buyurtma.title()} {mevalar_menu[buyurtma]} so'm")
    else:
        print(f"Kechirasiz, bizda {buyurtma} yo'q ")
