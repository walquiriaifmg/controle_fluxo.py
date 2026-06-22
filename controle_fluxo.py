def mostrar_menu():
    print("=== Menu de estudos ===")
    print("1 - Contar de 1 até um número")
    print("2 - Calcular média de notas")
    print("3 - Mostrar a tabuada de um número")
    print("4 - Sair")


while True:
    mostrar_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        limite = int(input("Digite o número final da contagem: "))
        for numero in range(1, limite + 1):
            print(numero)

    elif opcao == "2":
        quantidade = int(input("Quantas notas deseja informar? "))
        soma = 0
        contador = 1

        while contador <= quantidade:
            nota = float(input(f"Digite a nota {contador}: "))
            soma = soma + nota
            contador = contador + 1

        media = soma / quantidade
        print(f"Média final: {media:.2f}")

        if media >= 60:
            print("Situação: aprovado")
        elif media >= 40:
            print("Situação: recuperação")
        else:
            print("Situação: reprovado")

    elif opcao == "3":
        numero = int(input("Digite um número para ver a tabuada: "))
        print(f"Tabuada do {numero}:")
        for i in range(1, 11):
            print(f"{numero} x {i} = {numero * i}")

    elif opcao == "4":
        print("Encerrando o programa...")
        break

    else:
        print("Opção inválida. Tente novamente.")