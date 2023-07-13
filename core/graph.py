import io
from datetime import date, datetime

import matplotlib
from django.shortcuts import HttpResponse

from finance.models import TesouroIpca, TesouroPrefixado

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import pandas as pd
import PIL
import PIL.Image
import seaborn as sns


def showimageIPCA(request):
    # Construct the graph
    query = TesouroIpca.objects.filter(data_vencimento__gte=datetime.today())
    df = pd.DataFrame(query.values("data_vencimento", "data_base", "pu_base_manha"))
    available_dates = df["data_vencimento"].unique()
    df = [
        df[df["data_vencimento"] == date].set_index("data_base")
        for date in available_dates
    ]
    df = [
        df[i].rename(columns={"pu_base_manha": str(available_dates[i])[:4]})
        for i in range(len(df))
    ]
    df = pd.concat(df, axis=1)
    df.drop("data_vencimento", axis=1, inplace=True)
    df.dropna(inplace=True)
    df = (df / df.iloc[0]) * 1
    sns.lineplot(data=df, linewidth=2, dashes=False)
    plt.legend(ncol=2, loc="upper left")
    plt.title("Tesouro IPCA")
    plt.xlabel("")
    plt.ylabel("Valor do PU")
    plt.ylim(0.9, 1.3)
    plt.grid(True)
    # Store image in a string buffer
    buffer = io.BytesIO()
    canvas = plt.get_current_fig_manager().canvas
    canvas.draw()
    pilImage = PIL.Image.frombytes(
        "RGB", canvas.get_width_height(), canvas.tostring_rgb()
    )
    pilImage.save(buffer, "PNG")
    plt.close()
    # Send buffer in a http response the the browser with the mime type image/png set
    return HttpResponse(buffer.getvalue(), content_type="image/png")


def showimagePrefixado(request):
    # Construct the graph
    query = TesouroPrefixado.objects.filter(data_vencimento__gte=datetime.today())
    df = pd.DataFrame(query.values("data_vencimento", "data_base", "pu_base_manha"))
    available_dates = df["data_vencimento"].unique()
    df = [
        df[df["data_vencimento"] == date].set_index("data_base")
        for date in available_dates
    ]
    df = [
        df[i].rename(columns={"pu_base_manha": str(available_dates[i])[:4]})
        for i in range(len(df))
    ]
    df = pd.concat(df, axis=1)
    df.drop("data_vencimento", axis=1, inplace=True)
    df.dropna(inplace=True)
    df = df.loc[date(year=2023, month=1, day=1) :]
    df = (df / df.iloc[0]) * 1
    df.loc[date(year=2023, month=1, day=1) :]
    sns.lineplot(data=df, linewidth=2, dashes=False)
    plt.legend(ncol=2, loc="upper left")
    plt.title("Tesouro Prefixado")
    plt.xlabel("")
    plt.ylabel("Valor do PU")
    plt.ylim(0.9, 1.3)
    plt.grid(True)
    # Store image in a string buffer
    buffer = io.BytesIO()
    canvas = plt.get_current_fig_manager().canvas
    canvas.draw()
    pilImage = PIL.Image.frombytes(
        "RGB", canvas.get_width_height(), canvas.tostring_rgb()
    )
    pilImage.save(buffer, "PNG")
    plt.close()
    # Send buffer in a http response the the browser with the mime type image/png set
    return HttpResponse(buffer.getvalue(), content_type="image/png")
