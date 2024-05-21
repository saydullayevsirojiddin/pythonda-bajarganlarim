##choy=False
#alat=True
#non=True
#sharbat=True
#if choy:
#	print("choy sotib oldi")
#	narhi=narhi+1000
#if salat:
#	print("salat sotib oldi")
#	narhi=narhi+3000
#if non:
#	print("non sotib oldi")
#	narhi=narhi+3000
#if sharbat:
#	print("sharbat sotib oldi")
#	narhi=narhi+2000
#print(f"Jami {narhi} so'm bo'ldi")

#menu=['osh','tandir','manti','shashlik','norin','sho\'rva']
#ovqat=input("Siz qanday ovqat yiysiz? ")
#if ovqat.lower() in menu:
#	print("Buyurtma qabul qilindi")
#else:
#	print("Afsuske bunday ovqat yo\'q")

menu= ['osh','tandir','manti','shashlik','non','norin','sho\'rva']
Buyurtmalar=['osh','tandir','manti','shashlik','dolma']

if Buyurtmalar:
	for taom in Buyurtmalar:
		if taom in menu:
			print(f"Menuda {taom} bor")
		else:
			print(f"Kechirasiz. Menuda {taom} yo'q")
else:
	print("Buyurtmalar yo\'q")

