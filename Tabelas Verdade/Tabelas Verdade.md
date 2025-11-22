# $$(A \land B \land C) \lor (B \land C \land D)$$
O paciente será atendido SE: (Tem agendamento **E** documentos OK **E** médico disponível) **OU** (Documentos OK **E** médico disponível **E** pagamentos em dia)
A = Agendamento
B = Documentos
**C** = Médico Disponível
D = Pagamentos em dia

| A   | B   | C   | D   | ( A ∧ B ∧ C ) ∨ ( B ∧ C ∧ D ) |
| --- | --- | --- | --- | ----------------------------- |
| 1   | 1   | 1   | 1   | 1                             |
| 1   | 1   | 1   | 0   | 1                             |
| 1   | 1   | 0   | 1   | 0                             |
| 1   | 0   | 1   | 1   | 0                             |
| 0   | 1   | 1   | 1   | 1                             |
| 0   | 0   | 0   | 1   | 0                             |
| 0   | 0   | 1   | 0   | 0                             |
| 0   | 1   | 0   | 0   | 0                             |
| 1   | 0   | 0   | 0   | 0                             |
| 0   | 0   | 0   | 0   | 0                             |
| 1   | 1   | 0   | 0   | 0                             |
| 0   | 0   | 1   | 1   | 0                             |
| 1   | 0   | 0   | 1   | 0                             |
| 0   | 1   | 1   | 0   | 0                             |
| 1   | 0   | 1   | 0   | 0                             |
| 0   | 1   | 0   | 1   | 0                             |

# $$C \land (B \lor D)$$
"O paciente será atendido SE: (Há médico disponível) **E** (Tem documentos **OU** pagamentos em dia)"
B = Documentos
C = Médico
D = Pagamento em dia

|C|B|D|C ∧ ( B ∨ D )|
|---|---|---|---|
|1|1|1|1|
|1|1|0|1|
|1|0|1|1|
|0|1|1|0|
|0|0|1|0|
|0|1|0|0|
|1|0|0|0|
|0|0|0|0|
