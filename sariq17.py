# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 23:46:31 2021

@author: sirojiddin
"""
"""
#input
ism = input("Ismingiz nima ? ")
savol = f"Salom, {ism.title()}. yoshingiz nechchida ? "
yosh = input(savol)
yosh = int(yosh)
height = input("Bo'yingiz nechchida ")
height = float(height)

#while 
son = 1
while son <= 5:
    print(son, end=', ')
    son += 1
print("Dastur tugadi")

#while end input
print(" Kiritilgan dasturni qaytaruvchi dastur.")
savol = "Istalgan son kiriting: "
savol += "(dasturni to'xtatish uchun 'exit' deb tozing.)"
qiymat = ''
while qiymat != "exit":
    qiymat=input(savol)
    if qiymat != "exit":
        print(float(qiymat)**2)
print("Dastur tugadi")

# ishora
print(" Kiritilgan dasturni qaytaruvchi dastur.")
savol = "Istalgan son kiriting: "
savol += "(dasturni to'xtatish uchun 'exit' deb tozing.)\n"
qiymat = ''
ishora = True
while qiymat != "exit":
    qiymat=input(savol)
    if qiymat == "exit":
        ishora = False
    else:    
        print(float(qiymat)**2)
print("Dastur tugadi")

#break while
print(" Kiritilgan dasturni qaytaruvchi dastur.")
savol = "Istalgan son kiriting: "
savol += "(dasturni to'xtatish uchun 'exit' deb tozing.)\n"
qiymat = ''

while True:
    qiymat=input(savol)
    if qiymat == "exit":
        break
    else:    
        print(float(qiymat)**2)
print("Dastur tugadi")

#break
son = 0
while son <=11:
    son += 1
    if son == 5:
        break
    else:
        print(son)

#continue
son = 0
while son <=11:
    son += 1
    if son == 5:
        continue
    if son == 3:
        continue
    else:
        print(son)

#AMALIYOT
# 1.	Foydalanuvchidan yaxshi ko'rgan kitoblarini kiritishni 
# so'rang. Foydalanuvchi stop so'zini yozishi bilan dasturni 
# to'xtating

ism = input("Ismingiz nima: ")
k = "Yaxshi ko'rgan kitobingizni kiriting: "
print("Dasturdan chiqish uchun 'stop' so'zini kiriting ")
kitob = ''
while kitob!="stop":
    kitob = input(k)
    if kitob=="stop":
        break
    else:
        print(f"Salom {ism.title()}. {kitob.title()} yaxshi kitob!")
print("Siz 'stop' kirittingiz. Dastur tugadi")
"""
# 2.	Muzeyga chipta narhi foydalanuvchining yoshiga bog'liq: 7 dan 
# yoshlarga - 2000 so'm, 7-18 gacha 3000 so'm, 18-65 gacha 10000 so'm,
# 65 dan kattalarga bepul. Shunday while tsikl yozingki, dastur 
# foydalanuvchi yoshini so'rasin va chipta narhini chiqarsin. Foydalanuvchi
# exit yoki quit deb yozganda dastur to'xtasin (ikkita shartni ham tekshiring).

ism = input("Ismingiz nima: ")
k = "Yoshingiz nechchida: "
print("Dasturdan chiqish uchun 'exit' yoke 'quit'  so'zini kiriting ")
yosh = ''
while yosh!="exit" and yosh!='quit':
    yosh = int(input(k))
    if yosh == "stop" and yosh == "quit":
        break
    elif yosh<7:
        print(f"Salom {ism.title()}. Sizning yoshingiz {yosh} da. Sizga chipta narhi 2000 ming!")
    else:
        print(f"Salom {ism.title()}. {k} yaxshi kitob!")
print("Siz 'stop' kirittingiz. Dastur tugadi")








