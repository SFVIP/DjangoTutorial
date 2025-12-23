from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(req):
    return HttpResponse("Hello World! You are at the polls index!")


def detail(req, question_id):
    return HttpResponse(f"You are looking at question {question_id}.")


def results(req, question_id):
    response = f"You are looking at the results of question {question_id}."
    return HttpResponse(response)


def vote(req, question_id):
    return HttpResponse(f"You are voting on question {question_id}.")
