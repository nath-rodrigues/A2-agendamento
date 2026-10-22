from datetime import datetime
from horario import Horario
from sistema_reservas import SistemaReservas
from excecoes import (ErroDisciplinaDiferente, ErroHorarioCancelado, ErroHorarioLotado, ErroHorarioPassado, ErroLimiteSemanal, ErroReservaDuplicada)

AGORA = datetime(2026, 10, 19, 12, 0) #data fixa, igual a dos testes, pra sempre dar o mesmo resultado

def mostrar_horarios(lista):
    if len(lista) == 0: #se a lista veio vazia, avisa
        print("   nenhum horario livre")
    for h in lista: #percorre os horarios e mostra um por linha
        if h.individual:
            tipo = "individual"
        else:
            tipo = "grupo " + str(len(h.alunos)) + "/" + str(h.capacidade) #ex: grupo 1/3
        print("   " + h.disciplina + " - " + h.monitor + " - " + h.inicio.strftime("%d/%m %H:%M") + " - " + tipo)

def tentar_reservar(sistema, aluno, disciplina, horario):
    #tenta reservar e mostra se deu certo ou qual erro apareceu
    try:
        sistema.reservar(aluno, disciplina, horario, AGORA)
        print("   OK: " + aluno + " reservou " + disciplina + " " + horario.inicio.strftime("%d/%m %H:%M"))
    except (ErroDisciplinaDiferente, ErroHorarioCancelado, ErroHorarioLotado, ErroHorarioPassado, ErroLimiteSemanal, ErroReservaDuplicada) as erro:
        print("   ERRO (" + type(erro).__name__ + "): " + aluno + " -> " + str(erro))

def main():
    sistema = SistemaReservas()

    #cadastrando os horarios, como se o monitor tivesse feito isso
    calc1 = Horario("Calculo", "Julia", datetime(2026, 10, 21, 14, 0))
    calc2 = Horario("Calculo", "Julia", datetime(2026, 10, 22, 14, 0))
    calc3 = Horario("Calculo", "Julia", datetime(2026, 10, 23, 14, 0))
    calc_grupo = Horario("Calculo", "Julia", datetime(2026, 10, 24, 10, 0), False, 2) #em grupo, cabem 2
    calc_cancelado = Horario("Calculo", "Julia", datetime(2026, 10, 25, 10, 0))
    calc_cancelado.cancelado = True
    calc_passado = Horario("Calculo", "Julia", datetime(2026, 10, 18, 14, 0)) #antes do AGORA
    fisica = Horario("Fisica", "Joao", datetime(2026, 10, 21, 16, 0))

    for h in [calc1, calc2, calc3, calc_grupo, calc_cancelado, calc_passado, fisica]:
        sistema.cadastrar_horario(h)

    print("1) horarios livres de Calculo (cancelado e passado nao aparecem):")
    mostrar_horarios(sistema.listar_livres("Calculo", AGORA))

    print("\n2) reserva normal (tem que dar certo):")
    tentar_reservar(sistema, "Joana", "Calculo", calc1)

    print("\n3) horario individual que ja foi ocupado:")
    tentar_reservar(sistema, "Nathália", "Calculo", calc1)

    print("\n4) mesma aluna tentando o mesmo horario de novo:")
    tentar_reservar(sistema, "Joana", "Calculo", calc1)

    print("\n5) horario de outra disciplina:")
    tentar_reservar(sistema, "Joana", "Calculo", fisica)

    print("\n6) limite semmanal (a Joana ja tem 1, a segunda passa e a terceira nao):")
    tentar_reservar(sistema, "Joana", "Calculo", calc2)
    tentar_reservar(sistema, "Joana", "Calculo", calc3)

    print("\n7) horario em grupo com capacidade 2 (o terceiro aluno nao entra):")
    tentar_reservar(sistema, "Nathália", "Calculo", calc_grupo)
    tentar_reservar(sistema, "Caio", "Calculo", calc_grupo)
    tentar_reservar(sistema, "Davi", "Calculo", calc_grupo)

    print("\n8) horario cancelado e horario que ja passou:")
    tentar_reservar(sistema, "Nathália", "Calculo", calc_cancelado)
    tentar_reservar(sistema, "Nathália", "Calculo", calc_passado)

    print("\n9) horarios livres de Calculo no final:")
    mostrar_horarios(sistema.listar_livres("Calculo", AGORA))

if __name__ == "__main__":
    main()