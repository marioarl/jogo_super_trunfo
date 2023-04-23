from colorama import Fore, init, Back
init(autoreset=True)

def inicio():
    print(Fore.BLUE + "*"*65)
    print(f"{Back.WHITE}{Fore.BLACK}{'*'} {'S U P E R  T R U N F O - T A N Q U E S  D E  G U E R R A':^61} {'*'}")
    print(Fore.BLUE + "*"*65)

def placar(a,b,c,d):
    print(f"{Fore.GREEN}{'P L A C A R':^61}")
    print(f"{'':>6}", f"{'_'}"*47)
    print(f"{Back.WHITE}{Fore.BLACK}{'JOGADOR:':>15} {len(a)} cartas    ||||  COMP:    {len(b)} cartas ")
    print(f"{Back.WHITE}{Fore.BLACK}{'BATALHA:':>15} {(c)}            ||||  BATALHA: {(d)}         ")
    print(f"{'':>6}", f"{'_'}"*47)


def menu():
    print("\n\n\t\tEscolha a categoria:\n\t\t[ 1 ] - Potencia\n\t\t"
                            "[ 2 ] - Velocidade\n\t\t"
                            "[ 3 ] - Alcance\n\t\t"
                            "[ 4 ] - Peso\n\t\t"
                            "[ 5 ] - Comprimento\n\t\t"
                            )

def menuPos(a):
    print("\n\n\t\tEscolha a categoria:\n\t\t[ 1 ] - Potencia\n\t\t"
                            "[ 2 ] - Velocidade\n\t\t"
                            "[ 3 ] - Alcance\n\t\t"
                            "[ 4 ] - Peso\n\t\t"
                            "[ 5 ] - Comprimento\n\n"
                            f"\t\t==> {a}")

def mCartaPre(a):
    print("\n")
    print(f"{'*'}"*10, f"{'SUA CARTA'}", f"{'*'}"*10 ,f"{'':>2}" , f"{'*'}"*9, f"{'COMPUTADOR'}", f"{'*'}"*9)
    print(f"{'*'}", f"{a['Pais']:^24}", f"\033[7;37;40m{a['ID']} *\033[m" ,f"{'':>2}" , f"*{'XXX':^28}*")
    print(f"* Modelo......: {a['Modelo']:<12}",f"{'*':>2}", f"{'':>2}" ,f"* Modelo......: {'XXXXXXX'}", f"{'*':>6}")
    print(f"* Potencia....: {a['Potencia']:>4}", f"{'KW':<9}*", f"{'':>2}" ,f"* Potencia....: {'XXXXX'} KW     *")
    print(f"* Velocidade..: {a['Velocidade']:>4}",f"{'Km/h':<9}*",f"{'':>2}" , f"* Velocidade..: {'XXXXX'} Km/h   *")
    print(f"* Alcance.....: {a['Alcance']:>4}", f"{'Km':<9}*",f"{'':>2}" ,f"* Alcance:....: {'XXXXX'} Km     *")
    print(f"* Peso........: {a['Peso']:>4}", f"{'t':<9}*", f"{'':>2}" ,f"* Peso........: {'XXXXX'} t      *")
    print(f"* Comprimento.: {a['Comprimento']:>4}", f"{'m':<9}*",f"{'':>2}" ,f"* Comprimento.: {'XXXXX'} m      *")
    print(f"{'*'}"*31, f"{'':>2}" ,f"{'*'}"*30)

def mCartaPos(a, b):
    print("\n")
    print(f"{'*'}"*10, f"{'SUA CARTA'}", f"{'*'}"*10 ,f"{'':>2}" , f"{'*'}"*9, f"{'COMPUTADOR'}", f"{'*'}"*9)
    print(f"{'*'}", f"{a['Pais']:^24}",f"\033[7;37;40m{a['ID']} *\033[m" , f"{'':>2}" , f"*{b['Pais']:^24}", f"\033[7;37;40m{b['ID']} *\033[m")
    print(f"* Modelo......: {a['Modelo']:<12}",f"{'*':>2}", f"{'':>2}" ,f"* Modelo......: {b['Modelo']:<12}", f"{'*':>1}")
    print(f"* Potencia....: {a['Potencia']:>4}", f"{'KW':<9}*", f"{'':>2}" ,f"* Potencia....: {b['Potencia']:>4}", f"{'KW':<8}*")
    print(f"* Velocidade..: {a['Velocidade']:>4}",f"{'Km/h':<9}*",f"{'':>2}" , f"* Velocidade..: {b['Velocidade']:>4}", f"{'Km/h':<8}*")
    print(f"* Alcance.....: {a['Alcance']:>4}", f"{'Km':<9}*",f"{'':>2}" ,f"* Alcance:....: {b['Alcance']:>4}", f"{'Km':<8}*")
    print(f"* Peso........: {a['Peso']:>4}", f"{'t':<9}*", f"{'':>2}" ,f"* Peso........: {b['Peso']:>4}", f"{'t':<8}*")
    print(f"* Comprimento.: {a['Comprimento']:>4}", f"{'m':<9}*",f"{'':>2}" ,f"* Comprimento.: {b['Comprimento']:>4}", f"{'m':<8}*")
    print(f"{'*'}"*31, f"{'':>2}" ,f"{'*'}"*30)

def jogVence(a,b):
    print(f"\n{'':>14}", f"{'*'}"*26)
    print(f"{'':>14}", f"*  {a['Modelo']:^21}", f"{'*'}")
    print(f"{'*':>16}", f"{'*':>24}")
    print(f"{'':>14}", f"* {b:^22}", f"{'*'}")
    print(f"{'':>14}", f"{'*'}"*26, f"\n\n")

def compVence(a,b):
    print(f"\n{'':>14}", f"{'*'}"*26)
    print(f"{'':>14}", f"*  {a['Modelo']:^21}", f"{'*'}")
    print(f"{'*':>16}", f"{'*':>24}")
    print(f"{'':>14}", f"* {b:^22}", f"{'*'}")
    print(f"{'':>14}", f"{'*'}"*26, f"\n\n")


def empate(a):
    print(f"\n{'':>14}", f"{'*'}"*26)
    print(f"{'*':>16}", f"{'*':>24}")
    print(f"{'*':>16}", f"{'*':>24}")
    print(f"{'':>14}", f"* {a:^22}", f"{'*'}")
    print(f"{'':>14}", f"{'*'}"*26, f"\n\n")


