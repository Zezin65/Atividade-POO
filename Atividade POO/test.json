import json

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def exibir_informacoes(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}")

    def to_dict(self):
        return {"nome": self.nome, "idade": self.idade}

class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"Matrícula: {self.matricula}")

    def to_dict(self):
        data = super().to_dict()
        data["matricula"] = self.matricula
        return data

class Professor(Pessoa):
    def __init__(self, nome, idade, disciplina):
        super().__init__(nome, idade)
        self.disciplina = disciplina

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"Disciplina: {self.disciplina}")

    def to_dict(self):
        data = super().to_dict()
        data["disciplina"] = self.disciplina
        return data

class Escola:
    def __init__(self, arquivo='dados.json'):
        self.arquivo = arquivo
        self.alunos = []
        self.professores = []
        self.carregar_dados()

    def carregar_dados(self):
        try:
            with open(self.arquivo, 'r') as f:
                dados = json.load(f)
                self.alunos = [Aluno(**aluno) for aluno in dados.get('alunos', [])]
                self.professores = [Professor(**professor) for professor in dados.get('professores', [])]
        except FileNotFoundError:
            self.alunos = []
            self.professores = []
        except json.JSONDecodeError:
            print("Erro ao carregar o arquivo de dados. Inicializando dados vazios.")
            self.alunos = []
            self.professores = []

    def salvar_dados(self):
        dados = {
            "alunos": [aluno.to_dict() for aluno in self.alunos],
            "professores": [professor.to_dict() for professor in self.professores]
        }
        with open(self.arquivo, 'w') as f:
            json.dump(dados, f, indent=4)

    def adicionar_aluno(self, nome, idade, matricula):
        aluno = Aluno(nome, idade, matricula)
        self.alunos.append(aluno)
        self.salvar_dados()
        print(f"Aluno {nome} foi adicionado com sucesso.")

    def adicionar_professor(self, nome, idade, disciplina):
        professor = Professor(nome, idade, disciplina)
        self.professores.append(professor)
        self.salvar_dados()
        print(f"Professor {nome} foi adicionado com sucesso.")

    def listar_alunos(self):
        if not self.alunos:
            print("Nenhum aluno cadastrado.")
        else:
            print("Lista de Alunos:")
            for aluno in self.alunos:
                aluno.exibir_informacoes()

    def listar_professores(self):
        if not self.professores:
            print("Nenhum professor cadastrado.")
        else:
            print("Lista de Professores:")
            for professor in self.professores:
                professor.exibir_informacoes()

def menu():
    escola = Escola()

    while True:
        print("\n---- Sistema de Gestão Escolar ----")
        print("1. Adicionar um Aluno")
        print("2. Adicionar um Professor")
        print("3. Listar Alunos")
        print("4. Listar Professores")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Nome do Aluno: ")
            idade = input("Idade do Aluno: ")
            matricula = input("Matrícula do Aluno: ")
            escola.adicionar_aluno(nome, idade, matricula)

        elif opcao == '2':
            nome = input("Nome do Professor: ")
            idade = input("Idade do Professor: ")
            disciplina = input("Disciplina do Professor: ")
            escola.adicionar_professor(nome, idade, disciplina)

        elif opcao == '3':
            escola.listar_alunos()

        elif opcao == '4':
            escola.listar_professores()

        elif opcao == '5':
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida, tente novamente.")

menu()
