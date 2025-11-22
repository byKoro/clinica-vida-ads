pacientesLista = [
    {
        "id": 0,
        "nome": "Maria Silva",
        "idade": 45,
        "telefone": "(11) 98765-4321"
    },
    {
        "id": 1,
        "nome": "João Victor",
        "idade": 19,
        "telefone": "(21) 99988-7766"
    },
    {
        "id": 2,
        "nome": "Helena Costa",
        "idade": 72,
        "telefone": "(31) 95555-4444"
    },
    {
        "id": 3,
        "nome": "Pedro Alves",
        "idade": 30,
        "telefone": "(41) 91111-2222"
    },
    {
        "id": 4,
        "nome": "Ana Lúcia",
        "idade": 19,
        "telefone": "(51) 93333-6666"
    },
    {
        "id": 5,
        "nome": "Ana Luzia",
        "idade": 22,
        "telefone": "(51) 93333-6666"
    }
]

VERMELHO = '\033[91m'
VERDE = '\033[92m'
RESET = '\033[0m'

def main():

  while True:
    print("===== Sistema da Clínica Vida + =====")
    print("1. Cadastrar paciente")
    print("2. Ver estatísticas")
    print("3. Buscar paciente")
    print("4. Listar todos os pacientes.")
    print("0. Sair")

    try:
      escolha = int(input("Selecione uma opção: "))
      if escolha < 0 or escolha > 4:
        print(f"{VERMELHO}Valor inválido{RESET}")
    except ValueError:
      print(f"{VERMELHO}Valor inválido{RESET}")

    if escolha == 1:
      cadastrarPacientes()
      pass

    elif escolha == 2:
      # Verificar lista vazia
      if len(pacientesLista) == 0:
        print(f"{VERMELHO}Cadastre algum paciente antes de acessar esse menu.{RESET}")

      else:
        verEstatisticas()
        pass
    
    elif escolha == 3:
      if len(pacientesLista) == 0:
        print(f"{VERMELHO}Cadastre algum paciente antes de acessar esse menu.{RESET}")
      else:
       buscarPacientes()
      pass

    elif escolha == 4:
      if len(pacientesLista) == 0:
        print(f"{VERMELHO}Cadastre algum paciente antes de acessar esse menu.{RESET}")
      else:
        listarPacientes()
      pass

    elif escolha == 0:
      print(f"{VERDE}Programa finalizado{RESET}")
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
        print(f"{VERMELHO}A idade deve ser um número: {RESET}")
        
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

def verEstatisticas():
  while True:
    print("===== Sistema da Clínica Vida + =====")
    print("=========== Ver estáticas ===========")
    print("1. Total de Pacientes")
    print("2. Idade média dos pacientes")
    print("3. Paciente mais velho e mais novo")
    print("0. Voltar")

    try:
      escolha = int(input("Selecione uma opção: "))
      if escolha < 0 or escolha > 3:
        print(f"{VERMELHO}Valor inválido{RESET}")
    except ValueError:
      print(f"{VERMELHO}Valor inválido{RESET}")

    if escolha == 1: 
      totalPacientes = len(pacientesLista)
      print(f"{VERDE}O total de pacientes é de : {totalPacientes}{RESET}")

    if escolha == 2:
      soma_idade = 0
      for paciente in pacientesLista:
        soma_idade = soma_idade + paciente["idade"]

      media_idade = soma_idade / len(pacientesLista)
      print(f"{VERDE}A idade média de todos os pacientes é de: {media_idade}{RESET}")

    if escolha == 3:
      # Busca do paciente mais novo
      paciente_mais_novo = pacientesLista[0]["idade"]
      id_paciente_mais_novo = 0

      for paciente in pacientesLista:
        if paciente_mais_novo > paciente["idade"]:
          paciente_mais_novo = paciente["idade"]
          id_paciente_mais_novo = paciente["id"]
        else:
          pass
      
      print(f"{VERDE}O paciente mais novo é: {pacientesLista[id_paciente_mais_novo]['nome']} com {pacientesLista[id_paciente_mais_novo]['idade']} anos de idade.{RESET}")
      # Busca do paciente mais velho

      print("="*60)

      paciente_mais_velho = pacientesLista[0]["idade"]
      id_paciente_mais_velho = 0
      for paciente in pacientesLista:
        if paciente_mais_velho < paciente["idade"]:
          paciente_mais_velho = paciente["idade"]
          id_paciente_mais_velho = paciente["id"]
        else:
          pass
      print(f"{VERDE}O paciente mais velho é: {pacientesLista[id_paciente_mais_velho]['nome']} com {pacientesLista[id_paciente_mais_velho]['idade']} anos de idade.{RESET}")
    if escolha == 0:
      break 

def buscarPacientes():
  # Cabeçalho
  termo_busca = str(input("Digíte o nome do paciente: ").lower())
  encontrado = False
  
  print("\n" + "="*60)
  cabecalho = f"|{'ID':^5}|{'NOME':<25}|{'IDADE':>8}|{'TELEFONE':<18}|"
  print(cabecalho)
  print("-"*60)


  for paciente in pacientesLista:
    if termo_busca in paciente['nome'].lower():
      linha = (
        f"|{paciente['id']:^5}|"        
        f"{paciente['nome']:<25}|"      
        f"{paciente['idade']:>8}|"      
        f"{paciente['telefone']:<18}|"   
      )
      print(linha)
      encontrado = True

  print("="*60)

  if not encontrado:
    print(f"{VERMELHO}Nenhum paciente com o nome {termo_busca} foi encontrado!{RESET}")

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