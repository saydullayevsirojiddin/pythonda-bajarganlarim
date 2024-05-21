'''
Siz uyxudan turdingiz va telifonni qo'lga olib haftaning qaysi kuni va 
havo haroratini ko'rdingiz.
1) Bugun kun nima?
2) Harorat nechchi?
Agar kun yakshanba yoke shanba bo'lsa bugun dam olish kuni va harorat
30 dan katta bo'lsa 
ekranga chiqarsin: bugun dam olish kuni, cho'milgani kettik
Agar kun yakshanba yoke shanba bo'lsa bugun dam olish kuni va harorat
30 dan kichik bo'lsa 
ekranga chiqarsin: bugun dam olish kuni, uyda dam olamiz
Agar ish kuni bo'lsa: Bugun ishga boramiz
degan dega dastur tuzing?
'''

kun=input("Bugun nima kun?: ")
harorat=int(input("Bugun havo harorati nechchi: "))

if kun.lower()=='yakshanba' or kun.lower()=="shanba" and harorat>=30:
	print("Bugun dam olish kuni. Cho'milgani kettik")
elif kun.lower()=='yakshanba' or kun.lower()=="shanba" and harorat<30:
	print("Uyda dam olamiz! counter o'ynaymiz")
else:
	print("Ishga boramiz")






