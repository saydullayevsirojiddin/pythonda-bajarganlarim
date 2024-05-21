# 16-d.py
"""
def uchburchak(a,b,c):
	if a+b>c and a+c>b and b+c>a:
		d = "uchburchak yasasa bo'ladi"
	else:
		d = "uchburchak yasab bo'lmaydi"
	return d
a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
print(uchburchak(a, b, c))

def yigindi():
	c=a+b
	return c
def ayirma():
	c=a-b
	return c
def kopaytma():
	c=a*b
	return c
def bolinma():
	c=a/b
	return c
a = int(input("a="))
b = int(input("b="))
amal = int(input('amal:'))
if amal==1:
	print(yigindi())
elif amal==2:
	print(ayirma())
elif amal==3:
	print(kopaytma())
elif amal==4:
	print(bolinma())
else:
	print("boshqa amal tanladingiz")

from math import*
def aylana():
	s=pi*r**2
	return round(s,2)
def tortburchak():
	s=a*b
	return s
def uchburchak():
	p=(a+b+c)/2
	s=sqrt(p*(p-a)*(p-b)*(p-c))
	return s


shakil = int(input('shakil: '))
if shakil==1:
	print("Aylana ning yuzi topish:")
	r=int(input("r = "))
	print("S = ",aylana())
elif shakil==2:
	print("Tortburchakning yuzi topish: ")
	a=int(input("a = "))
	b=int(input("b = "))
	print("S = ",tortburchak())
elif shakil==3:
	print("Uchburchakning yuzi topish: ")
	a=int(input("a = "))
	b=int(input("b = "))
	c=int(input("c = "))
	print("S = ",uchburchak())
"""
def summa(*sonlar):
    print(sonlar)
    s=0
    for i in sonlar[0]:
        s+=i
    return s
#murojaat
print(summa(list(map(int,input().split()))))














