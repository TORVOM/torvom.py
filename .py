emloqimport socket
#pip install time
#pip install socket
#pip insrall subprocess
print('verção: 0.0.4')

#>>>>>>>>>>>>>>> CORES #
norm = '\033[m'        #
cvermelho = '\033[31m' #
cazul = '\033[34m'     #
cverde = '\033[32m'    #
#=======================
def pesquisaGoogle():
        print(f'{cvermelho}caso não queira prencher\nnão coloque nada{cverde}')
        Pp = str(input(f'''palavra específica
que você quer encontrar
|
|___|>{norm}'''))
        print('')
        Ps = str(input(f'''{cverde}site especifico
que quer encontrar
|
|___|>{norm}'''))
        print('')
        Pa = str(input(f'''{cverde}quer que seja em
algum arquivo? se sim, qual?
pdf, txt?..
|
|___|>{norm}'''))
        print(f'''
{cverde}copie e cole no google o texto a baixo.

{cazul}"{Pp}" site:{Ps} filetype:{Pa}
{norm}
''')

def portaIp():
        site01 = str(input(f'''{cverde}informe o host
|
|___|>{norm}'''))
        ports = [21,22,23,88,443,80,8080,8090,7777,24,25]
        for port in ports:
                client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                reap = client.connect_ex((site01, port))
                if reap == 0:
                        print(f'{cverde}[+]{norm} {port} aberta\n')
                else:
                        print(f"{cvermelho}[-]{norm} {port} fechada\n")
client.close()



while True:
        resut01 = int(input(f'''{cverde}
[01] pesquisa avançada no google
{cvermelho}[02]{cverde} procurar portas ips
[03]
|
|___|>{norm}'''))
        if resut01 == 1:
                pesquisaGoogle()
        elif resut01 == 2:
                portaIp()
        else:
                print(f'{cvermelho}opção não e>
