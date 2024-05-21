"""
22	Uch xonali son berilgan. Uning raqamlari o`suvchi yoki kamayuvchi 
ketma-ketlik tashkil etishi  rostlikka tekshirilsin.
"""
x = int(input("3 xonali son kiriting: "))
a = x//100
b = x%100//10
c = x%10
print((a<b<c)^(a>b>c))