from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(req):
    return HttpResponse("Hello World! You are at the polls index!")


def detail(req, question_id):
    return HttpResponse("You are looking at question %s." % question_id)


def results(req, question_id):
    response = "You are looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(req, question_id):
    return HttpResponse("You are voting on question %s." % question_id)
