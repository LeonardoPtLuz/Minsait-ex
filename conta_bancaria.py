from time import sleep

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        
    
    def deposito(self, valor):
        if valor >= 1000:
            print('UAU TUDO ISSO?!')
            self.saldo += valor
        else:
            print('PASSA ESSA MERRECA PRA CÁ...')
            self.saldo += valor
        
        
    def saque(self, valor):
        if (valor <= self.saldo):
            self.saldo -= valor
        else:
            print('Saldo de saque não é suficiente!')
    
            
    def consultar_saldo(self):
        print(f'Saldo disponível: {self.saldo:.2f}')
        
        
class ContaEspecial(ContaBancaria):
    def bajular_cliente(self):
        print('O senhor gostaria de um cafezinho?')
        
        
cliente = ContaEspecial(titular='Cliente', saldo=0)

print('-' * 40)

cliente.deposito(float(input('Valor do deposito: ')))
sleep(1)
print()

cliente.saque(float(input('Valor do saque: ')))
print()
sleep(1)

cliente.consultar_saldo()
print()
sleep(1)

cliente.bajular_cliente()

print('-' * 40)