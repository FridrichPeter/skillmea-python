## Úloha 1
import tkinter

canvas = tkinter.Canvas(width=640, height=480)
canvas.pack()

# Získanie veľkosti kruhu od používateľa
velkost_kruhu = int(input("Zadajte veľkosť kruhu: "))

# Výpočet súradníc stredného kruhu
stred_x = 320
stred_y = 240

# Vykreslenie stredného kruhu
canvas.create_oval(stred_x - velkost_kruhu, stred_y - velkost_kruhu, stred_x + velkost_kruhu, stred_y + velkost_kruhu)

# Výpočet a vykreslenie ďalších kruhov
for i in range(1, 5):
    polomer = velkost_kruhu * i

    # Kruhy s rovnakým stredom, ale rôznym polomerom
    #canvas.create_oval(stred_x - polomer, stred_y - polomer, stred_x + polomer, stred_y + polomer)
    #canvas.create_oval(stred_x - polomer, stred_y - polomer, stred_x + polomer, stred_y + polomer)

    # Kruhy so stredom posunutým od stredného kruhu
    canvas.create_oval(stred_x - polomer, stred_y - polomer * 2, stred_x + polomer, stred_y + polomer * 2)
    canvas.create_oval(stred_x - polomer, stred_y - polomer * 2, stred_x + polomer, stred_y + polomer * 2)

# Zobrazenie výsledného obrázka
canvas.mainloop()




## Úloha 2
#
# Nakresli olympíjske kruhy. Opýtaj sa používateľa na polomer kruhov a na
# súradnice prvého kruhu. pomocou výpočtov potom zisti súradnice všetkých
# ostatných kruhov. Všimni si, že kruhy sa na X-ovej osi nedotýkajú. Je tam
# istý offset. Offset nastav ako 2% z veľkosti polomeru.


####################


polomer = int(input("Zadajte polomer kruhov: "))


x1 = int(input("Zadajte x-ovú súradnicu prvého kruhu: "))
y1 = int(input("Zadajte y-ovú súradnicu prvého kruhu: "))


offset = 0.02 * polomer
x2 = x1 + polomer * 3 + offset
y2 = y1
x3 = x1 + polomer * 6 + offset * 2
y3 = y1
x4 = x1 + polomer * 1.5 + offset * 0.5
y4 = y1 + polomer * 1.5
x5 = x1 + polomer * 4.5 + offset * 1.5
y5 = y1 + polomer * 1.5

# Vykreslenie olympijských kruhov
canvas.create_oval(x1 - polomer, y1 - polomer, x1 + polomer, y1 + polomer, width=6, outline="blue")
canvas.create_oval(x2 - polomer, y2 - polomer, x2 + polomer, y2 + polomer, width=6, outline="black")
canvas.create_oval(x3 - polomer, y3 - polomer, x3 + polomer, y3 + polomer, width=6, outline="red")
canvas.create_oval(x4 - polomer, y4 - polomer, x4 + polomer, y4 + polomer, width=6, outline="yellow")
canvas.create_oval(x5 - polomer, y5 - polomer, x5 + polomer, y5 + polomer, width=6, outline="green")


canvas.mainloop()


