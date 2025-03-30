# import locale
from datetime import date, datetime
from multiprocessing import Process

import matplotlib
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from finance.models import TesouroIpca, TesouroPrefixado, TesouroSelic

matplotlib.use("svg")
sns.set_theme(style="whitegrid", palette="muted", font_scale=1)
# locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")


def treasure_graph():
    func_list = [
        showimageIPCA,
        showimageIpcaMonthly,
        showimageIpcaWeekly,
        showimagePrefixado,
        showimagePrefixadoMonthly,
        showimagePrefixadoWeekly,
        showimageSelic,
        showimageSelicMonthly,
        showimageSelicWeekly,
    ]
    for func in func_list:
        process = Process(target=func)
        process.start()


def showimageIPCA():
    query = TesouroIpca.objects.filter(data_vencimento__gte=datetime.today())
    df = pd.DataFrame(query.values("data_vencimento", "data_base", "pu_base_manha"))
    available_dates = df["data_vencimento"].unique()
    df = [df[df["data_vencimento"] == date].set_index("data_base") for date in available_dates]
    df = [df[i].rename(columns={"pu_base_manha": str(available_dates[i])[:4]}) for i in range(len(df))]
    df = pd.concat(df, axis=1)
    df.drop("data_vencimento", axis=1, inplace=True)
    df.dropna(inplace=True)
    df = (df / df.iloc[0]) * 1
    sns.lineplot(data=df, linewidth=2, dashes=False)
    plt.legend(ncol=2, loc="upper left")
    plt.title("Tesouro IPCA -- Anual")
    plt.xlabel("")
    plt.ylabel("Valor do PU")
    plt.ylim(0.9, 1.3)
    fmt = mdates.DateFormatter("%b")
    X = plt.gca().xaxis
    X.set_major_formatter(fmt)
    plt.savefig("core/static/core/img/tesouro_ipca.svg", format="svg", bbox_inches="tight")
    plt.close()


def showimagePrefixado():
    # Construct the graph
    query = TesouroPrefixado.objects.filter(data_vencimento__gte=datetime.today())
    df = pd.DataFrame(query.values("data_vencimento", "data_base", "pu_base_manha"))
    available_dates = df["data_vencimento"].unique()
    df = [df[df["data_vencimento"] == date].set_index("data_base") for date in available_dates]
    df = [df[i].rename(columns={"pu_base_manha": str(available_dates[i])[:4]}) for i in range(len(df))]
    df = pd.concat(df, axis=1)
    df.drop("data_vencimento", axis=1, inplace=True)
    df.dropna(inplace=True)
    df = df.loc[date(year=date.today().year, month=1, day=1) :]
    df = (df / df.iloc[0]) * 1
    sns.lineplot(data=df, linewidth=2, dashes=False)
    plt.legend(ncol=2, loc="upper left")
    plt.title("Tesouro Prefixado -- Anual")
    plt.xlabel("")
    plt.ylabel("Valor do PU")
    plt.ylim(0.9, 1.3)
    fmt = mdates.DateFormatter("%b")
    X = plt.gca().xaxis
    X.set_major_formatter(fmt)
    plt.savefig("core/static/core/img/tesouro_prefixado.svg", format="svg", bbox_inches="tight")
    plt.close()


def showimageSelic():
    # Construct the graph
    selic = TesouroSelic.objects.filter(data_vencimento__year="2029").values("data_base", "pu_base_manha")
    df_selic = pd.DataFrame(selic).set_index("data_base").rename(columns={"pu_base_manha": "Selic-2029"})
    ipca = TesouroIpca.objects.filter(data_vencimento__year="2029").values("data_base", "pu_base_manha")
    df_ipca = pd.DataFrame(ipca).set_index("data_base").rename(columns={"pu_base_manha": "IPCA-2029"})
    pre = TesouroPrefixado.objects.filter(data_vencimento__year="2029").values("data_base", "pu_base_manha")
    df_pre = pd.DataFrame(pre).set_index("data_base").rename(columns={"pu_base_manha": "prefixado-2029"})
    df = pd.concat([df_pre, df_selic, df_ipca], axis=1)
    df = df.loc[date(year=date.today().year, month=1, day=13) :]
    df = (df / df.iloc[0]) * 1
    sns.lineplot(data=df, linewidth=2, dashes=False)
    plt.legend(ncol=2, loc="upper left")
    plt.title("Selic-Prefixado-IPCA -- Anual")
    plt.xlabel("")
    plt.ylabel("Valor do PU")
    plt.ylim(0.9, 1.3)
    fmt = mdates.DateFormatter("%b")
    X = plt.gca().xaxis
    X.set_major_formatter(fmt)
    plt.savefig("core/static/core/img/tesouro_selic.svg", format="svg", bbox_inches="tight")
    plt.close()


