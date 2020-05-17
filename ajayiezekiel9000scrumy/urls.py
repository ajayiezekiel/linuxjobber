from django.urls import path
from ajayiezekiel9000scrumy import views

urlpatterns= [
    path('', views.get_grading_parameters, name="get_grading_parameters"),
    path('movegoal/<int:goal_id>', views.move_goal, name="movegoal" ),
    path('addgoal/', views.add_goal, name="addgoal"),
    path('home/', views.home, name="home"),
]