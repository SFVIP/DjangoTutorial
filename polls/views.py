from django.http import Http404, HttpResponse
from django.shortcuts import render

from .models import Question


# Create your views here.
def index(req):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(req, "polls/index.html", context)


def detail(req, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(req, "polls/detail.html", {"question": question})

def results(req, question_id):
    response = f"You are looking at the results of question {question_id}."
    return HttpResponse(response)


def vote(req, question_id):
    return HttpResponse(f"You are voting on question {question_id}.")
