# import locale

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from finance.models import EttjDay, EttjMonth, EttjWeek, LastEttj

sns.set_theme(style="darkgrid", palette="muted", font_scale=1)

# locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")


def graph_di():
    save_image_ettj()
    save_image_ettj_day()
    save_image_ettj_month()
    save_image_ettj_week()
    save_image_histogram()
    save_image_ettj_day_360()


def save_image_ettj_day_360():
    day = EttjDay.objects.all()
    last_day = LastEttj.objects.all()
    month = EttjMonth.objects.all()
    week = EttjWeek.objects.all()
    df_day = pd.DataFrame.from_records(day.values())[3:]
    df_last_day = pd.DataFrame.from_records(last_day.values())[3:]
    df_month = pd.DataFrame.from_records(month.values())[3:]
    df_week = pd.DataFrame.from_records(week.values())[3:]
    sns.lineplot(data=df_day, x="days", y="pre_360", label="hoje", linewidth=2)
    sns.lineplot(data=df_last_day, x="days", y="pre_360", label="ontem", linewidth=2)
    sns.lineplot(data=df_month, x="days", y="pre_360", label="inicio do mes", linewidth=2)
    sns.lineplot(data=df_week, x="days", y="pre_360", label="inicio da semana", linewidth=2)
    plt.title("curvas de juros 360")
    plt.ylabel("")
    plt.xlabel("")
    plt.savefig("core/static/core/img/ettj_day_360.svg", format="svg", bbox_inches="tight")
    plt.close()


def save_image_ettj_day():
    day = EttjDay.objects.all()
    last_day = LastEttj.objects.all()
    df_day = pd.DataFrame.from_records(day.values())
    df_last_day = pd.DataFrame.from_records(last_day.values())
    sns.lineplot(data=df_day, x="days", y="pre_252", label="hoje", linewidth=2)
    sns.lineplot(data=df_last_day, x="days", y="pre_252", label="ontem", linewidth=2)
    plt.title("curvas hoje")
    plt.ylabel("")
    plt.xlabel("")
    plt.savefig("core/static/core/img/ettj_day.svg", format="svg", bbox_inches="tight")
    plt.close()


def save_image_ettj_week():
    day = EttjDay.objects.all()
    week = EttjWeek.objects.all()
    df_day = pd.DataFrame.from_records(day.values())
    df_week = pd.DataFrame.from_records(week.values())
    sns.lineplot(data=df_day, x="days", y="pre_252", label="hoje", linewidth=2)
    sns.lineplot(data=df_week, x="days", y="pre_252", label="inicio da semana", linewidth=2)
    plt.title("curva de juros inicio da semana")
    plt.ylabel("")
    plt.xlabel("")
    plt.savefig("core/static/core/img/ettj_week.svg", format="svg", bbox_inches="tight")
    plt.close()


def save_image_ettj_month():
    day = EttjDay.objects.all()
    month = EttjMonth.objects.all()
    df_day = pd.DataFrame.from_records(day.values())
    df_month = pd.DataFrame.from_records(month.values())
    sns.lineplot(data=df_day, x="days", y="pre_252", label="hoje", linewidth=2)
    sns.lineplot(data=df_month, x="days", y="pre_252", label="inicio do mes", linewidth=2)
    plt.title("curva de juros inicio do mes")
    plt.ylabel("")
    plt.xlabel("")
    plt.savefig("core/static/core/img/ettj_month.svg", format="svg", bbox_inches="tight")
    plt.close()


def save_image_ettj():
    day = EttjDay.objects.all()
    last_day = LastEttj.objects.all()
    month = EttjMonth.objects.all()
    week = EttjWeek.objects.all()
    df_day = pd.DataFrame.from_records(day.values())
    df_last_day = pd.DataFrame.from_records(last_day.values())
    df_month = pd.DataFrame.from_records(month.values())
    df_week = pd.DataFrame.from_records(week.values())
    sns.lineplot(data=df_day, x="days", y="pre_252", label="hoje", linewidth=2)
    sns.lineplot(data=df_last_day, x="days", y="pre_252", label="ontem", linewidth=2)
    sns.lineplot(data=df_month, x="days", y="pre_252", label="inicio do mes", linewidth=2)
    sns.lineplot(data=df_week, x="days", y="pre_252", label="inicio da semana", linewidth=2)
    plt.title("curvas de juros")
    plt.ylabel("")
    plt.xlabel("")
    plt.savefig("core/static/core/img/ettj.svg", format="svg", bbox_inches="tight")
    plt.close()


def save_image_histogram():
    day = EttjDay.objects.all()
    last_day = LastEttj.objects.all()
    df_day = pd.DataFrame.from_records(day.values())
    df_last_day = pd.DataFrame.from_records(last_day.values())
    df_day = df_day.append(df_last_day)
    sns.histplot(data=df_day, x="pre_252", bins=50, kde=True)
    plt.title("histogram")
    plt.savefig("core/static/core/img/ettj_histogram.svg", format="svg", bbox_inches="tight")
    plt.close()
