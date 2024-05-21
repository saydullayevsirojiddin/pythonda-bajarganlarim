from math import*
"""
x = float(input("x = "))
y = float(input("y = "))
z = float(input("z = "))

t = 2*cos(x-pi/6)/(0.5+pow(sin(y),2))*(1+z**2/(3-z**2/5))
print("javob: ",round(t,6))
"""

x = 5
y = 4.5
z = 0.5

a = pow(sin(x*y-pow(e,x)),2)/(1+x/y*2.05+0.001*pow(e,pow(x,2)))
b = sqrt(x**2-y**2)*log(z)+log(10,(y+z))/(sqrt(x**2-y**2)+1)
print("javob1: ",a)
print("javob2: ",b)