turmaA = [
    ("Jose Cerqueira", "A104341", [18, 15, 11]),
    ("Luisa Lopes", "A103264", [16, 18, 16])
]

turmaB = [
    ("Maria Cerqueira", "A103907", [20, 15, 13]),
    ("Andre Soares", "A103124", [18, 16, 12])
]

escola = [("turmaA", turmaA), ("turmaB", turmaB)]

def MostrarMenu():
    print('''Seja bem vindo à aplicação de gestão de alunos.
            1)----Criar uma turma---------------------------
            2)----Inserir um aluno na turma-----------------
            3)----Listar uma turma----------------------------
            4)----Consultar um aluno por id-----------------
            5)----Guardar a turma em ficheiro---------------
            6)----Carregar uma turma dum ficheiro-----------
            0)----Sair da aplicação-------------------------''' )

def existeturma(nome_turma, escola):
    nome_turma = nome_turma.lower()  # Conversão para minúsculas
    return any(turma_nome.lower() == nome_turma for turma_nome, _ in escola)

def CriarTurma(nome_turma, escola):
    nome_turma = nome_turma.lower()
    if not existeturma(nome_turma, escola):
        escola.append((nome_turma, []))
        print(f"A turma {nome_turma} foi criada com sucesso.")
    else:
        print("Essa turma já existe!")

def inserir_aluno(nome_turma, aluno):
    nome_turma = nome_turma.lower()
    for turma_nome, turma_alunos in escola:
        if turma_nome.lower() == nome_turma:
            if aluno[1] not in [a[1] for a in turma_alunos]:
                turma_alunos.append(aluno)
                print(f"O {aluno[0]} foi adicionado na turma {nome_turma}.")
            else:
                print("Aluno com o mesmo ID já existe na turma.")
            return
    print("Turma não encontrada.")

def listar(nome_turma):
    nome_turma = nome_turma.lower()
    for turma_nome, turma_alunos in escola:
        if turma_nome.lower() == nome_turma:
            print(f"--- Lista de alunos na turma {nome_turma} ---")
            for aluno in turma_alunos:
                print(f"Aluno: {aluno[0]}, ID: {aluno[1]}, Notas: {aluno[2]}")
            return
    print("Turma não encontrada.")

def consultar_aluno(id_aluno, nome_turma):
    nome_turma = nome_turma.lower()
    for turma_nome, turma_alunos in escola:
        if turma_nome.lower() == nome_turma:
            for aluno in turma_alunos:
                if aluno[1] == id_aluno:
                    print(f"Aluno encontrado: Nome: {aluno[0]}, ID: {aluno[1]}, Notas: {aluno[2]}")
                    return
    print("Aluno não encontrado.")

def guardar_turma(nome_turma, fnome):
    nome_turma = nome_turma.lower()
    file = open(fnome, "w")
    for turma_nome, turma_alunos in escola:
        if turma_nome.lower() == nome_turma:
            for aluno in turma_alunos:
                nome, id, [notaTPC, notaProj, notaTeste] = aluno
                file.write(f"{nome}, {id} |{notaTPC}|{notaProj}|{notaTeste}|")
                file.write("\n")

            print(f"Turma '{nome_turma}' guardada com sucesso em '{fnome}'.")
            file.close()
            return
        print("Turma não encontrada.")
    

def recuperar_turma(fnome):
    turma = []
    with open(fnome, "r") as file:  # Usando 'with' para abrir o arquivo
        for line in file:
            partes = line.strip().split("|")  # Divide a linha pelo caracter '#'
            if len(partes) >= 2:  # Verifica se a linha contém as duas partes
                nome, id = partes[0].split(",")  # Divide a primeira parte pelo ',' para separar nome e ID
                notas = list(map(int, partes[1].split("|")))  # Converte as notas para inteiros
                aluno = (nome, id, notas)  # Cria a tupla do aluno
                turma.append(aluno)  # Adiciona o aluno na lista
    if turma:  # Verifica se a lista de alunos não está vazia
        print("Turma recuperada do ficheiro:")
        for aluno in turma:
            print(f"Aluno: {aluno[0]}, ID: {aluno[1]}, Notas: {aluno[2]}")
    else:
        print("Nenhuma turma foi recuperada ou o arquivo está vazio.")
1


def Menu():
    global escola
    
    while True:
        MostrarMenu()
        opcao = int(input("O que deseja fazer?"))
        
        if opcao == 0:
            print("Saiu da aplicação! Até breve!")
            break

        elif opcao == 1:
            nome_turma = input("Nome da turma que deseja criar? ").lower()
            CriarTurma(nome_turma, escola)

        elif opcao == 2:
            nome_turma = input("Em que turma deseja adicionar o aluno? ").lower()
            id_aluno = input("Inserir id do aluno: ")
            nome = input("Inserir nome: ")
            notaTPC = int(input("Nota do TPC? "))
            notaProj = int(input("Nota do projeto? "))
            notaTeste = int(input("Nota do teste? "))
            aluno = (nome, id_aluno, [notaTPC, notaProj, notaTeste])
            inserir_aluno(nome_turma, aluno)

        elif opcao == 3:
            nome_turma = input("Nome da turma que deseja listar? ").lower()
            listar(nome_turma)

        elif opcao == 4:
            nome_turma = input("Nome da turma do aluno: ").lower()
            id_aluno = input("Id do aluno a procurar? ")
            consultar_aluno(id_aluno, nome_turma)

        elif opcao == 5:
            nome_turma = input("Nome da turma a guardar? ").lower()
            guardar_turma(nome_turma, "turma.txt")

        elif opcao == 6:
            turma = recuperar_turma("turma.txt")
            nome_turma = input("Qual turma quer recuperar? ").lower()
            escola.append((nome_turma, turma))

Menu()
