from colorama import *
import codecs

choice = str(input(Fore.YELLOW + "INFORME 'C' PARA CODIFICAR E 'D' PARA DECODIFICAR: "))
if choice == "C" or choice == "c":
    message = input(Fore.RESET + "\nMENSAGEM PARA CODIFICAR: ")
    enc = codecs.getencoder("rot-13")
    os = enc(message)[0]
    print(Fore.GREEN + 'MENSAGEM CODIFICADA: ', os)
elif choice == "D" or choice == "d":
    cleartxt = input(Fore.RESET + "\nMENSAGEM PARA DECODIFICAR: ")
    enc = codecs.getdecoder("rot-13")
    secret = enc(cleartxt)[0]
    print(Fore.GREEN + "MENSAGEM DECODIFICADA: ", secret)
else:
    print(Fore.RED + "\n------------------------")
    print("$---COMANDO INVALIDO---$")
    print("------------------------")
print(Fore.RESET)
