#18-d.py
"""
s=input('Son kiriting: ')
try:
	s = int(s)
except:
	print('Siz son kiritmadingiz')
	s = len(s)
else:
	pass
finally:
	pass
print(s)
"""
ism = input('Ismingizni kiriting:')
yil = input('Tug`ilgan yilingizni kiriting:')
try:
    yil = int(yil)
except ValueError:
    print('Tug`ilgan yilingizni xato kiritdingiz')
else:
    print('Hurmatli', ism, 'aka, sizning yoshingiz', 2021 - yil, 'da ekan.')
finally:
    print('dastur ishi tugadi')

