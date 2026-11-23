from django.urls import path

from . import views

app_name = "polls"

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),

    path('question/add', views.QuestionCreateView.as_view(), name='question-add'),
    path('<int:pk>question/edit', views.QuestionUpdateView.as_view(), name='question-edit'),
    path('<int:pk>question/delete', views.QuestionDeleteView.as_view(), name='question-delete'),

    path('choice/add', views.ChoiceCreateView.as_view(), name='choice-add'),
]
