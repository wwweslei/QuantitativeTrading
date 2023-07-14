from django.urls import include, path

from . import graph, views

urlpatterns = [
    path("", views.index, name="index"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/profile/", views.profile, name="profile"),
    path(
        "accounts/portifolio_user_form/",
        views.portifolio_user_form,
        name="portifolio_user_form",
    ),
    path("accounts/signup/", views.signup, name="signup"),
    path("showimageIPCA/", graph.showimageIPCA, name="showimageIPCA"),
    path("showimagePrefixado/", graph.showimagePrefixado, name="showimagePrefixado"),
    path("showimageSelic/", graph.showimageSelic, name="showimageSelic"),
]
