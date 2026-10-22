# Sistema de Agendamento de Monitorias

Felipe Higashi - 2669986
Nathália Rodrigues - 2670097

## 2. Relatório de execução

### 2.1 Como executar

- **Python:** 3.13 ou superior.
- **Bibliotecas:** nenhuma externa (apenas `datetime` e `unittest`, da biblioteca padrão).
- **Arquivo principal:** `agendamento/codigo/main.py`.
- **Executar o sistema:** `cd agendamento/codigo` e depois `python main.py`.
- **Executar os testes:** `cd agendamento/codigo` e depois `python -m unittest -v test_reserva`.

### 2.2 Plano e execução

| Data | Planejado | Realizado | Quem |
|---|---|---|---|
| 16/10 | Análise e descrição | Feito em aula; Parte 1 enviada | Felipe e Nathália. |
| 17/10 | 5 histórias | Histórias 1 a 5 no repositório | Felipe (1, 2 e 3), Nathália (4, 5). |
| 18/10 | Projeto inicial | Registrado no repositório | Nathália. |
| 19/10 | Implementação, em conjunto | Dividida por arquivos: `Horario` e `Reserva`; `excecoes.py` e `SistemaReservas` | Nathália e Felipe. |
| 20/10 | Testes de aceitação | 10 testes, todos passando | Felipe. |
| 21/10 | Documentação e relatório | README, `main.py`, PDF | Nathália. |
| 22/10 | Autoavaliação e envio | **[PREENCHER]** | Felipe e Nathália. |

### 2.3 Atrasos e mudanças em relação ao projeto inicial

1. **Listagem de horários livres:** adicionado o método `listar_livres` ao `SistemaReservas`; o projeto inicial só especificava a reserva. A listagem é necessária para demonstrar o sistema e usa a mesma regra de horário livre da reserva.
2. **Parâmetro `agora`:** reservar e listar aceitam uma data de referência opcional, para testar horários que já passaram sem depender do relógio do computador.
3. **Arquivos:** o código ficou em `horario.py`, `reserva.py`, `sistema_reservas.py` e `excecoes.py`, para separar responsabilidades e evitar conflitos entre os dois integrantes.
4. **Exceções:** o projeto inicial dizia apenas "avisa com um erro"; foi criada uma exceção para cada regra, para que cada teste verifique exatamente a regra que falhou.
5. **Semana:** o limite de 2 reservas usa a semana ISO (segunda a domingo), que o projeto inicial não definia.
6. **`main.py`:** adicionado para demonstrar o sistema funcionando.

**Atrasos:** não houve atrasos em relação ao plano.