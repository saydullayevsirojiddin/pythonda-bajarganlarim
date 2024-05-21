#++++++++++++++++FOR LOOP++++++++++++++++
#+++++++++++++++++uchun+++++++++++++++++++
mehmonlar = ['Ali','Vali','Hasan','Husan','Toxir']
for i in mehmonlar:
	print("Salom mehmon", i,"xush kelibsiz")

mehmonlar = ['Ali','Vali','Hasan','Husan','Toxir']
for j in mehmonlar:
	print(f"Hurmatli {i}, sizni 23 may kuni sizni nahor oshga taklif qilamiz")
	print("Hurmat bilan Polanchayevlar oilasi")

sonlar = list(range(0,11,2))
for son in sonlar:
	print(f"{son} ning kivadrati {son**2} ga teng")

sonlar = list(range(11)) # 0 da 10 gacha sonlar ro'yhati
sonlar_kivadrati = [] # bo'sh ro'yhat
for s in sonlar:
	sonlar_kivadrati.append(son**2) # uning kivadratini hisoblaydi

print("sonlar",sonlar)
print("sonlar_kivadrati",sonlar_kivadrati)	

dostlar=[]
print("Eng yaqin 5 ta  do'stingizni kiriting")
for n in range(5):
	dostlar.append(input(f"{n+1} Do'stlaringizni ismini kiriting: "))
print(dostlar)








