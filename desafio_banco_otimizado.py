# Desafio Sistema bancário Otimizado 
# Saque = deve receber os argumentos apenas por nome (Keyword only)
# Depósito = deve receber argumentos apenas por posição (Positional Only)
# Extrato = deve receber argumentos por posição e por nome (Positional only e Keyword only)
# Criar Usuário = deve armazenar o usuário em uma lista, um usuário é composto por: nome, data de nascimento
#cpf e endereço. Não podemos cadastrar usuários com o mesmo cpf

import textwrap


def menu():
    menu = """\n
    ===============Menu===============
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova Conta
    [lc]\tListar Contas
    [nu]\tNovo Usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))

def depositar(saldo, deposito, extrato, /): # apenas por posição
 
    if deposito < 0:
        print("impossível depositar um número negativo!")
    else:
        saldo += deposito
        extrato += f'Depósito: R$ {deposito:.2f}\n'
        print("\n Depósito realizado!")

    return saldo, extrato

def sacar(*, saldo, saque, extrato, limite, numero_saques, limite_saques): #apenas por nome

    excedeu_saldo = saque > saldo
    excedeu_limite = saque > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saques:
        print("limite de saques atingido")
    
    elif excedeu_limite:
        print(f"Impossivel sacar (maior que R$ 500)")
    
    elif excedeu_saldo:
        print(f"Impossível sacar, pois o saldo é de: R$ {saldo:.2f}")

    elif saque > 0:
        saldo -= saque
        numero_saques += 1
        extrato += f'Saque: R$ {saque:.2f}\n'
        print(f"Saque de R${saque:.2f} Realizado com Sucesso!")
    else:
        print("houve alguma falha na operação")
    
    return saldo, extrato
    

def exibir_extrato(saldo, /, *, extrato): # por posição e por nome
    print("\n----------EXTRATO----------")
    print("Não foram realizadas Movimentações" if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("---------------------------")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Já existe usuário com esse CPF")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuário criado com sucesso")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("usuário não encontrado, fluxo encerrado")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))



def main():

    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    saldo = 0
    limite = 500
    numero_saques = 0
    extrato = ""
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":

            deposito = float(input("Digite o valor para deposito: "))
            
            saldo, extrato = depositar(saldo, deposito, extrato)

        elif opcao == "s":

            saque = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar (
                saldo=saldo,
                saque=saque,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )
            
        elif opcao == "nu":
            criar_usuario(usuarios)
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)
        elif opcao == "lc":
            listar_contas(contas)
        elif opcao == "e":
           exibir_extrato(saldo, extrato = extrato)
        elif opcao == "q":
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada...")

            
main()