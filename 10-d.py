#10-dars.py
"""
n = 0
while n<=50:
	print(n)
	n += 2

##Palindirom sonlarni aniqlaydigan Dastur ishlash
son = input('Biror son kiriting: ')
son2 = son[::-1]
for x in range(len(son)):
	p = True
	if( son[x] != son2[x]):
		print(x,'Soningiz palimdirom emas.')
		p = False
		break
if p:
	print('Soningiz palendirom.')

##kara kara	 2 x 2 = 4, 2 karadan 9 karagacha
for x in range(2,10):
	for y in range(2,10):
		print(x,' x ',y,' = ',x*y)

for x in range(2,10):
	for y in range(2,10):
		#print(x,' x ',y,' = ',x*y)
		if x==2:
			print(x,' x ',y,' = ',x*y,end='  /////  ')
		if x==3:
			print(x,' x ',y,' = ',x*y,'\n')


b=1
q=2
i=1
while b<100:
	print("b[",i,"]=",b)
	b*=q
	i+=1

a=1.0
narx=100
while a<=2.0:
	a+=0.1
	print(round(a,2),'kg = ', round((a*narx,2), "so'm"))

a = int(input(' a = '))
b = int(input(' b = '))
while a>b:
	a=a-b
print(a)

a = int(input(' a = '))
b = int(input(' b = '))
while a>b:
	a=a-b
	print(a)
else:
	b=b-a
	print(b)

a = int(input(' a = '))
b = int(input(' b = '))
while a!=b:
	if a>b:
		a=a-b
		print(a)
	else:
		b=b-a
		print(b)


## N  gacha Tub sonlarni chiqarish
N = int(input("N="))
k=2
tub=True
while N>=k:
	tub=True
	for i in range(2,int(k/2)+1):
		if k%i==0:
			tub=False
			break
	if tub:
		print(k)
	k+=1


## sonning tub ko'paytuvchilarini chiqaruvchi dastur
## masalan: 24=2*2*2*3,  36=2*2*3*3
n=int(input('Biror sonni kiriting: N = '))
k=2
tub=True
tublar = []
while(n>=k):
    tub=True
    for i in range(2,int(k/2)+1):
        if k%i==0:
            tub=False
            break
    if tub:
        tublar.append(k)
    k+=1
javob = []
for i in tublar:
    while n % i == 0:
        javob.append(i)
        n /= i
print(javob)

## N(N>1) butun son berilgan. 3^K<N tengsizlik o`rinli bo`ladigan
## eng katta K butun soni topilsin.
n=int(input("n="))
k=1

while 3**k<n:
	k+=1
	print(k-1)

## N sonini raqamlarini yig'indisini chiqarish
## 1-USUL
n=int(input())
k=0
if(n<0):
    n*=(-1)

while n>0:
    k=k+(n%10)
    n//=10
print(k)

## 2-USUL
n = input('Biror son kiriting: N = ')
s = 0
for i in range(len(n)):
    s += int(n[i])
print(s)

## 3-USUL
n,k=input(),0;
for i in n: k=k+int(i);
print(k)
"""
##3-misol
N = int(input(' N = '))
K = int(input(' K = '))
p=0
while N>K:
	N=N-K
	p+=N
	print(p,N)





