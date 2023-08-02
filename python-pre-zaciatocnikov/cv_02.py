#import------

#------import



#Úloha 1
dice = "+-------+\n| {0}     |\n|   {1}   |\n|     {2} |\n+-------+"

vstup_1 = "o"
vstup_2 = " "
vstup_3 = "o"

vystup = dice.format(vstup_1, vstup_2, vstup_3)
print(vystup)

#Úloha 2
cislo = int(input("Daj sem daku cifru, už aj: "))
bin_cislo = format(cislo, '032b')
print(bin_cislo)

#input = 9
#bin = 00000000000000000000000001100011

#Úloha 3
width = int(input("Zadajte šírku zarovnania: "))

print("{:{width}} {:{width}} {:{width}} {:{width}}".format(
    "Dec", "Bin", "Okt", "Hex", width=width
))
for i in range(16):
    print("{:{width}d} {:{width}b} {:{width}o} {:{width}x}".format(
        i, i, i, i, width=width
    ))
