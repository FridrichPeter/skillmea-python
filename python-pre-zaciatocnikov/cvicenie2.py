# Úloha 2
# opäť budeme pracovať so simulátorom kocky, ale v tomto prípade použijeme
# grafickú plochu na vykreslenie výsledku.

import tkinter
import random

canvas_width = 640
canvas_height = 480
canvas = tkinter.Canvas(width=canvas_width, height=canvas_height)
canvas.pack()

number = random.randint(1,6)

print("Na kocke padlo číslo {}".format(number))
print("Vykreslujem kocku...")

# skús iné veľkosti kocky, všetky ostatné výpočty sa prispôsobia
size = 300

# center of dice
x, y = canvas_width / 2, canvas_height / 2
unit = size / 5
radius = size*0.03

# Použi polygon ako obrys kocky. "radius" použijeme na vypočítanie zoseknutia
#
#    p2___p3
# p1/       \p4
#   |       |
#   |       |
# p8\_______/p5
#   p7    p6
#
 
p1 = x - size / 2,  y-size / 2 + radius
p2 = x - size / 2 + radius, y - size / 2
p3 = x + size / 2 - radius, y - size / 2
p4 = x + size / 2,  y-size / 2 + radius
p5 = x + size / 2,  y+size / 2 - radius
p6 = x + size / 2 - radius, y + size / 2
p7 = x - size / 2 + radius, y + size / 2
p8 = x - size / 2,  y+size / 2 - radius

canvas.create_polygon(p1, p2, p3, p4, p5, p6, p7, p8,
                      outline="black", fill="gray", width=3)

# Tu si vypočítame všetky súradnice bodiek dopredu.
# Skús prečítať tento kód a pochopiť ako funguje. Do svojho riešenia skús
# v skratke opísať akým spôsobom sa počítajú všetky body.
# 
# nápoveda:
#
#        a a a
#        1 2 3
#      +-------+
#   b1 | 1   2 |
#   b2 | 3 4 5 |
#   b3 | 6   7 |
#      +-------+
#

a1 = x - 1.5*unit
a2 = x
a3 = x + 1.5*unit

b1 = y - 1.5*unit
b2 = y
b3 = y + 1.5*unit

x1, y1 = a1, b1
x2, y2 = a3, b1
x3, y3 = a1, b2
x4, y4 = a2, b2
x5, y5 = a3, b2
x6, y6 = a1, b3
x7, y7 = a3, b3

####### tvoj opis #######
#
# Sem zadaj opis riešenia ako sa
# počítajú jednotlivé bodky na kocke
#
########## end ##########

# Kreslenie bodiek!
# tu začína úloha na logické podmienky. Cieľom je aby si použil(a) na
# vykreslenie každej bodky na kocke len jedno volanie "canvas.create_oval(...)"
# To znamená, že spolu tu bude iba 7 volaní "create_oval"
# Trik spočíva v tom, že musíš sledovať pri ktorých číslach sa vykreslí ktorá
# bodka. Napríklad stredná bodka sa vykresluje len keď padne 1, 3 alebo 5.
# Nevieš súradnice bodky? Použi (x1, y1) ako stred kružnice a "unit" ako
# PRIEMER kružnice ( priemer = 2*polomer ). Takýmto spôsobom sme vykreslovali
# kružnice v lekcí s grafikou.
#
# Nápoveda: riešenie spolu obsahuje 4 volania "if ..." a 7 volaní "create_oval"
# To je 11 riadkov kódu...


######## riešenie zapíš sem ########


############### end ################

canvas.mainloop()

