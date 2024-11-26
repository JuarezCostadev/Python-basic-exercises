
turma = []


for i in range(10):
    print(f"Informações do Aluno {i + 1}:")
    nome = input("Nome do aluno: ")
    matricula = input("Matrícula do aluno: ")
    
    
    aluno_info = {
        "Nome": nome,
        "Matrícula": matricula
    }
    
    
    turma.append(aluno_info)


print("\nInformações da Turma:")
for aluno in turma:
    print(f"Nome: {aluno['Nome']}, Matrícula: {aluno['Matrícula']}")


