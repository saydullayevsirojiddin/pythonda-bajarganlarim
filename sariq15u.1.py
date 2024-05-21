menu = ''' Bizning menu:
 Osh
 Sho'rva
 Tovuq
 Salat
 Xonim
 Qozonkabob
 Moshkichira
 Mastova
 Tefteli
 Dimlama'''
print(menu)
meals = {"OSH":34000,"SHO'RVA":12000,"TOVUQ":20000,"SALAT":10000,"XONIM":15000,"QOZONKABOB":34000,"MOSHKICHIRA":22000,"MASTOVA":35000,"TEFTELI":16000,"DIMLAMA":18000}
food1 = input().upper()
food2 = input().upper()
food3 = input().upper()
list = [food1,food2,food3]
summ = 0
for i in list:
 if i not in meals:
  print(i,": bizda bunday taom yo'q. :(")
 else:
  print(i,":",meals[i])
  summ += meals[i]
print("Jami :",summ)