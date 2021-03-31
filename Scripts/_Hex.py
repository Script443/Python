from colorama import *
import codecs
import binascii

init()
Escolha = str(input(Fore.YELLOW + "INFORME 'C' PARA CODIFICAR E 'D' PARA DECODIFICAR: "))
if Escolha == "C" or Escolha == "c":
    msg = input(Fore.RESET + "\nMENSAGEM PARA CODIFICAR: ")
    code = binascii.hexlify(msg.encode())
    print(Fore.GREEN + "MENSAGEM CODIFICADA ESTA ENTRE AS ASPAS: ",code)
    
elif Escolha == "D" or Escolha == "d":
    msg = bytes.fromhex(input(Fore.RESET + "\nMENSAGEM PARA DECODIFICAR: ")).decode('utf-8')
    print(Fore.GREEN + "MENSAGEM DECODIFICADA: ",msg)
else:
    print(Fore.RED + "\n------------------------")
    print("$---COMANDO INVALIDO---$")
    print("------------------------")
print(Fore.RESET)
