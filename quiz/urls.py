from django.urls import path
from . import views

urlpatterns = [
    path('', views.start_quiz, name='start_quiz'),
    path('question/', views.get_question, name='get_question'),
    path('question/<int:question_id>/submit/', views.submit_answer, name='submit_answer'),
    path('summary/', views.quiz_summary, name='quiz_summary'),
]
