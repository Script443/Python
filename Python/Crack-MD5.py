import hashlib
from colorama import *
init()
flag = 0
print(Fore.YELLOW + "INFORME O DIRETORIO DA WORDLIST COM DUAS BARRAS (EX: C://Diretorio//Diretorio//Arquivo)")
pass_hash = input(Fore.RESET + "Entre com a hash md5: ")
wordlist = input("Informe o caminho da sua Wordlist: ")
try:
    pass_file = open(wordlist, "r")
except:
    print("Arquivo nao encontrado")
    quit()
for word in pass_file:
    enc_wrd = word.encode('utf-8')
    digest = hashlib.md5(enc_wrd.strip()).hexdigest()
    if digest == pass_hash:
        print(Fore.RESET + "\nSenha Encontrada")
        print(Fore.GREEN + "A SENHA ENCONTRADA FOI: " + word)
        flag = 1
        break
    if flag == 0:
        print(Fore.RED + "\nA senha nao foi encontrada dentre as opções da lista")
print(Fore.RESET)
