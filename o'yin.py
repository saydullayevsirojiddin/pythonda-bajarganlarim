"""
1 dan 10 gacha sonni toping.
3 urinishingiz bor.
"""
from random import randint
son1 = randint(1, 10)
print('Men 1 - 10 oraliqdan bir son o`yladim, sizda 3 ta urinish bor')
n = 0
while n < 3:
    sonim = int(input('Shu sonni topib ko`ringchi... :'))
    n += 1
    if son1 == sonim:
        print('Qoyil, Barakalla, topdingiz')
        break
    elif son1 == 0:
        break
    elif son1 > sonim:
        print('Mening sonim kattaroq')
        print('Yana uriningchi...')
    else:
        print('Mening sonim kichikroq')
        print('Yana uriningchi...')
