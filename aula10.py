def calcular_imc(peso, altura):
    
    imc = peso / (altura ** 2)
    
    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif 18.5 <= imc <= 24.9:
        classificacao = "Peso normal"
    elif 25 <= imc <= 34.9:
        classificacao = "Sobrepeso"
    else:
        classificacao = "Obesidade"
    
    return imc, classificacao

peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

imc, classificacao = calcular_imc(peso, altura)

print(f"Seu IMC é: {imc:.2f}")
print(f"Classificação: {classificacao}")