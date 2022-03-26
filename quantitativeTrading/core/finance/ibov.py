import pandas as pd
# ver https://github.com/alvarobartt/pyrtfolio/

def get_ibov_info():
    url = "http://bvmf.bmfbovespa.com.br/indices/ResumoCarteiraTeorica.aspx?Indice=IBOV&amp;idioma=pt-br"
    html = pd.read_html(url, decimal=",", thousands=".")[0][:-1]
    df = html.copy()[["Código", "Ação", "Tipo", "Qtde. Teórica", "Part. (%)"]]
    df.rename(
        columns={
            "Código": "symbol",
            "Ação": "name",
            "Tipo": "type",
            "Qtde. Teórica": "quantity",
            "Part. (%)": "percentage",
        },
        inplace=True,
    )
    return df


asset = get_ibov_info()
print(asset)
