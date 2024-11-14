
#Fiz meu codigo utilizado o Json como banco de dados para armazenar os dados inseridos, Fiz varias implementações conforme o codigo
#foi testado, fiz ele mais robusto. Jogo do bixo, makake1


import json

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def exibir_informacoes(self):
        print(f"{'Nome':<15}: {self.nome}")
        print(f"{'Idade':<15}: {self.idade}")

    def to_dict(self):
        return {"nome": self.nome, "idade": self.idade}

class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"{'Matrícula':<15}: {self.matricula}")

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
        print(f"{'Disciplina':<15}: {self.disciplina}")

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
            print(f"Arquivo {self.arquivo} não encontrado. Criando um novo arquivo.")
            self.alunos = []
            self.professores = []
        except json.JSONDecodeError:
            print("Erro ao carregar o arquivo de dados. O arquivo pode estar corrompido.")
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
        if not nome or not matricula:
            print("Nome ou matrícula não podem estar vazios.")
            return
        try:
            idade = int(idade)
        except ValueError:
            print("Idade deve ser um número.")
            return
        aluno = Aluno(nome, idade, matricula)
        self.alunos.append(aluno)
        self.salvar_dados()
        print(f"Aluno {nome} foi adicionado com sucesso.")

    def adicionar_professor(self, nome, idade, disciplina):
        if not nome or not disciplina:
            print("Nome ou disciplina não podem estar vazios.")
            return
        try:
            idade = int(idade)
        except ValueError:
            print("Idade deve ser um número.")
            return
        professor = Professor(nome, idade, disciplina)
        self.professores.append(professor)
        self.salvar_dados()
        print(f"Professor {nome} foi adicionado com sucesso.")

    def listar_alunos(self):
        if not self.alunos:
            print("Nenhum aluno cadastrado.")
        else:
            print("\nLista de Alunos:")
            for aluno in self.alunos:
                aluno.exibir_informacoes()

    def listar_professores(self):
        if not self.professores:
            print("Nenhum professor cadastrado.")
        else:
            print("\nLista de Professores:")
            for professor in self.professores:
                professor.exibir_informacoes()

class SistemaEscola:
    def __init__(self):
        self.escola = Escola()

    def executar(self):
        while True:
            print("\n---- Sistema de Gestão Escolar ----")
            print("1. Adicionar um Aluno")
            print("2. Adicionar um Professor")
            print("3. Listar Alunos")
            print("4. Listar Professores")
            print("5. Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                self.adicionar_aluno()
            elif opcao == '2':
                self.adicionar_professor()
            elif opcao == '3':
                self.escola.listar_alunos()
            elif opcao == '4':
                self.escola.listar_professores()
            elif opcao == '5':
                print("Saindo do sistema...")
                break
            else:
                print("Opção inválida, tente novamente.")

    def adicionar_aluno(self):
        nome = input("Nome do Aluno: ")
        idade = input("Idade do Aluno: ")
        matricula = input("Matrícula do Aluno: ")
        self.escola.adicionar_aluno(nome, idade, matricula)

    def adicionar_professor(self):
        nome = input("Nome do Professor: ")
        idade = input("Idade do Professor: ")
        disciplina = input("Disciplina do Professor: ")
        self.escola.adicionar_professor(nome, idade, disciplina)

if __name__ == "__main__":
    sistema = SistemaEscola()
    sistema.executar()
