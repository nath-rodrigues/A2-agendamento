from datetime import datetime #traz a classe de data/hora
from excecoes import (ErroDisciplinaDiferente, ErroHorarioCancelado, ErroHorarioLotado, ErroHorarioPassado, ErroLimiteSemanal, ErroReservaDuplicada)
from reserva import Reserva

LIMITE_SEMANAL = 2

class SistemaReservas:
    def __init__(self):
        self.horarios = []
        self.reservas = []

    def cadastrar_horario(self, horario):
        self.horarios.append(horario) #recebe um Horario e adiciona na lista

    def listar_livres(self, disciplina, agora=None):
        if agora is None:
            agora = datetime.now() #se nao veio data, usa a data e hora reais
        livres = [] #lista vazia para guardar o resultado
        for h in self.horarios: #percorre cada horario
            if h.disciplina == disciplina and h.horario_livre(agora): #so entra se for da disciplina pedida e estiver livre
                livres.append(h) #guarda o horario que passou
        return livres #devolve a lista

    def reservas_na_semana(self, aluno, disciplina, data):
        semana = data.isocalendar()[:2] #devolve o par(ano, numero da semana). duas datas na semana tem o mesmo par
        total = 0 #contador
        for r in self.reservas: #percorre todas as reservas ja feitas
            mesma_semana = r.horario.inicio.isocalendar()[:2] == semana #compara a semana daquela reserva com a mesma procurada, e guarda true ou false
            if (r.aluno == aluno and r.horario.disciplina == disciplina and mesma_semana): #conta só se for do mesmo aluno, disciplina e semana
                total += 1
        return total

    def reservar(self, aluno, disciplina, horario, agora=None): #recebe o aluno, a disciplina escolhida e o horario
        if agora is None:
            agora = datetime.now()

        if horario.disciplina != disciplina:
            raise ErroDisciplinaDiferente("Horario nao e da disciplina escolhida")
        if horario.cancelado:
            raise ErroHorarioCancelado("Horario cancelado")
        if horario.inicio <= agora:
            raise ErroHorarioPassado("Horario ja passou")
        if aluno in horario.alunos:
            raise ErroReservaDuplicada("Aluno ja reservou este horario")
        if horario.lotado():
            raise ErroHorarioLotado("Horario lotado")
        if self.reservas_na_semana(aluno, disciplina, horario.inicio) >= LIMITE_SEMANAL:
            raise ErroLimiteSemanal("Limite semanal atingido")

        horario.alunos.append(aluno) #so chega aqui se nenhuma regra falhou, registra o aluno no horario
        reserva = Reserva(aluno, horario) #cria o objeto que liga os dois
        self.reservas.append(reserva) #guarda no sistema, para o limite semanal funcionar
        return reserva #devolve a reserva criada
