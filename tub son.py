# Ushbu metod sonning tub yoki tub emasligini aniqlaydi
def prime(n):
    b = True
    i = 2
    while i < n // 2:
        if n % i == 0:
            b = False
            break
        i += 1
    if b:
        print(str(n) + ' is prime')
    else:
        print(str(n) +' is not prime')