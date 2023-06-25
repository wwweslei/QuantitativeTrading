import sgs
import pandas as pd

# source https://www.bcb.gov.br/estatisticas/indecoreestruturacao

# Índices de preços
INPC = 188
IPCA = 433
IPCA_15 = 7478
IGPM = 189

# Força de trabalho e população em idade ativa
OCUPADAS = 24379
DESOCUPADA = 24380
FORCA_DE_TRABALHO = 24378
POPULACAO_EM_IDADE_ATIVA = 24370
TAXA_DE_DESOCUPACAO = 24369

# Rendimento médio real efetivo de todos os trabalhos
REMUNERACAO_MEDIA_NOMINAL = 24382
MASSA_SARAIAL = 28544

# Produto Interno Bruto e taxas médias de crescimento
PIP = 22099
EXPORTACOES = 22103
IMPORTACOES = 22104
AGRONEGOCIO = 22083
INDUSTRIA = 22084
SERVICOS = 22089

# Taxas de juros efetivas
SELIC = 4189
SELIC_META = 432
CDI = 4392
CDI_OVER = 12
POUPANCA = 196

# Reservas internacionais
RESEVAS_INTERNACIONAIS = 13621  


def consulta_bc(codigo_bcb):
  url = 'http://api.bcb.gov.br/dados/serie/bcdata.sgs.{}/dados?formato=json'.format(codigo_bcb)
  df = pd.read_json(url)
  df['data'] = pd.to_datetime(df['data'], dayfirst=True)
  df.set_index('data', inplace=True)
  return df

print(consulta_bc(CDI))