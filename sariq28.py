# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 09:32:40 2021

@author: sirojiddin
"""

class Talaba:
    def __init__(self,ismi, familiya, t_yil, ot_nomi, fakultet, n_kurs):
        self.ismi = ismi
        self.familiya = familiya
        self.t_yil = t_yil
        self.ot_nomi = ot_nomi
        self.fakultet = fakultet
        self.n_kurs = n_kurs
    
    def get_name(self):
        return self.ismi
        
    def tanishtir(self):
        return (f"Men {self.ismi} {self.familiya}, {self.t_yil} yilda tug'ulganman.",
              f"{self.ot_nomi} {self.fakultet} fakultetida {self.n_kurs}-kursda o'qiyman.")
        
talaba1 = Talaba("Ali", "Valiye", "2000", "UzMU", "Matematika", "2")
talaba2 = Talaba("Hasan", "Aliyev", "1998", "QDU", "Chet tili", "3")
talaba3 = Talaba("Sirojiddin", "Saydullayev", "1995", "TATU", "KI", "1")

print(talaba1.get_name())
print(talaba2.get_name())
print(talaba3.get_name())

print(talaba1.tanishtir())
print(talaba2.tanishtir())
print(talaba3.tanishtir())
