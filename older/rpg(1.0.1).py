import requests
import sys
try:
    requests.head("https://www.google.com")
except requests.ConnectionError:
    i = input("Brak połączenia z internetem\n")
    sys.exit()
from colorama import init, Fore, Back, Style
import random
init()
maxhp = 25
hp = 25
money = 0
Lvl = 0
xp = 0
slots = 15
items = 0
eqamount = []
najedzenie = 100
najedzeniemax = 100
eq = []

cena=["chleb",8, "skóra",20, "śledź",11, "łosoś",15,"karp",13,"diament",1500, "pół złota rybka","-","złoto",200,"węgorz",25]

exptolvl = [20, 35, 60, 90, 140, 200, 250, 350, 500, 575, 675, 750, 850, 1000] #5495 xp suma
legendarny = ["diament", "pół złota rybka"]
niezwykły = ["złoto", "węgorz"]
pospolity = ["chleb", "skóra", "śledź", "łosoś", "karp"]

itemyzwedkowania = ["wędkowaniepospolite", "wędkowanieniezwykłe", "wędkowanielegendarne"]
ryby = ["śledź", "karp", "łosoś", "węgorz", "pół złota rybka"]

wędkowaniepospolite = ["chleb", "skóra"]
wędkowanieniezwykłe = ["złoto"]
wędkowanielegendarne = ["diament"]

wędkowanie = ["ryby", "itemyzwedkowania"]

przerwy="================================================================="
def sell(co,ile=1):
    global eqamount
    global money
    global cena
    global items
    if co in eq:
            items-=ile
            eqamount[eq.index(co)]-=ile
            money+=(cena[cena.index(co)+1])*ile
            printc(f"Sprzedano {co} * {ile} za {(cena[cena.index(co)+1])*ile}$", color=Fore.GREEN)
def give(co,ile=1):
    global items
    global slots
    global eq
    if items+ile<=slots or cena[cena.index(co)+1]=="-":
        items+=ile
        if co not in eq: 
            eq.append(co)
            eqamount.append(ile)
        elif co in eq:
            eqamount[eq.index(co)]+=ile
    else:
        printc("Masz pełny ekwipunek. ", color=Fore.RED)
        if co not in eq: 
            eq.append(co)
            eqamount.append(ile)
        elif co in eq:
            eqamount[eq.index(co)]+=ile
        sell(co,ile)
def printc(s, color=Fore.WHITE, brightness=Style.NORMAL):
    print(f"{brightness}{color}{s}{Style.RESET_ALL}")
