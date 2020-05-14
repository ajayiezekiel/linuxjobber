from django.urls import path
from ajayiezekiel9000scrumy import views

urlpatterns= [
    path('', views.get_grading_parameters, name="get_grading_parameters")
]