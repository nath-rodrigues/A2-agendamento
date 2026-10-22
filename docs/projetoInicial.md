Sistema de Agendamento de Monitorias 

Alunos: Felipe Higashi e Nathália Rodrigues 

Projeto inicial:

história escolhida: 1- reserva de horário (prioridade alta).

"como aluno, eu quero reservar um horário livre de monitoria da disciplina que escolhi, para ser atendido sem precisar combinar por mensagem".


classes que vão implementar a história:

- Horario: representa um atendimento de 30 minutos. Guarda a disciplina, o monitor, a data e hora, se é individual ou em grupo, a capacidade, se foi cancelado e quem já reservou.

- Reserva: liga um aluno a um horário.

- SistemaReservas: guarda os horários e as reservas e faz a reserva do aluno, conferindo todas as regras da história. Se alguma regra não for cumprida, avisa c/ um erro.


teste que verifica cada critério de aceitação:

- o aluno só reserva um horário livre da disciplina escolhida: um teste em que o aluno escolhe uma disciplina e reserva um horário livre dela (sucesso) e outro em que o aluno escolhe uma disciplina e tenta reservar um horário que é de outra (falha);

- em horário individual, só cabe 1 reserva; em horário em grupo, só cabe até a capacidade definida pelo monitor: um teste em que um aluno reserva um horário individual e outro aluno tenta reservar o mesmo horário (falha na segunda), um enchendo o horário em grupo até a capacidade (sucesso) e outro passando da capacidade (falha);

- o aluno não pode ter mais de 2 reservas por semana na mesma disciplina: um teste c/ 2 reservas na semana (sucesso) e outro c/ a terceira (falha);

- o aluno não pode reservar o mesmo horário duas vezes: um teste reservando o mesmo horário duas vezes c/ o mesmo aluno (falha);

- horário cancelado ou de data que já passou não pode ser reservado: um teste c/ horário cancelado (falha) e outro c/ horário de data que já passou (falha).