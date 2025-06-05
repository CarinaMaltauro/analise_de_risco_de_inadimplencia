## Licença
Este projeto está licenciado sob a Licença Apache 2.0.

## Atribuição obrigatória
De acordo com os termos da licença Apache 2.0, qualquer pessoa que reutilizar este código (total ou parcialmente) deve incluir atribuição ao autor original:

Código criado por @CarinaMaltauro

A atribuição pode ser feita:

Nos arquivos de código (comentários)

Na documentação do projeto derivado

Ou em qualquer local visível e apropriado


## Projeto: Análise de Fatores de Risco de Inadimplência de Crédito

Este projeto tem como objetivo identificar fatores que influenciam o risco de inadimplência de clientes, com foco em variáveis comportamentais e socioeconômicas. A análise busca apoiar estratégias de mitigação de risco e melhoria no relacionamento com o cliente. 

## Sobre os Dados
O conjunto de dados analisado contém informações de clientes como:

Demográficos e socioeconômicos: sexo, idade, estado civil, escolaridade, número de dependentes, salário anual.

Comportamentais: quantidade e valor de transações, portfólio de produtos, interações com canais da empresa, meses de inatividade.

## 🔎 Métodos de Análise Aplicados

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

### 📌 Gráfico Boxplot

Identifica a dispersão dos dados. Apresenta a mediana, linha central dentro da caixa. E apresenta possíveis outliers, pontos fora da caixa que indicam comportamentos atípicos- por exemplo, clientes com uso excessivo de crédito ou movimentação fora do perfil usual. Se baseia nos quartis:

Q1: 25% dos menores valores

Q2: mediana, valor central

Q3: 75% dos valores


### 📌 Gráfico FacetGrid

Compara variáveis entre diferentes subgrupos. Permite observar tendências específicas em categorias distintas, facilitando uma análise visual comparativa entre adimplentes e inadimplentes.

## 🔎 Análise Exploratória

### Distribuição dos Dados

- Variáveis bem distribuídas: sexo, estado_civil, escolaridade, dependentes.

Permitem uma análise equilibrada e confiável.

- Variáveis com desequilíbrio: idade, salario_anual.

Poucas informações em algumas faixas das categorias, exigindo cautela em inferências.

### Correlação com o Risco de Inadimplência

- Fatores com pouca influência, porém presentes: qtd_transacoes_12m, valor_transacoes_12m, qtd_produtos, iteracoes_12m e meses_inativo_12m.

Interpretação: Fatores de engajamento com o banco demonstram alguma influência sobre a inadimplência, ainda que pouco.

- Fatores sem influência linear significativa: sexo, idade, estado_civil, escolaridade, salario_anual e dependentes.

Interpretação: Fatores demográficos não explicam bem o risco de inadimplência de forma isolada.

## Principais Resultados

- Clientes inadimplentes realizam menos transações e com menor valor médio (~R$2.500).

- Possuem menos produtos contratados quando comparado aos adimplentes (média 3 versus 4).

- Apesar de interagirem mais com os canais, as interações estão associadas a baixo volume financeiro (~R$10.000/ano).

## Conclusão
O perfil de risco de inadimplência está mais relacionado a comportamentos operacionais e de consumo do que a fatores socioeconômicos. Estratégias de monitoramento e prevenção devem:

- Priorizar o engajamento do cliente com os produtos e serviços bancários.

- Monitorar padrões de uso com baixa geração de receita, que podem sinalizar risco.
