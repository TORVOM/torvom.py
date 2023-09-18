#pip install socket
import urllib.request
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
st = f'{cazul}>{norm} '
op = f'{cazul}*{norm} '
#============================================
ve01 = 0
ve02 = 6
ve03 = 2
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

# opc 7 >
def verCaminho():
        dmn = int(input(f"""{cverde}
[01] protocolo {cazul}HTTPS{cverde}
[02] protocolo {cazul}HTTP{norm}

{op}"""))
        if dmn == 1:
                dmn = "https://"
        elif dmn == 2:
                dmn = "http://"
        else:
                pass
        caminhos = ["","/register","/profile","/checkout","/help","/support","/contact","/about","/blog","/news","/products","/services","/faq","/privacy","/terms","/search","/gallery","/events","/forum","/downloads","/portfolio","/testimonials","/feedback","/videos","/contact-us","/pricing","/partners","/sitemap","/resources","/events-calendar","/shop","/newsroom ","/forum-topic","/newsletter","/reviews","/testimonial","/contact-info","/pricing-plans","/affiliate-program","/team","/events-registration","/media","/downloads","/subscribe","/case-studies","/features","/test-drive","/feedback-form","/user-guide","/partnership","/press-releases","/knowledge-base","/contact-information","/join-us","/become-a-partner","/video-gallery","/catalog","/bookings","/sponsorship","/research","/events-gallery","/testimonials-page","/request-demo","/customer-service","/meet-the-team","/company-info","/terms-of-use","/customer-feedback","/affiliate-registration","/partner-program","/events-schedule","/subscribe-newsletter","/press-room","/blog-post","/customer-support-center","/our-team","/product-catalog","/client-testimonials","/contact-details","/pricing-packages","/join-our-team","/partner-with-us","/video-library","/online-store","/news-articles","/forum-discussion","/privacy-policy","/customer-service-support","/how-it-works","/admin","/top","/pinel","/login","/users","/shopp","/itens"]

        viajante = str(input(f"""{cverde}
DIGITE O NOME DO SITE COM O DOMÍNIO
EXEMPLO: SITE.COM

{st}"""))

        for c in caminhos:
                try:
                        lupa = f"{dmn}{viajante}{c}"
                        caminhar = urllib.request.urlopen(lupa)
                        print(f"""{cverde}
[{cazul}+{cverde}] {c}
{dmn}{viajante}{c}
{norm}""")
                except:
                        print(f"""{cvermelho}
[{cazul}-{cvermelho}] {c}
{dmn}{viajante}{c}
{norm}""")

# opc 4 >
def scannerIpHost():
        try:
                host02 = input(f'''{cverde}
host{st}''')
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
{st}'''))
        Ps = str(input(f'''{cverde}
site específico que
você quer encontrar.
{st}'''))
        Pa = str(input(f'''{cverde}
tipo arqetip.
pdf, txt, ftp?..
{st}'''))
        print(f'''
{cverde}copie e cole no google o texto a baixo.

{cazul}"{Pp}" site:{Ps} filetype:{Pa}
{norm}''')

# opc 2 >
def portaIp():
        hosts = str(input(f'''{cverde}
host{st}'''))
        ports = int(input(f'''{cverde}
porta{st}'''))
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
# opc 6 >
def kkkkk():
        while True:
                print(" :) kkkkkkkkkk")
# opc 5 >
def ferramentasInvestigacao():
        try:
                seleP = int(input(f'''{cverde}
[01] FERRAMENTAS (pagas)
[02] FERRAMENTAS (grátis)

{op}'''))
                if seleP == 1:
                        print(f'''{cverde}
$ pago   >
[01] puchar dados
[02] dispositivos na rede global
[03] ''')
                        seleS = int(input(f'''
{op}'''))
                        if seleS == 1:
                                print(f'''{cazul}
===========================
| NOME: i-find
| SITE: https://i-find.org
===========================
{norm}''')
                        elif seleS == 2:
                                print(f'''{cazul}
======≈====================
| NOME: shodan
| SITE: https://shodan
===========================
{norm}''')
                        else:
                                print(er)
                elif seleP == 2:
                        print(f'''{cverde}
* grátis >
[01] informações de arquivos
[02] puchar nome
[03] rastrear
''')
                        seleT = int(input(st))
                        if seleT == 1:
                                print(f'''{cazul}
==========================
| NONE: EXIF.tools
| SITE: https://exif.tools
==========================
{norm}''')
                        elif seleT == 2:
                                print(f'''{cazul}
primeiro tente conseguir acesst
ao {cvermelho}gmail{cazul} ou ao
{cvermelho}número de telefone{cazul}, use
isso como chave PIX e talvez você consiga o
o nome dela.
{norm}''')
                        elif seleT == 3:
                                print(f'''{cazul}
use a engenharia social para faser com que
o alvo acesse um gmail e senha que você
saiba quais são.
depois que ele acessar abra o rastreador de
contas do google.

NOME: Encontra dispositivo
baxe na play stor.

depois fassa loguin como convidado usando
o gmail que você deu para o seu alvo,
o google vai rastrea para você.
{norm}''')
                else:
                        print(er)
        except:
                print(ser)
try:
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
| [06] inceri códigos                   |
| [07] procura caminho do site          |
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
                        elif resut01 == 6:
                                kkkkk()
                        elif resut01 == 7:
                                verCaminho()
                        else:
                                print(er)
                except:
                        print(er)
                        try:
                                print(ser)
                        except:
                                pass
except:
        print(er)