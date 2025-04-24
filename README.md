## Projeto: Análise de Fatores de Risco de Inadimplência de Crédito

Este projeto tem como objetivo identificar fatores que influenciam o risco de inadimplência de clientes, com foco em variáveis comportamentais e socioeconômicas. A análise busca apoiar estratégias de mitigação de risco e melhoria no relacionamento com o cliente.

## Sobre os Dados
O conjunto de dados analisado contém informações de clientes como:

Demográficos e socioeconômicos: sexo, idade, estado civil, escolaridade, número de dependentes, salário anual.

Comportamentais: quantidade e valor de transações, portfólio de produtos, interações com canais da empresa, meses de inatividade.

## 🔎 Métodos Estatísticos Utilizados

### 📌 Correlação de Pearson

Correlação aplicada para verificar relação de risco de inadimplência e com variáveis numéricas. A força da correlação é medida pelo coeficiente de Pearson (r), que varia de -1 a +1:

+1.0: Correlação perfeita positiva

+0.7 a +0.9: Correlação forte positiva

+0.4 a +0.6: Correlação moderada positiva

+0.1 a +0.3: Correlação fraca positiva

0: Sem correlação linear

-0.1 a -0.3: Correlação fraca negativa

-0.4 a -0.6: Correlação moderada negativa

-0.7 a -0.9: Correlação forte negativa

-1.0: Correlação perfeita negativa

O sinal indica o tipo de relação:

Positivo: ambos os fatores aumentam juntos.

Negativo: quando um aumenta, o outro tende a diminuir.

### 📌 Boxplot
Boxplot utilizado para explorar a dispersão dos dados e identificar possíveis outliers. Ele se baseia nos quartis:

Q1 (1º quartil): 25% dos menores valores

Q2 (mediana): valor central

Q3 (3º quartil): 75% dos valores

A mediana é representada por uma linha central dentro da caixa. Os outliers são marcados como pontos fora da caixa e podem indicar comportamentos atípicos — por exemplo, clientes com uso excessivo de crédito ou movimentações fora do perfil usual.

### 📌 FacetGrid
FacetGrid compara variáveis entre diferentes subgrupos. Permite observar tendências específicas em categorias distintas (como sexo, escolaridade ou faixa etária), facilitando uma análise visual comparativa entre adimplentes e inadimplentes.

## 🔎 Análise Exploratória

### Distribuição dos Dados

- Variáveis bem distribuídas: sexo, estado_civil, escolaridade, dependentes.

Permitem uma análise equilibrada e confiável.

- Variáveis com desequilíbrio: idade, salario_anual.

Apresentam distribuição enviesada, exigindo cautela em inferências.

### Correlação com o Risco de Inadimplência
- Fatores com correlação fraca, porém presente: qtd_transacoes_12m, valor_transacoes_12m, qtd_produtos, iteracoes_12m, meses_inativo_12m

Interpretação: Fatores de engajamento com o banco demonstram alguma influência sobre a inadimplência, ainda que com correlação fraca.

- Fatores sem correlação linear significativa: sexo, idade, estado_civil, escolaridade, salario_anual, dependentes

Interpretação: Fatores demográficos não explicam bem o risco de inadimplência de forma isolada.

## Principais Resultados Gráficos
- Clientes inadimplentes realizam menos transações e com menor valor médio (~R$2.500).

- Possuem menos produtos contratados quando comparado aos adimplentes (média 3 versus 4).

- Apesar de interagirem mais com os canais, as interações estão associadas a baixo volume financeiro (~R$10.000/ano).

- É possível interagir com gráficos através do link: 

## Conclusão
O perfil de risco de inadimplência está mais relacionado a comportamentos operacionais e de consumo do que a fatores socioeconômicos. Estratégias de monitoramento e prevenção devem:

- Priorizar o engajamento do cliente com os produtos e serviços bancários.

- Monitorar padrões de uso com baixa geração de receita, que podem sinalizar risco.
