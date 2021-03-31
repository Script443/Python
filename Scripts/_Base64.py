import base64
from colorama import *

escolha = str(input(Fore.YELLOW + "INFORME 'C' PARA CODIFICAR OU 'D' PARA DECODIFICAR: "))
if escolha == "C" or escolha == "c":

    message = input(Fore.RESET + "\nMENSAGEM PARA CODIFICAR: ")
    message_bytes = message.encode()
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode()
    print(Fore.GREEN + "MENSAGEM CODIFICADA: ", base64_message)

elif escolha == "D" or escolha == "d":
    
    base64_message = input(Fore.RESET + '\nMENSAGEM PARA DECODIFICAR: ')
    base64_bytes = base64_message.encode()
    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode()
    print(Fore.GREEN + "MENSAGEM DECODIFICADA: ", message)
    
else:
    
    print(Fore.RED + "\n------------------------")
    print("$---COMANDO INVALIDO---$")
    print("------------------------")
print(Fore.RESET)
