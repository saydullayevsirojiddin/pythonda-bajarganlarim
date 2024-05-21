a = int(input("sekuntni kiriting: a = "))

a1=a//3600    # soati
a2=a%3600//60    #minuti
a3=a%60      #sekundi kelib chiqadi

print(a1, end=" soat ")
print(a2, end=" min ")
print(a3, end=" sekund")
