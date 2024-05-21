"""
#####5-misol:
n = int(input("n = "))
a = int(input("a = "))
b = int(input("b = "))

if n == 1:
	print("YIGINDI: ",a+b)
elif n == 2:
	print("AYIRMA: ",a-b)
elif n == 3:
	print("KO'PAYTMA: ",a*b)
elif n == 4:
	if not(b==0):
		print("BO'LINMAMA: ",a/b)
	else:
		print("maxraj 0 ga teng bo'la olmaydi")
"""
n = input("n = ")

if n > 0:
	print(n*1000//1000,"km")
if n > 0.1:
	print(n*1000%1000//100*100,"m")
if n > 0.01:
	print(n*1000//1000,"km")
if n > 0:
	print(n*1000//1000,"km")



