from conta_classe import Conta


class ContaPoupanca(Conta):
    def __init__(self, id_conta:Conta, saldo:Conta, taxa_rendimento):
        super().__init__(id_conta, saldo)
        self.taxa_rendiemnto = taxa_rendimento
        
        
    def depositar(self, valor):
        self.saldo += valor

    
    #Limite do saque da poupança é de no máximo 5k diário.    
    def sacar(self, valor):
        if valor > 5000:
            raise ValueError('O valor máximo de saque diário permitido é de: R$5.000,00')        
            
        elif valor <= self.saldo:
            self.saldo -= valor
            
        else:
            raise ValueError('\033[31mSaldo insuficiente!\033[m')
            
        
    def consulta_saldo_poupanca(self):
        print(f'Saldo disponível R$: {self.saldo:.2f}')
            
            
    def verificar_rendimento_ano(self):
        # Valor inicial aplicado
        valor_inicial = self.saldo
        
        # Atualmente a poupança está rendendo 0,5% ao mês + taxa referencial = 0,74% mês
        """
        https://www.remessaonline.com.br/blog/rendimento-da-poupanca-saiba-quanto-rende-de-juros-hoje/#:~:text=Em%20mar%C3%A7o%20de%202023%2C%20a,0%2C74%25%20ao%20m%C3%AAs.
        """
        #self.taxa_rendiemnto = 0.74

        # Transformando a porcentagem em valor numérico
        self.taxa_rendiemnto = self.taxa_rendiemnto / 100

        # Tempo de investimento
        meses = int(input('Meses que vai deixar rendendo: '))

        valor_final = valor_inicial * (1+self.taxa_rendiemnto)**meses

        print(f'Valor apos {meses} meses: R${valor_final:.2f}')
            