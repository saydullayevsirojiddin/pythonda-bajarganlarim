fan = ('Ona tili', 'Matematika', 'Fizika', 'Kimyo')
a_5 = ('Kamolova F.', 'Shokirov J.', 'Vahobov B.')
b_5 = ('Sobirova D.', 'Boborajabov G.', 'Shirinov F.')
for i in range(len(fan)):
    print(i + 1, fan[i])
tanlov_fan = int(input('fan tartib raqamini tanlang:'))
print('Siz', fan[tanlov_fan - 1], 'fanini tanladingiz, endi 5-A sinf oquvchilariga shu fan boyicha baho qoyib chiqing:')
a_5_baho = []
for i in range(len(a_5)):
    print(a_5[i], 'ga', fan[tanlov_fan - 1], 'fanidan ', end='')
    b = int(input('baho: '))
    a_5_baho.append(b)
for i in range(len(a_5)):
    print(a_5[i], ' - ', a_5_baho[i])
print('Endi esa, 5-B sinf uchun qaytadan:')

for i in range(len(fan)):
    print(i + 1, fan[i])
tanlov_fan = int(input('fan tartib raqamini tanlang:'))
print('Siz', fan[tanlov_fan - 1], 'fanini tanladingiz, endi 5-B sinf oquvchilariga shu fan boyicha baho qoyib chiqing:')
b_5_baho = []
for i in range(len(b_5)):
    print(b_5[i], 'ga', fan[tanlov_fan - 1], 'fanidan ', end='')
    b = int(input('baho: '))
    b_5_baho.append(b)
for i in range(len(b_5)):
    print(b_5[i], ' - ', b_5_baho[i])