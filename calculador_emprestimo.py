from datetime import datetime
from scipy.optimize import bisect


def calcular_taxa_juros(data_inicio, data_fim, valor_emprestado, valor_parcela, num_parcelas):
    data_atual = datetime.now()
    
    # Calcula o número de meses entre as datas de início e fim
    meses_totais = (data_fim.year - data_inicio.year) * 12 + (data_fim.month - data_inicio.month) + 1
    
    # Calcula o número de meses pagos até a data atual
    meses_pagos = (data_atual.year - data_inicio.year) * 12 + (data_atual.month - data_inicio.month)
    
    # Função para otimização (encontrar j)
    def calcular_q0(j):
        if j == 0:
            return valor_parcela * num_parcelas - valor_emprestado
        else:
            return (((1 - (1 + j)**(-num_parcelas)) / j) * valor_parcela) - valor_emprestado
    
    # Encontrar j usando método da bisseção com intervalo apropriado
    try:
        j = bisect(calcular_q0, 1e-10, 1.0, xtol=1e-6)
        
    except ValueError:
        print("Não foi possível encontrar uma taxa de juros válida dentro do intervalo especificado.")
        return None
    
    # Taxa de juros mensal encontrada
    taxa_juros_mensal = j * 100  # Convertendo para porcentagem
    
    # Calcula o número de parcelas pagas e a pagar
    parcelas_pagas = meses_pagos
    parcelas_a_pagar = meses_totais - meses_pagos
    
    # Calcula o saldo restante
    saldo_restante = valor_parcela * parcelas_a_pagar
    
    return taxa_juros_mensal, parcelas_pagas, parcelas_a_pagar, saldo_restante


def interacao_usuario(mensagem):
    while True:
        try:
            data_str = input(mensagem + " (formato: MM/AAAA): ")
            data = datetime.strptime(data_str, "%m/%Y")
            return data
        except ValueError:
            print("Formato de data inválido. Tente novamente.")


def main():
    print("Calculadora de Taxa de Juros por Parcela para contrato de Empréstimo")
    print("=" * 70)

    data_inicio = interacao_usuario("Digite a data de início do desconto")
    data_fim = interacao_usuario("Digite a data final do desconto")
    valor_parcela = float(input("Valor da parcela mensal: R$ "))
    valor_emprestado = float(input("Valor total emprestado: R$ "))
    num_parcelas = int(input("Quantidade de parcelas do contrato: "))
    
    taxa_juros, parcelas_pagas, parcelas_a_pagar, saldo_restante = calcular_taxa_juros(data_inicio, data_fim, valor_emprestado, valor_parcela, num_parcelas)

    if taxa_juros is not None:
        print(f"Parcelas pagas até o momento: {parcelas_pagas}")
        print(f"Parcelas restantes a pagar: {parcelas_a_pagar}")
        print(f"A taxa de juros por parcela atual é de: {taxa_juros:.2f}% ao mês")
        print(f"O saldo restante é de: R$ {saldo_restante:.2f}")

if __name__ == "__main__":
    main()
