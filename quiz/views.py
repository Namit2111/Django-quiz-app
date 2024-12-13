import uuid
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Question, QuizSession

def start_quiz(request):
    request.session['quiz_session_id'] = str(uuid.uuid4())
    QuizSession.objects.filter(session_id=request.session['quiz_session_id']).delete()
    return redirect('get_question')

def get_question(request):
    session_id = request.session.get('quiz_session_id')
    if not session_id:
        return redirect('start_quiz')
    
    answered_questions = QuizSession.objects.filter(session_id=session_id).values_list('question_id', flat=True)
    question = Question.objects.exclude(id__in=answered_questions).order_by('?').first()
    
    if not question:
        return redirect('quiz_summary')

    return render(request, 'question.html', {'question': question})

def submit_answer(request, question_id):
    session_id = request.session.get('quiz_session_id')
    if not session_id:
        return redirect('start_quiz')

    question = Question.objects.get(pk=question_id)
    user_answer = request.POST.get('answer')
    correct = user_answer == question.correct_option

    QuizSession.objects.create(session_id=session_id, question=question, answered_correctly=correct)
    return redirect('get_question')

def quiz_summary(request):
    session_id = request.session.get('quiz_session_id')
    if not session_id:
        return redirect('start_quiz')

    sessions = QuizSession.objects.filter(session_id=session_id)
    total = sessions.count()
    correct = sessions.filter(answered_correctly=True).count()
    incorrect = total - correct

    return render(request, 'summary.html', {
        'total': total,
        'correct': correct,
        'incorrect': incorrect,
        'details': sessions,
    })
