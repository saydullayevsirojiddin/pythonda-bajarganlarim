##12-d.py
"""
a=[2,3,5,7,2,8,7]
b=[]
for x in set(a):
	b.append(x)
print("b=",b)

a=[2,3,5,7,2,8,7]
print(set(a))

vil = ('andijon viloyat','qashqadaryo viloyat')
tuman = (("marxamat","asaka"),("koson","qarshi","nishon","g'uzor"))
for x in range(len(vil)):
	print(x+1,vil[x])
k=int(input("Viloyatingizni tanlang: "))
x_v=vil[k-1]
for i in range(len(tuman[k-1])):
	print(i+1,tuman[k-1][i])
n=int(input("Tumaningizni tanlang: "))
x_v=x_v+' '+tuman[k-1][n-1]
print("Siz",x_v,"da yashaysiz")
"""
fan = ('Matematika','Fizika','Kimyo','Informatika','ona tili')
sinf_5a = ("Aliyev G'ani","Valiyev Ali","B'riyev Avaz","Soliyev Vali")
sinf_5b = ("B'riyev G'ani","Valiyev Ali","Aliyev Avaz","Soliyev Vali")
sinf_5c = ("B'riyev G'ani","Valiyev Ali","Aliyev Avaz","Soliyev Vali")
sinflar = ['sinf_5a','sinf_5b','sinf_5c']
baxosi = ('3','4','5')

for i in range(len(fan)):
	print(f"{i+1}  {fan[i]}")
s=int(input("Fani tanlang: "))

for sinf in range(len(sinflar)):
	print(f"{sinf+1} => {sinflar[sinf]}")
a=int(input("Sinfni tanlang: "))
a_5_baho = []
for x in range(a):
	print(f"{x+1}  {sinf_5a[x]} fanidan ")
	a_5_baho.append(a)



