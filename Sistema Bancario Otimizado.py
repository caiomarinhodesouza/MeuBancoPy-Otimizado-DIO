# Listas para armazenar os usuários e contas
usuarios = []
contas = []

# Variáveis globais para conta e operações bancárias
limite_saque_diario = 3
limite_valor_saque = 500

# Função para realizar um depósito
def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Valor inválido para depósito.")
    return saldo, extrato

# Função para realizar um saque (recebendo argumentos por nome)
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor > saldo:
        print("Saldo insuficiente para realizar o saque.")
    elif valor > limite:
        print(f"O valor máximo para saque é R$ {limite:.2f}.")
    elif numero_saques >= limite_saques:
        print("Limite de saques diários alcançado.")
    else:
        saldo -= valor
        extrato.append(f"Saque: R$ {valor:.2f}")
        numero_saques += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
    return saldo, extrato, numero_saques

# Função para exibir o extrato (usando argumentos por posição e nome)
def mostrar_extrato(saldo, *, extrato):
    print("\n=== Extrato ===")
    if not extrato:
        print("Nenhuma operação realizada.")
    else:
        for operacao in extrato:
            print(operacao)
    print(f"Saldo atual: R$ {saldo:.2f}")

# Função para cadastrar um usuário
def cadastrar_usuario(nome, data_nascimento, cpf, endereco):
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            print("Usuário já cadastrado.")
            return
    usuario = {
        'nome': nome,
        'data_nascimento': data_nascimento,
        'cpf': cpf,
        'endereco': endereco
    }
    usuarios.append(usuario)
    print("Usuário cadastrado com sucesso.")

# Função para cadastrar uma conta corrente
def criar_conta_corrente(cpf):
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            numero_conta = len(contas) + 1
            conta = {
                'agencia': "0001",
                'numero_conta': numero_conta,
                'usuario': usuario
            }
            contas.append(conta)
            print(f"Conta criada com sucesso. Agência: 0001, Conta: {numero_conta}")
            return
    print("Usuário não encontrado. Cadastro de conta falhou.")

# Função principal para o menu de operações
def menu():
    saldo = 0.0
    extrato = []
    saques_diarios = 0

    while True:
        print("\n=== Banco Python ===")
        print("1 - Depósito")
        print("2 - Saque")
        print("3 - Extrato")
        print("4 - Cadastrar Usuário")
        print("5 - Criar Conta Corrente")
        print("6 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            valor = float(input("Digite o valor para depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)
        elif opcao == "2":
            valor = float(input("Digite o valor para saque: "))
            saldo, extrato, saques_diarios = sacar(
                saldo=saldo, valor=valor, extrato=extrato,
                limite=limite_valor_saque, numero_saques=saques_diarios,
                limite_saques=limite_saque_diario
            )
        elif opcao == "3":
            mostrar_extrato(saldo, extrato=extrato)
        elif opcao == "4":
            nome = input("Nome: ")
            data_nascimento = input("Data de nascimento: ")
            cpf = input("CPF: ")
            endereco = input("Endereço: ")
            cadastrar_usuario(nome, data_nascimento, cpf, endereco)
        elif opcao == "5":
            cpf = input("Digite o CPF do usuário para vincular a conta: ")
            criar_conta_corrente(cpf)
        elif opcao == "6":
            break
        else:
            print("Opção inválida, tente novamente.")

# Iniciar o programa
menu()
