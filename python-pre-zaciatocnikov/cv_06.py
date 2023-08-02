#ÚLOHA 1

cisla = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
nove_cisla = [cislo for cislo in cisla if cislo % 2 == 0]
print(nove_cisla)

#Výsledok printu úlohy 1
#[4, 16, 36, 64, 100]

#ÚLOHA 2

cisla = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
nove_cisla = [int(cislo) for cislo in cisla if cislo > 0]
print(nove_cisla)

#Výsledok printu úlohy 2
#[34, 44, 68, 44, 12]


#ÚLOHA 3

veta = "the quick brown fox jumps over the lazy dog"
slova = veta.split()
print(slova)
slova_dlzka = [len(slovo) for slovo in slova if slovo != "the"]
print(slova_dlzka)

#Výsledok printu úlohy 3
#[5, 5, 3, 5, 4, 4, 3, 4]