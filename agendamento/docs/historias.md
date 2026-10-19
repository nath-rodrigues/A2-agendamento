Sistema de Agendamento de Monitorias

Histórias de usuário:

1- reserva de horario:

historia: "como aluno, eu quero reservar um horário livre de monitoria da disciplina que escolhi, para ser atendido sem precisar combinar por mensagem".

critérios de aceitação:
- o aluno só reserva um horário livre da disciplina escolhida;
- em horário individual, só cabe 1 reserva; em horário em grupo, só cabe até a capacidade definida pelo monitor;
- o aluno não pode ter mais de 2 reservas por semana na mesma disciplina;
- o aluno não pode reservar o mesmo horário duas vezes;
- horário cancelado ou de data que já passou não pode ser reservado.

prioridade: alta. é o núcleo do pedido e resolve o problema do monitor com três alunos no mesmo horário e outros sem ninguém.

trecho e-mail: “A ideia é que o aluno escolha a disciplina, veja os horários livres e reserve um atendimento.” Para o limite semanal, “Talvez dois?”.


2- cadastro de horários

historia: "como monitor, eu quero cadastrar os horários em que posso atender, indicando se são individuais ou em grupo, para que os alunos possam reservá-los".

critérios de aceitação:
- cada horário cadastrado tem 30 minutos de duração;
- o monitor só cadastra horários da disciplina em que ele é monitor;
- em horário em grupo, o monitor define a capacidade (mínimo 2);
- o monitor não pode cadastrar dois horários que se sobreponham, nem em data que já passou.

prioridade: alta. sem horários cadastrados não há o que reservar, então a história 1 depende dela.

trecho e-mail: “cada monitor informa os horários em que pode atender” e “Cada atendimento dura 30 minutos, mas alguns monitores preferem atender em grupo”.


3- consulta de horários livres

história: "como aluno, eu quero ver os horários livres de uma disciplina, para escolher rapidamente um atendimento que caiba na minha rotina".

critérios de aceitação:
- ao escolher uma disciplina, aparecem só os horários dela;
- horários lotados, cancelados ou já passados não aparecem;
- os horários aparecem ordenados por data e hora;
- se não houver horário livre, o sistema informa isso.

prioridade: média. ajuda o aluno a decidir, mas a reserva em si já funciona se o aluno souber o horário. fica como história separada, porque a listagem é só consulta e a reserva é que aplica as regras.

trecho e-mail: “O sistema precisa ser fácil e rápido, senão os alunos vão continuar mandando mensagem.”


4- cancelamento de horário pelo monitor:

história: "como monitor, eu quero cancelar um horário que cadastrei p/ que os alunos recebam um aviso antes de irem até à monitoria."

critérios de aceitação:
- monitor cancela horários que ele mesmo cadastrou;
- depois de cancelar, os horários não aparecem livres mais;
- aluno que reservou o horário recebe um aviso c/ disciplina, data e hora;
- não é possível cancelar horário de uma data que já passou.

prioridade: média. resolve a reclamação dos alunos sobre os cancelamentos, mas depende primeiro se a reserva vai funcionar (fora do protótipo).

trecho e-mail: "às vezes precisa cancelar por causa de prova. Os alunos reclamam que só descobrem o cancelamento quando chegam na sala."


5- relatório de horas dos monitores:

história: "como coordenador, eu quero receber um relatório mensal com todas as horas trabalhadas por cada monitor, p/ calcular o pagamento da bolsa."

critérios de aceitação:
- relatório lista os monitores e as horas de cada um naquele mês;
- apenas os atendimentos realizados estarão no relatório;
- acesso apenas à coordenação;
- mês sem atendimentos não registram horas.

prioridade: baixa. é de bom proveito p/ coordenação, mas depende também, se as reservas e atendimentos existirem (no email nao fala se precisa resolver tudo isso de uma vez só). 

trecho e-mail: "A coordenação precisa de um relatório mensal com as horas atendidas por cada monitor, porque isso conta para o pagamento da bolsa. Essas informações de bolsa não podem ficar visíveis para todo mundo."