def ak():
    global xp
    global Lvl
    global hp
    global maxhp
    global najedzenie
    global legendarny
    global niezwykły
    global pospolity
    global najedzeniemax
    global slots
    global items
    global money
    akcja = input("Akcja:\n")
    printc(przerwy+"\n")
    
    if akcja == "pomoc":
        printc("wędkowanie - idź połowić ryby(potrzebujesz wędki)\nekwipunek - otwórz plecak\nużyj <przedmiot> - używa przedmiot\nsprzedaj <przedmiot>- sprzedaje przedmiot po cenie bazowej")
    elif akcja == "wędkowanie":
        drop = random.choices(wędkowanie, weights=(75, 25), k=1)[0]
        najedzenie-=10
        if drop == "ryby":
            drop = random.choices(ryby, weights=(30, 30, 30, 17, 2), k=1)[0]
            if drop in legendarny:
                xp += 100
                printc(f"Wyłowiłeś 1 * {drop} i otrzymałeś 100 doświadczenia!(Teraz: {xp}/{exptolvl[Lvl]})", color=Fore.YELLOW)
                give(drop)
            elif drop in niezwykły:
                xp += 5
                printc(f"Wyłowiłeś 1 * {drop} i otrzymałeś 5 doświadczenia!(Teraz: {xp}/{exptolvl[Lvl]})", color=Fore.GREEN)
                give(drop)
            else:
                xp += 3
                printc(f"Wyłowiłeś 1 * {drop} i otrzymałeś 3 doświadczenia!(Teraz: {xp}/{exptolvl[Lvl]})")
                give(drop)
        elif drop == "itemyzwedkowania":
            drop = random.choices(itemyzwedkowania, weights=(78, 24, 6), k=1)[0]
            if drop == "wędkowaniepospolite":
                drop = random.choice(wędkowaniepospolite)
                xp += 3
                printc(f"Wyłowiłeś 1 * {drop} i otrzymałeś 3 doświadczenia!(Teraz: {xp}/{exptolvl[Lvl]})")
                give(drop)
            elif drop == "wędkowanieniezwykłe":
                drop = random.choice(wędkowanieniezwykłe)
                xp += 5
                printc(f"Wyłowiłeś 1 * {drop} i otrzymałeś 5 doświadczenia!(Teraz: {xp}/{exptolvl[Lvl]})", color=Fore.GREEN)
                give(drop)
            elif drop == "wędkowanielegendarne":
                drop = random.choice(wędkowanielegendarne)
                xp += 30
                printc(f"Wyłowiłeś 1 * {drop} i otrzymałeś 30 doświadczenia(Teraz: {xp}/{exptolvl[Lvl]})!", color=Fore.YELLOW)
                give(drop)
    elif akcja == "ekwipunek":
        if items/slots>0.8:
            printc(f"Przedmioty: ({items}/{slots})",color=Fore.RED)
        elif items/slots>0.6:
            printc(f"Przedmioty: ({items}/{slots})",color=Fore.YELLOW)
        else:
            printc(f"Przedmioty: ({items}/{slots})",color=Fore.GREEN)
        for _ in range(len(eq)):
            item = (eq[_]) + " * " + str((eqamount[_]))
            if (eq[_]) in legendarny:
                printc(item, color=Fore.YELLOW)
            elif (eq[_]) in niezwykły:
                printc(item, color=Fore.GREEN)
            else:
                printc(str(item))
    elif akcja[:4]=="użyj":
        inuse = akcja[+5:]
        if inuse in legendarny or inuse in niezwykły or inuse in pospolity:
            if inuse not in eq or eqamount[eq.index(inuse)]==0:
                printc(f"Nie masz tego przedmiotu!",color=Fore.RED)
            else:
                items-=1
                eqamount[eq.index(inuse)]-=1
                if inuse=="chleb":
                    najedzenie+=7
                    printc(f'Zjadłeś {inuse} i odzyskałeś 7 punktów głodu',color=Fore.GREEN)
                elif inuse=="karp":
                    najedzenie+=5
                    printc(f'Zjadłeś {inuse} i odzyskałeś 5 punktów głodu',color=Fore.GREEN)
                elif inuse=="łosoś":
                    najedzenie+=8
                    printc(f'Zjadłeś {inuse} i odzyskałeś 8 punktów głodu',color=Fore.GREEN)
                elif inuse=="śledź":
                    najedzenie+=10
                    printc(f'Zjadłeś {inuse} i odzyskałeś 10 punktów głodu',color=Fore.GREEN)
                else:
                    items+=1
                    eqamount[eq.index(inuse)]+=1
                    printc(f"Nie można użyć tego przedmiotu!",color=Fore.RED)
        else:
            printc(f"Nie ma takiego przedmiotu!", color=Fore.RED)
    elif akcja[:8]=="sprzedaj":
        inuse = akcja[+9:]
        if inuse in legendarny or inuse in niezwykły or inuse in pospolity:
            if not inuse in eq or eqamount[eq.index(inuse)]==0:
                printc(f"Nie masz tego przedmiotu!",color=Fore.RED)
            elif cena[cena.index(inuse)+1]=="-":
                printc(f"Nie można sprzedać tego przedmiotu!",color=Fore.RED)
            else:
                sell(inuse)
        else:
            printc(f"Nie ma takiego przedmiotu!", color=Fore.RED)
    elif akcja[:3]=="kup":
        inuse = akcja[+4:]
        if inuse in legendarny or inuse in niezwykły or inuse in pospolity:
            if cena[cena.index(inuse)+1]=="-":
                printc(f"Nie można kupić tego przedmiotu!",color=Fore.RED)
            elif items==slots:
                printc(f"Nie masz miejsca w ekwipunku!",color=Fore.RED)
            elif money<int(cena[cena.index(inuse)+1])*2:
                printc(f"Nie stać cię!",color=Fore.RED)
            else:
                give(inuse)
                money-=cena[cena.index(inuse)+1]*2
                printc(f"Kupiono {inuse} za {cena[cena.index(inuse)+1]*2}$", color=Fore.GREEN)
        else:
            printc(f"Nie ma takiego przedmiotu!", color=Fore.RED)
    else:
        printc(f'Nie ma takiej akcji. Wpisz "pomoc"',color=Fore.RED)
    while(xp>=exptolvl[Lvl]):
        xp-=exptolvl[Lvl]
        Lvl+=1
        printc(f"Awansowałeś na poziom {Lvl}!",color=Fore.CYAN)
        maxhp+=5
        slots+=1
        najedzeniemax+=10
    if najedzenie<0 and akcja=="wędkowanie":
        hp+=round(((najedzenie)/10))
        printc(f"Staciłeś {round(((abs(najedzenie))/10))} punktów hp z powodu głodu!(Teraz: {hp}/{maxhp})",color=Fore.RED)
    if hp<0:
        print("\033c", end='')
        a = input("Umarłeś!\n")
        sys.exit()
    printc("\n"+przerwy)
    ak()
ak()