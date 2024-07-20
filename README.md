#  Calculadora de Taxa de Juros para Empréstimos

Este projeto consiste em uma calculadora desenvolvida em Python para determinar a taxa de juros mensal em contratos de empréstimos com base em pagamentos mensais fixos. A calculadora utiliza o método da bisseção para encontrar a taxa de juros que, quando aplicada aos pagamentos mensais e ao número de parcelas, equilibra o valor emprestado com o valor total pago ao longo do tempo.

### Funcionalidades Principais:
Entrada de Dados:

O usuário fornece a data de início e fim do contrato de empréstimo, o valor mensal da parcela, o valor total emprestado e a quantidade de parcelas do contrato.

### Cálculo da Taxa de Juros:

A função principal calcula o número total de meses entre as datas, o número de meses pagos até a data atual e o valor total já pago. Com esses dados, a função utiliza o método da bisseção para encontrar a taxa de juros mensal que equilibra o valor total emprestado com o valor total pago até o momento.
Saída de Resultados:

Após o cálculo, a calculadora exibe a taxa de juros mensal atual, o número de parcelas já pagas, o número de parcelas restantes e o saldo restante a ser pago.

### Finalidade:

Este projeto é ideal para quem deseja entender melhor o impacto financeiro de um empréstimo ao longo do tempo e tomar decisões conscientes baseadas em números precisos e calculados.

# Metodologia de Cálculo: 
## Mesma usado no BCB

Cálculo com juros compostos e capitalização mensal.
Fórmula q0=(((1-(1+j)^-n))/j)*p

Onde:
n = Nº de Meses
j = Taxa de Juros Mensal
p = Valor da Prestação
q0 = Valor Financiado
Obs.: O cálculo da taxa de juros (j) é feito por aproximação do Valor da Prestação (p) com margem de erro sobre p inferior a 0.000001.
