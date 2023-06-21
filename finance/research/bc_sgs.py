import sgs

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
CDI = 4392
POUPANCA = 196

ts = sgs.time_serie(PIP, start='02/01/2018', end='31/12/2018')
print(ts.tail())
