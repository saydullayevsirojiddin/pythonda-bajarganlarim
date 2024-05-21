#min(import math

#print(math.ceil(8.9))
##################################
#2 xil vaqt kiritiladi
# time1 = soat1, minut1, sekunt1
# time2 = soat2, minut2, sekunt2
soat1 = int(input("1-soat: "))
minut1 = int(input("1-minut: "))
sekunt1 = int(input("1-sekunt: "))

soat2 = int(input("2-soat: "))
minut2 = int(input("2-minut: "))
sekunt2 = int(input("2-sekunt: "))

secund=(soat2-soat1)*3600+(minut2-minut1)*60+sekunt2-sekunt1

print('natija: {}' .format(secund)) 
#########################################
a=int(input('3 xonali son kiriting:  '))
a1=a//100        # 100 lar xonasi
a2=a%100//10     # 10 lar xonasi
a3=a%10          # 1 lar xonasi
s=a1+a2+a3
print("natija:  s=",s) 