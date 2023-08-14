import dns.resolver
import socket
#pip install time
#pip install socket
#pip insrall dnspython
print('verção: 0.2.1')

#>>>>>>>>>>>>>>> CORES #
norm = '\033[m'        #
cvermelho = '\033[31m' #
cazul = '\033[34m'     #
cverde = '\033[32m'    #
#=======================
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
[02] conecção de portas ips/hosts
[03] trava chat
[04] scanner host
|
|___|>{norm}'''))
        if resut01 == 1:
                pesquisaGoogle()
        elif resut01 == 2:
                portaIp()
        elif resut01 == 3:
                print(f'''{cvermelho}copie o texto azul
e cole no chat que deseja trava.
>>ATENÇÃO, VOCÊ PODE DANIFICAR
SEU APARELHO AO COLAR NO CHAT OU APERTAR
ENTER!<<!{norm} Aperte >ENTER< para obter
o trava chat.
''')
                it1 = input(f'''{cvermelho}
caso queira sair
digite "S"{norm}''')
                if it1 == 's' or it1 == 'S':
                        print('ok...')
                else:
                        print(f'''{cazul}
||**By:LEIA>z҉҉҉҉؜؜؜؜҈҉҈҉؜؜؜؜҈҉҈҉؜؜؜؜҈҉҈҉؜؜؜؜҈҉҈҉؜؜؜؜҈҉҈҉؜؜؜؜҈҉҈҉؜؜؜؜҈҉҈҉؜؜؜؜҈҉҈҉؜؜؜؜҈҉҈҉؜؜؜؜҈҉҈҉؜؜؜؜҈҉҈҉؜؜؜؜҈҉҈҉؜؜؜؜҈҉҈҉؜؜؜؜҈҉҈҉؜؜؜؜҈҉҈҉؜؜؜؜҈҉҈҉؜؜؜؜҈҉҈҉؜؜؜؜҈҉҈҉؜؜؜؜҈҉҈҉؜؜؜؜҈҉҈҉؜؜؜؜҈҉҈҉؜؜؜؜҈҉҈҉؜؜؜؜҈҉҈҉؜؜؜؜҈҉҈҉؜؜؜؜҈҉҈҉؜؜؜؜҈҉҈҉؜؜؜؜҈҉҈҉؜؜؜؜҈҉҈҉؜؜؜؜҈҉҈҉؜؜؜؜҈҉҈҉؜؜؜؜҈҉҈҉؜؜؜؜҈҉҈҉؜؜؜؜҈҉҈҉؜؜؜؜҈҉҈҉**||
{norm}''')
        elif resut01 == 4:
                scannerIpHost()
        else:
                print(f'{cvermelho}opção não existente{norm}')
