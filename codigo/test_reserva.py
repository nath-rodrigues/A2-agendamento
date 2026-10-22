import unittest
from datetime import datetime
from horario import Horario
from sistema_reservas import SistemaReservas
from excecoes import (ErroDisciplinaDiferente, ErroHorarioCancelado, ErroHorarioLotado, ErroHorarioPassado, ErroLimiteSemanal, ErroReservaDuplicada)

AGORA = datetime(2026, 10, 19, 12, 0) #data fixa, representa o momento "atual" dos testes

class TesteReserva(unittest.TestCase):
    def setUp(self): #o setUp roda antes de cada teste e cria um sistema novo e vazio para evitar interferencia
        self.sistema = SistemaReservas()

    #criterio 1: so reserva horario livre da disciplina escolhida
    def test_reserva_horario_livre_da_disciplina(self):
        h = Horario("Calculo", "Maria", datetime(2026, 10, 21, 14, 0)) #cria o horario do dia 21/10 (14:00)
        self.sistema.reservar("Ana", "Calculo", h, AGORA) #a ana reserva esse horario de calculo considerando que agora é AGORA (19/10 12:00)
        self.assertIn("Ana", h.alunos) #confere se Ana esta na lista h.alunos. se estiver, o teste continua, se nao, falha

    def test_reserva_horario_de_outra_disciplina_falha(self):
        h = Horario("Fisica", "Maria", datetime(2026, 10, 21, 14, 0))
        with self.assertRaises(ErroDisciplinaDiferente): #significa “o que estiver dentro deste bloco precisa lançar esse erro”. se lançar, o teste passa. se nao lançar nada, ou lançar outro erro, o teste falha
            self.sistema.reservar("Ana", "Calculo", h, AGORA)
        self.assertNotIn("Ana", h.alunos) #confere que a Ana nao foi adicionada

    #critério 2: individual e grupo
    def test_individual_segundo_aluno_falha(self):
        h = Horario("Calculo", "Maria", datetime(2026, 10, 21, 14, 0)) #horario individual
        self.sistema.reservar("Ana", "Calculo", h, AGORA) #ana ocupa a unica vaga
        with self.assertRaises(ErroHorarioLotado): #bia tenta o mesmo horario e deve receber o erro
            self.sistema.reservar("Bia", "Calculo", h, AGORA)

    def test_grupo_aceita_ate_a_capacidade(self):
        h = Horario("Calculo", "Maria", datetime(2026, 10, 21, 14, 0), False, 3) #horario em grupo
        self.sistema.reservar("Ana", "Calculo", h, AGORA)
        self.sistema.reservar("Bia", "Calculo", h, AGORA)
        self.sistema.reservar("Caio", "Calculo", h, AGORA) #tres alunos reservam
        self.assertEqual(len(h.alunos), 3) #confere que o tamanho da lista de alunos é igual a 3

    def test_grupo_alem_da_capacidade_falha(self):
        h = Horario("Calculo", "Maria", datetime(2026, 10, 21, 14, 0), False, 3)
        self.sistema.reservar("Ana", "Calculo", h, AGORA)
        self.sistema.reservar("Bia", "Calculo", h, AGORA)
        self.sistema.reservar("Caio", "Calculo", h, AGORA)
        with self.assertRaises(ErroHorarioLotado): #o quarto aluno davi deve receber o erro
            self.sistema.reservar("Davi", "Calculo", h, AGORA)

    #critério 3: limite semanal
    def test_duas_reservas_na_semana_funcionam(self):
        h1 = Horario("Calculo", "Maria", datetime(2026, 10, 21, 14, 0))
        h2 = Horario("Calculo", "Maria", datetime(2026, 10, 22, 14, 0))
        self.sistema.reservar("Ana", "Calculo", h1, AGORA)
        self.sistema.reservar("Ana", "Calculo", h2, AGORA)
        self.assertIn("Ana", h1.alunos)
        self.assertIn("Ana", h2.alunos)

    def test_terceira_reserva_na_semana_falha(self):
        h1 = Horario("Calculo", "Maria", datetime(2026, 10, 21, 14, 0))
        h2 = Horario("Calculo", "Maria", datetime(2026, 10, 22, 14, 0))
        h3 = Horario("Calculo", "Maria", datetime(2026, 10, 23, 14, 0))
        self.sistema.reservar("Ana", "Calculo", h1, AGORA)
        self.sistema.reservar("Ana", "Calculo", h2, AGORA)
        with self.assertRaises(ErroLimiteSemanal): #terceira reserva deve lançar o erro
            self.sistema.reservar("Ana", "Calculo", h3, AGORA)

    #critério 4: mesmo horário duas vezes
    def test_reserva_duplicada_falha(self):
        h = Horario("Calculo", "Maria", datetime(2026, 10, 21, 14, 0), False, 3)
        self.sistema.reservar("Ana", "Calculo", h, AGORA)
        with self.assertRaises(ErroReservaDuplicada): #ana tenta de novo o mesmo horario e recebe o erro
            self.sistema.reservar("Ana", "Calculo", h, AGORA)

    #critério 5: cancelado ou passado
    def test_horario_cancelado_falha(self):
        h = Horario("Calculo", "Maria", datetime(2026, 10, 21, 14, 0))
        h.cancelado = True
        with self.assertRaises(ErroHorarioCancelado): #deve lançar o erro de horario cancelado
            self.sistema.reservar("Ana", "Calculo", h, AGORA)

    def test_horario_passado_falha(self):
        h = Horario("Calculo", "Maria", datetime(2026, 10, 18, 14, 0)) #horario em 18/10 que é antes de AGORA (19/10)
        with self.assertRaises(ErroHorarioPassado): #deve lançar o erro de horario passado
            self.sistema.reservar("Ana", "Calculo", h, AGORA)

if __name__ == "__main__":
    unittest.main()