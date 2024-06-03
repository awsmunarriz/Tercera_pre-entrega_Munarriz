from django.contrib import admin
from django.urls import path
from AppWeb.views import lista_productos


urlpatterns = [
    path('admin/', admin.site.urls),
    path('lista-productos/', lista_productos),
]