#17-d.py
"""
from turtle import*
bob = Turtle()
bob.width(6)
bob.color('red')
bob.speed(0)
n=5
for x in range(75):
	bob.right(5)
	n += 5
	for x in ['red','blui','red','blui','red','blui']:
		bob.color(x)
		bob.forward(n)
		bob.left(120)

def yigindi(n):
    n=abs(n)
    if n>0:
        return n+yigindi(n-1)
    else:
        return 0
n=int(input("N="))
print(yigindi(n))


def ekub(a,b):
    if a!=b:
        if a>b:
            return ekub(a-b,b)
        else:
            return ekub(a,b-a)
    else:
        return a
def ekuk(a,b):
    return a*b/ekub(a,b)

a = int(input("a="))
b = int(input("b="))
print(ekub(a,b))
print(ekuk(a,b))


# 1^2+2^2+3^2+4^2+...+n^2
def kv_YIG(n):
    if n>0:
        return n**2+kv_YIG(n-1)
    else:
        return 0
n=int(input("N="))
print(kv_YIG(n))

# 1^1+2^2+3^3+4^4+...+n^n
def nkivay(n):
    if n>0:
        return n**n+nkivay(n-1)
    else:
        return 0
n=int(input("N="))
print(nkivay(n))
"""
##33-misol
a=[1,1]
n=int(input('n='))
b=a
print(b[1],end=',')
for i in range(2,n+1):
	b.append(a[i-1])
	a[i]=a[i-2]+a[i-1]
	print(b[i], end=',')










