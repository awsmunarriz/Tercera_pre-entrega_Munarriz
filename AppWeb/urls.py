from django.urls import path
from AppWeb.views import lista_productos


urlpatterns = [
    path('lista-productos/', lista_productos),
]