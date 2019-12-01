from django.urls import path
from . import views

urlpatterns = [
path("",views.project_index,name="project_index"),
path("<int:pk>/",views.project_detail,name="project_detail"),
]
#for the path of project detail, the url will
#vary based on the primary key so in order to keep this
#dynamic we use <int:pk>
#and based on the dynamically generated urls depending on the
#project to view