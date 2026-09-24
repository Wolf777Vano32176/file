from rich.console import Console
console = Console(force_terminal=True)
import random
bonys = 0
posithion = 0
posithion2 = 0
while True:
    a = console.input("  [bold #66FF00]чи хочете ви кинути кубик[/bold #66FF00]")
    if a == "yes1" or a == "так1":
        number = random.randint(1, 6)
        print (f"на кубику випало {number} число")
        posithion += number
        if posithion==14 or posithion==47 or posithion==55 or posithion==58 or posithion==72:
            lovushka = random.randint(1, 10)
            posithion -=lovushka
            console.print(F" [bold #B22222]ви попали в ловушку ви вераєтесь на {lovushka} назад[/bold #B22222]")
        if posithion == 27 or posithion2 == 46 or posithion == 59 or posithion == 76 or posithion == 84:
            bonys = 4
            posithion += bonys
            console.print(F" [bold #FFFF00]ви попали в бонус на {bonys} в перед[/bold #FFFF00]")
        print (f"зелений гравець знаходиться на {posithion} позиції")
    if posithion >= 100:
        print ("зелений гравець виграв")
        break
    b = console.input("  [bold #000080]чи хочете ви кинути кубик[/bold #000080]")
    if b ==  "yes2" or b == "так2":
        number = random.randint(1, 6)
        print(f"на кубику випало {number} число")
        posithion2 += number
        print(f"синій гравець знаходиться на {posithion2} позиції")
        if posithion2 >= 100:
            print("синій гравець виграв")#FFFF00#B22222
            break
        if posithion2 == 14 or posithion2 == 47 or posithion ==55 or posithion2 == 58 or posithion2 == 72:
            lovushka = random.randint(1, 10)
            print(f"на кубику випало {number} число")
            posithion2 -= lovushka
            console.print(F" [bold #B22222]ви попали в ловушку ви вераєтесь на {lovushka} назад[/bold #B22222]")
        if posithion2 == 27 or posithion2 == 46 or posithion2 == 59 or posithion2 == 76 or posithion2 == 84:
            bonys = 4
            console.print(F" [bold #B22222]ви попали в бонус на {bonys} в перед[/bold #B22222]")
            posithion2 += bonys
            console.print(f"ви попали в бонус тепер ви на {posithion2} кліточці")
