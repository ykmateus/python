numero = 8
tentativas = 0
while True:
    tentativa = int(input("Adivinhe o número (entre 1 e 10): "))
    if tentativa > numero:
        print("O número é menor, tente novamente.")
        tentativas += 1
    elif tentativa < numero:
        print("O número é maior, tente novamente.")
        tentativas += 1
    elif tentativa == numero:
        tentativas += 1
        print(f"Parabéns, você acertou o número {numero} com {tentativas} tentativas.")
        break
    else:
        print("Opção inválida.")
       
