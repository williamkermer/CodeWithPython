notas = []

for x in range(3):

    codigo_aluno = int(input("RM: "))
    nota_aluno = float(input("Nota: "))
    resultado = (codigo_aluno, nota_aluno)
    notas.append(resultado)

print(notas)
print("Quantidade de notas:", len(notas))