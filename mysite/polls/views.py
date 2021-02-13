from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question
from django.template import loader

def index (request):
    lastest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'lastest_question_list':lastest_question_list,
    }
    return render(request, 'polls/index.html', context)

def detail (request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', context= {'question': question})

def results (request, question_id):
    response = f'You are looking at the results of question{question_id}'
    return HttpResponse(response)

def vote (reques, question_id):
    return HttpResponse(f'You are vote on question{question_id}')



# Create your views here.
