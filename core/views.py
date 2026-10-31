from django.shortcuts import render, HttpResponse

from core.models import Question


# Create your views here.

def question_view(request):

    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)


