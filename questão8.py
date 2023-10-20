lista_produtos = []
total_produtos = 0

while True:

    menu = int(input("""
    Escolha uma opção:
    1 - Adicionar produto
    2 - Remover produto
    3 - Alterar produto
    4 - Exibir lista de produtos
    0 - Encerrar    
    """))

    if menu == 1:

        produto = str(input("Qual produto deseja adicionar?: "))
        qntd = int(input("Quantos produtos?"))
        valor = float(input("Valor do produto: "))
        valor_produto = valor * qntd
        total_produtos += valor_produto
        lista_produtos.append({"produto": produto, "Quantidade": qntd, "Valor": valor, "Valor total": valor_produto})
        print("Produto adicionado com sucesso!")

    elif menu == 2:

        # Opção para remover produto
        produto_remover = str(input("Qual produto deseja remover?: "))
        for item in lista_produtos:
            if item["produto"] == produto_remover:
                valor_produto_removido = item["Valor total"]
                lista_produtos.remove(item)
                total_produtos -= valor_produto_removido
                print(f"Produto '{produto_remover}' removido com sucesso!")
                break
        else:
            print(f"Produto '{produto_remover}' não encontrado na lista.")

    elif menu == 3:
        # Adicione a lógica para alterar um produto na lista
        alterar = str(input("Qual produto deseja alterar?"))
        quantidade_atualizada = int(input("Quantos produtos?"))
        valor_atualizado = float(input("Valor do produto: "))
        valor_total = quantidade_atualizada * valor_atualizado
        for item in lista_produtos:
            if item["produto"] == alterar:
                valor_produto_removido = item["Valor total"]
                total_produtos -= valor_produto_removido
                total_produtos += valor_total
                item["Quantidade"] = quantidade_atualizada
                item["Valor"] = valor_atualizado
                item["Valor total"] = valor_total
                print(f"Produto '{alterar}' alterado com sucesso!")
            else:
                print(f"Produto '{alterar}' não encontrado na lista.")

    elif menu == 4:
        print("\nLista de Produtos:")
        for item in lista_produtos:
            print(f"Produto: {item['produto']}, Quantidade: {item['Quantidade']}, Valor: {item['Valor']}, Valor Total: {item['Valor total']}")
        print(f"Total de Produtos: {total_produtos}")

    elif menu == 0:
        print("Encerrando o programa.")
        break

    else:
        print("Opção inválida. Tente novamente.")

 