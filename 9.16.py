a = int(input(" a = "))
c = int(input(" c = "))
if a>c:
	i=c
	for i in range(c,a,1):
		print(i, end=';')
else:
	i=a
	for i in range(a,c,1):
		print(i, end=';')