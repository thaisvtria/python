cigarros_por_dia = int(input("Digite a quantidade de cigarros fumados por dia: "))
anos_fumando = int(input("Digite a quantidade de anos que fuma: "))
cigarros_totais = cigarros_por_dia * 365 * anos_fumando
tempo_perdido_minutos = cigarros_totais * 10
tempo_perdido_dias = tempo_perdido_minutos / 1440
print(f"O total de dias de vida perdidos é: {tempo_perdido_dias:.2f} dias")