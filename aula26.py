numeros = []
for i in range(5):
    num = int(input(f"digite o {i+1}° números "))
    numeros.append(num)

    # caucula o maior, o menor e a soma
    maior_num = max(numeros)
    menor_num = min(numeros)
    soma_num = sum(numeros)

    # exibe os resultados
    print(f"o maior número: {maior_num}")
    print(f"o menor número: {menor_num}")
    print(f"a soma total é: {soma_total}")