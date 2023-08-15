import dns.resolver
import socket
from time import sleep
#pip install time
#pip install socket
#pip install dnspython
sleep(1)
#>>>>>>>>>>>>>>> CORES #
norm = '\033[m'        #
cvermelho = '\033[31m' #
cazul = '\033[34m'     #
cverde = '\033[32m'    #
sist = '\033[m'        #
#=======================
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> sistema #
er = '\n' + cvermelho +'comando errado/erro' + norm + '\n'                         #
#============================================
vp1 = 0
vp2 = 3
vp3 = 8
vpg = vp1 + '.' + vp2 + '.' + vp3
print(vpg)
def travaChats():
        trv = input(f'''{cvermelho}
=========≈≈=============================
ATENÇÃO: caso você aperte enter ou cole
o texto em algum chat o seu dispositivo
pode ser danificado. >não use para o mal<
{cvermelho}
========================================
{cverde}caso não queira o trava
chat digite "S"
se quiser aperte >ENTER<
COPIE O TEXTO AZUL E COLE NO CHAT DO ALVO
|
|___>{norm}''')
        if trv != 's' or trv != 'S':
                print(f'''{cazul}
>^<
{norm}''')
        else:
                try:
                        print('ok...\n')
                except:
                        print(er)
def scannerIpHost():
        try:
                host02 = input(f'''{cverde}
scanner host>{norm} ''')
                ip = socket.gethostbyname(host02)
                print(f'\no ip do host {cverde}{host02}{norm} é {cazul}{ip}')
        except:
                print(f'\n{cvermelho}esse host não existe{norm}')
                pass
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
você quer encontrar.                                                                                                                                                             |
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

def portaIp():
        hosts = str(input(f'''{cverde}
host>{norm}'''))
        ports = int(input(f'''{cverde}
porta>{norm}'''))
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        code = client.connect_ex((hosts, ports))
        if code != 0:
                print(f'\n{cvermelho}[-]{cazul} {ports} fechada{norm}\n')
        else:
                print(f"\n{cverde}[+]{cazul} {ports} aberta{norm}\n")
        client.close()



while True:
        resut01 = int(input(f'''{cverde}

=========================================
[01] pesquisa avançada no google
[02] verificação de conecção (server)
[03] trava chat
[04] scanner ip host
|
|___|>{norm}'''))
        if resut01 == 1:
                pesquisaGoogle()
        elif resut01 == 2:
                portaIp()
        elif resut01 == 3:
                travaChats()
        elif resut01 == 4:
                scannerIpHost()
        else:
                try:
                        print(er)
                except:
                        print(er)
