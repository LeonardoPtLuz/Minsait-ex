import random

class SerVivo:
    def __init__(self, vida, ataque):
        self.vida = vida
        self.ataque = ataque
        

class Personagem(SerVivo):
    def __init__(self, vida, ataque, nome):
        super().__init__(vida, ataque)
        self.nome = nome
        

class Monstro(SerVivo):
    def __init__(self, vida, ataque, tipo):
        super().__init__(vida, ataque)
        self.tipo = tipo

        
class Lobo(Monstro):
    def __init__(self, vida, ataque, tipo, forca):
        super().__init__(vida, ataque, tipo)
        self.forca = forca
        
    def atacar(self, dano_causado, dano_recebido):
        personagem.vida -= dano_causado
        monstro_lobo.vida -= dano_recebido
    
    
class Goblin(Monstro):
    def __init__(self, vida, ataque, tipo, inteligencia):
        super().__init__(vida, ataque, tipo)
        self.inteligencia = inteligencia
        
    def atacar(self, dano_causado, dano_recebido):
        personagem.vida -= dano_causado
        monstro_goblin.vida -= dano_recebido
        

print('-' * 40)

personagem = Personagem(nome='Herói', vida=50, ataque="1d8")
print(f'Personagem: {personagem.nome} | Vida: {personagem.vida} | Ataque: {personagem.ataque}')

monstro_lobo = Lobo(vida=30, ataque="1d6", tipo='Lobo', forca=0)
print(f'Monstro: {monstro_lobo.tipo} | Vida: {monstro_lobo.vida} | Ataque: {monstro_lobo.ataque}')

monstro_goblin = Goblin(vida=10, ataque="1d6", tipo='Goblin', inteligencia=0)
print(f'Monstro: {monstro_goblin.tipo} | Vida: {monstro_goblin.vida} | Ataque: {monstro_goblin.ataque}')

print('-' * 40)


atk_acao = str(input('Deseja Iniciar? [S/N]: '))

while atk_acao not in 'Nn':
    personagem_atk_lobo = random.randint(1, 8)
    personagem_atk_goblin = random.randint(1, 8)
    lobo_atk = random.randint(1, 6)
    goblin_atk = random.randint(1, 6)

    if personagem.vida > 0:
        
        print()
        print('-'*15, 'START', '-'*15)

        print(f'Vida do personagem: {personagem.vida}')
        
        if (monstro_lobo.vida <= 0) and (monstro_goblin.vida <= 0):
            print('Ambos inimigos foram derrotados!')
            break
        
        if monstro_lobo.vida <= 0:
            print(f'O inimigo {monstro_lobo.tipo} foi derrotado!')
        else:
            print(f'Vida do Lobo: {monstro_lobo.vida}')
            monstro_lobo.atacar(dano_causado=lobo_atk, dano_recebido=personagem_atk_lobo)
    
        if monstro_goblin.vida <= 0:
            print(f'O inimigo {monstro_goblin.tipo} foi derrotado!')   
        else:
            print(f'Vida do Goblin: {monstro_goblin.vida}')
            monstro_goblin.atacar(dano_causado=goblin_atk, dano_recebido=personagem_atk_goblin)
        
            
        print('-'*30)
            
        atk_acao = str(input('Deseja Atacar? [S/N]: '))
        
        print()
        
    else:
        print(f'O {personagem.nome} foi derrotado!')
        print('-'*30)
        break       
    
        


