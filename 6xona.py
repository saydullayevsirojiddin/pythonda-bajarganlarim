### 123456

a = int (input("6 xonali son yozing: "))
a1=a%10     # 1 lar xonasi
a2=a%100//10   # 10 lar xonasi
a3=a%1000//100  #100 lar xonasi
a4=a%10000//1000
a5=a//10000%10
a6=a//100000

s1=a1+a2+a3
s2=a4+a5+a6
if s1==s2:
	print(f"{a}bu son to'gri keladi")
else:
	print(f"{a}bu son r'g'ri kelmaydi")