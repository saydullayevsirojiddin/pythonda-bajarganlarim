#Ixtiyoriy kivadrat tenglamani yechish
# a*x^2+b*x+c=0
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
D = b*b-4*a*c
if D == 0:
  x = -b/(2*a)
  print('x = ',x )
elif D > 0:
  x1 = (-b + pow(D,1/2))/(2*a)
  x2 = (-b - pow(D,1/2))/(2*a)
  print('x1 =',x1,
        'x2 =',x2)
elif D < 0:
  print('yechimga ega emas')
