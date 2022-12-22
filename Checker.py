import requests
import random
import string
import time

print("""Thzin Gen V1""")
time.sleep(2)
print("NITRO.CODES.txt/valid")
time.sleep(0.3)
print("Thzin Nitro Gen Checker")
time.sleep(0.2)
print("CARREGANDO...")
time.sleep(0.2)
print("50% CARREGADO")
time.sleep(0.8)
print("100% CARREGADO")
time.sleep(0.8)

num = int(input('Insira quantos códigos voce quer gerar e verifique: '))

with open("Nitro Codes.txt", "w", encoding='utf-8') as file:
    print("Seus códigos nitro estão sendo gerados, seja paciente se você digitou o número alto!")

    start = time.time()

    for i in range(num):
        code = "".join(random.choices(
            string.ascii_uppercase + string.digits + string.ascii_lowercase,
            k = 16
        ))

        file.write(f"https://discord.gift/{code}\n")

    print(f" quantidade de códigos gerados {num} | Tempo gasto: {time.time() - start}\n")

with open("Nitro Codes.txt") as file:
    for line in file.readlines():
        nitro = line.strip("\n")

        url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

        r = requests.get(url)

        if r.status_code == 200:
            print(f" Valido | {nitro} ")
            break
        else:
            print(f" Invalido | {nitro} ")

input("\nVocê gerou, agora pressione enter para fechar isso, você obterá códigos válidos em Valid Codes.txt se você vir vazio, então você não teve sorte, gere 20 milhões de códigos para sorte ou então.")
