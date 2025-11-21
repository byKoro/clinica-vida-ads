pacientesLista = []

def main():

  while True:
    print("===== Sistema da Clínica Vida + =====")
    print("1. Cadastrar paciente")
    print("2. Ver estatísticas")
    print("3. Buscar paciente")
    print("4. Listar todos os pacientes.")
    print("0. Sair")

    escolha = int(input("Selecione uma opção: "))

    if escolha == 1:
      cadastrarPacientes()
      pass

    elif escolha == 2:
      verEstatisticas()
      pass

    elif escolha == 3:
      buscarPacientes()
      pass

    elif escolha == 4:
      listarPacientes()
      pass

    elif escolha == 0:
      print("Programa finalizado")
      break

def cadastrarPacientes():
    # Receber Pacientes
    print("===== Sistema da Clínica Vida + =====")
    print("======== Cadastro do Paciente =======")
    id_paciente = len(pacientesLista)
    nome_input = str(input("Digíte o nome completo do paciente: "))
    while True:
      try:
        idade_input = int(input("Digíte a idade do paciente: "))
        break
      except ValueError:
        print("A idade deve ser um número: ")
        
    telefone_input = str(input("Digíte o telefone do paciente: "))

    # Salvar Pacientes
    novo_paciente = {
      "id":id_paciente,
      "nome":nome_input,
      "idade":idade_input,
      "telefone":telefone_input

    }
    pacientesLista.append(novo_paciente)

    print("Paciente Cadastrado com sucesso: ")

def listarPacientes():
    if not pacientesLista: 
        print("\nNenhum paciente cadastrado.")
        return 

    print("\n" + "="*60)
    print(" " * 20 + "RELATÓRIO DE PACIENTES")
    print("="*60)
    
    # Cabeçalho da Tabela
    cabecalho = f"|{'ID':^5}|{'NOME':<25}|{'IDADE':>8}|{'TELEFONE':<18}|"
    print(cabecalho)
    print("-"*60)
    
    # Loop para imprimir os dados de cada paciente
    for paciente in pacientesLista:
        linha = (
            f"|{paciente['id']:^5}|"        
            f"{paciente['nome']:<25}|"      
            f"{paciente['idade']:>8}|"      
            f"{paciente['telefone']:<18}|"   
        )
        print(linha)
    
    print("="*60)
    print(f"Total de Pacientes: {len(pacientesLista)}")


if __name__ == "__main__":
  main()