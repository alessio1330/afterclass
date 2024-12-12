from django.urls import path

from .views import (
    about,
    index,
    curso_list,
    comision_list,
    alumno_list,
    curso_create,
    comision_create,
    alumno_create,
)

app_name = "curso"

urlpatterns = [
    path("", index, name="index"),
    path("about/", about, name="about"),
    path("curso/list/", curso_list, name="curso_list"),
    path("curso/create/", curso_create, name="curso_create"),
    path("comision/list/", comision_list, name="comision_list"),
    path("comision/create/", comision_create, name="comision_create"),
    path("alumno/list", alumno_list, name="alumno_list"),
    path("alumno/create/", alumno_create, name="alumno_create"),
]
