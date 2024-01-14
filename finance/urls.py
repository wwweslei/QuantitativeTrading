from django.urls import path

from . import views

urlpatterns = [
    path("update", views.update, name="update"),
    path("fii_update", views.fii_update, name="fii_update"),
    path("treasury_update", views.treasury_update, name="treasury_update"),
    path("di_update", views.di_update, name="di_update"),
    path("etf_update", views.etf_update, name="etf_update"),
    path("stock_update", views.stock_update, name="stock_update"),
    path("index_b3_update", views.index_b3_update, name="index_b3_update"),
    path("sgs_update", views.sgs_update, name="sgs_update"),
]
