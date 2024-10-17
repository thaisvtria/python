#Thaís Vitória
soma = 0

# Loop pelos números de 1 a 50
for i in range(1, 51):
    if i % 2 == 0:  # Verifica se o número é par
        soma += i  # Adiciona o número par à soma

print(f"A soma dos números pares entre 1 e 50 é: {soma}")