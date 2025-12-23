from django.http import HttpResponse
from django.shortcuts import render

from .models import Question


# Create your views here.
def index(req):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    output = ", ".join([q.question_text for q in latest_question_list])
    return HttpResponse(output)


def detail(req, question_id):
    return HttpResponse(f"You are looking at question {question_id}.")


def results(req, question_id):
    response = f"You are looking at the results of question {question_id}."
    return HttpResponse(response)


def vote(req, question_id):
    return HttpResponse(f"You are voting on question {question_id}.")
