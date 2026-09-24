from rich.console import Console
console = Console(force_terminal=True)
import random

a = random.randint(1,10)
sproba = 3
points = 0
pidcaska = 0
while True:
    guess = int(input("random_number:"))
    if guess == a:
        console.print (f"[bold green][/bold green][bold #FFA800 ]you win [/bold #FFA800]")
        a = random.randint(1, 10)
        console.print(
            "[bold green][/bold green]   [bold #6A7DB0][/bold #6A7DB0]")
        sproba += 2
        console.print("  [bold #33FF00]рівень пройдено добавлені дві жизні[/bold #33FF00]" +"\n"+

            f"[bold green][/bold green][bold #FFA800 ]тепер у вас {sproba} жизнів[/bold #FFA800]")
        points += sproba * 100
        print (points)
        if points > 250:
            answer = console.input ("  [bold #33FF00] чи хочете ви купити додаткову спробу?[/bold #33FF00]")
            if answer == "yes" or answer == "так":
                sproba += 1
                print ("у вас ",sproba, "спроб","та" )
                points -= 250
                print ("у вас ", points,"очків")

    else:
        sproba -= 1
        console.print(f"[bold #33FF00]you lose,у вас залишилось{sproba},спроб [/bold #33FF00]")
        print("you lose,у вас залишилось ",sproba,"спроб")
        if sproba==0:
            console.print("  [bold #66FF00][/bold #66FF00]")
            print("відповідь була",a)
        b = console.input("  [bold #66FF00]чи хочете ви купити підсказку[/bold #66FF00]")
        if b == "yes" or b == "так":
            pidcaska += 0
            console.print(f"[bold #33FF00]правильна відповідь між проміжком{a-1,a+2 } [/bold #33FF00]")



