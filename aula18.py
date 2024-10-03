def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_para_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_para_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_para_celsius(kelvin):
    return kelvin - 273.15

def kelvin_para_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def main():
    while True:
        print("Conversor de Temperaturas:")
        print("1. Converter de Celsius para Fahrenheit")
        print("2. Converter de Celsius para Kelvin")
        print("3. Converter de Fahrenheit para Celsius")
        print("4. Converter de Fahrenheit para Kelvin")
        print("5. Converter de Kelvin para Celsius")
        print("6. Converter de Kelvin para Fahrenheit")
        print("7. Sair")
        
        opcao = input("Selecione uma opção: ")
        
        if opcao == '7':
            print("Saindo do programa.")
            break
        
        if opcao in {'1', '2', '3', '4', '5', '6'}:
            try:
                temperatura = float(input("Digite a temperatura: "))
            except ValueError:
                print("Por favor, insira um número válido.")
                continue
            
            if opcao == '1':
                resultado = celsius_para_fahrenheit(temperatura)
                print(f"{temperatura}°C é igual a {resultado:.2f}°F")
            elif opcao == '2':
                resultado = celsius_para_kelvin(temperatura)
                print(f"{temperatura}°C é igual a {resultado:.2f}K")
            elif opcao == '3':
                resultado = fahrenheit_para_celsius(temperatura)
                print(f"{temperatura}°F é igual a {resultado:.2f}°C")
            elif opcao == '4':
                resultado = fahrenheit_para_kelvin(temperatura)
                print(f"{temperatura}°F é igual a {resultado:.2f}K")
            elif opcao == '5':
                resultado = kelvin_para_celsius(temperatura)
                print(f"{temperatura}K é igual a {resultado:.2f}°C")
            elif opcao == '6':
                resultado = kelvin_para_fahrenheit(temperatura)
                print(f"{temperatura}K é igual a {resultado:.2f}°F")
        else:
            print("Opção inválida! Por favor, escolha uma opção entre 1 e 7.")

if __name__ == "__main__":
    main()