def showimageIpcaMonthly():
    # Construct the graph
    query = TesouroIpca.objects.filter(data_vencimento__gte=datetime.today())
    df = pd.DataFrame(query.values("data_vencimento", "data_base", "pu_base_manha"))
    available_dates = df["data_vencimento"].unique()
    df = [df[df["data_vencimento"] == date].set_index("data_base") for date in available_dates]
    df = [df[i].rename(columns={"pu_base_manha": str(available_dates[i])[:4]}) for i in range(len(df))]
    df = pd.concat(df, axis=1)
    df.drop("data_vencimento", axis=1, inplace=True)
    df.dropna(inplace=True)
    df = df.loc[date(year=date.today().year, month=date.today().month, day=1) :]
    df = (df / df.iloc[0]) * 1
    sns.lineplot(data=df, linewidth=2, dashes=False)
    plt.legend(ncol=2, loc="upper left")
    plt.title("Tesouro IPCA -- Mensal")
    plt.xlabel("")
    plt.ylabel("Valor do PU")
    plt.ylim(0.95, 1.05)
    fmt = mdates.DateFormatter("%d")
    X = plt.gca().xaxis
    X.set_major_formatter(fmt)
    plt.savefig("core/static/core/img/tesouro_ipca_monthly.svg", format="svg", bbox_inches="tight")
    plt.close()


def showimageSelicMonthly():
    # Construct the graph
    selic = TesouroSelic.objects.filter(data_vencimento__year="2029").values("data_base", "pu_base_manha")
    df_selic = pd.DataFrame(selic).set_index("data_base").rename(columns={"pu_base_manha": "Selic-2029"})
    ipca = TesouroIpca.objects.filter(data_vencimento__year="2029").values("data_base", "pu_base_manha")
    df_ipca = pd.DataFrame(ipca).set_index("data_base").rename(columns={"pu_base_manha": "IPCA-2029"})
    pre = TesouroPrefixado.objects.filter(data_vencimento__year="2029").values("data_base", "pu_base_manha")
    df_pre = pd.DataFrame(pre).set_index("data_base").rename(columns={"pu_base_manha": "prefixado-2029"})
    df = pd.concat([df_pre, df_selic, df_ipca], axis=1)
    df = df.loc[date(year=date.today().year, month=date.today().month, day=1) :]
    df = (df / df.iloc[0]) * 1
    sns.lineplot(data=df, linewidth=2, dashes=False)
    plt.legend(ncol=2, loc="upper left")
    plt.title("Selic-Prefixado-IPCA -- Mensal")
    plt.xlabel("")
    plt.ylabel("Valor do PU")
    plt.ylim(0.95, 1.05)
    fmt = mdates.DateFormatter("%d")
    X = plt.gca().xaxis
    X.set_major_formatter(fmt)
    plt.savefig("core/static/core/img/tesouro_selic_monthly.svg", format="svg", bbox_inches="tight")
    plt.close()


def showimagePrefixadoMonthly():
    # Construct the graph
    query = TesouroPrefixado.objects.filter(data_vencimento__gte=datetime.today())
    df = pd.DataFrame(query.values("data_vencimento", "data_base", "pu_base_manha"))
    available_dates = df["data_vencimento"].unique()
    df = [df[df["data_vencimento"] == date].set_index("data_base") for date in available_dates]
    df = [df[i].rename(columns={"pu_base_manha": str(available_dates[i])[:4]}) for i in range(len(df))]
    df = pd.concat(df, axis=1)
    df.drop("data_vencimento", axis=1, inplace=True)
    df.dropna(inplace=True)
    df = df.loc[date(year=date.today().year, month=date.today().month, day=1) :]
    df = (df / df.iloc[0]) * 1
    sns.lineplot(data=df, linewidth=2, dashes=False)
    plt.legend(ncol=2, loc="upper left")
    plt.title("Tesouro Prefixado -- Mensal")
    plt.xlabel("")
    plt.ylabel("Valor do PU")
    plt.ylim(0.95, 1.05)
    fmt = mdates.DateFormatter("%d")
    X = plt.gca().xaxis
    X.set_major_formatter(fmt)
    plt.savefig("core/static/core/img/tesouro_pre_monthly.svg", format="svg", bbox_inches="tight")
    plt.close()


