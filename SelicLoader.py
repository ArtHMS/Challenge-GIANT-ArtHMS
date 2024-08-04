import pandas as pd
import requests

# Class that will configure the URL of an API to obtain selic data between dates
class CarregadorSelic:
    def __init__(self, data_inicial='01/01/2000', data_final='01/03/2021'):
        self.data_inicial = data_inicial
        self.data_final = data_final
        self.url_selic = f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json&dataInicial={data_inicial}&dataFinal={data_final}"

    # The method fetches data from the selic API and returns it in JSON format, or generates an exception if the requests fail    
    def buscar_dados_selic(self):
        resposta = requests.get(self.url_selic)
        if resposta.status_code == 200:
            dados = resposta.json()
            return dados
        else:
            raise Exception("Falha ao buscar dados da API")
    
    # The method transforms the selic API data into a pandas DataFrame with properly formatted date and value columns
    def processar_dados_selic(self, dados):
        df = pd.DataFrame(dados)
        df['data'] = pd.to_datetime(df['data'], format='%d/%m/%Y')
        df['valor'] = df['valor'].astype(float) / 100
        return df
    
    # The method obtains and processes the Selic data, returning a final DataFrame
    def obter_dataframe_selic(self):
        dados_brutos = self.buscar_dados_selic()
        dados_processados = self.processar_dados_selic(dados_brutos)
        return dados_processados
    
    # Filtering Selic data for the specified period based on rates
    def calcular_valor_ganho(self, df, capital, data_inicial, data_final):
        df_periodo = df[(df['data'] >= data_inicial) & (df['data'] <= data_final)]
        
        valor_total = capital
        for _, linha in df_periodo.iterrows():
            valor_total *= (1 + linha['valor'])
        
        return valor_total - capital
    
    # The method finds the period of days that maximizes the gain on invested capital based on selic rates 
    def calcular_melhor_periodo(self, df, capital, dias=500):
        melhor_inicio = None
        melhor_fim = None
        melhor_valor = 0
        
        for i in range(len(df) - dias):
            data_inicial = df.iloc[i]['data']
            data_final = df.iloc[i + dias]['data']
            valor_ganho = self.calcular_valor_ganho(df, capital, data_inicial, data_final)
            if valor_ganho > melhor_valor:
                melhor_inicio = data_inicial
                melhor_fim = data_final
                melhor_valor = valor_ganho
        
        return melhor_inicio, melhor_fim, melhor_valor
    
    # Calculates and returns capital and accumulated earnings at a specified frequency based on Selic rates
    def calcular_ganhos_frequencia(self, capital, frequencia):
        df = self.obter_dataframe_selic()
        
        df = df.set_index('data').resample(frequencia).apply(lambda x: (1 + x).prod() - 1)
        df['valor_acumulado'] = (1 + df['valor']).cumprod() * capital
        df['valor_ganho'] = df['valor_acumulado'] - capital
        
        df = df[['valor_acumulado', 'valor_ganho']]
        df.reset_index(inplace=True)
        df.rename(columns={'data': 'Date', 'valor_acumulado': 'Capital', 'valor_ganho': 'Amount earned'}, inplace=True)
        
        return df
    
    # Realizes the return of gains made from capital "Days", "Month", "Years"
    def calcular_ganhos_diarios(self, capital):
        return self.calcular_ganhos_frequencia(capital, 'D')
    
    def calcular_ganhos_mensais(self, capital):
        return self.calcular_ganhos_frequencia(capital, 'ME')
    
    def calcular_ganhos_anuais(self, capital):
        return self.calcular_ganhos_frequencia(capital, 'YE')

if __name__ == '__main__':
    carregador = CarregadorSelic(data_inicial='01/01/2000', data_final='01/03/2021')
    capital = 657.43
    
    ganhos_diarios = carregador.calcular_ganhos_diarios(capital)
    print("Ganhos Diários")
    print(ganhos_diarios.head())
    
    ganhos_mensais = carregador.calcular_ganhos_mensais(capital)
    print("\nGanhos Mensais")
    print(ganhos_mensais.head())
    
    ganhos_anuais = carregador.calcular_ganhos_anuais(capital)
    print("\nGanhos Anuais")
    print(ganhos_anuais.head())

    melhor_inicio, melhor_fim, melhor_valor = carregador.calcular_melhor_periodo(carregador.obter_dataframe_selic(), capital)
    print(f"\nThe best day to invest is {melhor_inicio.date()}, with an amount earned of {melhor_valor} after 500 days ({melhor_inicio.date()} to {melhor_fim.date()})")

    print("\nArgs:")
    print("start_date=date(2000, 1, 1),")
    print("end_date=date(2021, 3, 1),")
    print("capital=657.43,")
    print("frequency='day',")
    print("save_csv=False")
    print(ganhos_diarios)