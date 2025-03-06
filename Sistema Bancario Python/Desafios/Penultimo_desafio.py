

class ContaBancaria:
    def __init__ (self, nome_titular):
        self.nome_titular = nome_titular
        self.contas = []

class Conta:

    def __init__(self):
        self._saldo = 0

    @property
    def saldo(self):
        return self._saldo


    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")

        elif valor > 0:
            self._saldo -= valor
            print("\n=== Saque realizado com sucesso! ===")
            return True

        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

        return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("\n=== Depósito realizado com sucesso! ===")
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
            return False

        return True 

class PessoaFisica(ContaBancaria):
    def __init__(self, nome_titular):
        self.nome_titular = nome_titular

def realizar_transacoes(transacoes):
    saldo = 0
    extrato = []
    mensagem_erro = ""

    for transacao in transacoes:
        if transacao > 0:  # Depósito
            saldo += transacao
            extrato.append(transacao)
        else:  # Saque
            if abs(transacao) > saldo:
                mensagem_erro = ", Saque não permitido;"
            else:
                saldo += transacao  # Como transação é negativa, subtrai do saldo
                extrato.append(transacao)
                mensagem_erro = ";"
    
    # Remover o último saque do extrato
    for i in range(len(extrato) -1, -1):
        if extrato[i] < 0:
            extrato.pop(i)
            break
    
    return saldo, extrato, mensagem_erro

nome_titular = input().strip()  
conta = ContaBancaria(nome_titular)  

entrada_transacoes = input().strip() 
transacoes = [int(valor) for valor in entrada_transacoes.split(",")]  

saldo_final, extrato_final, mensagem = realizar_transacoes(transacoes)
extrato_formatado = ", ".join(f"{('+' if valor > 0 else '')}{int(valor)}" for valor in extrato_final)


print(f"Operações: {extrato_formatado}"f"{mensagem}" f" Saldo: {saldo_final}")