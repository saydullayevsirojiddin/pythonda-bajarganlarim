"""
14-dars
3, 4, 5-savollar

"""
operatorlar = {'if':'agar', 'else':'yoke','int':'butun son', 'floar':'haqiqiy son', 'print':'konsolga chop etish'}
a = input('kalit so\'z kiriting: ')
for x in range(operatorlar):
	if a == x:
		print(a)
	else:
		print("bu so'z ro'yhatimizda yo'q, uzur so'raymiz")




