from conta_corrente_classe import ContaCorrente
from conta_poupanca_classe import ContaPoupanca
from menu_classe import Menu
from time import sleep

if __name__ == "__main__":
    
    Menu.menu_intro()

    try:
        
        opcao_menu = (int(input('Digite: ')))
        
    except Exception as erro:
        print(f'(\033[31mApenas números inteiros!\033[m) {erro.__class__}')
            

    while True:
        if opcao_menu != 3:
            try:
                if opcao_menu == 1:
                    sleep(1)
                    print('[\033[32mCONTA CORRENTE\033[m]')
                    sleep(1)
                    cliente_corrente = ContaCorrente(id_conta="cliente1", saldo=0, limite=5000)
                    
                    while True:
                        try:
                            cliente_corrente.depositar(float(input('Valor do deposito R$: ')))
                            break
                        except ValueError as e:
                            print(str(e))
                    while True:
                        try:
                            cliente_corrente.sacar(float(input('Valor do saque R$:')))
                            break
                        except ValueError as e:
                            print(str(e))
                            
                    cliente_corrente.consulta_saldo_corrente()
                    sleep(1)
                    Menu.menu_intro()

                elif opcao_menu == 2:
                    sleep(1)
                    print('[\033[36mCONTA POUPANÇA\033[m]')
                    sleep(1)
                    cliente_poupanca = ContaPoupanca(id_conta="cliente1", saldo=0, taxa_rendimento=0.74)
                    
                    while True:
                        try:
                            cliente_poupanca.depositar(float(input('Valor do deposito R$: ')))
                            break
                        except ValueError as e:
                            print(str(e))
                    while True:
                        try:
                            cliente_poupanca.sacar(float(input('Valor do saque R$:')))
                            break
                        except ValueError as e:
                            print(str(e))
                            
                    cliente_poupanca.verificar_rendimento_ano()
                    sleep(1)
                    print()
                    Menu.menu_intro()
                    
            except Exception as erro:
                print(f'(\033[31mApenas números!\033[m) {erro.__class__}')               
            
            try:
                
                opcao_menu = (int(input('Digite: ')))
                
            except Exception as erro:
                print(f'(\033[31mApenas números inteiros!\033[m) {erro.__class__}')
                
            
        else:
            break
        
        
    print("Obrigado e volte sempre!")

