                                                                                                                                                                            """9-dars.py
                                                                                                                                                                            hafta = ['dushanba','seshanba','chorshnba','payshanba','juma','shanba','yakshnba']
                                                                                                                                                                            for kun in hafta:
                                                                                                                                                                                    print(kun)
                                                                                                                                                                            s=0
                                                                                                                                                                            for i in range(3,100,3):
                                                                                                                                                                                    print(s,"+",i,"=",s+in)
                                                                                                                                                                                    s+=1
                                                                                                                                                                            ###### sonning tub yoke murakkab SONLIGINI ANIQLAYDIGAN SON KIRITNG
                                                                                                                                                                            s=int(input("SON KIRITING"))
                                                                                                                                                                            tub=False
                                                                                                                                                                            for i in range(2,int(s/2)):
                                                                                                                                                                                    if (s%1==0):
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            tub=True
                                                                                                                                                                                            break
                                                                                                                                                                            if not tub:
                                                                                                                                                                                    print(s," tub son")
                                                                                                                                                                            else:
                                                                                                                                                                                    print(s," murakkab son")

                                                                                                                                                                            CONTINUE SEKIL DAVON ETSIN
                                                                                                                                                                            BREAK SEKILNI TO'XTATISH

                                                                                                                                                                            for x in range(100):
                                                                                                                                                                                    if x == 15:
                                                                                                                                                                                            continue #  1 dan 100 gacha sonlardan 15ni chiqarmasin
                                                                                                                                                                                    else:
                                                                                                                                                                                            print(x)

                                                                                                                                                                            for x in range(100):
                                                                                                                                                                                    if x == 15:
                                                                                                                                                                                            break #  1 dan 100 gacha son ORASIDA 15 bo'sa  shu songacha sekil davom etadi
                                                                                                                                                                                    else:	
                                                                                                                                                                                            print(x)
                                                                                                                                                                                            continue

                                                                                                                                                                            1-misol
                                                                                                                                                                            n = int(input(" n = "))
                                                                                                                                                                            k = int(input(" k = "))
                                                                                                                                                                            if n>0:
                                                                                                                                                                                    True
                                                                                                                                                                            else:
                                                                                                                                                                                    print(" n naturl son")

                                                                                                                                                                            for i in range(n):
                                                                                                                                                                                    print(k)

                                                                                                                                                                            s = 0
                                                                                                                                                                            for i in range(-1):
                                                                                                                                                                                    print(i)
                                                                                                                                                                            else:
                                                                                                                                                                                    print("for ishlamadi")

                                                                                                                                                                            ###### 1 dan 100 gacha sonlar yig'indisi
                                                                                                                                                                            s=sum(list(range(101)))
                                                                                                                                                                            print(s)
                                                                                                                                                                            ###### 1 dan 100 gacha toq sonlarni chiqarish
                                                                                                                                                                            s=list(range(1,100,2))
                                                                                                                                                                            print(s)
                                                                                                                                                                            ###### 1 dan 100 gacha juft sonlarni chiqarish
                                                                                                                                                                            s=list(range(2,101,2))
                                                                                                                                                                            print(s)
                                                                                                                                                                            ###### 5 dan n gacha 2 qadam sonlarni chiqarish
                                                                                                                                                                            n=int(input())
                                                                                                                                                                            s=list(range(5,n,2))
                                                                                                                                                                            print(s)

                                                                                                                                                                            ##2-misol
                                                                                                                                                                            A=int(input(" A = "))
                                                                                                                                                                            B=int(input(" B = "))
                                                                                                                                                                            if A>B:
                                                                                                                                                                                    True
                                                                                                                                                                            else:
                                                                                                                                                                                    print(" A>B bo'lish kk")
                                                                                                                                                                            for i in range(B,A+1):
                                                                                                                                                                                    print(i)
                                                                                                                                                                            ##3-misol
                                                                                                                                                                            A=int(input(" A = "))
                                                                                                                                                                            B=int(input(" B = "))
                                                                                                                                                                            if A<B:
                                                                                                                                                                                    True
                                                                                                                                                                            else:
                                                                                                                                                                                    print(" A<B bo'lish kk")

                                                                                                                                                                            for i in range(B,A,-1):
                                                                                                                                                                                    print(i)		

                                                                                                                                                                            ##4-misol
                                                                                                                                                                            Narx = 14000
                                                                                                                                                                            for i in range(1,11):
                                                                                                                                                                                    Narxlar = i*Narx
                                                                                                                                                                                    print(f"{i} konfetni narxi {Narxlar} sum.")

                                                                                                                                                                            ##5-misol
                                                                                                                                                                            Narx = 14000
                                                                                                                                                                            for i in range(1,11):
                                                                                                                                                                                    Narxlar = i/10*Narx
                                                                                                                                                                                    print(f"{i/10} konfetni narxi {Narxlar} sum.")

                                                                                                                                                                            6-misol
                                                                                                                                                                            Narx = 14000
                                                                                                                                                                            for i in range(12,22,2):
                                                                                                                                                                                    Narxlar = i/10*Narx
                                                                                                                                                                                    print(f"{i/10} konfetni narxi {Narxlar} sum.")
                                                                                                                                                                            ##7-misol
                                                                                                                                                                            A = int(input(" A = "))
                                                                                                                                                                            B = int(input(" B = "))
                                                                                                                                                                            if B>A or A>0 and B>0:
                                                                                                                                                                                    s=0
                                                                                                                                                                                    for x in range(A,B+1):
                                                                                                                                                                                            s+=x
                                                                                                                                                                                    print("Yig'indi: ",s)
                                                                                                                                                                            else:
                                                                                                                                                                                    print("A va B natural sonlar")

                                                                                                                                                                            ##8-misol
                                                                                                                                                                            A = int(input(" A = "))
                                                                                                                                                                            B = int(input(" B = "))
                                                                                                                                                                            if B>A or A>0 and B>0:
                                                                                                                                                                                    p=1
                                                                                                                                                                                    for x in range(A,B+1):
                                                                                                                                                                                            p*=x
                                                                                                                                                                                    print("Ko'paytma: ",p)
                                                                                                                                                                            else:
                                                                                                                                                                                    print("A va B natural sonlar")

                                                                                                                                                                            ##9-misol
                                                                                                                                                                            A=int(input(" A = "))
                                                                                                                                                                            B=int(input(" B = "))
                                                                                                                                                                            if B>A or A>0 and B>0:
                                                                                                                                                                                    s=0
                                                                                                                                                                                    for y in range(A,B+1):
                                                                                                                                                                                            s+=y**2
                                                                                                                                                                                    print("Kivadratlari yig'indisi: ",s)
                                                                                                                                                                            else:
                                                                                                                                                                                    print("A va B naturla sonlar")

                                                                                                                                                                            ##10-misol  => 1+1/2+…+1/N 
                                                                                                                                                                            N = int(input(" N = "))
                                                                                                                                                                            if N>0:
                                                                                                                                                                                    y = 1
                                                                                                                                                                                    for x in range(2,N+1,2):
                                                                                                                                                                                            y+=1/x
                                                                                                                                                                                    print("Yig'indi: ", y)
                                                                                                                                                                            else:
                                                                                                                                                                                    print("N naturl son ")

                                                                                                                                                                            ##11-misol    => N3+(N+1)3+(N+2)3…+(2N)3
                                                                                                                                                                            N = int(input(" N = "))
                                                                                                                                                                            natija=0
                                                                                                                                                                            for x in range(N):
                                                                                                                                                                                    natija+=(x+1)**3
                                                                                                                                                                                    print(f"({x} + 1)**3 = {natija}")

                                                                                                                                                                            ##12-misol    =>   1,1*1,2*1,3*…{1,N}  
                                                                                                                                                                            N = int(input(" N = "))
                                                                                                                                                                            natija=1
                                                                                                                                                                            for x in range(1,N,1):
                                                                                                                                                                                    natija*=(1+x/10)
                                                                                                                                                                                    print(f" {natija}")
                                                                                                                                                                            else:
                                                                                                                                                                                    print("eror")

                                                                                                                                                                            ##13-misol    =>   1,1-1,2+1,3-(pow(-1,x)+x/10)
                                                                                                                                                                            #N = int(input(" N = "))
                                                                                                                                                                            #natija=0
                                                                                                                                                                            #for x in range(1,N):
                                                                                                                                                                            #	natija+=(1+x/10*(-1)**(x+1))
                                                                                                                                                                            #print(natija)

                                                                                                                                                                            ##14-misol    =>   N2=1+3+5+…+(2N-1)
                                                                                                                                                                            n = int(input(" n = "))
                                                                                                                                                                            natija1=n**2
                                                                                                                                                                            print(natija1)
                                                                                                                                                                            natija2=0
                                                                                                                                                                            for x in range(1,n*2,2):
                                                                                                                                                                                    natija2 += x
                                                                                                                                                                                    print(natija2)
                                                                                                                                                                            print(f"{natija1} = {natija2}")

                                                                                                                                                                            ##15-misol    =>   N2=1+3+5+…+(2N-1)
                                                                                                                                                                            A = float(input(" A = "))
                                                                                                                                                                            N = int(input(" N = "))
                                                                                                                                                                            #for x in range():
                                                                                                                                                                            p = pow(A,N)
                                                                                                                                                                            print(p)	

                                                                                                                                                                            ##16-misol    =>      A^1, A^2, A^3, A^4,A^N   

                                                                                                                                                                            A = float(input(" A = "))
                                                                                                                                                                            N = int(input(" N = "DLLs
p=1
for x in range(1,N+1):
	p=pow(A,x)
	print(p)

##17-misol    =>      A^1+A^2+A^3+A^4+...+A^N   
A = float(input(" A = "))
N = int(input(" N = "))
p=0
for x in range(1,N+1):
	p+=pow(A,x)
print(p)

##18-misol    =>      1-A^0+A^2-A^3+…+(-1)^N*A^N.   
A = float(input(" A = "))
N = int(input(" N = "))
p=1
for x in range(1,N+1):
	p+=pow(A,x)*pow(-1,x)
print(p)

##19-misol    =>      N! = 1*2*3*4*5*...*N 
N = int(input(" N = "))
p=1
for x in range(1,N+1):
	p*=x
print("N! = ", p)

##20-misol    =>     1!+2!+…+N!
N = int(input(" N = "))
p=1
s=0
for x in range(1,N+1):
	p*=x
	s+=p
print("s = ", s)

1+1*2+1*2*3+2*3*4
x=8
x|2
print(x)

for i in range(65, 92):
	print(chr(i))         ### ANSI codiga mos simvollarni chiqarish

for i in "ABCDFQWIUYHHKJBABSMNBMXV":
	print(ord(i))         ### ANSI simvollariga mos codini chiqarish 
  ### Kiritilgan matnni AISCI dagi kodlarini chiqaruvchi dastur

a= input("ismingizni kiriting: ")
for i in a.upper():             # .upper() harflarni katta qilib chiqaradi
	print(i,"=>",ord(i), end = " , ")7

##31-misol  A0=2;  Ak=2+1/Ak-1    k=1,2,… Ketma-ketlikning
            ##A1, A2, …, AN  elementlari chiqarilsin.
a=2
k = int(input("k = "))
print(a, end=',')
for x in range(k):
	a = 2+1/a
	print(a, end=' , ')

##31-misol
n = int(input("N naturla son kiriting: "))
a = [2]
b = []
for i in range(n+1):
	b.append(a[i])
	a[i] = 2 + 1 / a[i-1]
	a.append(a[i])
print(b)

##21-misol  =>  1+1/(1!)+1/(2!)+…+1/(N!)
n = int(input(" N = "))
p=1
s=1
a=1
for x in range(1,n):
	p*=x
	s+=p
	a+=1+1/s
print(a)

##22-misol  =>  1+x+x2/(2!)+…+xN/(N!)
n = int(input(" n = "))
x = int(input(" x = "))
a=0
p=1
s=0
for i in range(1,n):
	p*=i
	
	a+=1+x+pow(x,i)/p
print(a)

##23-misol   ??????????????????///
x = int(input(" x = "))
n = int(input(" n = "))
p=1
s=1
for i in range(n):
	p*=(2*i-1)
	s+=x-pow(-1,i)*pow(x,(2*i-1))/p
print(s)

##32-misol
k=int(input(" k = "))
a=[]
print("a 0 = ",a)
for i in range(1,k+1):
	a=(a+1)/i
	print('a',i,'=',a)

##33-misol
a=[1,1]
n=int(input('n='))
b=a
print(b[1],end=',')
for i in range(2,n+1):
	b.append(a[i-1])
	a[i]=a[i-2]+a[i-1]
	print(b[i], end=',')

##34-misol
a=[2,1]
x=int(input('x='))
b=a
print(b[1],end=', ')
for n in range(2,x+2):
	b.append(a[n-1])
	a[n]=(a[n-2]+2*a[n-1])/2
	print(b[n], end=' ,')

##35-misol ??????????????????????????
a=[2,1]
x=int(input('x='))
b=a
print(b[1],end=',')
for n in range(4,x+2):
	b.append(a[n-1])
	a[n]=a[n-2]+2*a[n-1]-2*a[n-3]
	print(b[n], end=',')	

##35-misol
n=int(input('n = '))
k=int(input('k = '))
s=0
for i in range(1,n+1):
	s+=pow(i,k)
	print(s)

##35-misol
n=int(input('n = '))
k=int(input('k = '))

for i in range(1,n):
	p=0
	for j in range(1,k):
		s=i**j
		p+=s
	print(p)

rang = ["qora", "oq", "qizil"]
mashina = ["Spark", "Nexia", "Lacetti"]
for x in rang:
	for y in mashina:
		print(x, y)

import datetime as dt
x = dt. datetime. now()
print(x)

## n gacha bo'lgan barcha tup sonlarni chiqarish
n = int(input('n='))
print("2 tub son ekanligini hamma biladi")
for i in range(3,n):
	t=True
	for j in range(2,i):
		if i%j==0:
			t=False
	if t==True:
		print(i,'tup son')
## MUKAMMAL SONNI TEKSHIRISH
n = int(input('n='))
s=0
for j in range(1,n):
	if n%j==0:
		s+=j
if s==n:
	print(n,'mukammal son')
else:
	print(n,"mukammal son emas")

#### n gacha  MUKAMMAL SONNI TEKSHIRISH
n = int(input('n='))
for i in range(1,n):
	s=0
	for j in range(1,i):
		if i%j==0:
			s+=j
	if s==i:
		print(i,'mukammal son')
"""
a=1
b=2
a,b=b,a
print(a,b)







