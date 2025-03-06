
def filtrar_transacoes(transacoes, limite):
    transacoes_filtradas = []

    for valor in transacoes:
        if abs(valor) > limite:
            transacoes_filtradas.append(valor)

    # Retorna a lista de transações filtradas
    return transacoes_filtradas

    # TODO: Itere sobre cada transação na lista:

        # TODO: Verifique se o valor absoluto da transação é maior que o limite:
        
            # TODO: Adicione a transação à lista filtrada:
            


#Entrada=[100, -50, 300, -150], 100
entrada = input()

#Adicionando [100, -50, 300, -150] a entrada_transacoes e adicionando 100 a limite (SUBSTRINGS"")
entrada_transacoes, limite = entrada.split("],") 
#Retirando os colchetes e espaços, aproximando todos os caracteres
entrada_transacoes = entrada_transacoes.strip("[]").replace(" ", "") 
limite = float(limite.strip())  # Converte o limite para float

# Convertendo os valores para uma lista de ints
transacoes = [int(valor) for valor in entrada_transacoes.split(",")]

# TODO: Filtre as transações que ultrapassam o limite:
resultado = filtrar_transacoes(transacoes, limite)

print(f"Transações: {resultado}")