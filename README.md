# Calculadora de Taxa de Juros para Empréstimos.

Este script Python calcula a taxa de juros mensal de um empréstimo com base nas informações fornecidas pelo usuário, utilizando o método de bisseção para otimização. Considera o valor total emprestado, o valor das parcelas mensais, o número total de parcelas e as datas de início e fim do empréstimo.

## Funcionalidades:

* **Entrada de Dados:** O usuário fornece as datas de início e fim do empréstimo, o valor total emprestado, o valor das parcelas mensais e o número total de parcelas.
* **Cálculos Realizados:** Determina a taxa de juros mensal e anual que iguala o valor presente das parcelas ao valor emprestado.
Calcula o número de parcelas pagas até a data atual e o número de parcelas restantes.
Estima o saldo devedor restante.

### Bibliotecas:

* **scipy:** Para otimização numérica.
* **datetime:** Para manipulação de datas.
  
#### Versão do Python:

* Python 3.12.

#### Como Usar:

Execute o script Python.
Insira as datas no formato MM/AAAA, o valor da parcela mensal, o valor total emprestado e o número total de parcelas quando solicitado.
O script exibirá a taxa de juros mensal e anual, o número de parcelas pagas, o número de parcelas restantes e o saldo devedor atual.

### Metodologia de Cálculo:

O cálculo utiliza a técnica de bisseção para encontrar a taxa de juros mensal que faz com que o valor presente das parcelas seja igual ao valor emprestado. A precisão é ajustada para garantir que a diferença entre o valor presente calculado e o valor emprestado seja inferior a 0.000001.

#### Fórmula Utilizada:
```
q0=(((1-(1+j)^-n))/j)*p

Onde:
n = Nº de Meses
j = Taxa de Juros Mensal
p = Valor da Prestação
q0 = Valor Financiado
```
* Observação: A taxa de juros mensal (j) é encontrada por aproximação da fórmula acima, com uma margem de erro mínima sobre o valor da prestação (p).
