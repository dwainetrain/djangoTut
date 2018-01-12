#from django.shortcuts import render
from django.http import Http404
from django.template import loader
from django.shortcuts import get_object_or_404, render

from .models import Question

# Previous Version
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     return HttpResponse(template.render(context, request))

# Render is a shortcut for the above process
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

# The older more manual version
# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk = question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, 'polls/detail.html', {'question': question})

# This uses the django shortcut for flinging a 404
def detail(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return render(request, response % question_id)

def vote(request, question_id):
    return render(request, "You're voting on question %s." % question_id)
