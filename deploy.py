from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import dash_bootstrap_components as dbc
import pandas as pd

# Dados
df = pd.read_csv("dados_tratados.csv", sep=";")

# Inicializar app com tema escuro do Bootstrap
app = Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])

# Opções para os gráficos
opcoes_boxplot = {
    'qtd_transacoes_12m': 'Quantidade de Transações (12m)',
    'valor_transacoes_12m': 'Valor de Transações (12m)',
    'qtd_produtos': 'Quantidade de Produtos',
    'iteracoes_12m': 'Interações (12m)',
    'meses_inativo_12m': 'Meses Inativo (12m)'
}

opcoes_dispersao = {
    'qtd_vs_valor': 'Qtd. Transações x Valor Transações',
    'valor_vs_iteracoes': 'Valor Transações x Interações'
}

# Layout
app.layout = dbc.Container([
    html.H1("Análise de Fatores por Inadimplência (Default)", className="text-center text-light mb-4"),

    dbc.Row([
        dbc.Col([
            html.Label("Tipo de Gráfico:", className="text-light"),
            dcc.RadioItems(
                id='tipo_grafico',
                options=[
                    {'label': 'Boxplot', 'value': 'boxplot'},
                    {'label': 'Dispersão', 'value': 'dispersao'}
                ],
                value='boxplot',
                labelStyle={'display': 'inline-block', 'margin-right': '15px'},
                style={'color': 'white'}
            )
        ])
    ]),

    dbc.Row([
        dbc.Col([
            html.Label("Escolha a Relação:", className="text-light"),
            dcc.Dropdown(
                id='relacao_grafico',
                style={
                    "backgroundColor": "#2c2c2c",
                    "color": "white",
                    "border": "1px solid #555",
                    "width": "100%", # ocupa toda coluna
                },
                className="text-light"
            )
            ], width=4)  # Define a largura para menos da metade da tela
], className="mb-4 mt-3"),

    dbc.Row([
        dbc.Col([
            dcc.Graph(id='grafico_final')
        ])
    ])
], fluid=True)


# Callback para atualizar opções para os gráficos
@app.callback(
    Output('relacao_grafico', 'options'),
    Output('relacao_grafico', 'value'),
    Input('tipo_grafico', 'value')
)
def atualizar_relacoes(tipo):
    if tipo == 'boxplot':
        opcoes = [{'label': nome, 'value': var} for var, nome in opcoes_boxplot.items()]
        valor_default = list(opcoes_boxplot.keys())[0]
    else:
        opcoes = [{'label': nome, 'value': var} for var, nome in opcoes_dispersao.items()]
        valor_default = list(opcoes_dispersao.keys())[0]
    return opcoes, valor_default


# Callback para atualizar gráfico
@app.callback(
    Output('grafico_final', 'figure'),
    Input('tipo_grafico', 'value'),
    Input('relacao_grafico', 'value')
)
def atualizar_grafico(tipo, relacao):
    if tipo == 'boxplot':
        fig = px.box(df, x='default', y=relacao, color='default', template='plotly_dark')
        fig.update_layout(title=f"Distribuição de {relacao} por Default")
    else:
        if relacao == 'qtd_vs_valor':
            fig = px.scatter(
                df, x='qtd_transacoes_12m', y='valor_transacoes_12m',
                color='default', size='valor_transacoes_12m', template='plotly_dark'
            )
            fig.update_layout(title='Qtd. Transações vs Valor Transações')
        elif relacao == 'valor_vs_iteracoes':
            fig = px.scatter(
                df, x='valor_transacoes_12m', y='iteracoes_12m',
                color='default', size='iteracoes_12m', template='plotly_dark'
            )
            fig.update_layout(title='Valor Transações vs Interações')
        else:
            fig = px.scatter(template='plotly_dark')

    return fig

# Executar
if __name__ == '__main__':
    app.run(debug=False)