from conta_classe import Conta


class ContaCorrente(Conta):
    def __init__(self, id_conta:Conta, saldo:Conta, limite):
        super().__init__(id_conta, saldo)
        self.limite = limite

    #Limite do deposito da conta corrente 5k dia.
    def depositar(self, valor):
        if (valor <= self.limite):
            self.saldo += valor

        else:
            raise ValueError('O valor do depósito diário máximo permito é de: R$5.000,00')


    def sacar(self, valor):
        if valor > 1000:
            raise ValueError('O valor máximo de saque diário perimitido é de: R$1.000,00')
    
        elif valor <= self.saldo:
            self.saldo -= valor

        else:
            raise ValueError('\033[31mSaldo insuficiente!\033[m')


    def consulta_saldo_corrente(self):
        print(f'Saldo disponível R$: {self.saldo:.2f}')
        


