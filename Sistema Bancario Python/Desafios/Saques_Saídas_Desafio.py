''' 
Para ler e escrever dados em Python, utilizamos as seguintes funções: 
- input: lê UMA linha com dado(s) de Entrada do usuário;
- print: imprime um texto de Saída (Output), pulando linha.  
'''

def calcular_saldo(transacoes):

    # TODO: Itere sobre cada transação na lista:
    #lista = transacoes.strip("[]").replace(" ", "")
        # TODO: Adicione o valor da transação ao saldo
    saldo = list(map(float, entrada_usuario.split(",")))
    br = sum(saldo)

    # TODO: Retorne o saldo formatado em moeda brasileira com duas casas decimais:
    return f"Saldo: R$ {br:.2f}"

#Entrada=[100, -50, 200]
entrada_usuario = input()

entrada_usuario = entrada_usuario.strip("[]").replace(" ", "")

transacoes = [float(valor) for valor in entrada_usuario.split(",")]

# TODO: Calcule o saldo com base nas transações informadas:
resultado = calcular_saldo(transacoes)

print(resultado)