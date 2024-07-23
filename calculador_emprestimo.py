from datetime import datetime
from scipy.optimize import bisect


def calcular_taxa_juros(data_inicio, data_fim, valor_emprestado, valor_parcela, num_parcelas):
    data_atual = datetime.now()

    # Calcula o número de meses entre as datas de início e fim.
    meses_totais = (data_fim.year - data_inicio.year) * 12 + (data_fim.month - data_inicio.month) + 1

    # calcula o número de meses pagos até a data atual.
    meses_pagos = (data_atual.year - data_inicio.year) * 12 + (data_atual.month - data_inicio.month)


    def calcular_q0(j):
        """
        Função para otimização (encontrar J = Taxa de juros mensal).

        Onde:
            num_parcelas = Números de Meses.
            valor_parcela = Valor da Prestação.
            j = Taxa de Juros Mensal.
            q0 = Valor Financiado.
        """
        if j == 0:
            return valor_parcela * num_parcelas - valor_emprestado
        
        else:
            return (((1 - (1 + j) ** (- num_parcelas)) / j) * valor_parcela) - valor_emprestado
        
    # Encontrar (J = Taxa de juros mensal) com método da BISSEÇÃO com interlavo.
    try:
        j = bisect(calcular_q0, 1e-10, 1.0, xtol=1e-6)

    except ValueError:
        print("Não foi opssível encontrar a taxa de juros válida dentro do interlvalo especificado.")
        return None
    
    # Convertendo a taxa de juros encontrada para porcetagem.
    taxa_juros_mensal = j * 100
    taxa_juros_anual = taxa_juros_mensal * 12

    # Calcula o número de parcelas pagas e a pagar.
    parcelas_pagas = meses_pagos
    parcelas_a_pagar = meses_totais - meses_pagos

    # Calcula o saldo restante.
    saldo_restante = valor_parcela * parcelas_a_pagar

    return taxa_juros_mensal, taxa_juros_anual, parcelas_pagas, parcelas_a_pagar, saldo_restante


def interacao_usuario(mensagem):
    while True:
        try:
            data_str = input(mensagem + "(formato: MM/AAAA): ")
            data = datetime.strptime(data_str, "%m/%Y")
            return data
        
        except ValueError:
            print("Formato de data inválido: Tente novamente.")


def main():
    print("Calculadora de Taxa de Juros para contrato de Empréstimo".center(60))
    print("=" * 60)

    data_inicio = interacao_usuario("\nDigite a data de início do desconto")
    data_fim = interacao_usuario("Digite a data final do desconto")
    valor_parcela = float(input("Valor da parcela mensal: R$ "))
    valor_emprestado = float(input("Valor total emprestado: R$ "))
    num_parcelas = int(input("Quantidade de parcelas do contrato: "))

    taxa_juros, taxa_juros_anual, parcelas_pagas, parcelas_a_pagar, saldo_restante = calcular_taxa_juros(data_inicio, data_fim, valor_emprestado, valor_parcela, num_parcelas)

    if taxa_juros is not None:
        print(f"Parcelas pagas até o momento: {parcelas_pagas}")
        print(f"Parcelas restantes a pagar: {parcelas_a_pagar}")
        print(f"A taxa de juros atual é de: {taxa_juros:.2f}% a.m, {taxa_juros_anual:.2f}% a.a")
        print(f"O saldo restante é de: R$ {saldo_restante:.2f}")

if __name__ == "__main__":
    main()