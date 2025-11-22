ALGORITMO Processo_Atendimento_Fila
VAR
    FILA_PACIENTES : LISTA DE REGISTRO // Simulação da Fila (Estrutura FIFO)
    paciente_atendido : REGISTRO
    nome, cpf : CARACTER
    i : INTEIRO
    
INÍCIO
    // ----------------------------------------------------
    // DECLARAÇÃO DO REGISTRO/ESTRUTURA DO PACIENTE
    // ----------------------------------------------------
    // Defina a estrutura de dados (Registro)
    REGISTRO PACIENTE:
        Nome : CARACTER
        CPF : CARACTER
    FIM_REGISTRO

    // Inicializa a Fila
    FILA_PACIENTES := CRIAR_LISTA()

    // ----------------------------------------------------
    // 1. INSERIR 3 PACIENTES NA FILA (OPERAÇÃO ENFILEIRA)
    // ----------------------------------------------------
    ESCREVA "--- INSERÇÃO NA FILA ---"
    
    PARA i DE 1 ATÉ 3 FAÇA
        ESCREVA "Digite o nome do paciente ", i, ":"
        LEIA nome
        ESCREVA "Digite o CPF do paciente ", i, ":"
        LEIA cpf
        
        // Cria um novo registro de paciente
        NOVO_PACIENTE := NOVO PACIENTE(Nome: nome, CPF: cpf)
        
        // Adiciona ao final da Fila (ENFILEIRA / ADICIONAR_FIM)
        ADICIONAR_FIM(FILA_PACIENTES, NOVO_PACIENTE) 
        ESCREVA "Paciente ", NOVO_PACIENTE.Nome, " adicionado à fila."
    FIM_PARA
    
    // ----------------------------------------------------
    // 2. REMOVER O PRIMEIRO PACIENTE PARA ATENDIMENTO (OPERAÇÃO DESENFILEIRA)
    // ----------------------------------------------------
    ESCREVA "\n--- ATENDIMENTO (DESENFILEIRAR) ---"
    
    SE TAMANHO(FILA_PACIENTES) > 0 ENTÃO
        // Remove o paciente da frente da fila (o que entrou primeiro)
        paciente_atendido := REMOVER_INICIO(FILA_PACIENTES) 
        
        ESCREVA "Paciente ", paciente_atendido.Nome, " (CPF: ", paciente_atendido.CPF, ") foi REMOVIDO para atendimento."
    SENÃO
        ESCREVA "A fila estava vazia."
    FIM_SE
    
    // ----------------------------------------------------
    // 3. MOSTRAR QUEM AINDA ESTÁ NA FILA
    // ----------------------------------------------------
    ESCREVA "\n--- PACIENTES RESTANTES NA FILA ---"
    
    SE TAMANHO(FILA_PACIENTES) > 0 ENTÃO
        ESCREVA "Pacientes restantes na fila (do primeiro para o último):"
        PARA CADA paciente NA FILA_PACIENTES FAÇA
            ESCREVA "- Nome: ", paciente.Nome, ", CPF: ", paciente.CPF
        FIM_PARA
    SENÃO
        ESCREVA "Nenhum paciente restante na fila."
    FIM_SE
    
FIM_ALGORITMO