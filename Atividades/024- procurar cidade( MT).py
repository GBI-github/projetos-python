print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 24\033[0m \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'MANIPULAÇÃO DE TEXTO' :^32}\033[0m")
print(f"{'PROCURAR CIDADE':^32}")
print(f"\033[4;37m{'-' * 32}\033[0m")
cidade = str(input("Nome da sua cidade: ")).upper()
print(cidade[:5] == 'SANTO')
