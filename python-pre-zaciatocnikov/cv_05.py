import random
import pyfiglet

def game():
    meno_hraca = input("Zadaj svoje meno kamarát: ")
    spravne = 0
    nespravne = 0
    pocet_tipov = 0

    # Popis MasterMind v figlet fonte
    ascii_art = pyfiglet.figlet_format("MasterMind", font="slant")
    print(ascii_art)

    while True:
        cislo = random.randint(1,10)
        print(f"{meno_hraca}, hádaj číslo od 1 do 10. Ak chceš skončiť, napíš 'KONIEC'. HAVE FUN!")


        while True:
            tip = input("Tvoj tip: ")
            pocet_tipov += 1

            if tip.upper() == 'KONIEC':
                print(f"Hra sa skončila. {meno_hraca}, tvoje štatistiky:")
                print(f"Počet správnych tipov: {spravne}")
                print(f"Počet nesprávnych tipov: {nespravne}")
                print(f"Celkový počet tipov: {pocet_tipov}")
                return

            try:
                tip = int(tip)
                if 1 <= tip <=10:
                    if tip == cislo:
                        spravne += 1
                        print(f"Uhádol si {meno_hraca}!")
                        break
                    else:
                        nespravne +=1
                        print("Zle, daj ešte!")
                else:
                    print("Zadaj číslo od 1 do 10.")
            except ValueError:
                print("Zadaj číslo, alebo 'KONIEC'.")

game()