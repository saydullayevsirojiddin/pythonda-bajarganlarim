# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 09:28:03 2021

14.DARS
@author: sirojiddin
"""
"""
dict1 = {
    'kartoshka' : '4500',
    'sabzi' : '3000',
    'piyoz' : '2000',
    'pamidor' : '2500',
    'chesnok' : '13000',
    'kola' : '10000',
    'fanta' : '10000',
    'nestle' : '3000',
    'pepse' : '10000',
    'montella' : '3000',
    'olma' : '4500',
    'nok' : '3000',
    'uzum' : '12000',
    'gilos' : '12500',
    'shaftoli' : '13000',
    'guruch' : '4500',
    "no'xot" : '3000',
    'loviya' : '12000',
    'girichka' : '12500',
    'mosh' : '13000'
    }
for kalit, qiymat in dict1.items():
    print(f" {kalit.title()} 1 kg = {qiymat} ")

royhat = ['anor','uzum','non','baliq']
for i in dict1:
    if i in royhat:
        print(f"{i.title()}  {dict1[i]} so'm")
    else:
        print(f"{i.title()}, kechirasiz bunday maxsulot yo'q")

dict1 = {
    'kartoshka':4500,
    'piyoz':5500,
    'olma':13500,
    'banan':13500,
    'behi':12000,
    'olcha':11000
    }
print(dict1.items() )
a=int(input('necha kg olasiz = '))
print(a*(dict1.get(input("mahsulot nomini kiriting="),
                   "Bunday mahsulot yoq")))

dict1 = {
    'Kartoshka':12000,
    'Piyoz':5000,
    'Banan':14500,
    'Olma':12005,
    'Sabzi':10000,
    'Karam':3000
}
n = 1
for i in dict.items(dict1):
    print(n,'.', i)
    n += 1

m = input('Nima olmoqchisiz?:')
kg = int(input('Qancha olmoqchisiz? '))

print(kg, 'kg', m, kg*int(dict1.get(m, 0)))    
"""
dict1={
    "Salom":"Hello",
    "Tula":"Pay",
    "Xayr":"GoodBay",
    "Bir":"One"
    }
x=list(map(str,input().split()))
print(x)
for i in x:
    print(dict1.get(i,i),end=" ")

 
    
    
    