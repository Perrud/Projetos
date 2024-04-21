saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

usuários = {}

def AdicionarUsuário(nome, saldo = 0, limite = 500, extrato = "", numero_saques = 0, LIMITE_SAQUES = 3):
    usuários[nome] = [saldo, limite, extrato, numero_saques, LIMITE_SAQUES]

def Depósito(usuário, valor):
    usuários[usuário][0] += valor

def Saque(usuário, valor):
    if usuários[usuário][0] < valor:
        print("Impossível sacar, apenas R${:.2f} na conta".format(usuários[usuário][0]))
    elif usuários[usuário][1] < valor:
        print("Impossível sacar, limite de R${:.2f}".format(usuários[usuário][1]))
    elif usuários[usuário][3] <= 0: #aqui está errado preciso configurar para considerar os saques realizados e comparar com o limite disponível
        print("Impossível sacar, limites de saques atingidos")
    else:
        usuários[usuário][0] -= valor
        usuários[usuário][0] #colocar para tirar do limite
        usuários[usuário][2] = "\nSaque de R${:.2f}".format(valor, usuários[usuário][0])
        print("Saque de R${:.2f} realizado. Resta R${:.2f} na conta".format(valor, usuários[usuário][0]))

def Extrato(usuário):
    print("-- Extrato --")
    print(usuários[usuário][2])

while True:
    print("""Opções:
          (a) Criar conta
          (b) Depósito
          (c) Saque
          (d) Extrato
""")
    a = input("Insira a função desejada >")
    if a == 'a':
        AdicionarUsuário(input("Nome> "))
    elif a == "b":
        Depósito(input("Usuário> "), input("Valor> "))
    elif a == "c":
        Saque(input("Usuário> "), input("Valor> "))
    elif a == "d":
        Extrato(input("Usuário> "))
    elif a == "q":
        break