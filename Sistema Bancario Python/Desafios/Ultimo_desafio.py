import textwrap

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = int(saldo)
    
    def __str__(self):
        return f"{self.titular}: R$ {self.saldo}"

class SistemaBancario:
    def __init__(self):
        self.contas = []
    
    def criar_conta(self, titular, saldo):
        self.contas.append(ContaBancaria(titular, saldo))
    
    def listar_contas(self):
        print(", ".join(str(conta) for conta in self.contas))

def main():
    sistema = SistemaBancario()
    
    while True:
        entrada = input().strip()
        if entrada.upper() == "FIM":  
            break
        
        try:
            titular, saldo = entrada.split(", ")
            sistema.criar_conta(titular, saldo)
        except ValueError:
            print("Entrada inválida. Use o formato: Nome, Valor")
    
    sistema.listar_contas()

if __name__ == "__main__":
    main()