def showimageIpcaWeekly():
    # Construct the graph
    query = TesouroIpca.objects.filter(data_vencimento__gte=datetime.today())
    df = pd.DataFrame(query.values("data_vencimento", "data_base", "pu_base_manha"))
    available_dates = df["data_vencimento"].unique()
    df = [df[df["data_vencimento"] == date].set_index("data_base") for date in available_dates]
    df = [df[i].rename(columns={"pu_base_manha": str(available_dates[i])[:4]}) for i in range(len(df))]
    df = pd.concat(df, axis=1)
    df.drop("data_vencimento", axis=1, inplace=True)
    df.dropna(inplace=True)
    df = df.loc[date(year=date.today().year, month=date.today().month, day=date.today().day - date.today().weekday()) :]
    df = (df / df.iloc[0]) * 1
    sns.lineplot(data=df, linewidth=2, dashes=False)
    plt.legend(ncol=2, loc="upper left")
    plt.title("Tesouro IPCA -- Semanal")
    plt.xlabel("")
    plt.ylabel("Valor do PU")
    plt.ylim(0.98, 1.02)
    fmt = mdates.DateFormatter("%d")
    X = plt.gca().xaxis
    X.set_major_formatter(fmt)
    plt.savefig("core/static/core/img/tesouro_ipca_weekly.svg", format="svg", bbox_inches="tight")
    plt.close()


def showimageSelicWeekly():
    # Construct the graph
    selic = TesouroSelic.objects.filter(data_vencimento__year="2029").values("data_base", "pu_base_manha")
    df_selic = pd.DataFrame(selic).set_index("data_base").rename(columns={"pu_base_manha": "Selic-2029"})
    ipca = TesouroIpca.objects.filter(data_vencimento__year="2029").values("data_base", "pu_base_manha")
    df_ipca = pd.DataFrame(ipca).set_index("data_base").rename(columns={"pu_base_manha": "IPCA-2029"})
    pre = TesouroPrefixado.objects.filter(data_vencimento__year="2029").values("data_base", "pu_base_manha")
    df_pre = pd.DataFrame(pre).set_index("data_base").rename(columns={"pu_base_manha": "prefixado-2029"})
    df = pd.concat([df_pre, df_selic, df_ipca], axis=1)
    df = df.loc[date(year=date.today().year, month=date.today().month, day=date.today().day - date.today().weekday()) :]
    df = (df / df.iloc[0]) * 1
    sns.lineplot(data=df, linewidth=2, dashes=False)
    plt.legend(ncol=2, loc="upper left")
    plt.title("Selic-Prefixado-IPCA -- Semanal")
    plt.xlabel("")
    plt.ylabel("Valor do PU")
    plt.ylim(0.98, 1.02)
    fmt = mdates.DateFormatter("%d")
    X = plt.gca().xaxis
    X.set_major_formatter(fmt)
    plt.savefig("core/static/core/img/tesouro_selic_weekly.svg", format="svg", bbox_inches="tight")
    plt.close()


def showimagePrefixadoWeekly():
    # Construct the graph
    query = TesouroPrefixado.objects.filter(data_vencimento__gte=datetime.today())
    df = pd.DataFrame(query.values("data_vencimento", "data_base", "pu_base_manha"))
    available_dates = df["data_vencimento"].unique()
    df = [df[df["data_vencimento"] == date].set_index("data_base") for date in available_dates]
    df = [df[i].rename(columns={"pu_base_manha": str(available_dates[i])[:4]}) for i in range(len(df))]
    df = pd.concat(df, axis=1)
    df.drop("data_vencimento", axis=1, inplace=True)
    df.dropna(inplace=True)
    df = df.loc[date(year=date.today().year, month=date.today().month, day=date.today().day - date.today().weekday()) :]
    df = (df / df.iloc[0]) * 1
    sns.lineplot(data=df, linewidth=2, dashes=False)
    plt.legend(ncol=2, loc="upper left")
    plt.title("Tesouro Prefixado -- Semanal")
    plt.xlabel("")
    plt.ylabel("Valor do PU")
    plt.ylim(0.98, 1.02)
    fmt = mdates.DateFormatter("%d")
    X = plt.gca().xaxis
    X.set_major_formatter(fmt)
    plt.savefig("core/static/core/img/tesouro_pre_weekly.svg", format="svg", bbox_inches="tight")
    plt.close()
