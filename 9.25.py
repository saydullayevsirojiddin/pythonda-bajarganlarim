from math import *
a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
D=sqrt(b**2-4*a*c)
if D<0:
	print("Yechimi ye'q")
else:
	if D==0:
		x=-b/2*a
		print(x)
	else:
		x1=(-b-sqrt(D))/2*a
		x2=(-b+sqrt(D))/2*a
		print('x1 = ',x1,"\nx2 = ",x2 )