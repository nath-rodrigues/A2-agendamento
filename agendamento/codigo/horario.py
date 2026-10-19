MINUTOS_MONITORIA = 30;

class Horario:
    def __init__(self, disciplina, monitor, inicio, individual = True, capacidade = 1):
        if not individual and capacidade < 2:
            raise ValueError("capacidade minima precisa ser de 2")    
        self.disciplina = disciplina
        self.monitor = monitor # *usado pra fins de organizaçao
        self.inicio = inicio # data e hora que começa
        self.individual = individual
        self.capacidade = capacidade if not individual else 1 # individiual sempre tem capacidade 1
        self.cancelado = False # começa sem ta cancelado
        self.alunos = [] # ja foi reservado

    def lotado (self):
        return len(self.alunos) >= self.capacidade 
    def horario_livre(self, agora):
        return not self.cancelado and self.inicio > agora and not self.lotado()
    # se horario nao for cancelado, se nao aconteceu e aidna tem vaga, retorna True