import hashlib
from colorama import *
init()
flag = 0
print(Fore.YELLOW + "INFORME O DIRETORIO DA WORDLIST COM DUAS BARRAS (EX: C://Diretorio//Diretorio//Arquivo)")
pass_hash = input(Fore.RESET + "ENTRE COM A HASH MD5: ")
wordlist = input("INFORME O CAMINHO DA SUA WORDLIST: ")
try:
    pass_file = open(wordlist, "r")
except:
    print("ARQUIVO NAO ENCONTRADO")
    quit()
for word in pass_file:
    enc_wrd = word.encode('utf-8')
    digest = hashlib.md5(enc_wrd.strip()).hexdigest()
    if digest == pass_hash:
        print(Fore.RESET + "\nSENHA ENCONTRADA")
        print(Fore.GREEN + "A SENHA ENCONTRADA FOI: " + word)
        flag = 1
        break
    if flag == 0:
        print(Fore.RED + "\nNÃO É ESTA SENHA")
print(Fore.RESET)
