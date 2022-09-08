from django.urls import path
from . import views

app_name = "questions"
urlpatterns = [
    # Class Base Views
    path("", views.IndexView.as_view(), name='index'),
    path("<int:pk>/", views.DetailView.as_view(), name='detail'),
    path("<int:pk>/results/", views.ResultView.as_view(), name='results'),
    # Function Base View
    path("<int:question_id>/vote/", views.vote, name='vote')
]
