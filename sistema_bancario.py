class ContaBancaria:
    def __init__(self, numero_conta, titular):
        self.numero_conta = numero_conta
        self.titular = titular
        self.saldo = 0.0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f'Depósito de R${valor:.2f} realizado com sucesso! Novo saldo: R${self.saldo:.2f}')
        else:
            print('Valor de depósito deve ser positivo.')

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f'Saque de R${valor:.2f} realizado com sucesso! Novo saldo: R${self.saldo:.2f}')
        else:
            print('Saque inválido. Verifique o valor e seu saldo.')

    def verificar_saldo(self):
        print(f'Saldo atual: R${self.saldo:.2f}')


class Banco:
    def __init__(self):
        self.contas = {}

    def criar_conta(self, numero_conta, titular):
        if numero_conta not in self.contas:
            conta = ContaBancaria(numero_conta, titular)
            self.contas[numero_conta] = conta
            print(f'Conta criada com sucesso! Número da conta: {numero_conta}, Titular: {titular}')
        else:
            print('Número da conta já existe.')

    def obter_conta(self, numero_conta):
        return self.contas.get(numero_conta, None)


# Exemplo de uso
banco = Banco()
banco.criar_conta('1234', 'João Silva')

conta = banco.obter_conta('1234')
conta.depositar(500)
conta.sacar(200)
conta.verificar_saldo()
