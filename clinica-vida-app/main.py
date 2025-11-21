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
    print("Nãom há pacientes para ver aqui")
    return
  print("\n=== Lista de Todos os Pacientes ===")
  for paciente in pacientesLista:
    print(f"ID: {paciente['id']} | Nome: {paciente['nome']} | Idade: {paciente['idade']} | Telefone: {paciente['telefone']}")


if __name__ == "__main__":
  main()