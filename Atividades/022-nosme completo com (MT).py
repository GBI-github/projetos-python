print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 22\033[0m \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'MANIPULAÇÃO DE TEXTO' :^32}\033[0m")
print(f"{'ORDEM DE APRESENTAÇÃO':^32}")
print(f"\033[4;37m{'-' * 32}\033[0m")
nome = str(input("Informe seu nome: ")).strip()
nome1 = nome.split()
print(f"Nome: {nome.upper()} \n"
      f"Nome: {nome.lower()}")
print(f"Total de Letras: {len(nome) - nome.count(' ')}")
print(f"1º nome: {len(nome1[0])} letras")
