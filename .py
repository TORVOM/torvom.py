#pip install time
#pip install socket
#pip install dnspython
#import dns.resolver <- talvez não precise!
import socket
from time import sleep
ve03 = 9
sleep(1.5)
#>>>>>>>>>>>>>>> CORES #
norm = '\033[m'        #
cvermelho = '\033[31m' #
cazul = '\033[34m'     #
cverde = '\033[32m'    #
sist = '\033[4;30;43m' #
#=======================
ve01 = 0
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> sistema #
er = '\n' + cvermelho +'comando errado/erro <01>' + norm + '\n'                           #
ser = '\n' + cvermelho + 'comando errado/erro <02>' + norm + '\n'                         #
#============================================
ve01 = 0
ve02 = 4
ve03 = 7
vercc = f'{sist}{ve01}.{ve02}.{ve03}{norm}'
print()
# opc 3 >
def travaChats():
        trvs = str(input(f'''{cvermelho}
=========≈≈=============================
ATENÇÃO: caso você aperte enter ou cole
o texto em algum chat o seu dispositivo
pode ser danificado. >{norm}não use para o mal{cvermelho}<
========================================
{cverde}
COPIE O TEXTO AZUL E COLE NO CHAT DO ALVO

>ENTER<{norm}'''))
        if trvs != 's' or trvs != 'S':
                print(f'''{cazul}
 ||**My:leia!>z҉҉҉҉ ؜؜؜؜҈҉҈҉؜؜؜؜҈҉҈҉؜؜؜؜҈҉҈҉؜؜؜؜҈҉҈҉؜؜؜؜҈҉҈҉؜؜؜؜҈҉҈҉؜؜؜؜҈҉҈҉؜؜؜؜҈҉҈҉؜؜؜؜҈҉҈҉؜؜؜؜҈҉҈҉؜؜؜؜҈҉҈҉؜؜؜؜҈҉҈҉؜؜؜؜҈҉҈҉؜؜؜؜҈҉҈҉؜؜؜؜҈҉҈҉؜؜؜؜҈҉҈҉؜؜؜؜҈҉҈҉؜؜؜؜҈҉҈҉؜؜؜؜҈҉҈҉؜؜؜؜҈҉҈҉؜؜؜؜҈҉҈҉؜؜؜؜҈҉҈҉؜؜؜؜҈҉҈҉؜؜؜؜҈҉҈҉؜؜؜؜҈҉҈҉؜؜؜؜҈҉҈҉؜؜؜؜҈҉҈҉؜؜؜؜҈҉҈҉؜؜؜؜҈҉҈҉؜؜؜؜҈҉҈҉؜؜؜؜҈҉҈҉؜؜؜؜҈҉҈҉؜؜؜؜҈҉҈҉؜؜؜؜҈҉҈҉**||
{norm}''')
        else:
                print('ok...\n')
# opc 4 >
def scannerIpHost():
        try:
                host02 = input(f'''{cverde}
scanner host>{norm} ''')
                ip = socket.gethostbyname(host02)
                print(f'\no ip do host {cverde}{host02}{norm} é {sist}{ip}{norm}')
        except:
                print(f'\n{cvermelho}esse host não existe{norm}')
                pass
# opc 1 >
def pesquisaGoogle():
        print(f'{cvermelho}caso não queira pre-encher\nalgo não coloque nada.{cverde}\n')
        input('entendi! >ENTER<\n')
        Pp = str(input(f'''{cverde}
palavra específica
que você quer encontrar.
|
|___|>{norm}'''))
        Ps = str(input(f'''{cverde}
site específico que
você quer encontrar.
|
|___|>{norm}'''))
        Pa = str(input(f'''{cverde}
tipo arqetip.
pdf, txt, ftp?..
|
|___|>{norm}'''))
        print(f'''
{cverde}copie e cole no google o texto a baixo.

{cazul}"{Pp}" site:{Ps} filetype:{Pa}
{norm}''')

# opc 2 >
def portaIp():
        hosts = str(input(f'''{cverde}
host>{norm}'''))
        ports = int(input(f'''{cverde}
porta>{norm}'''))
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
                code = client.connect_ex((hosts, ports))
                if code != 0:
                        print(f'\n{cvermelho}[-]{cazul} {ports} fechada{norm}\n')
                else:
                        print(f"\n{cverde}[+]{cazul} {ports} aberta{norm}\n")
                client.close()
        except:
                print(er)
# opc 5 >
def ferramentasInvestigacao():
        print(ser)
while True:
        resut01 = int(input(f'''{cverde}



inf.=========> TORVOM
| criador: ADM
| verção: {vercc}{cverde}
=========================================
| [01] pesquisa avançada no google      |
| [02] verificação de conecção (server) |
| [03] trava chat                       |
| [04] scanner ip host                  |
| [05] ferramentas de investigação      |
| [06] enceri  códigos                  |
=========================================
<(○-○)>


{cazul}*{norm} '''))
        try:
                if resut01 == 1:
                        pesquisaGoogle()
                elif resut01 == 2:
                        portaIp()
                elif resut01 == 3:
                        travaChats()
                elif resut01 == 4:
                        scannerIpHost()
                elif resut01 == 5:
                        ferramentasInvestigacao()
                else:
                        print(er)
        except:
                print(er)
                try:
                        print(ser)
                except:
                        pass
