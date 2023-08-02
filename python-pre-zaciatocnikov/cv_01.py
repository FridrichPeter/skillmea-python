import sys
import math
import random


#Úloha 1
max_float = sys.float_info.max
previous_float = max_float - 1

print(previous_float)
#1.7976931348623157e+308

#Úloha 2
a = 10
b = 14
c = math.sqrt(a**2 + b**2)
print(c)

cislo = int(input("Zadaj číslo bro: "))
last_three_num = cislo % 1000

print("Posledné tri cifry:", last_three_num)

#Úloha 3
def hod_kockou():
    return random.randint(1, 6)

vysledok = hod_kockou()
print(vysledok)

#Úloha 4
print("="*20)
meno = input("Zadajte svoje meno: ")
vek = input("Zadajte svoj vek: ")
adresa = input("Zadajte svoju adresu: ")
print("="*20)

print("meno:", meno)
print("vek:", vek)
print("adresa:", adresa)
