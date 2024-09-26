Explicação do Código

Classe ContaBancaria:

__init__: Inicializa a conta com um número, titular e saldo inicial (0).
depositar: Método para depositar um valor na conta.
sacar: Método para sacar um valor da conta, garantindo que o saldo não fique negativo.
verificar_saldo: Exibe o saldo atual da conta.
Classe Banco:

__init__: Inicializa o banco com um dicionário para armazenar contas.
criar_conta: Método para criar uma nova conta, verificando se o número da conta já existe.
obter_conta: Método para obter uma conta com base no número.
