from django.urls import path
from . import views

# Set or establish the application namespace.
app_name = "polls"

urlpatterns = [
  # ex: /polls/
  # path("", views.index, name="index"),
  path("", views.IndexView.as_view(), name="index"),

  # ex: /polls/specifics/1/
  # path("specifics/<int:question_id>/", views.detail, name="detail"),

  # /polls/1/
  path("<int:pk>/", views.DetailView.as_view(), name="detail"),

  # ex: /polls/1/results/
  # path("<int:question_id>/results/", views.results, name="results"),
  path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),

  # ex: /polls/1/vote/
  # This request will be handled by the
  # vote() function in polls/views.py.
  # path("<int:question_id>/vote/", views.vote, name="vote")
  path("<int:question_id>/vote/", views.vote, name="vote"),

  # /polls/errors/
  path('errors', views.errors, name='errors'),

  path('404', views.generate_404, name='generate_404'),
  path('500', views.generate_500, name='generate_500')
]