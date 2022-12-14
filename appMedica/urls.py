from django.urls import path
from .views import *

urlpatterns = [
    path("about", about, name="about"),
    path("appointment", appointment, name="appointment"),
    path("blog", blog, name="blog"),
    path("contact", contact, name="contact"),
    path("gallery", gallery, name="gallery"),
    path("", home, name="home"),
    path("login", loginV, name="login1"),
    path("services", services, name="services"),
    path("team", team, name="team"),
    path("citas", citas, name="citas"),
    path("cerrar", cerrar_sesion, name="cerrar")
]
