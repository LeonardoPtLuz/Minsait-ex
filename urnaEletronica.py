class UrnaEletronica:
    def __init__(self):
        self.candidatos = [ {"nome_candidato": "Fulano1", "partido": "Partido1"},
                            {"nome_candidato": "Funalo2", "partido": "Partido2"} ]
    
        
    def exibe_candidatos(self):
        for candidato in self.candidatos:
            print(candidato.get("nome_candidato"))
            print(candidato.get("partido"))
            print('-' * 20)
            
    
    def adiciona_candidato(self, nome_candidato, partido):
        self.candidatos.append({"nome_candidato": nome_candidato, "partido": partido})   
        
        
    def remove_ultimo_candidato(self):
        self.candidatos.pop()
    
        
    def atualiza_candidato(self, idx, chave, valor):
        self.candidatos[idx][chave] = valor


urna = UrnaEletronica()

urna.adiciona_candidato('Fulano3', 'Partido3')

urna.exibe_candidatos()

urna.remove_ultimo_candidato()

urna.exibe_candidatos()

urna.atualiza_candidato(0, 'nome_candidato', 'Fulano4')
urna.atualiza_candidato(0, 'partido', 'Partido4')

urna.exibe_candidatos()