"""print("Sizning yoshingiz nechichida: ")
t_yil = int(input("Tug'ulgan yilingiz: "))
h_yil = int(input("Hozirgi yil: "))
yosh = h_yil-t_yil

if yosh >= 30:
	print("Siz qaribsiz")
else:
	print("Siz yoshsiz")

print("Sizning yoshingiz nechichida: ")
t_yil = int(input("Tug'ulgan yilingiz: "))
h_yil = int(input("Hozirgi yil: "))
yosh = h_yil-t_yil

if yosh <= 7:
	print("Siz bog'cha yoshidasiz")
elif yosh == 12:
	print("Siz 1-mo'chal yoshidasiz")
elif yosh <= 18:
	print("Siz maktab o'quvchisisiz")
elif yosh >= 18:
	print("Siz balog'at yoshidasiz")
elif yosh >= 30:
	print("Siz qaribsiz")
 To`g`ri to`rtburchakning 3 ta uchi butun sonlardan iborat
 koordinatalar bilan berilgan va shu uchlar orasidagi 
 tomonlar koordinata o`qlariga parallel to`rtburchakning
 to`rtinchi uchining koordinatasi topilsin.
1 1 1 5 4 5
4 1
"""
x1=int(input('X1 koordinatasini kiriting: '))
y1=int(input('Y1 koordinatasini kiriting: '))
x2=int(input('X2 koordinatasini kiriting: '))
y2=int(input('Y2 koordinatasini kiriting: '))
x3=int(input('X3 koordinatasini kiriting: '))
y3=int(input('Y3 koordinatasini kiriting: '))

if x1 == x3 and y1 == y2:
	x = x2 - x1
	x4 = x3 + x
	print("x4 = ",x4,"\n y4 = ",y3)
else:
	print("""Bu to'g'ri to'rtburchakning 
		tomonlari x va y ga parallel emas""")